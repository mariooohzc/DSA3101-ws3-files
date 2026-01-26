FROM ubuntu:22.04

# Set environment variable for your script
ENV DATETIME_STR=2025-08-03T19:00:00

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set working directory in the container
WORKDIR /app

# Copy your script into the image
COPY uv_index_request.py .

# Install requests globally
RUN pip3 install requests

# Default command (so you can override or use interactively)
#CMD ["bash"]

# Make run automatically
CMD ["python3", "uv_index_request.py"]