a= input()

list=[]
listiki=[]
def flat(x):
    for i in x:
        if type(i)!=str or type(i)!=int or type(i)!=float:
            flat(i) 
        else: list.append(x)

flat(a)
print(list)
b =input()

def reverse(x):
     list.append(x.reverse())
     for i in x:
         type(i)==type([0,0])
         reverse(i)
     
reverse(b)
print(listiki)
