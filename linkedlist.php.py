import re
import urllib

pattern = re.compile(r'and the next nothing is ([0-9]*)')
next = 12345
while True:
    doc = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' %(next))
    for content in doc:
        print content
        match = pattern.search(content)
        if match and next != 92118:
            next = match.groups()[0]
        else:
            next = str(int(next) / 2)
    print
