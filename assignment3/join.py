import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: attributes of the order or the lineItem
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: the string "order"
    # value: the attributes of the order and line items concatenated
    order = None
    line_items = []

    for v in list_of_values:
        if v[0] == "order":
            order = v
        else:
            line_items.append(v)
    for line_item in line_items:
        mr.emit(order + line_item)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
