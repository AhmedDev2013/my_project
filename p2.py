numbers=[int(a) for a in input("Enter numbers: ").split(",")]
numbers.sort()
numbers_count={}
for a in numbers:
    if a in numbers_count:
        numbers_count[a]+=1
    else:
        numbers_count[a]=0

for k,v in numbers_count.items():
    print(f"{k} has appeared {f'{v} times' if v>1 else 'once' } ")
