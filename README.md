# qr-generator

Generate QR code using FastAPI


# Run all tests

- Use the command: `python run_tests.py`

# Run tests individually
## Pytest

- Run test with `pytest -v`

## Coverage report

- Run test with `coverage run -m pytest -v`
- Then generate report with: `coverage report -m`

## Pylint

- Run code style checks with: `pylint --extension-pkg-whitelist='pydantic' app`