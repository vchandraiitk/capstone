from google.cloud import storage

def upload_mar(bucket_name, gcs_path="models/simple-v1/simple-v1.mar"):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    ##blob = bucket.blob(gcs_path)
    ##blob.upload_from_filename("model-store/simple-v1.mar")
    
    blob = bucket.blob("models/simple-v1/simple-v1.mar")
    blob.upload_from_filename("model-store/simple-v1.mar")
    print(f"✅ Uploaded to gs://{bucket_name}/{gcs_path}")

