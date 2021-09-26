from model_funcs.file_worker import read_from_file
from tests.test_file_worker import TEST_FILEPATH
from tests.test_file_worker.conf_test import create_test_data_in_file, clean_text_file


def test_read_from_file_one():
    expected_data = ['one\n', 'two\n', 'three\n']
    create_test_data_in_file(expected_data)
    assert expected_data == read_from_file(TEST_FILEPATH)


def test_read_from_file_two():
    expected_data = ['onrgrgrgrge\n', 'two\n', 'three\n',
                     "four\n"]
    create_test_data_in_file(expected_data)
    assert expected_data == read_from_file(TEST_FILEPATH)


def test_read_from_file_three():
    expected_data = ['three\n',
                     "four\n"]
    create_test_data_in_file(expected_data)
    assert expected_data == read_from_file(TEST_FILEPATH)