# Pull the Python base image
FROM python:3.7

WORKDIR /app

# COPY allfiles to the working diretory
ADD . /app

# Install requirements
RUN \
    echo "==> Install test requirements..."   && \
    pip3 install --no-cache-dir -r requirements.txt --upgrade

#ENTRYPOINT ["./run_tests.sh"]

ENTRYPOINT ["python3"]
CMD ["app.py"]
