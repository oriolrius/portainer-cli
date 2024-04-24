FROM python:3.11-slim

WORKDIR /portainer

COPY . .

RUN pip install --no-cache-dir flit

ENV FLIT_ROOT_INSTALL=1
RUN flit install --deps develop --symlink

ENTRYPOINT ["portainer"]
