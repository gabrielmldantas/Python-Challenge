import re

pattern = re.compile(r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]')
with open('equality.txt', 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            print match.groups()[0],
print