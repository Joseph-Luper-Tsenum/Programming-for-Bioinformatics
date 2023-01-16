#!/usr/bin/env python3

"""
The implementation of algorithm that counts the sequence coverage from BED file.
"""

import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Compute sequence coverage from BED file.')
    parser.add_argument('-i', '--input', type=str, help='The path to input file name.', required=True)

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        input_lines = [line.replace('\t', ' ').strip() for line in f.readlines()]  # bringing to the same format

    chr_coord_dict = {}

    # Transforming chromosome coordinates into convenient format
    for line in input_lines:
        chr, st, end = line.split(' ')
        if chr not in chr_coord_dict:
            chr_coord_dict[chr] = [(int(st), int(end))]
        else:
            chr_coord_dict[chr] += [(int(st), int(end))]

    for chr, ints in chr_coord_dict.items():
        # Getting boundaries of input coordinates
        min_coord, max_coord = min(ints, key=lambda x: x[0])[0], max(ints, key=lambda x: x[1])[1]

        # The idea behind algorithm is next:
        # We got the minimum and maximum position of the coordinates for a certain chromosome
        # Now we will create a list that has the length of max_coord - min_coord + 1, the list is called 'coverage'
        # Next, we will iterate over each interval and fill with 1 the 'coverage' list at the places that correspond to
        #   this interval
        # Eventually we will have a list (or array) like this: [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 1, 1]
        # The first coverage period is [1, 1, 1], then [2, 2], then [3, 3, 3, 3, 3], and finally [1, 1]

        coverage = [0]*(max_coord - min_coord + 1)
        for st, end in ints:
            for i in range(st - min_coord, end - min_coord):
                coverage[i] += 1

        cover_st = 0
        curr_cover = coverage[0]

        for i in range(1, len(coverage)):
            if coverage[i] != curr_cover:
                print(f'{chr}\t{cover_st+min_coord}\t{i+min_coord}\t{curr_cover}')
                curr_cover = coverage[i]
                cover_st = i

