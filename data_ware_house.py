import pandas as pd
import numpy as np

# Define o tamanho limite para categorias de 600:
total_de_produtos = 600
produtos = {
    "produto_id": range(1, total_de_produtos + 1),
    "nome": [f"Produto {i}" for i in range(1, total_de_produtos + 1)],
    "categoria": np.random.choice(["Eletrônicos", "Roupas", "Alimentos"], total_de_produtos),
}

# Coloca todos os produtos dentro do Data Frame:
df_produtos = pd.DataFrame(produtos)

# Define 1000 vendas:
total_de_vendas = 1000
data_vendas = {
    "data": np.random.choice(pd.date_range("2024-04-01", periods=30), total_de_vendas),
    "produto_id": np.random.randint(1, total_de_produtos + 1, total_de_vendas),
    "quantidade": np.random.randint(50, 500, total_de_vendas),
    "valor_total": np.random.randint(1000, 10000, total_de_vendas),
}

# Coloca todas as vendas dentro do Data Frame:
df_vendas = pd.DataFrame(data_vendas)

# Salva as vendas num arquivo .csv:
df_vendas.to_csv("vendas.csv", index=False)

#Salva os produtos num arquivo .csv:
df_produtos.to_csv("produtos.csv", index=False)

# Atrela cada arquivo .csv a uma variavel:
df_vendas = pd.read_csv("vendas.csv")
df_produtos = pd.read_csv("produtos.csv")

# Agrupa as vendas e os produtos:
df_merge = pd.merge(df_vendas, df_produtos, on="produto_id", how="inner")

# Cria um arquivo .csv para armazenar as informações que foram agrupadas
df_merge.to_csv("data_warehouse.csv", index=False)

# Salva em uma variável para poder fazer a leitura do warehouse
df_warehouse = pd.read_csv("data_warehouse.csv")
print("Conteúdo do data_warehouse.csv")
print(df_warehouse)

