
import modulo as m

m.limpar()
while True:
    print("1 _ Calcular Quadrado")
    print("2 _ Calcular Retangulo")
    print("3 _ Calcular Triangulo")
    print("4 _ Calcular Circulo")
    print("5 _ Calcular trapezio")
    print("6 _ sair do Programa")
    opcao = input("opção desejada: ").strip()
    m.limpar()

    match opcao:
        case "1":
         l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
         m.limpar()
         area = m.quadrado(l)
         print(f"Area do quadrado {area}")
         continue
         
        case "2":
         b = float(input("Informe a base do retangulo: ").strip().replace(",","."))
         h = float(input("Informe a altura do retangulo: ").strip().replace(",","."))
         m.limpar()
         area = m.retangulo(b, h)
         print(f"Area do retangulo: {area}")
         continue
      
        case "3":
         b = float(input("Informe a base do triangulo: ").strip().replace(",","."))
         h = float(input("Informe a altura do triangulo: ").strip().replace(",","."))
         m.limpar()
         area = m.triangulo(b, h)
         print(f"Area do triangulo {area}")
         continue

         
        case "4":
         r = float(input("Informe o raio do circulo: ").strip().replace(",","."))
         m.limpar()
         area = m.circulo(r)
         print(f"Area do circulo{area}")
         continue       

        case "5":
         b = float(input("informe a base menos do trapezio: ").strip().replace(",","."))
         B = float(input("informe a base maior do trapezio: ").strip().replace(",","."))
         h = float(input("informe a altura do trapazio: ").strip().replace(",","."))
         m.limpar()
         area = m.trapezio(b, B, h)
         print(f"Area do trapezio: {area}")
         continue

        case "6":
         break
        
        case _:
         print("Opção Invalida.")
         continue