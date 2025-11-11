import re

def extract_email_list(file = "/home/hanlong/python-practice/data/email_exchanges_big.txt"):
    with open(file, 'r') as f:
        text = f.read()
        emails = re.findall(r"[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+", text)
        emails_set = set(emails)
        return emails_set

print(extract_email_list())

