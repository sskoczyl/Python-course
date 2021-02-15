import random

tab=random.sample(range(1, 100), 20)
print(tab)
print("Average value=", sum(tab)/len(tab))
print("Max=", max(tab))
print("Min=", min(tab))
tab.sort()
print("Second max=", tab[-2])
print("Second min=", tab[1])

even=0
for i in tab:
    if(i%2==0):
        even+=1

print("Even=", even)
print("Odd=", len(tab)-even)