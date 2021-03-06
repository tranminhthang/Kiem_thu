import unittest
import triangle
import math

class test(unittest.TestCase):
    def test_10(self):
        self.assertEquals(triangle.detect_triangle('b',5,6),"du lieu dau vao khong hop le")
    def test_11(self):
        self.assertEquals(triangle.detect_triangle(4,-5,6),"du lieu dau vao khong hop le")
    def test_12(self):
        self.assertEquals(triangle.detect_triangle(4,5,-6),"du lieu dau vao khong hop le")
        

    def test_13(self):
        self.assertEquals(triangle.detect_triangle(2**32 +40, 2**32-10, 2**32 -15),"du lieu dau vao khong hop le")
    def test_14(self):
        self.assertEquals(triangle.detect_triangle(2**32-10,2**32 +40, 2**32 -15),"du lieu dau vao khong hop le")
    def test_15(self):
        self.assertEquals(triangle.detect_triangle(2**32-10, 2**32 -15,2**32 +40),"du lieu dau vao khong hop le")
        
    def test_16(self):
        self.assertEquals(triangle.detect_triangle('b',5,6),"du lieu dau vao khong hop le")
    def test_17(self):
        self.assertEquals(triangle.detect_triangle(4,'d',6),"du lieu dau vao khong hop le")
    def test_18(self):
        self.assertEquals(triangle.detect_triangle(4,5,'e'),"du lieu dau vao khong hop le")

    def test_21(self):
        self.assertEquals(triangle.detect_triangle(4,4,9),"day khong phai la 1 tam giac")
    def test_22(self):
        self.assertEquals(triangle.detect_triangle(9,4,4),"day khong phai la 1 tam giac")
    def test_23(self):
        self.assertEquals(triangle.detect_triangle(9,4,4),"day khong phai la 1 tam giac")

        
    def test_5(self):
        self.assertEquals(triangle.detect_triangle(4,5,6),"tam giac thuong")
    def test_6(self):
        self.assertEquals(triangle.detect_triangle(4,4,4),"tam giac deu")
    def test_7(self):
        self.assertEquals(triangle.detect_triangle(4,4,5),"tam giac can")
    def test_8(self):
        self.assertEquals(triangle.detect_triangle(3,4,5),"tam giac vuong")
    def test_9(self):
        self.assertEquals(triangle.detect_triangle(4,4,math.sqrt(32)),"tam giac vuong can") 
if __name__ == '__main__':
   unittest.main()
