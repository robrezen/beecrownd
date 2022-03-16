def c_triangulo (valores):

    triangulo = (valores[0]*valores[2])/2
    return triangulo

def c_circulo (valores):

    circulo = 3.14159*valores[2]*valores[2]
    return circulo
               
def c_trapezio (valores):

    trapezio = ((valores[0] + valores[1])*valores[2])/2
    return trapezio

def c_quadrado (valores):

    quadrado = valores[1]*valores[1]
    return quadrado

def c_retangulo (valores):

    retangulo = valores[0]*valores[1]
    return retangulo

a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

valores =[a,b,c]

triangulo = c_triangulo(valores)
circulo = c_circulo(valores)
trapezio = c_trapezio(valores)
quadrado = c_quadrado(valores)
retangulo = c_retangulo(valores)
                
print('TRIANGULO: %.3f'% triangulo)
print('CIRCULO: %.3f'% circulo)
print('TRAPEZIO: %.3f'% trapezio)
print('QUADRADO: %.3f'% quadrado)
print('RETANGULO: %.3f'% retangulo)  