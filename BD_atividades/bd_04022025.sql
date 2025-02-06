create database faculdade;
use faculdade;

drop table aluno;
create table aluno (
id int primary key auto_increment,
curso int not null,
turmas int not null,
constraint fk_curso foreign key (curso) references curso (id)
);

describe aluno;

alter table aluno add constraint fk_curso foreign key (curso) references curso (id);
alter table aluno add constraint fk_turmas foreign key (turmas) references turma (id);

describe turma;

drop table turma;

create table turma (
id int primary key auto_increment,
periodo_letivo int not null,
alunos int not null,
disciplina int not null,
professor int not null,
constraint fk_peridoLetivo foreign key (periodo_letivo) references periodoLetivo (id),
constraint fk_alunos foreign key (alunos) references aluno (id),
constraint fk_disciplina foreign key (disciplina) references disciplina (id),
constraint fk_professor foreign key (professor) references professor (id)
);

alter table turma add constraint fk_turmas foreign key (turmas) references turma (id);

drop table curso;

alter table curso add constraint fk_faculdade foreign key (faculdade) references faculdade (id);

create table disciplina (
id int primary key auto_increment,
turmas varchar (30) not null
);
create table faculdade (
id int primary key auto_increment,
cursos varchar (30) not null,
instituto varchar (30) not null
);
create table professor (
id int primary key auto_increment,
turmas varchar (30) not null,
instituto varchar(30) not null
);
create table PeriodoLetivo (
id int primary key auto_increment,
turmas varchar(30) not null
);
create table instituto (
id int primary key auto_increment,
faculdades varchar(30),
professores varchar(30)
);

