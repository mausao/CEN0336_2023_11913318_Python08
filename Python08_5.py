#!/usr/bin/env python3
import re
sequencia = {}
codons_frames = {}
protein_frames = {}
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}


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

for geneId in codons_frames.keys():
    protein_frames[geneId] = {}
    for frame in codons_frames[geneId]:
        protein = ""
        for codon in codons_frames[geneId][frame]:
            if codon in translation_table:
                protein += translation_table[codon]
            else:
                print("O codon não está presente no dicionário de tradução")
                exit()
        protein_frames[geneId][frame] = protein
        
with open ("Python_08.translated.aa", "w") as outputFile:
    for geneId in protein_frames.keys():
        for frame in protein_frames[geneId]:
            headline = geneId + "_" + frame + "\n"
            outputFile.write(headline)
            proteina = protein_frames[geneId][frame] + "\n"
            outputFile.write(proteina)
