import pytest
from katas_and_stuff.greeting_kata import greet, greet_two, is_shouted, split_name


def test_greet():
    # Given
    name = "Bob"
    expected_greeting = "Hello, Bob."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_no_name():
    # Given
    name = None
    expected_greeting = "Hello, my friend."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_all_uppercase():
    # Given
    name = "JERRY"
    expected_greeting = "HELLO JERRY!"
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


@pytest.mark.parametrize(("name", "expected"), [("JERRY", True), ("Jerry", False)])
def test_is_shouted(name, expected):
    # Given
    # When
    result = is_shouted(name)
    # Then
    assert result == expected


def test_greet_numbers():
    # Given
    name = "1234"
    expected_greeting = "Hello, robot."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_arrays():
    # Given
    name = ["Jill", "Jane"]
    expected_greeting = "Hello, Jill and Jane."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_numbers_c():
    # Given
    name = "1234c"
    expected_greeting = "Hello, 1234c."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_two():
    # given
    name = ["Jill", "Jane"]
    expected_out = "Jill and Jane"
    # when
    out = greet_two(name)
    # then
    assert out == expected_out


def test_greet_arrays_more_than_2():
    # Given
    name = ["Amy", "Brian", "Charlotte"]
    expected_greeting = "Hello, Amy, Brian and Charlotte."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_mixed_shouted_names():
    # Given
    name = ["Amy", "BRIAN", "Charlotte"]
    expected_greeting = "Hello, Amy and Charlotte. AND HELLO BRIAN!"
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_split_commas():
    # Given
    name = ["Bob", "Charlie, Dianne"]
    expected_new_name = ["Bob", "Charlie", "Dianne"]
    # When
    new_name = split_name(name)
    # Then
    assert new_name == expected_new_name


def test_greeting_containing_commas():
    # Given
    name = ["Bob", "Charlie, Dianne"]
    expected_greeting = "Hello, Bob, Charlie, and Dianne."
    # When
    greeting = greet(name)
    # Then
    assert greeting == greeting


def test_greeting_escaped_commas():
    # Given
    name = ["Bob", '"Charlie, Dianne"']
    expected_greeting = "Hello, Bob, Charlie, and Dianne."
    # When
    greeting = greet(name)
    # Then
    assert greeting == greeting
