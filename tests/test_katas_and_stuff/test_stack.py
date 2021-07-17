import pytest
from katas_and_stuff.stack import Stack

# given ?
@pytest.fixture
def my_stack():
    return Stack()


def test_new_stack_is_empty(my_stack):
    assert my_stack.is_empty()


def test_after_one_push_is_not_empty(my_stack):
    my_stack.push(0)
    assert not my_stack.is_empty()


def test_will_throw_underflow_when_empty_stack(my_stack):
    with pytest.raises(Stack.UnderflowException):
        item = my_stack.pop()


def test_one_push_one_pop_will_be_empty(my_stack):
    my_stack.push(0)
    my_stack.pop()
    assert my_stack.is_empty()


def test_push_twice_pop_once_will_not_be_empty(my_stack):
    my_stack.push(0)
    my_stack.push(0)
    my_stack.pop()

    assert not my_stack.is_empty()


@pytest.mark.parametrize(("x"), (99, 88))
def test_push_x_will_pop_x(my_stack, x):
    my_stack.push(x)
    assert my_stack.pop() == x


@pytest.mark.parametrize(("x", "y"), [(99, 88)])
def test_after_pushing_x_y_it_will_pop_y_x(my_stack, x, y):
    my_stack.push(x)
    my_stack.push(y)
    assert my_stack.pop() == y
    assert my_stack.pop() == x
