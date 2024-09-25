# Use a Python base image
FROM python:3.9-slim

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr


# Install Python dependencies from the requirements file
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy your app code
COPY . /app
WORKDIR /app

# Expose the app port (if needed)
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py"]
