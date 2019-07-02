FROM python:slim
EXPOSE 5000
ENV DOMAIN_API_URL=http://domain:5000
RUN apt-get update && apt-get install -y \
    curl \
 && rm -rf /var/lib/apt/lists/*
RUN pip install Flask requests
COPY front.py .
CMD python front.py
