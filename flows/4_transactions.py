import os


from prefect import task, flow
from prefect.transactions import transaction


@task
def write_file(contents: str):
    "Writes to a file."
    with open("side-effect.txt", "w") as f:
        f.write(contents)


@write_file.on_rollback
def del_file(transaction):
    "Deletes file."
    os.unlink("side-effect.txt")


@task
def quality_test():
    "Checks contents of file."
    with open("side-effect.txt", "r") as f:
        data = f.readlines()

    if len(data) < 2:
        raise ValueError("Not enough data!")


@flow
def pipeline(contents: str):
    with transaction():
        write_file(contents)
        quality_test()


if __name__ == "__main__":
    pipeline(contents="hello\nworld")