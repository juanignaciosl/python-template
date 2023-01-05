Template for Python projects.

Features:

- mypy (runs as a test, see `test_mypy_compliance`)
- flake8
- tox

# Installing

Clone and remove git history.

    git clone git@github.com:juanignaciosl/python-template.git mynewpythonproject
    cd mynewpythonproject && rm -rf .git

Setup a virtualenv:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

_Versions are not set at requirements.txt, you probably want to edit that file._

# Running in local

    python mymodule/greetings.py
    python -m pytest tests

You can also use `tox` for running the tests and linters.

## Manual linting

    mypy mymodule tests  # This is not needed, mypy is run at test step
    flake8 mymodule tests

# Running in Docker

    docker-compose build mymodule
    docker-compose run --rm mymodule tox
    docker-compose run --rm mymodule run
    docker-compose run --rm mymodule test
    docker-compose run --rm mymodule lint

# References

- [Four Horsemen of the Python Apocalypse](https://blog.kartones.net/post/four-horsemen-python-apocalypse/).
    - [Gist for running mypy as part of tests](https://github.com/Kartones/finished-games/blob/a7ff4fd0de0bab8cea434956396da68064262a1d/finishedgames/test/test_linters.py).
