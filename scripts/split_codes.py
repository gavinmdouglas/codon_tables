#!/usr/bin/python3

import sys

# Split each code into a separate file (that is really easy to parse).

current_id = None
aa_map = None
stop_and_start = None
base1 = None
base2 = None
base3 = None

with open('../combined_table/codon_tables.tsv', 'r') as codon_tab:
    for line in codon_tab:
        line = line.rstrip()

        if len(line) == 0:
            continue

        linesplit = line.split('\t')

        if linesplit[0] == 'id':
            current_id = linesplit[1]
        elif linesplit[0] == 'ncbieaa':
            aa_map = linesplit[1]
        elif linesplit[0] == 'sncbieaa':
            stop_and_start = linesplit[1]
        elif linesplit[0] == 'Base1':
            base1 = linesplit[1]
        elif linesplit[0] == 'Base2':
            base2 = linesplit[1]
        elif linesplit[0] == 'Base3':
            base3 = linesplit[1]

            # Sanity check that all other variables are set.
            if current_id is None or aa_map is None or stop_and_start is None or base1 is None or base2 is None or base3 is None:
                raise ValueError('One or more variables not set')

            # Sanity check that all variables are the same length.
            if len(aa_map) != len(stop_and_start) or len(aa_map) != len(base1) or len(aa_map) != len(base2) or len(aa_map) != len(base3):
                raise ValueError('One or more variables are not the same length')

            # Sanity check that length is 64.
            if len(aa_map) != 64:
                raise ValueError('Code length is not 64')

            # Write out to file.
            with open('../genetic_codes/code' + current_id + '.tsv', 'w') as out_file:

                out_file.write('codon\tamino_acid\tpossible_start\n')

                for i in range(64):
                    aa = aa_map[i]
                    misc = stop_and_start[i]

                    # Check if misc character is something other than -, M, or *:
                    if misc != '-' and misc != 'M' and misc != '*':
                        print(current_id, file=sys.stderr)
                        print(misc, file=sys.stderr)
                        sys.exit('Misc character is not - or M or *?')

                    nucl1 = base1[i]
                    nucl2 = base2[i]
                    nucl3 = base3[i]

                    codon = nucl1 + nucl2 + nucl3

                    # Sanity check that if this is a stop codon, that it was listed as such in both the ncbieaa and sncbieaa lines.
                    if aa == '*' and misc != '*' or aa != '*' and misc == '*':

                        # Apparently codes 27, 28, and 31 are weird, and the stop codons sometimes code for AAs.
                        if current_id == '27' or current_id == '28' or current_id == '31':
                            aa = aa + '/' + '*'
                        else:
                            print(current_id, file=sys.stderr)
                            print(aa_map, file=sys.stderr)
                            print(stop_and_start, file=sys.stderr)
                            sys.exit('Stop codon mismatch between ncbieaa and sncbieaa lines?')

                    if misc == 'M':
                        alt_start = 'yes'
                    else:
                        alt_start = 'no'

                    out_file.write(codon + '\t' + aa + '\t' + alt_start + '\n')

            # Reset variables.
            current_id = None
            aa_map = None
            stop_and_start = None
            base1 = None
            base2 = None
            base3 = None
