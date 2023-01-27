'''print("************* Cálculadora Python *************")

print("Escolha uma das opções abaixo: ")
print(" 1. Adição ")
print(" 2. Subtração ")
print(" 3. Multiplicação ")
print(" 4. Divisão ")
      
print()

opcao = int(input("Digite a opção escolhida: "))
print("A opção escolhida foi: " , opcao, " <<<=== ")
print()
valor1 = int(input("Entre com o valor 1: "))
print()
valor2 = int(input("Entre com o valor 2: "))
print()

if(opcao == 1):
    soma = valor1 + valor2
    print("O valor da soma é: ", soma )

elif(opcao == 2):
    subtracao = valor1 - valor2
    print("O valor da subtração é: ", subtracao )

elif(opcao == 3):
    multiplicacao = valor1 * valor2
    print("O valor da multiplicacao é: ",  multiplicacao )

elif(opcao == 4):
    divisao = valor1 / valor2
    print("O valor da multiplicacao é: ", divisao )

else:
    print("\n Opção inválida!")

print()

print("*** Obrigado por vir até aqui! ***")'''


#Testando retorno das funções e maneiras diferentes de retorno.
print("//////// Calculadora Python //////")


def soma(x, y):
    print('\nO valor da soma é: ', x + y)

def subtracao(x, y):
    return '\nO valor da subtração é: ', x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    print(x / y)
    

#Variável guarda o valor da opção escolhida e exibe ela na tela:
entrada = input('Escolha uma das opções:\n -Soma: 1\n -Subtração: 2\n -Multiplicação: 3\n -Divisão: 4\n -Digite aqui: ')
print('A opção escolhida foi: \n', entrada)

#Variável recebe os dois valores a serem calculados:
valor1 = int(input('Entre com o valor 1: '))
valor2 = int(input('Entre com o valor 2: '))


if(entrada == '1'):
    print(soma(valor1, valor2))

elif(entrada == '2'):
    print(subtracao(valor1, valor2))

elif(entrada == '3'):
    print('\nO valor da multiplicação: ', multiplicacao(valor1, valor2))
    
elif(entrada == '4'):
    print('O valor da divisão é:', divisao(valor1, valor2))

else:
    print('Opção digitada não encontrado!')

