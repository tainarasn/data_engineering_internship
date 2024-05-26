import os
import pandas as pd
from matplotlib import pyplot

# Diretório onde estão os arquivos CSV convertidos
converted_dir = '../data/converted'
subdirectories = [os.path.join(converted_dir, d) for d in os.listdir(converted_dir) if os.path.isdir(os.path.join(converted_dir, d))]

for subdir in subdirectories:
    print(f"Processando arquivos em {subdir}")
    
    # Lista todos os arquivos no subdiretório
    files = os.listdir(subdir)
    
    # Itera sobre cada arquivo no subdiretório
    for file in files:
        if file.endswith('.csv') and not file.startswith('Tab'):  # Ignora arquivos que não começam com 'Tab'
            print(f"Ignorando arquivo: {file}")
            continue  # Pula para o próximo arquivo sem processar
        
        csv_path = os.path.join(subdir, file)
        print(f"Processando arquivo: {csv_path}")

        # Lê o arquivo CSV como DataFrame
        df = pd.read_csv(csv_path)

        # Realiza as operações de limpeza
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Salva o DataFrame limpo de volta como CSV (substitui o arquivo original)
        df.to_csv(csv_path, index=False)

        print(f"Arquivo {csv_path} processado e salvo.")

print("Processamento de todos os arquivos concluído.")