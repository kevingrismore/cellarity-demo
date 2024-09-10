from prefect import task, flow
from prefect.transactions import transaction


@task(cache_key_fn=lambda *args, **kwargs: "static-key1")
def load_data():
    return "some-data"


@task(cache_key_fn=lambda *args, **kwargs: "static-key2")
def process_data(data, fail):
    if fail:
        raise RuntimeError("Error! Abort!")

    return len(data)


@flow
def multi_task_cache(fail: bool = True):
    with transaction():
        data = load_data()
        process_data(data=data, fail=fail)

if __name__ == "__main__":
    multi_task_cache.serve(parameters={"fail":True})