#!/usr/bin/python3
"""
Parses blocks of text into useful structures
"""
__author__ = 'heliosantos99@gmail.com (Helio Santos)'


import tkinter

def getMatrix(raw=None, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
    if raw is None:
        raw = get_from_clipboard()
    rawRows = [x.strip() for x in raw.split(lineSeparator)]
    rows = []
    for n, rawRow in enumerate(rawRows):
        if not rawRow or n < numLinesToIgnore:
            continue
        row = [x.strip() for x in rawRow.split(columnSeparator)]
        rows.append(row)
    return rows

def getList(raw=None, columnIndex=0, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
    mtx = getMatrix(raw, columnSeparator, lineSeparator, numLinesToIgnore)
    return [x[columnIndex] for x in mtx]
    
def getSet(raw=None, columnIndex=0, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0): 
    return set(getList(raw, columnIndex, columnSeparator, lineSeparator, numLinesToIgnore))

def get_from_clipboard():
    r = tkinter.Tk()
    text = r.clipboard_get()
    r.withdraw()
    r.update()
    r.destroy()
    return text