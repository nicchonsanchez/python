# Trabalho da faculdade

altura = float(input("Informe sua altura (metros): "))
peso = float(input("Informe seu peso (Kg): "))
imc = peso/(altura**2)

print(f"Seu IMC é {imc:.2f}")

if imc <= 18.5:
    print("Com base no calculo de IMC, você está num quadro considerado magro.")
elif 18.5 <= imc <= 24.9:
    print("Com base no calculo de IMC, você está com um peso considerado normal")
elif 25.0 <= imc <= 29.9:
    print("Com base no calculo de IMC, você está com  sobrepeso, obesidade de grau I.")
elif 30.0 <= imc <= 39.9:
    print("Com base no calculo de IMC, você está com obesidade, obesidade de grau II.")
else:
    print("Com base no calculo de IMC, você está com obesidade grave, obesidade de grau III. Recomendamos acompanhamento médico.")
    
