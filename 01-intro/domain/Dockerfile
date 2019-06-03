FROM python:slim
EXPOSE 5000
ENV DOMAIN_API_VERSION=v1
RUN apt-get update && apt-get install -y \
    curl \
 && rm -rf /var/lib/apt/lists/*
RUN pip install Flask
COPY domain.py .
CMD python domain.py
