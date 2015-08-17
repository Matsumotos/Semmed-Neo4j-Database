# This script was used to make the bash script to run POSTs.  If the limit on the Cypher queries is 1000, the resulting file needs to be copied 9 times.

f = open('post','w')

f.write('#!bash')

first = 'abcdefg'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = 'ngd'

for letter in first:
    for a in alphabet:
        f.write('\n\ncurl -H "Content-Type: application/json" -H "Accept: application/json; charset=UTF-8" -H "X-Stream: true" -X POST -d @' + name + letter + a + ' http://137.131.57.237:7474/db/data/transaction/commit')

f.close()
