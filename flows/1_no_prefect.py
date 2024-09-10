import logging
import sys

_logger = logging.getLogger()
_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
_logger.addHandler(handler)

def my_pipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

def extract():
    _logger.info("Extracting data")
    return [1, 2, 3]

def transform(data):
    _logger.info("Transforming data")
    return [str(d) for d in data]

def load(transformed_data):
    _logger.info("Loading data")
    for d in transformed_data:
        # Simulate a failure
        if d == "2":
            raise Exception("Failed to load data")

if __name__ == "__main__":
    my_pipeline()