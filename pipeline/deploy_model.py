from google.cloud import aiplatform

def deploy_model(project, location, bucket_name):
    aiplatform.init(project=project, location=location)
    model = aiplatform.Model.upload(
        display_name="simple-v1",
        artifact_uri=f"gs://{bucket_name}/models/simple-v1/",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.1-13:latest",
    )
    model.wait()
    print(f"✅ Model deployed: {model.resource_name}")
