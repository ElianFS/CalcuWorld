def resta():
  print("Resta")

  try:
    num1 = float(input("Ingresar primer numero: "))
    num2 = float(input("ingresar segundo numero: "))

    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
  except ValueError:
    print("Por favor, ingrese solo numeros reales.")
resta()
