import string

letras = string.ascii_lowercase
#f = lambda letra: chr(97 + ((ord(letra) - 97 + 2) % 26))
texto = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def translate(letra):
    r = divmod(ord(letra)+2, 123)
    if r[0] == 0:
        return chr(r[1])
    else:
        return chr(r[1] + 97)

for letra in texto:
    if letra.isalpha():
        print translate(letra),
    else:
        print letra,
print '\n'

url = "map"
for letra in url:
    print translate(letra),
print
