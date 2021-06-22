import os
from dotenv import load_dotenv
from fastapi import FastAPI
from google.cloud import storage


load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('CREDENTIALS')
app = FastAPI()

@app.get('/')
def hello():
    return {"Hello" : "Friend"}

@app.get('/pull_csv')
def pull_csv():
    
    bucket_name = os.getenv('BUCKET_NAME')
    source_blob_name = os.getenv('SOURCE_BLOB_NAME')
    destination_file_name = os.getenv('DESTINATION_FILE_NAME')

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


    return {f'Blob {source_blob_name} downloaded to {destination_file_name}' }
