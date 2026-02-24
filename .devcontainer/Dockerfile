FROM mcr.microsoft.com/devcontainers/python:3.10

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    libgl1 \
    libglx-mesa0 \
    libegl1 \
    libxrender1 \
    libxext6 \
    graphviz \
    tree \
    git-lfs \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates

RUN /usr/local/bin/python -m pip install --no-cache-dir --upgrade pip certifi

COPY requirements.txt* /tmp/pip-tmp/
RUN if [ -f /tmp/pip-tmp/requirements.txt ]; then \
    /usr/local/bin/python -m pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt; \
    fi \
    && rm -rf /tmp/pip-tmp

RUN echo "--- [BUILD CHECK] Python Version ---" && /usr/local/bin/python --version \
    && echo "--- [BUILD CHECK] Pip List ---" && /usr/local/bin/python -m pip list

USER vscode

RUN echo "alias py='/usr/local/bin/python'" >> /home/vscode/.bashrc