from prefect import flow, task

@flow
def my_flow():
    for i in range(100):
        my_task(i)

@task
def my_task(i):
    print(i)

if __name__ == "__main__":
    my_flow()