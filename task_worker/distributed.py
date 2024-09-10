from prefect import flow, task

@flow
def distributed_flow():
    for i in range(5):
        my_task.delay(i)

@task
def my_task(i):
    print(i)
    return i

if __name__ == "__main__":
    distributed_flow()