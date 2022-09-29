


def Score(s, DNA, k):
    '''Score function return value of the sequence, which is later compared
    with other sequence values in order to find a best match.
    As a parameter takes 's'- position of mer in seach line of DNA
    'DNA' - DNA sequence on witch it operates
    'k'- mer lenght .

        Score2 is a simplified version of Score function
    '''
    score = 0
    for i in range(k):
        cnt = dict(zip("acgt", (0, 0, 0, 0)))
        assert (cnt) == {'a': 0, 'c': 0, 'g': 0, 't': 0}, 'dict and zip dont work'
        for j, s_val in enumerate(s):
            base = DNA[j][s_val + i]
            cnt[base] += 1
        score += max(cnt.values())
    return score


if __name__ == '__main__':
    assert (Score([0, 1, 2], ['aagaa', 'tttat', 'aatat'], 2)) == 4, 'doesnt work correctly'
    assert (Score([0, 0, 0], ['aagaa', 'tttat', 'aatat'], 5)) == 11, 'doesnt work correctly'
    assert (Score([0, 0, 0], ['aagaa', 'tttat', 'aatat'], 0)) == 0, 'doesnt work correctly for k=0'
    assert (Score([7, 0, 0], ['aagaa', 'tttat', 'aatat'], 0)) == 0, 'doesnt work correctly for k>t'
    assert (Score([0, 0, 0], ['aagaa', 'tttat', 'aatat', 'gaagaa'], 2)) == 4, '!'
    assert (Score([0, 0, 0, 0], ['aagaa', 'tttat', 'aatat', 'gaagaa'], 2)) == 5, '!'
    assert (Score([0, 0, 0], ['aaa', 'ccc', 'ggg', 'ttt'], 3)) == 3, 'doesnt work for zero values'
    print('ok')


def Score2(s, DNA, k):
    A, C, G, T = 0, 0, 0, 0
    i = 0
    score = 0
    while (i < k):
        j = 0
        while (j < len(s)):
            baza = DNA[j][s[j] + i]
            if (baza == 'a'):
                A = A + 1
            elif (baza == 'c'):
                C = C + 1
            elif (baza == 'g'):
                G = G + 1
            elif (baza == 't'):
                T = T + 1
            j = j + 1
        score = score + max([A, C, G, T])
        i = i + 1
        A, C, G, T = 0, 0, 0, 0
    return (score)


if __name__ == '__main__':
    assert (Score2([0, 1, 2], ['aagaa', 'tttat', 'aatat'], 2)) == 4, 'doesnt work correctly'
    assert (Score2([0, 0, 0], ['aagaa', 'tttat', 'aatat'], 5)) == 11, 'doesnt work correctly'
    assert (Score2([0, 0, 0], ['aagaa', 'tttat', 'aatat'], 0)) == 0, 'doesnt work correctly for k=0'
    assert (Score2([7, 0, 0], ['aagaa', 'tttat', 'aatat'], 0)) == 0, 'doesnt work correctly for k>t'
    assert (Score2([0, 0, 0], ['aagaa', 'tttat', 'aatat', 'gaagaa'], 2)) == 4, '!'
    assert (Score2([0, 0, 0, 0], ['aagaa', 'tttat', 'aatat', 'gaagaa'], 2)) == 5, '!'
    print('ok')