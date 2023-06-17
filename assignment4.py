#Break
for i in range(10):
    if i==5:
        break
    print(i)

#continue
for i in range(10):
    if i%2==0:
        continue
    print(i)

#pass
for i in range(5):
    if i%2==2:
        pass
    else:
        print(i)

#for with else
numbers=[1,2,3,4,5]
for num in numbers:
    if num==0:
        print("encountering 0, exiting loop")
        break
    else:
        print("loop completed without encountering a break statement")
        
#while with else
num==0
while num<5:
    print("count:",num)
    num+=1
else:
    print("loop completed")