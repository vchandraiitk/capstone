from google.cloud import storage

def upload_mar(bucket_name, gcs_subdir="models/simple-v1/"):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Local .mar file path
    local_path = "model-store/simple-v1.mar"
    
    # Upload to GCS path (as simple-v1.mar under the given folder)
    blob = bucket.blob(f"{gcs_subdir}simple-v1.mar")
    blob.upload_from_filename(local_path)
    print(f"✅ Uploaded to gs://{bucket_name}/{gcs_subdir}simple-v1.mar")
