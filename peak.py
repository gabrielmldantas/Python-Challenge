import pickle

f = open('banner.p', 'r')
banner = pickle.Unpickler(f).load()
f.close()
f = open('a.txt', 'w')
for line in banner:
    for element in line:
        char, repeat = element
        f.write(char * repeat)
    f.write('\n')
f.close()

