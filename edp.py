
'''
Requirements:
pip install sympy
pip install matplotlib
'''

from sympy import *
from sympy.plotting import plot3d


a=pi
b=pi
x,y = symbols('x y') # variables simbólicas

# 
#Primer subproblema
u =((2*pi-2*pi*cosh(pi))/sinh(pi))*cosh(y) + 2*pi*sinh(y) + (cosh(sqrt(5)*y)*cos(2*x))/(sqrt(5)*sinh(sqrt(5)*pi)) + ((-cosh(sqrt(17)*pi)*cosh(sqrt(17)*y))/(sqrt(17)*sinh(sqrt(17)*pi)) + sinh(sqrt(17)*y)/sqrt(17) + 1/17)*cos(4*x)
fPoissonu = cos(4*x)
#
# 
#Segundo subproblema
w =((pi-pi*cosh(pi))/sinh(pi))*cosh(x) + pi*sinh(x) + (cosh(sqrt(2)*x)*cos(y))/(sqrt(2)*sinh(sqrt(2)*pi)) + ((-cosh(sqrt(5)*pi)*cosh(sqrt(5)*x))/(sqrt(5)*sinh(sqrt(5)*pi)) + sinh(sqrt(5)*x)/sqrt(5) + 1/5)*cos(2*y)
fPoissonw = cos(2*y)
#
#Problema completo
v = u + w
fPoisson = fPoissonw + fPoissonu

# Construccion Laplaciano
vx=v.diff(x)
vxx=vx.diff(x)
vy=v.diff(y)
vyy=vy.diff(y)
Lap=vxx+vyy

# Comprobación de que el laplaciano de nuestra solución es igual a la función de Poisson

#simplify(Lap - fPoisson)# PARA PROBLEMA LAPLACE
#simplify(-Lap + v - fPoisson) # PARA PROBLEMA POISSON
print(simplify(-Lap + v - fPoisson)) #Imprime 0 si es correcto el poisson

# Vamos a comprobar la expresión sobre las boundary conditions

BC_N=simplify(vy.subs([(x,x),(y,b)]))
BC_S=simplify(vy.subs([(x,x),(y,0)]))
BC_O=simplify(vx.subs([(x,0),(y,y)]))
BC_E=simplify(vx.subs([(x,a),(y,y)]))


print('BC_N : ')
print(BC_N)
print('BC_S : ')
print(BC_S)
print('BC_O : ')
print(BC_O)
print('BC_E : ')
print(BC_E)


# Realizamos comprobación sobre el flujo (Teorema de Green)

integral_Laplaciano = integrate(Lap, (x,0,a), (y,0,b)) # integración en dos variables
integralF = integrate(fPoisson, (x,0,a), (y,0,b))
integralv = integrate(v, (x,0,a), (y,0,b))
flujo= 0
simplify(integral_Laplaciano - flujo) # Debe dar cero

#print(simplify(integralv - integralF)) #Conserva Masa

# Representación gráfica de la función
plot3d(v, (x,0,a), (y,0,b))
# Representación gráfica de las BC
pltN = plot(BC_N, (x,0,a), title="Condición de contorno norte", ylabel=BC_N)
pltS = plot(BC_S, (x,0,a), title="Condición de contorno sur", ylabel=BC_S)
pltO = plot(BC_O, (y,0,b), title="Condición de contorno oeste", ylabel=BC_O)
pltE = plot(BC_E, (y,0,b), title="Condición de contorno este", ylabel=BC_E)
