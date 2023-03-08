"""Run tests"""
import os


def run_tests():
    """Run tests."""
    os.system("coverage run -m pytest -v")
    os.system('coverage report -m')
    os.system('pylint --extension-pkg-whitelist="pydantic" app')


if __name__ == "__main__":
    run_tests()
