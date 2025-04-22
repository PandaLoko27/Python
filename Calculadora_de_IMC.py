peso = float(input('Insira seu peso em quilos: '))
altura = float(input('Agora insira sua altura em metros: '))

imc = (peso/(altura)**2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.2f}, então você está Abaixo do peso normal')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu imc é de {imc:.2f}, então você está no peso normal')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu imc é de {imc:.2f}, então você está com excesso de peso')
elif imc >= 30 and imc <= 34.9:
    print(f'Seu imc é de {imc:.2f}, então você um obeso de classe  I')
elif imc >= 35 and imc <= 39.9:
    print(f'Seu imc é de {imc:.2f}, então você um obeso de classe II')
elif imc > 40:
    print(f'Seu imc é de {imc:.2f}, então você é um obeso de classe III')
else:
    print('Verifique se você inseriu os dados corretos')
