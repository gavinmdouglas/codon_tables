#!/usr/bin/python3

# Conver ASN.1-style codon table (in text format) info downloaded from NCBI
# to a version that is more intuitive to parse.

first_id = True

with open('../combined_table/codon_tables.tsv', 'w') as codon_out:
    with open('../combined_table/gc.prt', 'r') as asn1_in:
        for line in asn1_in:
            line = line.rstrip()

            # Skip lines that do not start with space.
            if len(line) == 0 or line[0] != ' ':
                continue

            linesplit = line.split()

            if linesplit[0] == 'id':
                if first_id:
                    first_id = False
                else:
                    print('', file=codon_out)

                print('id' + '\t' + linesplit[1], file=codon_out)
            elif linesplit[0] == 'ncbieaa':
                print('ncbieaa' + '\t' + linesplit[1].replace('"', '').replace(',', ''), file=codon_out)
            elif linesplit[0] == 'sncbieaa':
                print('sncbieaa' + '\t' + linesplit[1].replace('"', ''), file=codon_out)
            elif linesplit[0] == '--':
                print(linesplit[1] + '\t' + linesplit[2], file=codon_out)
