from mymodule import greetings


def test_works() -> None:
    assert greetings.greetings() == "Hi!"
