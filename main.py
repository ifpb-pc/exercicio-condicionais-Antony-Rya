def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero"))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("par")
    else:
        print("ímpar")
def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    operador = input("Digite um o operador: ")
    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            resultado = num1 / num2
    print(float(resultado))

def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    num3 = float(input("Digite outro numero: "))
    if num1 > num2 and num1 > num3:
        print(float(num1))
    elif num2 > num1 and num2 > num3:
        print(float(num2))
    else:
        print(float(num3))

def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
    idade = int(input("Digite sua idade: "))
    if idade >= 60:
        print("Idoso")
    elif idade >= 20 and idade <= 59:
        print("Adulto")
    elif idade >= 13 and idade <= 19:
        print("Adolescente")
    else:
        print("Criança")

def q6():
    """
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """
    A = int(input("Digite um numero: "))
    B = int(input("Digite outro numero: "))
    C = int(input("Digite outro numero: "))
    if A > B + C or B > A + C or C > A + B: 
        print("Inválido")
    elif A == B and B == C:
        print("Equilátero")
    elif A != B and A != C and C != B:
        print("Escaleno")
    else:
        print("Isósceles")

def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    nota = int(input("Digite sua nota: "))
    match nota:
        case x if x >= 90 and x <= 100:
            print("A")
        case x if x >= 80 and x <= 89:
            print("B")
        case x if x >= 70 and x <= 79:
            print("C")
        case x if x >= 60 and x <= 69:
            print("D")
        case x if x >= 50 and x <= 59:
            print("E")
        case x if x >= 0 and x <= 49:
            print("F")
        

def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    usuario = input("Digite o usuario: ")
    senha = input("Digite sua senha: ")
    if usuario == "admin" and senha == "12345":
        print("Acesso concedido")
    else:
        print("Acesso negado")

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    IMC = peso/altura**2
    match IMC:
        case x if x < 18.5:
            print("Abaixo do peso")
        case x if x >= 18.5 and x <= 24.9:
            print("Peso normal")
        case x if x >= 25 and x <= 29.9:
            print("Sobrepeso")
        case x if x >= 30 and x <= 34.9:
            print("Obeso")
        case x if x >= 35 and x <= 39.9:
            print("Muito obeso")

def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
    ano = int(input("Digite o ano"))
    if ano % 4 == 0:
        print("bissexto")
    else:
        print("não")
