# Set the base image to use for subsequent instructions
FROM python:3-slim AS builder
ADD . /app
WORKDIR /app


# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app -r requirements.txt

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app

# # Set the working directory inside the container
# WORKDIR /usr/src

# # Copy any source file(s) required for the action
COPY entrypoint.sh .

# # Configure the container to be run as an executable
ENTRYPOINT ["/app/entrypoint.sh"]
