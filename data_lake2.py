import pandas as pd
import numpy as np
import os

# Cria uma pasta para guardar os arquivos caso ela não exista:
if not os.path.exists('data_lake'):
    os.makedirs('data_lake')

# Limita um total de 10 arquivos 1000 linhas:
num_files = 10
num_rows_per_file = 1000

# Cria um array vazio para armazenas DataFrames:
dfs = []

# Usa um loop para criar e salvar arquivso .csv:
for i in range(num_files):

  # Código que gera informações aleatórias em uma linha:
    data = {
        'coluna1': np.random.randint(0, 100, num_rows_per_file),
        'coluna2': np.random.randn(num_rows_per_file),
        'coluna3': np.random.choice(['A', 'B', 'C'], num_rows_per_file)
    }

    # Cria um DataFrame com os dados:
    df = pd.DataFrame(data)

    # Define o nome do arquivo e salva como .csv:
    file_name = f'data_lake/dados{i+1}.csv'
    df.to_csv(file_name, index=False)

    # Adiciona o arquivo e o DataFrame ao array:
    dfs.append((file_name, df))

print("<- DADOS PARA O DATALAKE FORAM GERADOS COM SUCESSO ->")

# Exibe as informações dos arquivos que foram gerados:
for file_name, df in dfs:
    print(f"\nINFORMAÇÕES DO ARQUIVO: {file_name}\n")
    print(df.head())