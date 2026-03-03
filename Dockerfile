FROM python:3.10-slim

# Sistem bağımlılıkları kalsın, bunlar derleme için şart
RUN apt-get update && apt-get install -y \
    gcc g++ make cmake git libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Timeout'u engellemek için sadece temel özellikleri kuruyoruz
# AVX ve BLAS gibi ağır CPU optimizasyonlarını varsayılan bırakarak kurulumu hızlandırıyoruz
RUN pip install --no-cache-dir llama-cpp-python==0.3.2

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV GRADIO_SERVER_NAME="0.0.0.0"

EXPOSE 7860
CMD ["python", "app.py"]