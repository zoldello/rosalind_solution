#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Rabbits and Recurrence Relations
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/
'''
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC
import validator


def get_highest_GC_Content_from_fasta(fasta_records):
    round_num = 6

    if not fasta_records or (fasta_records.strip and not fasta_records.strip()):
        return None

    # remove first '>' to avoid empty string as first entry during later split
    # this results in fasta moving from string to a list
    fastas_items = fasta_records.strip('>').split('>')
    fastas = {}

    # map fastas_record to dict of fasta items
    for fasta in fastas_items:
        items = fasta.split('\n')
        id = items[0];
        dna_string = ''.join(items[1:])
        if not validator.is_string_valid_dna_string(dna_string):
            raise ValueError('DNA String in Fasta is invalid')
        seq = Seq(dna_string, generic_dna)
        fastas[id] = seq
    
    # get GC content information
    id_GCs_pair = { k:round(GC(v), round_num) for k, v in fastas.items() }
    max_GC = max(id_GCs_pair.values())
    max_id_GC_pair = { k:v for k,v in id_GCs_pair.items() if v == max_GC }

    # this condition may be a sign the file has an error
    if (len(max_id_GC_pair) == 0):
        return None

    max_id, max_GC= list(max_id_GC_pair.items())[0]
    return f'{max_id}\n{max_GC}';


def main():
    fastas_records = input('Input fastas to get max GC: ')
    max_GC = get_highest_GC_Content_from_fasta(fastas_records)
    print(max_GC)


if __name__ == '__main__':
    main()
