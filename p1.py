x,y=int(input("Enter x: ")),int(input("Enter y: "))
if x>y:
    x,y=y,x

numbers=[i for i in range(x,y+1) if i%2==2]
res=sum(numbers)
res_str="+".join([str(a) for a in numbers])
print(f"{res_str} = {res}")