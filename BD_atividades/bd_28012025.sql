create database escola2;
use escola2;
CREATE TABLE alunos (id INT AUTO_INCREMENT, nome VARCHAR(30) NOT NULL, fone VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL, PRIMARY KEY (id));
describe alunos;
use escola;
drop table alunos;
use escola2;
describe alunos;
create database departamento;
use departamento;

create table depto(
depto int auto_increment, 
descricao varchar (30) not null,
primary key(depto)
);

create table matricula (
matricula int auto_increment,
nome varchar(30) not null, 
endereço varchar(30) not null, 
depto int not null, 
primary key(matricula), 
constraint fk_maricula foreign key (depto) references depto (depto));




