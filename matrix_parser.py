#!/usr/bin/python3
"""
Parses blocks of text into useful structures
"""
__author__ = 'heliosantos99@gmail.com (Helio Santos)'


def getMatrix(raw, columnSepparator=',', rowSepparator='\n'):
    rawRows = [x.strip() for x in raw.split(rowSepparator)]
    rows = []
    for rawRow in rawRows:
        if not rawRow:
            continue
        row = [x.strip() for x in rawRow.split(columnSepparator)]
        rows.append(row)
    return rows

def getList(raw, columnIndex=0, columnSepparator=',', rowSepparator='\n'):
    mtx = getMatrix(raw, columnSepparator, rowSepparator)
    return [x[columnIndex] for x in mtx]
    
def getSet(raw, columnIndex=0, columnSepparator=',', rowSepparator='\n'):   
    return set(getList(raw, columnIndex, columnSepparator, rowSepparator))
