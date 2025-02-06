use escola;
drop table aluno;

create table aluno(
registroMatricula integer primary key auto_increment,
nome varchar (30) not null,
e_mail varchar (30) not null
);
insert into aluno (registroMatricula, nome, e_mail) values (null, "Pedro Giovani Teixeira", "pedrogio@hotmail.com");
describe aluno;
insert into aluno values (null, "Maria Madalena Faris","faris@gmail.com");
insert into aluno values (null, "jose Roberto Pereira","jroberto@gmail.com"),
(null, "Alencar Ribeiro", "alencar286@gmail.com"),
(null, "Isadora Martins", "isamartins@gmail.com"),
(null, "Mauricio Pereira", "pmauricio@hotmail.com"),
(null, "Bruno Ferreira", "ferreiracgr@bol.com.br");
