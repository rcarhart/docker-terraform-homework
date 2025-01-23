FROM python:3.12.8

# Install required Python dependencies
RUN pip install pandas sqlalchemy psycopg2-binary python-dotenv

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Set the default command to run the Python script
ENTRYPOINT [ "python", "ingest_data.py" ]
