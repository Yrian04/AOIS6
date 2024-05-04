from src.hash_table import HashTable


table = HashTable()
table['FG'] = 1
table['FGD'] = 2
table['EE'] = 5
print(table['FG'], table['FGD'])

table['FG'] = 3
print(table['FG'])

for key in table:
    print(key)

print('-'*10)
del table['FG']
for key in table:
    print(key)
