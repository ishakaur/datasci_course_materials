import MapReduce
import sys
import collections
import numpy

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# A = MxN
# B = NxL
# both are square matrices of 5x5 each
M = 5
N = 5
L = 5
A = 'a'
B = 'b'
indices = range(N)

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    for k in indices:
        if matrix == A:
            mr.emit_intermediate((i, k), record)
        else:
            mr.emit_intermediate((k, j), record)

def reducer(key, list_of_values):
    # key: index of resulting matrix
    # value: list of values that will go into the product
    a = [0]*N
    b = [0]*N
    for v in list_of_values:
        if v[0] == A:
            a[v[2]] = v[3]
        else:
            b[v[1]] = v[3]
    dot_product = numpy.dot(a, b)
    mr.emit((key[0], key[1], dot_product))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
