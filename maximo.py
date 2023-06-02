def maior1(n1, n2):
    if n1 > n2:
        return n1
    return n2

def maior2(n1, n2):
    return n1 if n1 > n2 else n2
   
maior3 = lambda n1, n2: n1 if n1 > n2 else n2 

print(maior1(4, 8))        #8

print(maior2(32, 2))       #32

print(maior3(687, 8233))   #8233