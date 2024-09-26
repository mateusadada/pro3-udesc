/* Digite aqui seu SQL */

UPDATE aluno
SET nome= "Heloisa Oliveira"
WHERE aluno.aluno_key = 5;

INSERT INTO aluno (aluno_key,nome, ingresso, sexo_key, cidade_key)
VALUES (10,'João de Matos', 2019, 1, 3);

DELETE FROM aluno
WHERE nome = 'Hermann Blumenau';

SELECT a.aluno_key, a.nome, a.ingresso, c.nome, s.nome, disciplina.sigla
FROM aluno a
JOIN matricula m ON a.aluno_key = m.aluno_key
JOIN cidade c ON a.cidade_key = c.cidade_key
JOIN sexo s ON a.sexo_key = s.sexo_key
JOIN disciplina ON m.disciplina_key = disciplina.disciplina_key
WHERE disciplina.sigla = 'REC-I';
