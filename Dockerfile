#1 Base build
FROM python:3.13.3-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gettext \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN pip install --upgrade pip
COPY backend/requirements.txt .
RUN uv pip install -r requirements.txt --system


COPY backend/ .

RUN useradd -m -r appuser 
RUN chown -R appuser /app

#COPY --chown=appuser:appuser . .

RUN chmod +x entrypoint.prod.sh
RUN chmod 755 entrypoint.prod.sh

RUN mkdir -p /app/staticfiles \
    && chmod -R 755 /app/staticfiles

RUN mkdir -p /app/media 
RUN chmod -R 775 /app/media

RUN mkdir -p /app/locale
RUN chmod -R 775 /app/locale

RUN chown -R appuser:appuser /app/staticfiles
RUN chown -R appuser:appuser /app/media
RUN chown -R appuser:appuser /app/locale


USER appuser 

EXPOSE 8000

CMD ["./entrypoint.prod.sh"]
