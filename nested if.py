tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
biology=int(input("enter your biology marks:"))
physics=int(input("enter your physics marks:"))
if(tamil>40):
    if(english>40):
        if(maths>40):
            if(biology>40):
                if(physics>40):
                    print("pass")
                else:
                    print("fail")
            else:
                print("fail")             
        else:
            print("fail")
    else:
        print("fail")
else:
    print("fail")
