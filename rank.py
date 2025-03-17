import itertools
def find_word(rank, length):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    permutations = itertools.permutations(characters, r = length)
    for i, p in enumerate(permutations):
        if i + 1 == rank:
            return ''.join(p)
rank = int(input().strip())
length = int(input().strip())
result = find_word(rank, length)
print(result, end="")