'''5. Write a PYTHON program to produce following design
A B C D E 
A B C D 
A B C 
A B
A
'''
s='ABCDE'
for i in range(4,-1,-1):
    print(s[0:(i+1)])
    
