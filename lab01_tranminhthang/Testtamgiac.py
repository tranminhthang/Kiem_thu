import unittest
import tamgiac
import math

class Testtamgiac(unittest.TestCase):
    def test_testtamgiac_10(self):
        self.assertEquals(tamgiac.tamgiac('b',5,6),"du lieu dau vao khong hop le")
    def test_testtamgiac_11(self):
        self.assertEquals(tamgiac.tamgiac(4,-5,6),"du lieu dau vao khong hop le")
    def test_testtamgiac_12(self):
        self.assertEquals(tamgiac.tamgiac(4,5,-6),"du lieu dau vao khong hop le")
        

    def test_testtamgiac_13(self):
        self.assertEquals(tamgiac.tamgiac(2**32 +40, 2**32-10, 2**32 -15),"du lieu dau vao khong hop le")
    def test_testtamgiac_14(self):
        self.assertEquals(tamgiac.tamgiac(2**32-10,2**32 +40, 2**32 -15),"du lieu dau vao khong hop le")
    def test_testtamgiac_15(self):
        self.assertEquals(tamgiac.tamgiac(2**32-10, 2**32 -15,2**32 +40),"du lieu dau vao khong hop le")
        
    def test_testtamgiac_16(self):
        self.assertEquals(tamgiac.tamgiac('b',5,6),"du lieu dau vao khong hop le")
    def test_testtamgiac_17(self):
        self.assertEquals(tamgiac.tamgiac(4,'d',6),"du lieu dau vao khong hop le")
    def test_testtamgiac_18(self):
        self.assertEquals(tamgiac.tamgiac(4,5,'e'),"du lieu dau vao khong hop le")

    def test_testtamgiac_21(self):
        self.assertEquals(tamgiac.tamgiac(4,4,9),"day khong phai la 1 tam giac")
    def test_testtamgiac_22(self):
        self.assertEquals(tamgiac.tamgiac(9,4,4),"day khong phai la 1 tam giac")
    def test_testtamgiac_23(self):
        self.assertEquals(tamgiac.tamgiac(9,4,4),"day khong phai la 1 tam giac")

        
    def test_testtamgiac_7(self):
        self.assertEquals(tamgiac.tamgiac(4,5,6),"tam giac thuong")
    def test_testtamgiac_8(self):
        self.assertEquals(tamgiac.tamgiac(4,4,4),"tam giac deu")
    def test_testtamgiac_9(self):
        self.assertEquals(tamgiac.tamgiac(4,4,5),"tam giac can")
    def test_testtamgiac_5(self):
        self.assertEquals(tamgiac.tamgiac(3,4,5),"tam giac vuong")
    def test_testtamgiac_51(self):
        self.assertEquals(tamgiac.tamgiac(4,4,math.sqrt(32)),"tam giac vuong can")

        

        
        
  
        
if __name__ == '__main__':
   unittest.main()
