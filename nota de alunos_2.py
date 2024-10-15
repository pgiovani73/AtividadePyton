aluno=(input("digite nome do aluno:"))
nota1=float(input("nota1:"))
nota2=float(input("nota2:"))
nota3=float(input("nota3:"))
nota4=float(input("nota4:"))
media=(nota1+nota2+nota3+nota4)/4
print("Nome do aluno:",aluno)
print("Notas do aluno:\n",nota1,"/",nota2,"/",nota3,"/",nota4)
if media>=9.1 and media<10:
    print("conceito: A - aprovado Media:",media)
elif media >=7.6 and media<=9.0:
    print("conceito: B - aprovado\nMedia:",media)
elif media >=6.0 and media <=7.5:
    print("conceito: C - aprovado\nMedia:",media)
elif media>=4.1 and media<=5.9:
    print("conceito: D - repprovado\nMedia:",media)
elif media<4.0:
    print("conceito: E - reprovado\nMedia:",media)