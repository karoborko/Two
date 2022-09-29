
def consensus(DNA):
    '''Consensus function constructs the best motive
     The function parameters are the units of the function of the 'MotifSearch' type,
     it executes on 2 loops - one corresponds to the length of the mer, the other to their number.
     From each iteration of the inner loop, the number of nucleotides a, c, g, t in the new one,
     which corresponds to the appropriate variables, is calculated. After exiting the loop from
     the list of issued ones, the one with the highest value (max ()) is selected.
     Then it is checked which variable will be added. Finally, the full string is returned, the length
     of the mer, which corresponds to the searched consensus motif.'''
    A, C, G, T = 0, 0, 0, 0
    i = 0
    Consensus = ''
    dlugosc = len(DNA)
    while (i < len(DNA[0])):
        j = 0
        while (j < dlugosc):
            baza = DNA[j][i]
            if (baza == 'a'):
                A = A + 1
            elif (baza == 'c'):
                C = C + 1
            elif (baza == 'g'):
                G = G + 1
            elif (baza == 't'):
                T = T + 1
            j = j + 1
        maxi = max([A, C, G, T])
        if (A == maxi):
            Consensus = Consensus + 'a'
        elif (C == maxi):
            Consensus = Consensus + 'c'
        elif (G == maxi):
            Consensus = Consensus + 'g'
        elif (T == maxi):
            Consensus = Consensus + 't'
        i = i + 1
        A, C, G, T = 0, 0, 0, 0
    return (Consensus)


if __name__ == '__main__':
    assert (consensus(['acca', 'cccc', 'aaaa'])) == 'acca', 'function dosent work'
    assert (consensus([''])) == '', 'function doesnt work for emty string'
    assert (consensus(['acgca'])) == 'acgca', 'dosent work strings longer than 4'
    print('ok')