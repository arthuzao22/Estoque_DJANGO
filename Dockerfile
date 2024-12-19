
FROM python:3.12.6-slim

# Definir variável de ambiente para evitar o buffer de logs do Python
ENV PYTHONUNBUFFERED 1

# Atualizar apt, instalar dependências necessárias e limpar o cache para reduzir o tamanho da imagem
RUN apt-get update && apt-get install -y \
    libpq-dev gcc tk-dev libtk8.6 && \
    rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . /app/

# Expor a porta do aplicativo
EXPOSE 8000

# Comando para rodar o aplicativo com gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]