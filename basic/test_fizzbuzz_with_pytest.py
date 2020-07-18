from fizzbuzz import fizzbuzz


def test_input_5_should_return_buzz():
    result = fizzbuzz(5)
    assert result == 'Buzz'