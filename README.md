# Gerador de SQL a partir de CSV 📊💻

Bem vindo(a)! Este repositório contém um script Python que lê um arquivo CSV e gera um arquivo SQL com instruções `INSERT` para um banco de dados 🗄️.

## Requisitos 🔧

- Python 3.x
- Biblioteca pandas (use `pip install pandas` para instalar)

## Como usar 🚀

1. Coloque o arquivo CSV no mesmo diretório do script py.
2. Execute o `gerar-sql.py` para gerar o arquivo `dados.sql` com as instruções de inserção.

### Exemplo do arquivo CSV (`infos_alunos.csv`) 📄

```csv
123456;aaaaaaaaaaaaaaaaaaa;dd-mm-aaaa;biologia
654321;bbbbbbbbbbbbbbbbbbb;dd-mm-aaaa;matematica
```

## O que o script faz 🤖

O script lê o arquivo CSV, converte os dados em maiúsculas (para as colunas de texto), e gera um arquivo SQL com instruções de inserção para a tabela aluno.

## Arquivo gerado (dados.sql) 📜

O arquivo dados.sql terá instruções no seguinte formato:

```
INSERT INTO aluno (matricula, nome, data_nascimento, curso) VALUES ('123456', 'AAAAAAAAAAAAAAAAAAA', 'DD-MM-AAAA', 'BIOLOGIA');
INSERT INTO aluno (matricula, nome, data_nascimento, curso) VALUES ('654321', 'BBBBBBBBBBBBBBBBBB', 'DD-MM-AAAA', 'MATEMATICA');
```

## Contribuição 🤝

Se você encontrar algum problema ou quiser sugerir melhorias 💡, fique à vontade para abrir um issue ou enviar um pull request 🔀.

---

🖤 **Obrigada por visitar este repositório!**
