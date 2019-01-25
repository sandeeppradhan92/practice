from inspect import Parameter, Signature

def make_signature(fields):
    return Signature(
        Parameter(field, Parameter.POSITIONAL_OR_KEYWORD)
        for field in fields)


class StructMeta(type):
    def __new__(cls, classname, bases, classdict):
        clsobj = super().__new__(cls, classname, bases, classdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj


class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for key, val in bound.arguments.items():
            setattr(self, key, val)


class Stock(Structure):
    _fields = ['name', 'amount', 'price']


