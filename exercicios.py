primeiro_numero = int(input("Digite um número inteiro: "))

segundo_numero = int(input("Digite outro número inteiro: "))

divisao_inteira = primeiro_numero // segundo_numero

resto_divisao = primeiro_numero % segundo_numero

print(f"A divisão inteira de {primeiro_numero} por {segundo_numero} é {divisao_inteira}")

if (resto_divisao != 0):
  print(f"E o resto da divisão é {resto_divisao}")