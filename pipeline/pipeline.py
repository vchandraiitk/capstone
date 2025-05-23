from google.cloud import storage
from pipeline.model import save_model
from pipeline.deploy_model import deploy_model

PROJECT = "planar-sun-456513-i8"
BUCKET = "capstone-group15"
LOCATION = "us-central1"
GCS_SUBDIR = "models/"  # ✅ no subfolder

def upload_model_pt(bucket_name, gcs_subdir="models/"):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"{gcs_subdir}simple_model.pt")  # ✅ match filename
    blob.upload_from_filename("model.pt")
    print(f"✅ Uploaded to gs://{bucket_name}/{gcs_subdir}simple_model.pt")

if __name__ == "__main__":
    save_model()  # saves model.pt locally
    upload_model_pt(bucket_name=BUCKET, gcs_subdir=GCS_SUBDIR)
    deploy_model(PROJECT, LOCATION, BUCKET, gcs_subdir=GCS_SUBDIR)
