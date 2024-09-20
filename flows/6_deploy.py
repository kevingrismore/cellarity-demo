from prefect import flow, task, get_run_logger as _logger
from prefect.docker import DockerImage
from prefect.runtime import task_run

@flow(retries=1, retry_delay_seconds=30)
def my_pipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
    raise Exception("Pipeline failed")

@task
def extract():
    _logger().info("Extracting data")
    return [1, 2, 3]

@task
def transform(data):
    _logger().info("Transforming data")
    return [str(d) for d in data]

@task(retries=1)
def load(transformed_data):
    _logger().info("Loading data")
    if task_run.get_run_count() == 1:
        for d in transformed_data:
            # Simulate a failure
            if d == "2":
                raise Exception("Failed to load data")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/kevingrismore/cellarity-demo.git",
        entrypoint="flows/6_deploy.py:my_pipeline",
    ).deploy(
        name="long-retry",
        work_pool_name="local",
    )