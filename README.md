> 🎓 **Proyecto educativo** - Desarrollado como trabajo de Tecnología para 4º ESO en San Felix Ikastola. 
> El objetivo es aprender sobre desarrollo web, contenedores Docker e Inteligencia Artificial de forma práctica.

# 🌈 Nolakoa Naiz Ni?

Test de bienestar emocional en euskera con análisis de IA.

## 🔗 Demo

**https://nolakoa.duckdns.org**

---

# 📚 EXPLICACIÓN SENCILLA (para presentar el proyecto)

## ¿Qué es este proyecto?

Hemos creado una **página web** que funciona como un **test de bienestar emocional** en euskera. Es como esos tests de revistas que te dicen "¿Cómo estás hoy?", pero digital y más inteligente.

## ¿Qué hace la aplicación?

1. **Te hace 10 preguntas** sobre cómo te sientes (emociones, cuerpo, energía...)
2. **Calcula una puntuación** de tu estado anímico (de 0% a 100%)
3. **Una Inteligencia Artificial** te da un consejo personalizado basado en tus respuestas

## ¿Cómo funciona por dentro?

### 🎨 El Frontend (lo que ves)
- Es una página web hecha con **HTML, CSS y JavaScript**
- HTML = la estructura (textos, botones, formularios)
- CSS = el diseño bonito (colores, formas, animaciones)
- JavaScript = la lógica (qué pasa cuando pulsas un botón)

### 🧠 El Backend (lo que no ves)
- Es un programa en **Python** que procesa tus respuestas
- Calcula tu puntuación con una fórmula matemática
- Se comunica con una IA para generar el consejo personalizado

### 🤖 La Inteligencia Artificial
- Usamos un modelo llamado **Qwen 2.5** (1.5 billones de parámetros)
- Es como ChatGPT pero más pequeño y funciona en nuestro propio servidor
- La IA lee tus respuestas y genera un consejo único para ti
- Como la IA no habla euskera muy bien, el consejo se genera en español y **Google Translate** lo traduce al euskera

### 📦 Docker (la "caja" del proyecto)
- Docker es como una **caja mágica** que contiene todo lo necesario para que la aplicación funcione
- Dentro de la caja está: Python, el código, las librerías...
- Ventaja: puedes mover la caja a cualquier ordenador y funcionará igual

### 🔒 El certificado SSL (el candadito verde)
- Para que la web sea segura (https://) necesitamos un **certificado digital**
- Es como un DNI para la web que demuestra que es de confianza
- Lo obtenemos gratis de **Let's Encrypt** (una organización sin ánimo de lucro)
- Usamos **Caddy** (un servidor web) que se encarga de todo automáticamente

### 🌐 El dominio (la dirección web)
- Usamos **DuckDNS** para tener una dirección fácil de recordar
- En vez de escribir números (62.171.182.50), escribes: nolakoa.duckdns.org

## Diagrama simple

```
    👤 Usuario
        ↓
   [Navegador web]
        ↓
   🌐 nolakoa.duckdns.org (dominio)
        ↓
   🔒 Caddy (servidor con SSL)
        ↓
   📦 Docker (contenedor)
        ↓
   🐍 Python + FastAPI (backend)
        ↓
   🤖 Ollama + Qwen (IA local)
        ↓
   🌍 Google Translate (euskera)
```

## ¿Por qué es interesante este proyecto?

1. **Usa tecnologías reales** que se usan en empresas (Python, Docker, IA)
2. **Es útil** - ayuda a reflexionar sobre cómo nos sentimos
3. **Respeta la privacidad** - la IA funciona en nuestro servidor, no enviamos datos a terceros
4. **Es gratuito** - usamos solo herramientas de código abierto (open source)
5. **Está en euskera** - ¡apoyamos nuestra lengua!

## Tecnologías utilizadas

| Tecnología | Para qué sirve |
|------------|----------------|
| HTML/CSS/JS | Página web (frontend) |
| Python | Lenguaje de programación (backend) |
| FastAPI | Framework para crear APIs web |
| Docker | Contenedores (empaquetar aplicaciones) |
| Ollama | Ejecutar modelos de IA localmente |
| Qwen 2.5 | Modelo de Inteligencia Artificial |
| Caddy | Servidor web con SSL automático |
| Let's Encrypt | Certificados SSL gratuitos |
| DuckDNS | Dominio gratuito |
| Google Translate | Traducción automática |

---

# 🛠️ DOCUMENTACIÓN TÉCNICA

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


## Responsible Use

Use this project only for lawful, authorized purposes.


## Third-Party Services & Trademarks

Third-party names and trademarks belong to their respective owners; no affiliation is implied.
