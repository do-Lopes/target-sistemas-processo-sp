# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

entrada = input("Digite uma entrada:")

entrada_invertida = ""

#Valor inicial de i = tamanho da string, iniciando do final(-1) e diminuindo em um a cada loop(-1)
for i in range(len(entrada) - 1, -1, -1):
    entrada_invertida += entrada[i]

print(entrada_invertida)