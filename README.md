# Gerador de SQL a partir de CSV 📊💻

Bem vindo(a)! Este projeto surgiu da minha própria necessidade de extrair muitos dados de arquivos CSV e gerar automaticamente comandos SQL para inserção no banco de dados 🗄️.

Ao precisar lidar com um grande volume de dados e simplificar o processo de inserção em uma tabela de banco de dados, desenvolvi este script Python  que lê um arquivo CSV, transforma os dados e gera um arquivo SQL com as instruções `INSERT` correspondentes.

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

Se você encontrar algum problema ou quiser sugerir melhorias, fique à vontade para abrir um issue ou enviar um pull request 🔀.

---

🖤 **Obrigada por visitar este repositório!**
