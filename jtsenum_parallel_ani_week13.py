#!/usr/bin/env python3

"""
The implementation of algorithm that finds the overlapping regions from 2 BED files.
"""

import argparse
import multiprocessing
import subprocess
import os
import re


def get_ani(file_pair):

    output_file = file_pair[0] + "_" + file_pair[1]
    command = f'dnadiff -p tmp/{output_file} {file_pair[0]} {file_pair[1]}'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    _, error = process.communicate()

    with open(f'tmp/{output_file}.report', 'r') as f:
        ani = float(re.findall(r"\d+\.\d+", f.readlines()[18])[0])

    return ani


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Find overlapping regions from 2 BED files.')
    parser.add_argument('-o', '--output', type=str, help='The path to the output file.', required=True)
    parser.add_argument('-t', '--threads', type=int, help='The number of threads.', default=8, required=False)
    parser.add_argument('inputs', help='The input fasta file.', nargs='+')

    args = parser.parse_args()

    os.makedirs('tmp', exist_ok=True)

    combs = [
        (args.inputs[i], args.inputs[k]) for i in range(len(args.inputs)) for k in range(len(args.inputs))
    ]
    out = '\t' + '\t'.join(args.inputs) + '\n'

    p = multiprocessing.Pool(processes=args.threads)
    result = p.map(get_ani, combs)
    p.close()
    p.join()

    for tmp_file in os.listdir('tmp'):
        os.remove(f'tmp/{tmp_file}')
    os.rmdir('tmp')

    i = 0

    for input_file_1 in args.inputs:
        out += f'{input_file_1}\t'
        for input_file_2 in args.inputs:
            out += f'{result[i]}\t'
            i += 1
        out = out.rstrip() + '\n'

    with open(args.output, 'w') as f:
        f.write(out.rstrip())
