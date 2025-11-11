from collections import Counter
import re

def find_most_common_words(file= "/home/hanlong/python-practice/data/donald_speech.txt", number=10):
    with open(file, 'r') as f:
        text = f.read().lower()
        words = re.findall(r"[a-zA-Z0-9']+", text)
        counter = Counter(words)
        return counter.most_common(number)

print(find_most_common_words())



