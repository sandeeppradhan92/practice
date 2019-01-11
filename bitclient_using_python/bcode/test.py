import unittest

from bencode import encode
from bdecode import decode


test_raw_values = [
    "this",
    12,
    [1,2,'3', ['a','b',16]],
    {'a':1, 'b':[1,2,'3', ['a','b',{'a':16}]]}
]

test_encoded_values = [
    "4:this",
    "i12e",
    "li1ei2e1:3l1:a1:bi16eee",
    "d1:ai1e1:bli1ei2e1:3l1:a1:bd1:ai16eeeee"
]


class TestBendecode(unittest.TestCase):
    def test_encode(self):
        for i in range(len(test_raw_values)):
            res = encode(test_raw_values[i])
            self.assertEqual(res, test_encoded_values[i])
    def test_decode(self):
        for i in range(len(test_encoded_values)):
            res = decode(test_encoded_values[i])
            self.assertEqual(res, test_raw_values[i])
    def test_encode_decodeing(self):
        for i in range(len(test_raw_values)):
            res = decode(encode(test_raw_values[i]))
            self.assertEqual(res, test_raw_values[i])

if __name__=="__main__":
    unittest.main()
