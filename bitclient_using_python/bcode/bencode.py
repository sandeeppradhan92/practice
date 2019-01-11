import re
try:
    import psyco # Optional, 2.5x improvement in speed
    psyco.full()
except ImportError:
    pass


def encode_string(var):
    return str(len(var))+':'+var

def encode_integer(var):
    return 'i'+str(var)+'e'

def encode_list(var):
    enc = 'l'
    for item in var:
        enc += encode(item)
    return enc+'e'

def encode_dict(var):
    enc = 'd'
    for key in var.keys():
        enc += encode(key)
        enc += encode(var[key])
    return enc+'e'

def encode(var):
    if isinstance(var, str):
        return encode_string(var)
    elif isinstance(var, int):
        return encode_integer(var)
    elif isinstance(var, list):
        return encode_list(var)
    elif isinstance(var, dict):
        return encode_dict(var)

if __name__ == "__main__":
    print(encode("this"))
    print(encode(12))
    print(encode([1,2,'3', ['a','b',16]]))
    print(encode({'a':1, 'b':[1,2,'3', ['a','b',{'a':16}]]}))
