def toArabic(num):
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V','IV','I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    arabic = 0

    i=0
    s=0 
    while s < len(num):
        if num[s] == symbols[i]:
            arabic += values[i]
            s += 1
        elif (len(num) - s >= 2) and (num[s] + num[s+1]) == symbols[i+1]:
                i +=1
                arabic += values[i]
                i +=1
                s += 2
        else:
            i += 2
    return arabic       



num=input("Podaj liczbe w systemie rzymskim:")
print(num+"=", toArabic(num))