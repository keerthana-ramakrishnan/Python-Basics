tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
biology=int(input("enter your biology marks:"))
physics=int(input("enter your physics marks:"))
avg=((tamil+english+maths+biology+physics)/500)*100
if(avg>80):
    print("destintion")
else:
    if(avg>60):
        print("first class")
    else:
        if(avg>80):
            print("second class")
        else:
            if(avg>80):
                print("third class")
            else:
                print("fail")
    
    
