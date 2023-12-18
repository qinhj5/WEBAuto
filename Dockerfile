# Use the base image
FROM markadams/chromium-xvfb-py3

# Set the timezone
ENV TZ "Asia/Shanghai"

# Set the encoding
ENV LANG C.UTF-8

# Set the environment variable
ENV PATH=$PATH:/code

# Set the working directory
WORKDIR /code

# Copy the local project files to the /code directory in the container
COPY . /code

# Install venv and requirements
RUN python3 -m venv venv

# Activate the virtual environment
ENV PATH=/code/venv/bin:$PATH

# Upgrade pip
RUN pip3 install --upgrade pip

# Install the dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Run the test command
CMD ["python3", "/code/main.py"]