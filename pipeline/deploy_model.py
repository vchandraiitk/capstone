from google.cloud import aiplatform

def deploy_model(project, location, bucket_name, gcs_subdir="models/"):
    aiplatform.init(project=project, location=location)

    model = aiplatform.Model.upload(
        display_name="simple-v1",
        artifact_uri=f"gs://{bucket_name}/{gcs_subdir}",  # ✅ will be gs://capstone-group15/models/
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.1-13:latest",
    )

    model.wait()
    print(f"✅ Model deployed to Vertex AI: {model.resource_name}")
