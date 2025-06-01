saida = 'n'

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao in ('+', 'adicao', 'adição'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao', 'subtração'):
        resultado = subracao(num1, num2)
    elif operacao in ('*', 'multiplicacao', 'multiplicação', 'x'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao', 'divisão'):
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

while saida.lower() == 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, / ou nome): ')
    resultado = calculadora(num1, num2, operacao)
    print('Resultado da operação: ' + str(resultado))
    saida = input('Deseja sair? (S/N): ')
