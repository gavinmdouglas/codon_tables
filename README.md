# codon_tables
Parsed, simplified alternative codon tables. This repository contains the common NCBI alternative codon tables (*with alternative start codons*) in a simple format that is easier to parse for quick scripts.

## Data tables
`code_info/` contains the codon tables in the most convenient format per code. These files are tab-delimited with self-explanatory columns. Stop codons are indicated with "\*" in the "amino\_acid" column. Note that for codes 27, 28, and 31, that the amino acid can be either "\*" or an actual amino acid, which is indicated with a "/". The "possible\_start" column indicates whether a codon can be a possible start codon, and code for M, when they are the initial codon in a sequence. 

The codes are also in the original NCBI format in combined tables within `combined_table`.


## Processing
I downloaded the (text) ASN.1 format of alternative codon tables (`gc.prt`) from NCBI (ftp://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt) on March 19th, 2024. 

I then converted this to a simple tab-delimited format (output to `codon_tables.tsv`) using `scripts/simplify_codon_asn1.py`.

I then split this combined table into individual tables per code (output to `code_info/`) with `scripts/split_codes.py`.
