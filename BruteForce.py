import itertools
import score


def Brutal(DNA, k):
    '''The BruteForce function forcibly checks all possible permutations of the inserted DNA sequences
     in order to find the most similar motifs. It is performed at the beginning of the loop which
    checks all lines for all possible mer positions (N-k + 1). The products method from the intertools library,
    repeated M times, is used for this. As a result, successive permutations are checked, each being the
    variable s. Each time the score for 's' is checked. If it is greater than the previous highest value
    and initially has 0, it becomes the highest value itself (bestscore), and 's' overrides the 'bestMotif'
    volatility. The result is a collection of top mer positions that the next loop's instructions turn into
    a theme list that is returned.'''
    M = len(DNA)
    N = len(DNA[0])
    if (len(DNA[0]) < k):
        return ([0])
    bestscore = 0
    bestMotif = []
    bestscore = 0
    for s in itertools.product(range(N - k + 1), repeat=M):
        if score.Score(s, DNA, k) > bestscore:
            bestscore = score.Score(s, DNA, k)
            bestMotif = s
    i = 0
    Motywy = []
    while (i < M):
        Motywy.append(DNA[i][bestMotif[i]:bestMotif[i] + k])
        i = i + 1
    return (Motywy)


if __name__ == '__main__':
    dna = [('ggcgttcaggca'), ('aagaatcagtca'), ('caaggagttcgc'), ('cacgtcaatcac'), ('caataatattcg')]
    print(Brutal(dna, 5))
    assert (Brutal(['aaagcgaa', 'caaagacc', 'ttttcaaa'], 3)) == ['aaa', 'aaa', 'aaa'], '!'
    assert (Brutal(['cgtcggct', 'caaaggtt', 'ttttcgaa'], 3)) == ['cgt', 'caa', 'cga'], '!'
    assert (Brutal(['aaaatc', 'tgtaaa'], 3)) == ['aaa', 'aaa'], 'Nie dziala dla t<3'
    assert (Brutal(['ttacct', 'tctgtc', 'cgttag', 'ccctaa', 'cgtcag'], 3)) == ['cct',
                                                                               'tct', 'cgt', 'cct',
                                                                               'cgt'], 'dosent work for t>3'
    assert (Brutal(['aaa'], 3)) == ['aaa'], 'dosent work for t=1'
    assert (Brutal([''], 3)) == [0], 'doesnt display error message'
    print('ok')