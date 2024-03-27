import random
def pwdgen(w,x,y,z,n,l):
    ul="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ll="abcdefghijklmnopqrstuvwxyz"
    d="0123456789"
    s="[]()%@#$^&*!_-{};:'<>,./?\""
    all=""
    if(w==1):
        all+=ul
    if(x==1):
        all+=ll
    if(y==1):
        all+=d
    if(z==1):
        all+=s
    print('\n',n,"PASSWORDS GENERATED SUCCESSFULLY!!")
    print("=======================================")
    for i in range(n):
        p="".join(random.sample(all,l))
        print(p)
a,b,c,d=0,0,0,0
print("PASSWORD GENERATOR")
print("==================")
l=int(input("Enter the length of password needed: "))
n=int(input("Enter the number of passwords needed: "))
a=int(input("Should the password contain Uppercase letters? (Y==1 & N==0): "))
b=int(input("Should the password contain Lowercase letters? (Y==1 & N==0): "))
c=int(input("Should the password contain digits? (Y==1 & N==0): "))
d=int(input("Should the password contain symbols? (Y==1 & N==0): "))
pwdgen(a,b,c,d,n,l)


