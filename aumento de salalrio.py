salario=float(input("Informe o salario:"))
print("|================================================|")
print("  Salario Atual:R$",salario)
if salario <= 280:
    percentual = 20
elif salario >280 and salario <700:
    percentual = 15
elif salario >=700 and salario<1500:
    percentual = 10
elif salario >=1500:
    percentual = 5

aumento=(salario*percentual/100)
    
print("  Percentual aplicado no salario:", percentual, "%")
print("  Valor do aumento do Salarioo:R$",aumento)
print("  Valor do salario Atual:R$",salario+aumento)
print("|================================================|")