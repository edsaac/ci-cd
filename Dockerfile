# Build the HTML from docs
FROM python:3.10 as docs
ENV SPHINXOPTS="-W --keep-going"

COPY . /app
WORKDIR /app
RUN python -m pip install -e .[docs]

WORKDIR /app/docs
RUN make html

## Nginx to serve HTML
FROM nginx:1.22-alpine as server
COPY --from=docs /app/docs/_build/html /usr/share/nginx/html

