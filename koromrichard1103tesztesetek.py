import unittest
def abs_max(a:int,b:int)-> int:
    if abs(a)>abs(b):
        print(abs(a))

    elif abs(b)>abs(a):
        print(abs(b))
    else:
        print("EGYENLŐ")

class tesztnagyobb(unittest.TestCase):
    def test_two_positive(self):
        fgv=abs_max(5,-7)
        print(fgv)

unittest.main()