# Contributing to FusionCast

Thank you for your interest in contributing to FusionCast! We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and examples.

## Development setup

1. Clone the repository and check out the latest code:

```
git clone https://github.com/JTall1ne/FusionCast.git
cd FusionCast
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -e .[dev]  # Install dependencies for development and testing
```

2. Copy `.env.template` to `.env` and set your API keys as needed.

## Running tests

We use [pytest](https://pytest.org) for testing. To run the test suite:

```
pytest -q
```

Please add tests for any new functionality. Ensure all tests pass and linting succeeds before submitting a pull request.

## Code style

We follow standard Python style (PEP 8) with [black](https://black.readthedocs.io) and [flake8](https://flake8.pycqa.org). Please format your code and fix any linter warnings. Our CI will check these automatically.

## Pull requests

- Submit your changes via a pull request targeting the `main` branch.
- Keep pull requests focused and small; separate unrelated changes into separate PRs.
- Include a clear description of what your change does and why.
- Update documentation and examples when appropriate.

## Code of Conduct

This project follows the Contributor Covenant Code of Conduct. Please be respectful in all interactions. See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for details.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0, the same as the rest of the project.
