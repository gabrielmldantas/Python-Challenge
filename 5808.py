import Image

cave = Image.open('cave.jpg')
img1 = Image.new('RGB', cave.size)
img2 = Image.new('RGB', cave.size)

for x in range(cave.size[0]):
    for y in range(cave.size[1]):
        if (x + y) % 2 == 0:
            img1.putpixel((x, y), cave.getpixel((x, y)))
        else:
            img2.putpixel((x, y), cave.getpixel((x, y)))

img1.save('1.jpg')
img2.save('2.jpg')

