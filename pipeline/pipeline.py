from google.cloud import aiplatform

def run_pipeline():
    aiplatform.init(project="planar-sun-456513", location="us-central1")

    model = aiplatform.Model.upload(
        display_name="simple-model",
        artifact_uri="gs://capstone-group15/models/simple-v1/",  # ✅ folder only
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.1-13:latest"
    )

    endpoint = aiplatform.Endpoint.create(display_name="simple-model-endpoint")

    model.deploy(
        endpoint=endpoint,
        deployed_model_display_name="simple-model-v1",
        machine_type="n1-standard-2"
    )

if __name__ == "__main__":
    run_pipeline()
