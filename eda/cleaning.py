import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Directory where the converted CSV files are located
converted_dir = '../data/converted'
subdirectories = [os.path.join(converted_dir, d) for d in os.listdir(converted_dir) if os.path.isdir(os.path.join(converted_dir, d))]

for subdir in subdirectories:
    print(f"Processando arquivos em {subdir}")
    
    #List all files in the subdirectory
    files = os.listdir(subdir)
    
    #Iterates over each file in the subdirectory
    for file in files:
        if not file.endswith('.csv') and not file.startswith('Tab'):  
            print(f"Ignorando arquivo: {file}")
            continue  #Skip to next file without processing
        
        csv_path = os.path.join(subdir, file)
        print(f"Processando arquivo: {csv_path}")

        #Read CSV file as DataFrame
        df = pd.read_csv(csv_path)

        #Performs cleaning operations
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        #Saves the cleaned DataFrame back as CSV (overwrites the original file)
        df.to_csv(csv_path, index=False)

        print(f"Arquivo {csv_path} processado e salvo.")

print("Processamento de todos os arquivos concluído.")