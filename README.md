## Local

Setup: `pip install -r requirements.txt`

Run: `python mymodule/greetings.py`

Test: `python -m pytest tests`

Lint: `flake8 mymodule tests`

## Docker

Run: `docker-compose run --rm mymodule run`

Test: `docker-compose run --rm mymodule test`

Lint: `docker-compose run --rm mymodule lint`
