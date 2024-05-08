# Use a base Python 3.9 image
FROM python:3.9

#Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt /app/

# Install dependecies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python script to the working directory
COPY producer.py /app/

# Run the Python script when conatiner starts
CMD ["python", "producer.py"]