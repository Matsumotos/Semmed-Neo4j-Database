# Remove repeats in the list of types for each word

f = open('words3', 'r')
f2 = open('words4', 'w')
for line in f:
    types = line.split('\t')
    new = list(set(types[1].split(',')))
    f2.write(types[0] + '\t' + ','.join(new) + '\t' + types[2])
f.close()
f2.close()
