from prefect.infrastructure.docker import DockerContainer

# alternative to creating DockerContainer block in the UI
docker_block = DockerContainer(
    image="angeldevicente/de-zoomcamp-prefect:v1",  
    image_pull_policy="ALWAYS",
    auto_remove=True,
)

docker_block.save("docker-de-zoomcamp", overwrite=True)
