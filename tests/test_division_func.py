from model_funcs.division import division_func
import pytest

# Тест на проверку работы функции
# при различных правильных ожидаемых данных
@pytest.mark.parametrize("a, b, expected_result",
                         [(10, 2, 5),
                          (-10, 2, -5),
                          (30, -3, -10),
                          (-40, -10, 4)])
def test_division(a, b, expected_result):
    assert division_func(a, b) == expected_result


# Проверка на вылет ожидаемого исключения
# После pytest.raises указываем нужное исключение
@pytest.mark.parametrize("expected_exception, devider",
                         [(ZeroDivisionError, 0),
                          (TypeError, "huhh")])
def test_division_with_error(expected_exception, devider):
    with pytest.raises(expected_exception):
        division_func(10, devider)
