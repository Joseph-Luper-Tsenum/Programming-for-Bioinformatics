#!/usr/bin/env python3

"""
The implementation of algorithm that finds the overlapping regions from 2 BED files.
"""

import argparse
import time


if __name__ == "__main__":

    script_start = time.time()

    parser = argparse.ArgumentParser(
        description='Find overlapping regions from 2 BED files.')
    parser.add_argument('-i1', '--input_1', type=str, help='The path to the first BED file.', required=True)
    parser.add_argument('-i2', '--input_2', type=str, help='The path to the second BED file.', required=True)
    parser.add_argument('-m', '--min_overlap', type=float, help='The percentage of minimum overlap between 2 regions.',
                        required=True)
    parser.add_argument('-j', '--join', help='If join the two entries from 2 BED files.', action='store_true')
    parser.add_argument('-o', '--output', type=str, help='The path to the output file.', required=True)

    args = parser.parse_args()

    with open(args.input_1, 'r') as f:
        input_1 = [line.replace('\t', ' ').strip().split(' ') for line in f.readlines()]  # bringing to the same format

    with open(args.input_2, 'r') as f:
        input_2 = [line.replace('\t', ' ').strip().split(' ') for line in f.readlines()]  # bringing to the same format

    out = ''
    curr_ind_1 = 0
    curr_ind_2 = 0

    while curr_ind_1 < len(input_1) and curr_ind_2 < len(input_2):
        chr_1, st_1, end_1 = input_1[curr_ind_1][0], int(input_1[curr_ind_1][1]), int(input_1[curr_ind_1][2])
        chr_2, st_2, end_2 = input_2[curr_ind_2][0], int(input_2[curr_ind_2][1]), int(input_2[curr_ind_2][2])
        if 'X' in chr_1 or 'Y' in chr_1:
            chr_1 = chr_1.replace('X', '23')
            chr_1 = chr_1.replace('Y', '24')
        if 'X' in chr_2 or 'Y' in chr_2:
            chr_2 = chr_2.replace('X', '23')
            chr_2 = chr_2.replace('Y', '24')
        # the first chromosome has lower index than the second chromosome
        if int(chr_1[chr_1.find('r') + 1:]) < int(chr_2[chr_2.find('r') + 1:]):
            curr_ind_1 += 1
        elif int(chr_1[chr_1.find('r') + 1:]) > int(chr_2[chr_2.find('r') + 1:]):  # reverse situation
            curr_ind_2 += 1
        else:
            min_overlap = (end_1 - st_1) / 100 * args.min_overlap

            # We have 9 situations:
            # 1) There is no overlap, the first region is on the left from the second region
            # 2) There is no overlap, the first region is on the right from the second region
            # 3) There is overlap, but it's still less than min_overlap - the first region is slightly on the left from
            # the second region
            # 4) There is overlap, but it's still less than min_overlap - the first region is slightly on the right from
            # the second region
            # 5) There is overlap, and it's bigger than min_overlap - the first region is slightly on the left from the
            #       second region - MATCH!
            # 6) There is overlap, but it's bigger than min_overlap - the first region is slightly on the right from the
            #       second region - MATCH!
            # 7) There is overlap, the first region is inside the second region
            # 8) There is overlap, the overlap is less than min_overlap, the second region is inside the first region
            # 9) There is overlap, the overlap is bigger than min_overlap, the second region is inside the first region

            if end_1 < st_2:  # 1)
                curr_ind_1 += 1
            elif end_2 < st_1:  # 2)
                curr_ind_2 += 1
            elif (end_1 < end_2) and (st_1 < st_2) and ((end_1 - st_2 + 1) < min_overlap):  # 3)
                curr_ind_1 += 1
            elif (end_2 < end_1) and (st_2 < st_1) and ((end_2 - st_1 + 1) < min_overlap):  # 4)
                curr_ind_2 += 1
            elif ((end_1 < end_2) and (st_1 < st_2)) or ((end_2 < end_1) and (st_2 < st_1)):  # 5) and 6)
                if args.join:
                    out = out + '\t'.join(input_1[curr_ind_1]) + '\t' + '\t'.join(input_2[curr_ind_2]) + '\n'
                else:
                    out = out + '\t'.join(input_1[curr_ind_1]) + '\n'

                if end_1 <= end_2:  # 5)
                    curr_ind_1 += 1
                if end_2 <= end_1:  # 6)
                    curr_ind_2 += 1
            elif st_1 >= st_2:  # 7)
                if args.join:
                    out = out + '\t'.join(input_1[curr_ind_1]) + '\t' + '\t'.join(input_2[curr_ind_2]) + '\n'
                else:
                    out = out + '\t'.join(input_1[curr_ind_1]) + '\n'
                curr_ind_1 += 1
            else:  # 8) and 9)
                if (end_2 - st_2) >= min_overlap:
                    if args.join:
                        out = out + '\t'.join(input_1[curr_ind_1]) + '\t' + '\t'.join(input_2[curr_ind_2]) + '\n'
                    else:
                        out = out + '\t'.join(input_1[curr_ind_1]) + '\n'
                curr_ind_2 += 1

    with open(args.output, 'w') as f:
        f.write(out)

    print(f"Minutes elapsed: {(time.time() - script_start) / 60}")
