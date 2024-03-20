#!/usr/bin/python3

# Quick check that code 11 table matches expectation.

codon_to_aa = {'TTT':'F', 'TTC':'F',
               'TTA':'L', 'TTG':'L',
               'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
               'TAT':'Y', 'TAC':'Y',
               'TAA':'*', 'TAG':'*',
               'TGT':'C', 'TGC':'C',
               'TGA':'*',
               'TGG':'W',
               'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
               'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
               'CAT':'H', 'CAC':'H',
               'CAA':'Q', 'CAG':'Q',
               'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
               'ATT':'I', 'ATC':'I', 'ATA':'I',
               'ATG':'M',
               'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
               'AAT':'N', 'AAC':'N',
               'AAA':'K', 'AAG':'K',
               'AGT':'S', 'AGC':'S',
               'AGA':'R', 'AGG':'R',
               'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
               'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
               'GAT':'D', 'GAC':'D',
               'GAA':'E', 'GAG':'E',
               'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

possible_start_codons = set(['ATG', 'ATT', 'ATC', 'ATA', 'CTG', 'GTG', 'TTG'])

obs_codon_to_aa = {}
obs_possible_start_codons = set()

with open('../genetic_codes/code11.tsv', 'r') as code11:
    code11.readline()
    for line in code11:
        line = line.rstrip()
        linesplit = line.split('\t')

        obs_codon_to_aa[linesplit[0]] = linesplit[1]

        if linesplit[2] == 'yes':
            obs_possible_start_codons.add(linesplit[0])

if codon_to_aa != obs_codon_to_aa:
    raise ValueError('codon_to_aa does not match expected')

if possible_start_codons != obs_possible_start_codons:
    raise ValueError('possible_start_codons does not match expected')
