t=int(input("enter the muliplication table you want:"))
ts=int(input("enter starting muliplication table value you want:"))
te=int(input("enter ending muliplication table value you want:"))
for ts in range(ts,te+1):
    a=ts*t
    print(ts, " X ",t," = ",a)
    ts+=1
