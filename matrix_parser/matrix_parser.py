#!/usr/bin/python3
"""
parse text into a matrix
"""
__author__ = 'heliosantos99@gmail.com (Helio Santos)'

from matrix_parser import MatrixParserBase

class MatrixParser(object):
    """docstring for MatrixParser"""
    def __init__(self):
        super(MatrixParser, self).__init__()
        self.rowNames = {}
        self.colNames = {}
    
    def parse(self, raw, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
        matrix = MatrixParserBase()
        matrix.parse(raw, columnSeparator, lineSeparator, numLinesToIgnore)
        self._prepare(matrix)

    def parse_from_clipboard(self, columnSeparator=',', lineSeparator='\n', numLinesToIgnore=0):
        matrix = MatrixParserBase()
        matrix.parse_from_clipboard(columnSeparator, lineSeparator, numLinesToIgnore)
        self._prepare(matrix)

    def _prepare(self, matrix):
        rows = MatrixSegment(self.rowNames)
        for i in range(matrix.maxHeight):
            rows.append(MatrixSegment(self.colNames))

        cols = MatrixSegment(self.colNames)
        for i in range(matrix.maxWidth):
            cols.append(MatrixSegment(self.rowNames))

        for i in range(matrix.maxHeight):
            for j in range(matrix.maxWidth):
                cell = MatrixCell(matrix[i][j] if j < len(matrix[i]) else None)
                if cell.val:
                    rows[i].append(cell)
                cols[j].append(cell)

        self.rows = rows
        self.cols = cols

    def __getitem__(self, idx):
        return self.rows[idx]

    def set_row_name(self, idx, name):
        self.rowNames[name] = idx

    def set_col_name(self, idx, name):
        self.colNames[name] = idx

    def transform(self, transformationLambda):
        for segment in self:
            segment.transform(transformationLambda)


class MatrixCell(object):
    """docstring for MatrixCell"""
    def __init__(self, val):
        super(MatrixCell, self).__init__()
        self.original = val
        self.val = val
    
    def transform(self, transformationLambda):
        self.val = transformationLambda(self.val)


class MatrixSegment(list):
    """docstring for MatrixSegment"""
    def __init__(self, names=None):
        self.base = super(MatrixSegment, self)
        self.base.__init__()
        self.names = {} if names is None else names

    def __getitem__(self, idx):
        if type(idx) is str:
            if idx in self.names:
                idx = self.names[idx]
            else:
                raise Exception("Name not found")
        return self.base.__getitem__(idx)

    def transform(self, transformationLambda):
        for segment in self:
            segment.transform(transformationLambda)



if __name__ == '__main__':
    raw = '''
    11,12 ,a;b;c,13,14,15
    21,22,d;e;f,23,24
    31,32,g;h;i,33,34,35
    41,42,j;k;l,43,44,45,46,47,48
    51,52,m;n;o,53,54,55
    ,,p;q;r,53,54,55
    '''

    parser = MatrixParser()
    parser.parse(raw)

    parser.rows[1].transform(lambda x: x + "...")
    parser.cols[2].transform(lambda x: x.split(';'))
    for x in parser:
        for y in x:
            print(y.val, end=' ')
        print()

    

