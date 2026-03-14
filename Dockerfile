FROM python:3.11

WORKDIR /app

COPY . .

# install required system tools
RUN apt-get update && apt-get install -y curl ca-certificates zstd

# install python dependencies
RUN pip install flask pypdf ollama werkzeug

# install ollama using official repo
RUN curl -fsSL https://ollama.com/install.sh | sh

# expose flask port
EXPOSE 5000

CMD ["bash", "-c", "ollama serve & flask --app app.py run --host=0.0.0.0 --port=5000"]