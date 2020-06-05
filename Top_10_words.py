# Top 10 words
# File source: https://www.fda.gov/consumers/consumer-updates/what-gene-therapy-how-does-it-work

fhand = open('genetherapy.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    x = (value, key)
    lst.append(x)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key, value)
