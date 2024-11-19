from InquirerPy import inquirer

nome=inquirer.text("qual e o seu nome?").execute()
cor=inquirer.select("qual a cor favorita?", choices=["azul","vermelho","verde"]).execute()

print(nome)
print(cor)

def valida_email(vol):
    if"@" not in vol:
        raise ValueError("por favor , insira um e-mail válido.")
    return vol
email=inquirer.text("qual é teu email?", validate=valida_email).execute()