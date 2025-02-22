import pandas as pd
import os

arquivo_csv = "infos_alunos.csv" #Nome do arquivo CSV

#Verifica se o arquivo existe
if not os.path.exists(arquivo_csv):
    print(f"Erro: O arquivo {arquivo_csv} não foi encontrado.")
else:
    try:
        df = pd.read_csv(arquivo_csv, encoding="utf-8", sep=";", header=None) #Leitura do arquivo CSV.
        
        nome_tabela = "aluno" #Nome da tabela
        nome_colunas = "(matricula, nome, data_nascimento, curso)" #Nomes das colunas
        
        with open("dados.sql", "w", encoding="utf-8") as f:
            for _, row in df.iterrows():
                valores = ", ".join(f"'{x.upper()}'" if isinstance(x, str) else str(x) for x in row.values)
                sql = f"INSERT INTO {nome_tabela} {nome_colunas} VALUES ({valores});"
                f.write(sql + "\n")
        
        print("Arquivo SQL gerado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")