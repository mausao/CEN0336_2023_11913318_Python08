#!/usr/bin/env python3
import re
genes = {}
with open ("Python_08.fasta", "r") as fasta:
    for linha in fasta:
        if linha.startswith(">") == True:
            indices = re.split("\s", linha)
            geneName = indices[0]
            if geneName not in genes:
                genes[geneName] = {}
        else:
            nt = re.split("\n", linha)
            bases = "".join(nt[0])
            for aa in bases:
                if aa not in genes[geneName]:
                    genes[geneName][aa] = 1
                else:
                    genes[geneName][aa] += 1
    for geneName, aa_count in genes.items():
        for base, count in aa_count.items():
            print(f"{geneName} {base}: {count}")
        print("\n")
