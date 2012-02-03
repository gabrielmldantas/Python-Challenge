def morris(x='1'):
    while True:
        l = [i for i in x]
        g = []
        t = 0
        a = l[0]
        while l:
            if l[0] == a:
                t += 1
                l.pop(0)
            else:
                g.append(str(t) + a)
                t = 0
                a = l[0]
            if not l:
                g.append(str(t) + a)
        next_ = ''.join(g)
        yield next_
        x = next_

g = morris()
for i in xrange(29):
    g.next()

print len(g.next())
