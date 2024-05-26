import os
import pandas as pd

def convert_xlsx(download_dir, xlsx_file, csv_file,filename):
    try:
        base_dir = download_dir
        csv_dir = os.path.join(base_dir,'converted', filename)
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

    
        # Upload the XLSX file
        xls = pd.ExcelFile(xlsx_file)


        # Iterate over the sheets in the XLSX file
        for sheet_name in xls.sheet_names:
            #Read spreadsheet as DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name)

            #CSV file name
            csv_file = os.path.join(csv_dir, f"{sheet_name}.csv")

            #Save the DataFrame as CSV
            df.to_csv(csv_file, index=False)
            print(f"Convertido: {sheet_name} para {csv_file}")
            
    except Exception as e:
        print(f"Erro ao converter arquivo: {e}")