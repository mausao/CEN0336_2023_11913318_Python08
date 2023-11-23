#!/usr/bin/env python3
import re
sequencia = {}

with open ("Python_08.fasta") as fasta:
    for linha in fasta:
        linha = linha.rstrip()
        if linha.startswith(">"):
            linhas_juntas = ""
            geneId = re.search(r"^>([\w]{8,10})", linha).group(1)
        else:
            linhas_juntas += linha.strip()
        sequencia[geneId] = "".join(linhas_juntas)
        
with open ("Python_08.codons-frame-1.nt", "w") as outputFile:
    for geneId in sequencia.keys():
        codons = re.findall(r".{3}", sequencia[geneId])
        headline = geneId + "-frame-1-codons\n"
        outputFile.write(headline)
        outputFile.write(" ".join(codons) + "\n")
