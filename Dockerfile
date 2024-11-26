# Use an official Python image as the base
FROM python:3.10.6-slim

# Set the working directory
WORKDIR /prod

# Copy and install dependencies, with cleanup to minimise image size
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the model
COPY potluck_code/food2vec_models/model.bin potluck_code/food2vec_models/

# Copy the application code
COPY raw_data raw_data
COPY potluck_code potluck_code
COPY style style
COPY app.py app.py
COPY .streamlit .streamlit
COPY setup.py setup.py
COPY assets assets


# Install the application as a package
RUN pip install .

# Expose the required port for Streamlit
EXPOSE 8080

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s \
    CMD curl -f http://localhost:8080 || exit 1

# Set the command to run the app
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
