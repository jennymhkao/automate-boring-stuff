#!/usr/bin/env python3
# tablePrinter.py - take a list of strings and display in a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) >= colWidths[i]:
                colWidths[i] = len(table[i][j])
    
    for b in range(len(table[0])):
        printList = []
        for a in range(len(table)):
            printList.append(table[a][b])
        for item in printList:
            print(item.rjust(colWidths[printList.index(item)]), end = ' ')
        print('')

printTable(tableData)