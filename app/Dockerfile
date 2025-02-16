FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV and libgomp
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY requirements.txt .
COPY YOLOv8m.pt .
COPY app.py .

# Install Python dependencies with upgraded pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
