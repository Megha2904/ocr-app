FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . /app
WORKDIR /app

# Command to run the app
CMD ["streamlit", "run", "app.py"]
