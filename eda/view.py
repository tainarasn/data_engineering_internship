import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos como exemplo
data = {
    "Região": ["Brasil", "Norte", "Rondônia", "Acre", "Amazonas", "Roraima", "Pará", "Região Metropolitana de Belém", "Amapá", "Tocantins", 
               "Nordeste", "Maranhão", "Piauí", "Ceará", "Região Metropolitana de Fortaleza", "Rio Grande do Norte", "Paraíba", "Pernambuco", 
               "Região Metropolitana de Recife", "Alagoas", "Sergipe", "Bahia", "Região Metropolitana de Salvador", "Sudeste", "Minas Gerais", 
               "Região Metropolitana de Belo Horizonte", "Espírito Santo", "Rio de Janeiro", "Região Metropolitana do Rio de Janeiro", "São Paulo", 
               "Região Metropolitana de São Paulo", "Sul", "Paraná", "Região Metropolitana de Curitiba", "Santa Catarina", "Rio Grande do Sul", 
               "Região Metropolitana de Porto Alegre", "Centro-Oeste", "Mato Grosso do Sul", "Mato Grosso", "Goiás", "Distrito Federal"],
    "Utilizaram": [177656.822, 14536.868, 1498.147, 651.348, 3216.277, 420.511, 6837.456, 1922.792, 623.225, 1289.904, 
                 48409.904, 5654.411, 2737.791, 7675.584, 3344.522, 2975.62, 3411.321, 8100.013, 3454.326, 2849.124, 1920.947, 13085.093, 3477.228, 
                 75598.609, 18379.764, 4625.536, 3427.822, 14646.539, 10770.231, 39144.484, 18604.133, 25771.8, 9745.617, 3030.41, 6048.506, 9977.677, 
                 3722.776, 13339.641, 2283.967, 2766.131, 5730.676, 2558.867],
    "Não Utilizaram": [102083.09, 6715.311, 710.57, 285.382, 1596.758, 268.027, 2962.659, 1227.217, 334.728, 557.187, 
                 21831.084, 1940.697, 1061.0, 3331.027, 1950.387, 1570.481, 1738.3, 3710.885, 2080.0, 1175.405, 982.846, 6320.443, 2468.34, 
                 49246.983, 10332.092, 3175.428, 2004.128, 9707.466, 7529.582, 27203.297, 13592.382, 15758.972, 5897.03, 2065.537, 3767.691, 
                 6094.251, 2610.59, 8530.74, 1455.931, 1526.026, 3541.957, 2006.826]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Filtrar por regiões específicas (Norte, Nordeste, Sudeste, Sul, Centro-Oeste)
regions = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
df_regions = df[df["Região"].isin(regions)]

# Plotar gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_regions["Região"], df_regions["Utilizaram"], label='Utilizaram', alpha=0.6)
plt.bar(df_regions["Região"], df_regions["Não Utilizaram"], label='Não utilizaram', alpha=0.6)
plt.xlabel('Região')
plt.ylabel('Situação')
plt.title('Situação por Região')
plt.legend()
plt.show()

# Plotar gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(df_regions["Região"], df_regions["Coluna_3"], marker='o', label='Coluna 3')
plt.plot(df_regions["Região"], df_regions["Coluna_4"], marker='o', label='Coluna 4')
plt.xlabel('Região')
plt.ylabel('Valores')
plt.title('Valores das Colunas 3 e 4 por Região')
plt.legend()
plt.show()
