
from input import*
from random import randint
import itertools
import unittest
import re

f = open('input.py')
line = f.readlines()
arr = []
numArr =[]
for i in range(0,len(line)):       
    if line[i].startswith("def main") and "'''" in line[i+1]:
        for j in range(i+2,len(line)):
            if "'''" in line[j]:   
                break
          
            arr = re.findall(r'\d+',line[j])
            mang = []
            k=0
            while (k < len(arr)):
                mang.append(int(arr[k]))
                k = k+1

            k=0
            l=0

            while (k < len(mang)):
                l = len(mang)-1
                while (l>k):
                    if (mang[k] > mang[l-1]):
                        x = mang[k]
                        y =  mang[k+1]
                        mang[k]= mang[l-1]
                        mang[l-1]=x
                        mang[k+1]= mang[l]
                        mang[l]=y
                        l = l-2
                    k = k+2
            k=1

            while (k < len(mang)):
                l = k+1
                while (l<len(mang)):
                    if (mang[k] >= mang[l] ):

                        if(mang[k]>mang[l+1]):
                            for i in range(k+1,len(mang)-2):
                                mang[i]= mang[i+2]
                            mang[len(mang)-1]='NULL'
                            mang[len(mang)-2]='NULL'
                                
                        else: 
                            mang[k]=mang[l+1]
                            for i in range(k+1,len(mang)-2):
                                mang[i]= mang[i+2]
                            mang[len(mang)-1]='NULL'
                            mang[len(mang)-2]='NULL'
                                
                    else :
                        l = l+2
                k = k+2
            k=0
            num = []

            while (k < len(mang)):
                if (mang[k]!= 'NULL'):                      
                    num.append(randint(int(mang[k]),int(mang[k+1])))
                k = k+2
            numArr.append(num)

for l in range(0,len(numArr)):
    print numArr[l]

class TestSequense(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
if __name__ == '__main__':
    m = 0;
    for i in itertools.product(*numArr):
        test_name = 'test_%d' %m
        m = m+1
        test = test_generator(main(*i)," ")
        setattr(TestSequense,test_name,test)
    unittest.main()
