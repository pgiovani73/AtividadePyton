aluno=(input("digite nome do aluno:"))
nota1=float(input("nota1:"))
nota2=float(input("nota2:"))
nota3=float(input("nota3:"))
media=(nota1+nota2+nota3)/3
print("Nome do aluno:",aluno)
print("Media da nota do aluno:", media)
if media==10:
    print("Aluno aprovado com distinção")
elif media>=7:
    print("Aluno aprovado")
else:
    print("Aluno reposvado")