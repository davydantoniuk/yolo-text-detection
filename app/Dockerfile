# Use the official Python image with version 3.10
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir streamlit torch torchvision torchaudio numpy opencv-python pillow ultralytics

# Expose the default Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
