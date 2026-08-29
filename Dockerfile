FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir pytest
ENV PYTHONPATH=/app/src
CMD ["python", "-c", "from quality_agent.core import QualityResult; print(QualityResult(True, 0, 0))"]
