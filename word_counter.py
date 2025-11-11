from collections import Counter

def find_most_common_words(file= "/home/hanlong/python-practice/data/data.txt", number=10):
    with open(file, 'r') as f:
        lines = f.readlines()
        words = [w for line in lines for w in line.split().lower()]
        counter = Counter(words)
        return counter.most_common(number)


