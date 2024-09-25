from prefect import flow, get_client
from prefect.runtime import deployment

@flow(log_prints=True)
def a_flow():
   deployment_id = deployment.get_id()
   with get_client(sync_client=True) as client:
       deployment_response = client.read_deployment(deployment_id)
       print(deployment_response.work_pool_name)


if __name__ == "__main__":
    if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/kevingrismore/cellarity-demo.git",
        entrypoint="flows/8_get_work_pool.py:a_flow",
    ).deploy(
        name="print_work_pool",
        work_pool_name="local",
    )