number= int (input("Please Type Your Number:"))
list=[]

for i in range(2,number):
    situation=False
    for a in range(2,i):
        if i % a ==0:
            situation=True
            print("It is not a Prime Number")
            break
    if not situation:
        list.append(i)

for i in list:
    print(i)

print("Between 0 and {} there is {} prime numbers".format(number,len(list)))    


