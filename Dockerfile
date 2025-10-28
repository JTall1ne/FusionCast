# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy pyproject file and install dependencies
COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install .

# Copy the rest of the application code
COPY . .

# Default command: open a bash shell
CMD ["bash"]
