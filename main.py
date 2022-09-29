import BruteForce as Brute

import Consensus as c

DNA = ['tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
       'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
       'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
       'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
       'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
       'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
       'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta',
       'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
       'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
       'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg']

k = 79

wynik = Brute.Brutal(DNA, k)
a = c.consensus(wynik)
print(c.consensus(wynik))
'''
try:
    plik=open("Brute.txt",'w+')
    print(plik.read())
except IOError:
    print("\nBlad dostepu do pliku")

try:
    plik.write('przy merze'+str(k)+'wynik wynosi\n'+a)
except IOError:
    print("\nBlad zapisu")
plik.close()

assert(len(c.consensus(wynik)))==k,'doszlo do bledu zwiazanego z k-merami'
'''