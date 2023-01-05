import subprocess
import sys


def test_mypy_compliance() -> None:
    mypy_binary = subprocess \
        .check_output('which mypy', shell=True, stderr=sys.stderr) \
        .decode('ascii') \
        .replace('\n', '')

    result = subprocess.call(f'{mypy_binary} mymodule tests',
                             shell=True,
                             stdout=sys.stdout,
                             stderr=sys.stderr)
    assert result == 0
