def soma(n1, n2):
  resultado = n1 + n2
  return resultado 

def multiplicacao(n1, n2):
  resultado = n1 * n2
  return resultado 

def divisao(n1, n2):
  resultado = n1 / n2
  return resultado

def subtracao(n1,n2):
  resultado = n1 - n2
  return resultado 

while True:
    operador = input("Digite o operador (+, -, *, /) ou 'sair'': ")
    if operador == "sair":
        break
    if operador not in ["+", "-", "*", "/"]:
        print("Operador invalido.")
        continue
        
    try: 
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Digite um número válido")
        continue

    if operador == "+":
      print(soma(n1,n2))
    elif operador == "-":
      print(subtracao(n1,n2))
    elif operador == "*":
      print(multiplicacao(n1,n2))
    elif operador == "/":
        try:
          print(divisao(n1,n2))
        except ZeroDivisionError as e:
          print("Não existe divisão por zero") 
     
    else:
      print("Operador invalido.")
