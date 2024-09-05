print("Donner un nombre puis son image")
x0=float(input())
fx0=float(input())
print("Donner un autre nombre puis son image")
x1=float(input())
fx1=float(input())

a = (fx1-fx0)/(x1-x0)

b = fx0-a*x0

print("L'expression de f(x) est ",str(a),"*x+",str(b))

print("---------------------")
print("Avec un peu plus d'efforts : ...")
print("---------------------")

res="L'expression de f(x) est f(x)="
if a!=0:
  if a == 1:
    res = res + "x"
  else:
    if a == -1:
      res = res + "-x"
    else:
        res = res + str(a) + "*x"
  if b > 0:
    res = res + "+" + str(b)
  else:
    if b<0:
      res = res + str(b)
else:
  res = res + str(b)

print(res)




####
#
# test :
#
####

# f(x)=0 : 
#    Données -> 0  0  1  0
  
# f(x)=x : 
#    Données -> 1  1  2  2

# f(x)=-x : 
#    Données -> 1  -1  2  -2
 
# f(x)=x+2 : 
#    Données -> 1  3  2  4

# f(x)=-x-3 : 
#    Données -> 1  -4  2  -5

# f(x)=2x+4
#    Données -> 1  6  2  8

# f(x)=-2x-3
#    Données -> 1  -5  2  -7
 
# quelques problèmes :

# f(x)=1/3x+1
#    Données -> 3  2  6  3

# f(x)=x+1
#    Données -> 0.1  1.1  0.2  1.2
