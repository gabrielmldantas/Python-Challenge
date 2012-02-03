with open('ocr.txt') as f:
    rare = ''
    for line in f:
        for char in line:
            if char.isalpha():
                rare += char
print rare
