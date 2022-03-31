def reverse_complement(dna):
    revers = dna[::-1]
    list = []
    for i in range(0, len(revers)):
        if revers[i] == "A":
            list.append('T')
        if revers[i] == "T":
            list.append('A')
        if revers[i] == "G":
            list.append('C')
        if revers[i] == "C":
            list.append('G')
        result = ''.join(list)
    return result
