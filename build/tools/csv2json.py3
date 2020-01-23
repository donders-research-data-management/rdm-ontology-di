#!/usr/bin/env python

import json
import csv
import os
import sys
import argparse

# execute the main program
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert vocabulary keywords from CSV to JSON format')

    parser.add_argument('csv_input', help='path to the input CSV file in which vocabulary keywords are defined')
    parser.add_argument('json_output', help='path to the output JSON file')
    parser.add_argument('-d', '--delimiter',
                        action='store_const',
                        default=';',
                        const=str,
                        help='the delimiter between word and context reference id')

    args = parser.parse_args()

    if os.path.exists(args.csv_input):
        # read CSV file and convert into vocabulary dictionary
        csv_f = open(args.csv_input, 'r')
        voc_dict = {}
        row_id = 0
        for row in csv.reader(csv_f, delimiter=args.delimiter):
            row_id += 1
            if len(row) < 2:
                sys.stderr.write('insufficient data columns, line: %d' % row_id)
                continue
            ref = row[-1]
            key = args.delimiter.join(row[:-1])
            voc_dict[ref] = key
        csv_f.close()

        # looping over voc_dict to update 'keyword' with hierarchy
        voc_list = []
        for id, k in voc_dict.items():
            id_fields = id.split('.')
            for i in reversed(range(0, len(id_fields)-1)):

                # find the voc with match branch id
                branch_id = '.'.join(id_fields[0:i+1])

                try:
                    k = '%s;%s' % (voc_dict[branch_id], k)
                except KeyError as e:
                    sys.stderr.write('warning: expected branch not found: %s' % branch_id)

            voc_list.append( {'keyword': k, 'id': id} )

        # sort voc_list by ID
        voc_list.sort(key=lambda x:x['id'])

        # dump vocabulary dictionary into JSON file
        json_f = open(args.json_output, 'w')
        #json.dump(voc_dict, json_f, indent=2, separators=(',',':'))
        json.dump(voc_list, json_f, indent=2, separators=(',',':'))
        json_f.close()

        exit(0)
    else:
        sys.stderr.write('file not found: %s' % args.csv_input)
        exit(1)



