import requests
import word_counter

url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

response = requests.get(url)

# print(response.text)

print(word_counter.find_most_common_words((response.text), number=10))
