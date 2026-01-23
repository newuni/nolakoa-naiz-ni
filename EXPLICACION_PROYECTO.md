# 🌈 NOLAKOA NAIZ NI? - Explicación del Proyecto

## ¿Qué es este proyecto?

Hemos creado una **página web** que funciona como un **test de bienestar emocional** en euskera. Es como esos tests de revistas que te dicen "¿Cómo estás hoy?", pero digital y más inteligente.

---

## ¿Qué hace la aplicación?

1. **Te hace 10 preguntas** sobre cómo te sientes (emociones, cuerpo, energía...)
2. **Calcula una puntuación** de tu estado anímico (de 0% a 100%)
3. **Una Inteligencia Artificial** te da un consejo personalizado basado en tus respuestas

---

## ¿Cómo funciona por dentro? (La tecnología)

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
- Como la IA no habla euskera muy bien, el consejo se genera en español y luego **Google Translate** lo traduce al euskera

### 📦 Docker (la "caja" del proyecto)
- Docker es como una **caja mágica** que contiene todo lo necesario para que la aplicación funcione
- Dentro de la caja está: Python, el código, las librerías...
- Ventaja: puedes mover la caja a cualquier ordenador y funcionará igual

### 🔒 El certificado SSL (el candadito)
- Para que la web sea segura (https://) necesitamos un **certificado digital**
- Es como un DNI para la web que demuestra que es de confianza
- Lo obtenemos gratis de **Let's Encrypt** (una organización sin ánimo de lucro)
- Usamos **Caddy** (un servidor web) que se encarga de todo esto automáticamente

### 🌐 El dominio (la dirección web)
- Usamos **DuckDNS** para tener una dirección fácil de recordar
- En vez de escribir números (62.171.182.50), escribes: nolakoa.duckdns.org

---

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

---

## ¿Por qué es interesante este proyecto?

1. **Usa tecnologías reales** que se usan en empresas (Python, Docker, IA)
2. **Es útil** - ayuda a reflexionar sobre cómo nos sentimos
3. **Respeta la privacidad** - la IA funciona en nuestro servidor, no enviamos datos a terceros
4. **Es gratuito** - usamos solo herramientas de código abierto (open source)
5. **Está en euskera** - ¡apoyamos nuestra lengua!

---

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

## URL del proyecto

🔗 **https://nolakoa.duckdns.org**

---

*Proyecto creado por Alba y Leizuri, con ayuda tecnológica de Nimbus 🐙*
