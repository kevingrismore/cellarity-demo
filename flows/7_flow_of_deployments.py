from prefect import flow, task, get_run_logger as _logger
from prefect.deployments import run_deployment
from prefect.docker import DockerImage
from prefect.futures import wait

@flow
def parent():
    futures = []
    for i in range(2):
        futures.append(run_child.submit(i))

    wait(futures)

@flow
def child(i):
    _logger().info(i)

@task
def run_child(i):
    run_deployment(name="child/child-deployment", parameters=dict(i=i))


if __name__ == "__main__":
    parent.deploy(
        name="parent-deployment",
        image=DockerImage(
            name="kevingrismoreprefect/cellarity-pipeline:2",
            platform="linux/amd64",
        ),
        work_pool_name="ecs-asg",
    )
    child.deploy(
        name="child-deployment",
        image=DockerImage(
            name="kevingrismoreprefect/cellarity-pipeline:2",
            platform="linux/amd64",
        ),
        work_pool_name="ecs-asg",
    )