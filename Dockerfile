# Use the official uv image for the binary
FROM ghcr.io/astral-sh/uv:latest AS uv_bin

# Use the official Python 3.13 slim image
FROM python:3.13-slim

# Declare build-time arguments
ARG GIT_BRANCH
ARG GIT_COMMIT

# Set them as environment variables so the app can see them
ENV APP_GIT_BRANCH=$GIT_BRANCH
ENV APP_GIT_COMMIT=$GIT_COMMIT

# Copy uv binaries
COPY --from=uv_bin /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation for faster startup in Python 3.13
ENV UV_COMPILE_BYTECODE=1

# Copy lockfiles
COPY pyproject.toml uv.lock ./

# Install dependencies 
# We use --system because we are inside a dedicated container
RUN uv pip install --system --no-cache -r pyproject.toml

# Copy the rest of your router app
COPY . .

EXPOSE 8501

# Entrypoint remains the same
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]