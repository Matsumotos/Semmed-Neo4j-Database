# Remove repeated words and coalesce the word's types into a list if it has multiple types
f = open('words2', 'r')
f2 = open('words3', 'w')
word = f.readline().split('\t')

for line in f:
    new = line.split('\t')
    if new[0] != word[0]:
	f2.write(word[0] + '\t' + word[1] + '\t' + word[2])
	word = new
    else:
	word[1] = word[1] + ',' + new[1]

f2.write(word[0] + '\t' + word[1] + '\t' + word[2])
f.close()
f2.close()
