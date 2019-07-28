#!/usr/bin/env sh
set -e
case "$1" in
  run)
    exec python mymodule/greetings.py
  ;;
  lint)
    exec flake8 mymodule tests
  ;;
  test)
    exec python -m pytest tests
  ;;
esac

exec "$@"
