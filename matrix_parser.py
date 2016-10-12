#!/usr/bin/python3
"""
Parses blocks of text into useful structures
"""
__author__ = 'heliosantos99@gmail.com (Helio Santos)'

import tkinter


class MatrixParser:

    def __init__(self):
        self.columnNames = {}
        self.rowNames = {}

    def parse(raw, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
        rawRows = [x.strip() for x in raw.split(lineSeparator)]
        rows = []
        ignoredRows = []
        for n, rawRow in enumerate(rawRows):
            if not rawRow or n < numLinesToIgnore:
                ignoredRows.append(rawRow)
                continue
            row = [x.strip() for x in rawRow.split(columnSeparator)]
            rows.append(row) 

        parser = MatrixParser()       
        parser.matrix = rows
        parser.ignoredRows = ignoredRows
        return parser

    def parse_from_clipboard(columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
        r = tkinter.Tk()
        text = r.clipboard_get()
        r.withdraw()
        r.update()
        r.destroy()
        return MatrixParser.parse(text, columnSeparator, lineSeparator, numLinesToIgnore)

    def get_row(self, rowIndex):
        rowIndex = self._to_row_index(rowIndex)
        return self.matrix[rowIndex]

    def get_column(self, columnIndex):
        columnIndex = self._to_column_index(columnIndex)
        return [x[columnIndex] for x in self.matrix]

    def get_cell(self, rowIndex, columnIndex):
        rowIndex = self._to_row_index(rowIndex)
        columnIndex = self._to_column_index(columnIndex)
        return self.matrix[rowIndex][columnIndex]

    def get_row_set(self, rowIndex):
        rowIndex = self._to_row_index(rowIndex)
        return set(self.get_row(rowIndex))

    def get_column_set(self, columnIndex):
        columnIndex = self._to_column_index(columnIndex)
        return set(self.get_column(columnIndex))

    def transform_cell(self, rowIndex, columnIndex, transformationLambda):
        rowIndex = self._to_row_index(rowIndex)
        columnIndex = self._to_column_index(columnIndex)
        self.matrix[rowIndex][columnIndex] = transformationLambda(self.matrix[rowIndex][columnIndex])

    def transform_row(self, rowIndex, transformationLambda):
        rowIndex = self._to_row_index(rowIndex)
        for columnIndex in range(len(self.matrix[rowIndex])):
            self.transform_cell(rowIndex, columnIndex, transformationLambda)

    def transform_column(self, columnIndex, transformationLambda):
        for rowIndex in range(len(self.matrix)):
            self.transform_cell(rowIndex, columnIndex, transformationLambda)

    def transform_matrix(self, transformationLambda):
        for rowIndex in range(len(self.matrix)):
            self.transform_row(rowIndex, transformationLambda)

    def _to_row_index(self, rowIndexOrName):
        if rowIndexOrName in self.rowNames:
            return self.rowNames[rowIndexOrName]
        return rowIndexOrName

    def _to_column_index(self, columnIndexOrName):
        if columnIndexOrName in self.columnNames:
            return self.columnNames[columnIndexOrName]
        return columnIndexOrName

    def set_column_name(self, columnIndex, columnName):
        self.columnNames[columnName] = columnIndex

    def set_row_name(self, rowIndex, rowName):
        self.rowNames[rowName] = rowIndex


"""
depricated
"""
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


"""
depricated
"""
def getList(raw=None, columnIndex=0, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
    mtx = getMatrix(raw, columnSeparator, lineSeparator, numLinesToIgnore)
    return [x[columnIndex] for x in mtx]


"""
depricated
""" 
def getSet(raw=None, columnIndex=0, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0): 
    return set(getList(raw, columnIndex, columnSeparator, lineSeparator, numLinesToIgnore))


"""
depricated
"""
def get_from_clipboard():
    r = tkinter.Tk()
    text = r.clipboard_get()
    r.withdraw()
    r.update()
    r.destroy()
    return text

if __name__ == '__main__':
    pass
