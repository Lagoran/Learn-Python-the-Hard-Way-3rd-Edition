FROM ghcr.io/astral-sh/uv:latest as builder

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY app/ ./app/

# Install dependencies with locked versions
RUN uv sync --locked --no-dev

# Production image
FROM python:3.12-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY --from=builder /app/app ./app

# Set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Add user context to run as non-root
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# Expose port 5000
EXPOSE 5000

# Run the application
# Improve security headers and worker configuration
CMD ["uvicorn", "app.main:app", \
     "--host", "0.0.0.0", \
     "--port", "5000", \
     "--workers", "1"]