# Use a base Python image
FROM python:3.9-slim

# Install system dependencies for Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Copy the requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app
WORKDIR /app

# Expose the app port (if needed)
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py"]
