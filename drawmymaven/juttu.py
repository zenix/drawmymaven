import string
search = 'wrote dependency tree to: '
str = '[INFO] wrote dependency tree to: /Users/a121865/SW/git/omaelisa/omaelisa/ya/palveluikkuna/corporate-ip-network-management-application/tree.txt'
position = str.index(search) + len(search)
print str[position:len(str)]