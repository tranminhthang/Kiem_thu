import math
def detect_triangle(a,b,c):
    
    x = ""
    y = ""
    z = 0
    ketqua="tam giac"
    if ( a <= 0 or b<= 0 or c<=0 or a > 2**32 -1  or b > 2**32 -1 or c > 2**32 -1 or ('a' < a and a < 'z')or ('a' < b and b < 'z')or ('a' < c and c < 'z') or
         ('A' < a and a < 'Z')or ('A' < b and b < 'Z')or ('A' < c and c < 'Z')):
        ketqua= "du lieu dau vao khong hop le"

        
    elif ( a+b<c or b+c <a or a+c <b ):
        ketqua= "day khong phai la 1 tam giac"

    
        
    else:
        #tam giac vuong
        if (a*a+b*b-round(c*c,10)==0 or b*b+c*c-round(a*a, 10)==0 or a*a+c*c-round(b*b,10)==0):
            x = " vuong"
            z=1
            
            
        #tam giac can hoac deu
        if (a==b or b== c or c==a):
            z = 1
            y = " can"
            if ( a==b and b==c and c==a):
                y = " deu"            
        if (z !=1):
            ketqua = ketqua + " thuong"
             
        else:
            ketqua = ketqua +x +y
            
    print ketqua
    return ketqua
    

    

if __name__ == "__main__":
    detect_triangle(math.sqrt(2),math.sqrt(2), 2)
    detect_triangle(math.sqrt(2),1, 1)
    detect_triangle(1, math.sqrt(2), 1)
    detect_triangle(1,1,math.sqrt(2))
    
    
