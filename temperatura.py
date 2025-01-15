#Conversor de temperatura
fim = False
while(fim != True):
  try:
    celsius = float(input("Informe a temperatura em °C: "))

    fahrenheit = celsius * 1.8 + 32
  except ValueError:
    print("O tipo de dado informado está incorreto.")
  else:
    print(f"A temperatura em °F: {fahrenheit}")
    fim = True