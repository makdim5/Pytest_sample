from tests.test_file_worker import TEST_FILEPATH
import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open(TEST_FILEPATH, "w"):
        pass


def create_test_data_in_file(test_data):
    with open(TEST_FILEPATH, "a") as file_open:
        file_open.writelines(test_data)
