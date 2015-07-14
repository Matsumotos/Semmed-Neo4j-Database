f = open('preds', 'r')
f2 = open('preds2', 'w')
word = f.readline().split('\t')

for line in f:
    new = line.split('\t')
    if new[0] == word[0] and new[3] == word[3] and new[4] == word[4]:
	word[2] = word[2] + '`' + new[2]
    else:
        f2.write(word[0] + '\t' + word[1] + '\t' + word[2] + '\t' + word[3] + '\t' + word[4])
        word = new

f2.write(word[0] + '\t' + word[1] + '\t' + word[2] + '\t' + word[3] + '\t' + word[4])
f.close()
f2.close()
