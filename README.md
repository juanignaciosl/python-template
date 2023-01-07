Template for Python projects.

Features:

- mypy (runs as a test, see `test_mypy_compliance`)
- flake8
- tox
- black (as a check, you should setup your environment to run it)
- isort (as a check, you should setup your environment to run it)

# Installing

Clone and remove git history.

    git clone git@github.com:juanignaciosl/python-template.git mynewpythonproject
    cd mynewpythonproject && rm -rf .git

Setup a virtualenv:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

_Versions are not set at requirements.txt, you probably want to edit that file._

At this point, you probably want to run...
1. `git init && git add . && git commit -a -m "First commit"`.
2. Search for `mymodule` and replace it with your own module in all files but this one.
3. `git add . && git commit -a -m "mymodule -> myactualmodule"`.

# Running in local

    python mymodule/greetings.py

Use `tox` for running all the tests and linters.

# Running in Docker

    docker-compose build mymodule
    docker-compose run --rm mymodule tox
    docker-compose run --rm mymodule run
    docker-compose run --rm mymodule test
    docker-compose run --rm mymodule lint

# Pending improvements

- [ ] Remove the need for replacing mymodule at config files.
- [ ] Pre-commit or pre-push hook.

# References

- [Four Horsemen of the Python Apocalypse](https://blog.kartones.net/post/four-horsemen-python-apocalypse/).
    - [Gist for running mypy as part of tests](https://github.com/Kartones/finished-games/blob/a7ff4fd0de0bab8cea434956396da68064262a1d/finishedgames/test/test_linters.py).
