from pipeline.model import save_model
from pipeline.mar_creator import create_mar
from pipeline.gcs_upload import upload_mar
from pipeline.deploy_model import deploy_model

PROJECT = "planar-sun-456513-i8"
BUCKET = "capstone-group15"
LOCATION = "us-central1"
GCS_SUBDIR = "models/simple-v1/"

if __name__ == "__main__":
    save_model()
    create_mar()
    upload_mar(bucket_name=BUCKET, gcs_subdir=GCS_SUBDIR)
    deploy_model(PROJECT, LOCATION, BUCKET, gcs_subdir=GCS_SUBDIR)
