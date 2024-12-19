# Usar a imagem oficial do Python do Docker Hub
FROM python:3.12.6-slim

# Definir variável de ambiente para evitar o buffer de logs do Python
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências para dentro do contêiner
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto para dentro do contêiner
COPY . /app/

# Expor a porta que o aplicativo vai rodar
EXPOSE 8000

# Definir o comando para rodar o aplicativo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
