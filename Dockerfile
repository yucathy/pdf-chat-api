# Dockerfile
FROM python:3.10-slim

# install system dependency
RUN apt-get update && apt-get install -y \
    build-essential \
    libmupdf-dev \
    libfreetype6-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# set up work dir
WORKDIR /app

# copy dependent file
COPY requirements.txt .

# install dependent lib
RUN pip install --no-cache-dir -r requirements.txt

# copy current work folder
COPY ./app ./app
COPY ./test ./test

# set up active command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
