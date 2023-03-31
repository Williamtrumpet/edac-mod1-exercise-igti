import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

#Download de arquivos de um Bucket da a AWS
s3_client.download_file("datalake-igti-edac-william",
                        "raw-data/enem/MICRODADOS_ENEM_2020.csv",
                        "MICRODADOS_ENEM_2020.csv")

df = pd.read_csv("MICRODADOS_ENEM_2020.csv", sep=";")
print(df)

#Upload de arquivos para um Bucket na AWS
s3_client.upload_file('MICRODADOS_ENEM_2020.csv',
                      'datalake-igti-edac-william',
                      'raw-data/enem/MICRODADOS_ENEM_2020.csv')