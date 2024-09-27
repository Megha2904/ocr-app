# Start with the base image
FROM python:3.9-slim

# Install Tesseract-OCR and Hindi language support
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-hin \
    libtesseract-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Streamlit configuration to avoid gathering stats prompt
RUN mkdir -p ~/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
\n\
[global]\n\
browser.gatherUsageStats = false\n\
" > ~/.streamlit/config.toml

# Expose the port that the Streamlit app runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
