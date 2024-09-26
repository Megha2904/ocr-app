# Start with the base image
FROM python:3.9-slim

# Install Tesseract-OCR dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Streamlit app runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
