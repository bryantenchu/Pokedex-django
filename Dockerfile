# Usar imagen base de Python
FROM python:3.9-slim

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=pokedex.settings \
    PORT=8000

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear directorios necesarios
RUN mkdir -p staticfiles media

# Crear script de inicio
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "Starting Django Pokedex application..."\n\
\n\
# Recopilar archivos estáticos\n\
echo "Collecting static files..."\n\
python manage.py collectstatic --noinput\n\
\n\
# Aplicar migraciones\n\
echo "Applying database migrations..."\n\
python manage.py migrate --noinput\n\
\n\
# Iniciar servidor\n\
echo "Starting Django development server on 0.0.0.0:$PORT"\n\
exec python manage.py runserver 0.0.0.0:$PORT\n\
' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Exponer puerto
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Comando de inicio
ENTRYPOINT ["/app/entrypoint.sh"]