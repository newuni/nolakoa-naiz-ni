# 🌈 Nolakoa Naiz Ni?

Test de bienestar emocional en euskera con análisis de IA.

## 🔗 Demo

**https://nolakoa.duckdns.org**

## 📋 Descripción

Aplicación web que evalúa el estado anímico del usuario mediante un cuestionario de 10 preguntas. Incluye:

- ✅ Cálculo de puntuación numérica (0-100%)
- ✅ Análisis personalizado con IA (Qwen 2.5)
- ✅ Traducción automática a euskera (Google Translate)
- ✅ Interfaz responsive y moderna
- ✅ SSL automático con Caddy + Let's Encrypt

## 🛠️ Tecnologías

- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Backend**: Python 3.11, FastAPI, httpx
- **IA**: Ollama + Qwen 2.5 1.5B
- **Traducción**: Google Translate API (free)
- **Contenedor**: Docker
- **SSL/Proxy**: Caddy
- **DNS**: DuckDNS

## 🚀 Instalación

### Requisitos
- Docker y Docker Compose
- 4GB RAM mínimo (para el modelo de IA)
- Dominio configurado (DuckDNS o similar)

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/TU_USUARIO/nolakoa-naiz-ni.git
cd nolakoa-naiz-ni
```

2. Configurar el dominio en `Caddyfile`:
```
tu-dominio.duckdns.org {
    reverse_proxy 127.0.0.1:8096
}
```

3. Iniciar los servicios:
```bash
docker-compose up -d
```

4. Descargar el modelo de IA:
```bash
docker exec ollama ollama pull qwen2.5:1.5b
```

5. Acceder a https://tu-dominio.duckdns.org

## 📁 Estructura del proyecto

```
nolakoa-naiz-ni/
├── backend.py          # API FastAPI con lógica de cálculo e IA
├── static/
│   └── index.html      # Frontend completo (HTML+CSS+JS)
├── Dockerfile          # Imagen Docker del backend
├── docker-compose.yml  # Orquestación de servicios
├── Caddyfile           # Configuración del proxy SSL
├── test_api.sh         # Tests unitarios
└── EXPLICACION_PROYECTO.md  # Explicación para presentación
```

## 🧪 Tests

```bash
./test_api.sh
```

## 📊 API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Página principal |
| `/api/analyze` | POST | Analizar respuestas del test |
| `/api/health` | GET | Estado del servicio |

### Ejemplo de petición

```bash
curl -X POST https://nolakoa.duckdns.org/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "q1": "nekatuta",
    "q2": "negative",
    "q3": "estresa",
    "q4": 5,
    "q5": "negative",
    "q6": 3,
    "q7": "lo egin",
    "q8": "lana",
    "q9": "inor ez",
    "q10": "familia"
  }'
```

## 🔒 SSL

El certificado SSL se obtiene automáticamente mediante Caddy + Let's Encrypt usando el challenge TLS-ALPN-01.

## 📝 Licencia

MIT

## 👥 Créditos

Creado por Alba y Leizuri para San Felix Ikastola.  
Desarrollo técnico asistido por Nimbus 🐙
