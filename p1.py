x,y=int(input("Enter x: ")),int(input("Enter y: "))
if x>y:
    x,y=y,x
res=0
res_str=""
for i in range(x,y+1):
    if i%2==0:
        res+=i
        res_str+=str(i)+"+"

print(f"{res_str[:-1]} = {res}")