peso = float(input("Qual seu peso ? "))
altura = float(input("Qual sua altura ? "))

resultado = None

imc = round(peso / (altura ** 2), 2)

if(imc < 18.50):
    resultado = "Magreza"
elif (imc >= 18.5 and imc < 24.90):
    resultado = "Normal"
elif (imc >= 24.9 and imc < 30):
    resultado = "Sobrepeso"
elif (imc >= 30):
    resultado = "Obesidade"

print(f"""O cálculo do seu IMC resultou em  {imc} \nIndicando que o seu corpo está em  {resultado}""")
