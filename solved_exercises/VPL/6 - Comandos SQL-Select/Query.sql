/* Digite aqui seu SQL */
SELECT
    aluno.aluno_key,
    aluno.nome,
    aluno.ingresso,
    cidade.nome,
    sexo.nome,
    disciplina.sigla
FROM
    aluno, cidade, sexo, disciplina, matricula
WHERE
    (aluno.sexo_key = 1) and
    (aluno.cidade_key = 2) and
    (disciplina.disciplina_key = 2) and
    (aluno.sexo_key = sexo.sexo_key) and
    (cidade.cidade_key = aluno.cidade_key) and
    (matricula.disciplina_key = disciplina.disciplina_key) and
    (aluno.aluno_key = matricula.aluno_key)
