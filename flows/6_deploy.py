from prefect import flow, task, get_run_logger as _logger
from prefect.docker import DockerImage
from prefect.runtime import task_run
import time

@flow(retries=1, retry_delay_seconds=30)
def my_pipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
    time.sleep(20)
    raise Exception("Pipeline failed")

@task
def extract():
    _logger().info("Extracting data")
    return [1, 2, 3]

@task
def transform(data):
    _logger().info("Transforming data")
    return [str(d) for d in data]

@task
def load(transformed_data):
    _logger().info("Loading data")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/kevingrismore/cellarity-demo.git",
        entrypoint="flows/6_deploy.py:my_pipeline",
    ).deploy(
        name="long-retry",
        work_pool_name="local",
    )