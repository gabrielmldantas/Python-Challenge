import Image
import re

image = Image.open('oxygen.png')
secret = ['s']
i = 5

while i < 629:
    secret.append(chr(image.getpixel((i, 43))[0]))
    i += 7
secret = ''.join(secret)
print secret

pattern = re.compile(r'\[(.*)\]\]')
exp = pattern.findall(secret)[0]
chars = map(chr, [int(char.lstrip()) for char in exp.split(',')])
print ''.join(chars)

