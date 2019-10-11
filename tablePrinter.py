tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    #for i in range(len(table)):
    i = 0
    for e in range(len(table[i])):
        print(table[i][e].rjust(7),end="")
        print(table[i+1][e].rjust(7),end="")
        print(table[i+2][e].rjust(7))       
printTable(tableData)
