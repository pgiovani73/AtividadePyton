litros = float(input("Digite a quantidade de litros abastecidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ")

preco_alcool = 1.90
preco_gasolina = 2.50

if tipo_combustivel.upper() == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
            preco_litro = preco_alcool * (1 - desconto)
elif tipo_combustivel.upper() == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
            preco_litro = preco_gasolina * (1 - desconto)

valor_a_pagar = litros * preco_litro

print(f"O valor total a ser pago é: R$ {valor_a_pagar:.2f}")