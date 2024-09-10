from prefect import flow, task, get_run_logger as _logger

@flow
def my_pipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

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
    for d in transformed_data:
        # Simulate a failure
        if d == "2":
            raise Exception("Failed to load data")

if __name__ == "__main__":
    my_pipeline()