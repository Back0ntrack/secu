FROM ubuntu:latest
# INSECURE: using latest tag, which can introduce unpredictable breaking changes or vulnerabilities.

RUN apt-get update && apt-get install -y python3 python3-pip
# INSECURE: apt-get without cleaning up caches inflates the image size.
# INSECURE: running as root user (no USER directive specified).

COPY . /app
WORKDIR /app

CMD ["python3", "main.py"]
