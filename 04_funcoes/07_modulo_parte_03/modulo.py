# biblioteca
import os
import math

def limpar():
    os.system("cls" if os.name =="nt" else "clear")

    # função do 1º grau: a*x*b = 0
def primeiro_grau(a,b):
    return -b/a if a != 0 else "nao existe raiz real."

# função de 2º grau: a*x² + b*x + c = 0
def segundo_grau(a,b,c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            yield x1
            yield x2
        elif delta == 0:
            yield -b/(2*a)  # trocar o return pelo o yield para duas ou mais informções 
        else:
            yield "não existem raízes reais." 
    else:
        yield primeiro_grau(b, c) 