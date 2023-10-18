import random
def main():
    l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l2=['A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l3=['0','1','2','3','4','5','6','7','8','9']
    l4=['!','@','#','$','%','&','*']
    var1=random.choice(l1)
    var2=random.choice(l2)
    var3=random.choice(l3)
    var4=random.choice(l4)
    s=""
    k=s+var2+var1+var4+var3
    p=l1+l2+l3+l4  #here we have merge all the list to create something new
    z=random.shuffle(p)
    n=int(input("enter the length of your password"))
    if len(k)==n:
        print(k)
    elif n> len(k):
        for i in range (n-len(k)):
            k=k+random.choice(ps)
        print(k)
    else:
        print("not possible")
if __name__=="__main__":
    main()