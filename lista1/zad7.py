import random

def generate(n):
    list=[]
    set="abc"

    for i in range(1,10):
        word=""
        for j in range(0,n):
            word=word+random.choice(set)

        list.append(word)
    
    return list

def find(list, templ):
    match=[]
    keys={}
    
    for i in range(0, len(templ)):
        if(templ[i]!='*'):
            keys[i]=templ[i]
    
    for word in list:
        is_good=0
        for i in range(0, len(word)):
            if(i not in keys.keys() or word[i]==keys.get(i)):
                is_good=1
            else:
                is_good=0
                break
        
        if(is_good):
            match.append(word)

    return match    
    

n=input("Podaj dlugosc ciagu: ")
list=generate(int(n))
print(list)
templ=input("Podaj wzorzec o dlugosci "+n+": ")
print("Ciagi pasujace do wzorca:",find(list,templ))


