#1 Base build
FROM python:3.13.3-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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

RUN chown -R appuser:appuser /app/staticfiles


USER appuser 

EXPOSE 8000

CMD ["./entrypoint.prod.sh"]
