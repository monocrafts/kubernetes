FROM registry.access.redhat.com/ubi9/ubi-minimal:latest

RUN microdnf install -y \
        python3 \
    && microdnf clean all

COPY patch.py /patch.py

ENTRYPOINT ["python3", "/patch.py"]
