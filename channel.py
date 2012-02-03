import re
import zipfile

pattern = re.compile(r'^Next nothing is ([0-9]*)$')
f = zipfile.ZipFile('channel.zip')

files = f.namelist()
comments = []
next = '90052'

while files:
    name = next + '.txt'
    content = f.read(name)
    comments.append(f.getinfo(name).comment)
    match = pattern.findall(content)
    if match:
        next = match[0]
    else:
        break
f.close()

print ''.join(comments)

