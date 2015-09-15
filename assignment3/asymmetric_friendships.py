import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    for v in list(set(list_of_values)):
      mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
