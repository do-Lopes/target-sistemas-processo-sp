# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


#Função fibonacci
def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        #Soma do ultimo valor(sequencia[-1]) com o penúltimo valor(sequencia[-2])
        sequencia.append(sequencia[-1] + sequencia[-2])
    #Verifica se o valor está no array "sequencia"
    if(n in sequencia):
        return True
    else:
        return False

#Entrada do usuário
n = int(input("Digite um número para verificar: "))

#Verificação da função fibonacci
if fibonacci(n):
    print(f"O número {n} pertence a sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence a sequência de Fibonacci.")