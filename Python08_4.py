#!/usr/bin/env python3
import re
sequencia = {}
codons_frames = {}

with open ("Python_08.fasta") as fasta:
    for linha in fasta:
        linha = linha.rstrip()
        if linha.startswith(">"):
            linhas_juntas = ""
            geneId = re.search(r"^>([\w]{8,10})", linha).group(1)
        else:
            linhas_juntas += linha.strip().upper()
        sequencia[geneId] = "".join(linhas_juntas)
        
for geneId in sequencia.keys():
    reverseSeq = sequencia[geneId][::-1]
    reverseSeq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    reverseSeq = reverseSeq.upper()
    codons_frames[geneId] = {}
    for frame in range(3):
        codons = re.findall(r".{3}", sequencia[geneId][frame:])
        frameId = "frame_+" + str(frame+1)
        codons_frames[geneId][frameId] = codons
        codonsReverse = re.findall(r".{3}", reverseSeq[frame:])
        frameId_reverse = "frame_-" + str(frame+1)
        codons_frames[geneId][frameId_reverse] = codonsReverse
            
with open ("Python_08.codons-6frames.nt", "w") as outputFile:
    for geneId in codons_frames.keys():
        for frame in codons_frames[geneId]:
            headline = geneId + "_" + frame + "\n"
            outputFile.write(headline)
            codons = " ".join(codons_frames[geneId][frame]) + "\n"
            outputFile.write(codons)





