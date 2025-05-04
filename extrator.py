import os
from dotenv import load_dotenv
import pandas as pd
from google.cloud import bigquery

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def extrator():
    gclient = bigquery.Client()
    tabelas = ['cnae', 'uf', 'ir_ipi', 'itr', 'natureza_juridica']
    query_padrao = "select * from `basedosdados.br_rf_arrecadacao`."
    for t in tabelas:
        try:
            query = query_padrao + t
            print(query)
            dados = gclient.query(query).to_dataframe()
            dados.to_csv(f'./dados_brutos/dados_{t}.csv', index=False)
            print(f'Tabela {t} extraída com sucesso!\n')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    extrator()
