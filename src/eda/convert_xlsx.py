import os
import pandas as pd

def convert_xlsx(self, xlsx_file, csv_file,filename):
    try:
        converted_dir = os.path.join(self.download_dir, 'converted')  # Diretório onde serão armazenados os arquivos convertidos
        if not os.path.exists(converted_dir):
            os.makedirs(converted_dir)

        # Carrega o arquivo XLSX
        xls = pd.ExcelFile(xlsx_file)

        # Itera sobre as planilhas no arquivo XLSX
        for sheet_name in xls.sheet_names:
            # Lê a planilha como DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name)

            # Nome do arquivo CSV
            csv_file = os.path.join(converted_dir, f"{filename}_{sheet_name}.csv")

            # Salva o DataFrame como CSV
            df.to_csv(csv_file, index=False)
            print(f"Convertido: {sheet_name} para {csv_file}")
            
    except Exception as e:
        print(f"Erro ao converter arquivo: {e}")