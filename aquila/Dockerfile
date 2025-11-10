FROM python:3.10-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates openssl \
 && rm -rf /var/lib/apt/lists/*
 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=on

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir .

RUN python -m pip install poetry==2.1.4

RUN python -m poetry install

ENTRYPOINT ["poetry", "run", "streamlit", "run", "aquila/dashboard/Welcome.py", "--server.port=8501", "--server.address=0.0.0.0"] 