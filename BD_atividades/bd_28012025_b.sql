create database relatorio;
use relatorio;

create table lucros (
codLucro int primary key auto_increment,
nomeLucro varchar (30) not null,
tipoLucro varchar (30) not null,
dataLucro date not null,
totalLucro float default 1 not null
);
create table despesas (
codDespesas int primary key auto_increment,
nomeDespesa  varchar (30) not null,
tipoDespesa varchar (30) not null,
valorDespesa float default 1 not null,
dataDespesa date not null,
descriçãoDespesa varchar (30) not null,
codLucro int not null,
constraint fk_lucros foreign key (codLucro) references lucros (codLucro)
);