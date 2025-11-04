# vamos criar um programa com dois arquivos que sao modulo e main , 
# bibliotecas
import math
import os

#funções
def quadrado(l):
    return l**2

def retangulo(b,h):
    return (b*h)
            
def triagulo(b, h):
    return (b*h)/2

def circulo(r):
    return math.pi*(r**2)

def trapezio(b,B,h):
    return((b+B)*h)/2

def limpar():
    os.system("cls")


