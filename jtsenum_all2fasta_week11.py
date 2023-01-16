#!/usr/bin/env python3

"""
The implementation of all-to-fasta script that converts any file format (EMBL, FASTQ, GenBank, MEGA, SAM or
VCF) to FASTA format. The output of the script is an output file that has either .fna (nucleotide) or .faa
(amino acid) extensions.
"""

import argparse


def check_ext(seq):
    if not set(seq).difference(set('ACGTN')):
        return '.fna'
    else:
        return '.faa'


def fold_string(s, f):
    out = ''
    for k in range((len(s) // f) + 1):
        out += f'{s[k * f:min((k + 1) * f, len(s))]}\n'
    return out.strip()


def run_embl(input_lines, f):
    #
    # Here we process EMBL format files
    #

    out = ''
    entries = '\n'.join(input_lines).split('//')[:-1]  # Each entry is separated by '//', skipping the last empty entry
    AC, DE, sq_i, ext, seq = None, None, None, None, None

    # Finding the entry identifications
    for i, entry in enumerate(entries):
        entry_lines = entry.split('\n')
        for k, line in enumerate(entry_lines):
            if line.startswith('AC'):
                AC = line.replace('AC', '').replace(';', '').strip()

            if line.startswith('DE'):
                DE = line.replace('DE', '').strip()

            if line.startswith('SQ'):  # this is the sequence identifier
                sq_i = k + 1
                break

        seq = ''.join(entry_lines[sq_i:])  # joining different lines into string
        seq = ''.join([ch for ch in seq if not ch.isdigit()])  # removing numbers from the sequence
        seq = seq.replace(' ', '').replace('\t', '').upper()  # removing blank spaces, and capitalizing sequence

        out += f'>{AC}|{DE}\n{fold_string(seq, f)}\n'

    # Determining extension from the last sequence
    ext = check_ext(seq)

    return out.strip(), ext


def run_fastq(input_lines, f):
    #
    # Here we process FASTQ files
    #

    out = ''
    input_lines = [
        line if line.startswith('@') else line.replace('@', '') for line in input_lines
    ]  # cleaning '@' signs in the quality sequences
    entries = '\n'.join(input_lines).split('@')[1:]  # Each entry is separated by '@', skipping the first empty entry
    seq = None

    # Finding the entry identifications
    for i, entry in enumerate(entries):
        entry_lines = entry.split('\n')
        seq_id = entry_lines[0]
        seq = entry_lines[1].upper()
        out += f'>{seq_id}\n{fold_string(seq, f)}\n'

    # Determining extension from the last sequence
    ext = check_ext(seq)

    return out.strip(), ext


def run_gb(input_lines, f):
    #
    # Here we process GenBank files
    #

    out = ''
    entries = '\n'.join(input_lines).split('//')[:-1]  # Each entry is separated by '//', skipping the last empty entry
    AC, DE, V, sq_i, ext, seq = None, None, None, None, None, None

    # Finding the entry identifications
    for i, entry in enumerate(entries):
        entry_lines = entry.split('\n')
        for k, line in enumerate(entry_lines):
            if line.startswith('ACCESSION'):
                AC = line.replace('ACCESSION', '').replace(';', '').strip()

            if line.startswith('VERSION'):
                V = line.replace('VERSION', '').replace(';', '').strip()

            if line.startswith('DEFINITION'):
                DE = line.replace('DEFINITION', '').strip()

            if line.startswith('ORIGIN'):  # this is the sequence identifier
                sq_i = k + 1
                break

        seq = ''.join(entry_lines[sq_i:])  # joining different lines into string
        seq = ''.join([ch for ch in seq if not ch.isdigit()])  # removing numbers from the sequence
        seq = seq.replace(' ', '').replace('\t', '').upper()  # removing blank spaces, and capitalizing sequence

        out += f'>{AC if V is None else V}|{DE}\n{fold_string(seq, f)}\n'

    # Determining extension from the last sequence
    ext = check_ext(seq)

    return out.strip(), ext


def run_mega(input_lines, f):
    #
    # Here we process MEGA files
    #

    out = ''
    entry_dict = {}

    entries = '\n'.join(input_lines[3:]).split('#')[1:]  # each entry is separated by '#', skipping the first empty entry
    entries = list(map(lambda x: x.replace('\n', ' ').replace('\t', ' '), entries))  # bring seqs to the same format

    for entry in entries:
        id, seq = entry[:entry.find(' ')], entry[entry.find(' ') + 1:].replace(' ', '').upper()
        if id in entry_dict:
            entry_dict[id] += seq
        else:
            entry_dict[id] = seq

    for id, seq in entry_dict.items():
        out += f'>{id}\n{fold_string(seq, f)}\n'

    # Determining extension from the last sequence
    ext = check_ext(seq)

    return out.strip(), ext


def run_sam(input_lines, f):
    #
    # Here we process SAM files
    #

    out = ''

    entries = [line for line in input_lines if not line.startswith('@')]

    for entry in entries:
        line_info = entry.split('\t')
        id = line_info[0]
        seq = line_info[9]
        out += f'>{id}\n{fold_string(seq, f)}\n'

    # Determining extension from the last sequence
    ext = check_ext(seq)

    return out.strip(), ext


def run_vcf(input_lines, f):
    #
    # Here we process VCF files
    #

    out = ''

    sample_names = [line for line in input_lines if not line.startswith('##')][0].split('\t')[9:]
    info_mat = [line.split('\t') for line in input_lines if not line.startswith('#')]

    # Taking care of reference sequence
    ref_id = info_mat[0][0]
    ref_seq = ''.join([line[3] for line in info_mat])
    out += f'>{ref_id}\n{fold_string(ref_seq, f)}\n'

    # Determining extension from the reference sequence
    ext = check_ext(ref_seq)

    for j, sample_name in zip(range(9, len(info_mat[0])), sample_names):
        seq = ''
        for i in range(len(info_mat)):
            snp_i = int(info_mat[i][j].split(':')[0])
            snps = [info_mat[i][3]] + info_mat[i][4].split(',')
            seq += snps[snp_i]

        out += f'>{sample_name}\n{fold_string(seq, f)}\n'

    return out.strip(), ext


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='All-to-fasta script that converts any file format (EMBL, FASTQ, GenBank, MEGA, SAM or VCF) '
                    'to FASTA.')
    parser.add_argument('-i', '--input', type=str, help='The path to input file name.', required=True)
    parser.add_argument('-f', '--fold', type=int, default=70, help='The line fold, i.e., after how many bases should a '
                                                                   'new line be inserted.')

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        input_lines = [line.strip() for line in f.readlines()]

    # Defining the file format
    if input_lines[0].startswith('ID'):  # every EMBL format starts with ID
        out, ext = run_embl(input_lines, args.fold)
    elif input_lines[0].startswith('@') and input_lines[2].startswith('+'):  # every FASTQ format has periodic entries
        out, ext = run_fastq(input_lines, args.fold)
    elif input_lines[0].startswith('LOCUS'):  # every GenBank format starts with LOCUS
        out, ext = run_gb(input_lines, args.fold)
    elif input_lines[0].startswith('#MEGA'):  # every MEGA file starts with #MEGA identifier
        out, ext = run_mega(input_lines, args.fold)
    elif input_lines[0].startswith('##fileformat=VCFv'):  # every VCF start with #VCF version identifier
        out, ext = run_vcf(input_lines, args.fold)
    else:
        out, ext = run_sam(input_lines, args.fold)

    with open(f'mkryukov_{args.input}{ext}', 'w') as f:
        f.write(out)





