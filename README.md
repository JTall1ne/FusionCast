# FusionCast

FusionCast is an open-source toolkit for building weather intelligence systems that blend
traditional meteorological datasets with real-time signals from the public internet (social
media, connected sensors, webcams, and more). The project aims to make it easy to experiment
with multi-modal data fusion pipelines and serve insights through modern web APIs.

## Requirements

- Python 3.11 or newer
- macOS, Linux, or Windows 10+
- [UV](https://github.com/astral-sh/uv) or `pip` for dependency management (examples below use `uv`)

## Quickstart

```bash
# Clone the repository
git clone https://github.com/FusionCast/FusionCast.git
cd FusionCast

# Create a virtual environment (using uv)
uv venv --python 3.11
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`

# Install runtime dependencies
uv pip install .

# Install development tools (formatters, linters, tests)
uv pip install '.[dev]'
```

Prefer `pip`? Substitute the install commands above with:

```bash
python -m venv .venv
source .venv/bin/activate  # `.venv\\Scripts\\activate` on Windows
python -m pip install --upgrade pip
python -m pip install . '.[dev]'
```

Once installed you can start iterating on the code base inside the `src/` directory. The
primary Python package is published as `fusioncast`.

## Developer Workflow

### Code Style & Formatting

We use [Ruff](https://docs.astral.sh/ruff/) for linting, formatting, and import sorting.
Run the following to check your code:

```bash
ruff check .
```


## Environment Configuration

FusionCast uses several third-party APIs (for example, weather providers and real-time internet sources). To configure the required API keys:

1. Copy the `.env.template` file in the repository root to a new file named `.env`.
2. Open `.env` and fill in the environment variables with your own API keys (for example, `OPENAI_API_KEY`, `OPENWEATHERMAP_API_KEY`, `TWITTER_BEARER_TOKEN`, and others as needed).
3. When running scripts or the application, the `.env` file will be automatically loaded so that your environment variables are available. Do **not** commit your `.env` file to version control—use `.env.template` for sharing example values.

If you're running FusionCast inside a Docker container, you can pass the required environment variables using `--env-file .env` or specify them individually with `-e`. Ensure the container has access to your keys so that API calls succeed.





To auto-fix lint and formatting issues:

```bash
ruff check . --fix
ruff format .
```

### Type Checking

Run [mypy](http://mypy-lang.org/) in strict mode to ensure type safety:


```bash
mypy src
```

### Testing

Tests live under the `tests/` directory. (A formal test harness is added in the next step of the
FusionCast v1.0.0 plan.) When tests exist, run them with:

```bash
pytest
```

## Project Layout

- `src/fusioncast/`: Python package with core modules.
- `api/`: Future FastAPI application entry points.
- `data/`: Example datasets and fixtures (non-versioned large data should be stored elsewhere).
- `notebooks/`: Exploratory analysis and prototype notebooks.

## Licensing

FusionCast is released under the [Apache-2.0 License](LICENSE).
