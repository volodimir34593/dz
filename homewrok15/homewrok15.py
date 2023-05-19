# Файл test_module.py
import pytest
from my_project.module import my_function

def test_my_function():
    # Перевіряємо, чи функція повертає очікуваний результат
    assert my_function(3, 5) == 8
    assert my_function(10, 2) == 12

    # Перевіряємо, чи функція правильно обробляє виключні ситуації
    with pytest.raises(ValueError):
        my_function(5, "abc")

    with pytest.raises(ValueError):
        my_function(10, 0)