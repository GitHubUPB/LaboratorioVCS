import math
a=int(input("ingresar el Dato A"))
b=int(input("ingresar el Dato B"))
c=int(input("ingresar el Dato C"))

d=(b*b-4*a*c)

if a!=o:
    if d<0:
       print("las raices son las imaginarias")
    else:
        x1=(-b+(math.sqrt(d)))/(2*a)
        x2=(-b-(math.sqrt(d)))/(2*a)
       print("x1 = "+str (x1)+"x2 = "+str(x2))
else:
    print("el coeficiente A deber ser diferente de cero")
