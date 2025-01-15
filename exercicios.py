import math
from datetime import datetime

#Programa para calcular a divisão inteira entre números inteiros
primeiro_numero = int(input("Digite um número inteiro: "))

segundo_numero = int(input("Digite outro número inteiro: "))

divisao_inteira = primeiro_numero // segundo_numero

resto_divisao = primeiro_numero % segundo_numero

print(f"A divisão inteira de {primeiro_numero} por {segundo_numero} é {divisao_inteira}")

if (resto_divisao != 0):
  print(f"E o resto da divisão é {resto_divisao}")

#Programa para calcular a área de um círculo, recebendo o raio como entrada
raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio**2

print(f"A área do círculo é {area:.2f}")

#Programa para informar o dia, o ano e o mês
data_str = input("Digite uma data (dd/mm/aaaa): ")

data_obj = datetime.strptime(data_str, '%d/%m/%Y')

print(f"O dia é {data_obj.day}")
print(f"O mês é {data_obj.month}")
print(f"O ano é {data_obj.year}")