#!/usr/bin/env python3
import re
sequencias = {}

with open ("Python_08.fasta") as fasta:
    for linha in fasta:
        if linha.startswith(">"):
            geneId = re.search(r">([\w]{8,10})", linha).group(1)
            sequencias[geneId] = ""
        else:
            linha = linha.strip().replace("\n", "")
            sequencias[geneId] += linha
for geneId, sequencia in sequencias.items():
    for frames in range(3):
        headline = geneId + "-frame-"+ str(frames+1) + "codons"
        print(headline)
        frame = sequencia[frames:]
        framePrint = re.findall(r".{3}", frame)
        print(framePrint, "\n")
