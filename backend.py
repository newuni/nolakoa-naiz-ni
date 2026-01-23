#!/usr/bin/env python3
"""Backend ligero para el test de estado anímico con LLM opcional."""

import asyncio
import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:1.5b"
LLM_TIMEOUT = 30  # segundos
TRANSLATE_TIMEOUT = 10

async def translate_to_basque(text: str) -> Optional[str]:
    """Traduce texto a euskera usando Google Translate."""
    try:
        # Google Translate API informal (sin key)
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "es",  # español
            "tl": "eu",  # euskera
            "dt": "t",
            "q": text
        }
        async with httpx.AsyncClient(timeout=TRANSLATE_TIMEOUT) as client:
            r = await client.get(url, params=params)
            if r.status_code == 200:
                result = r.json()
                translated = "".join([part[0] for part in result[0] if part[0]])
                return translated
    except Exception as e:
        print(f"Translation error: {e}")
    return None

class FormData(BaseModel):
    q1: str  # 3 palabras estado
    q2: str  # clima: positive/negative
    q3: str  # emoción 24h
    q4: int  # paz mental 1-10
    q5: str  # síntomas: positive/neutral/negative
    q6: int  # fuerza física 1-5
    q7: str  # qué pide el cuerpo
    q8: str  # qué quita la calma
    q9: str  # quién roba energía
    q10: str  # qué es la felicidad

def calculate_score(data: FormData) -> dict:
    """Calcula el score numérico del estado anímico."""
    score = 0
    max_score = 40
    
    # Q2: Clima (10 puntos)
    if data.q2 == "positive":
        score += 10
    
    # Q4: Paz mental (1-10)
    score += data.q4
    
    # Q5: Síntomas físicos (10 puntos)
    if data.q5 == "positive":
        score += 10
    elif data.q5 == "neutral":
        score += 5
    
    # Q6: Fuerza física (1-5 -> 2-10)
    score += data.q6 * 2
    
    percentage = round((score / max_score) * 100)
    
    if percentage < 30:
        level = "low"
    elif percentage < 50:
        level = "medium"
    elif percentage < 75:
        level = "good"
    else:
        level = "great"
    
    return {"score": score, "max_score": max_score, "percentage": percentage, "level": level}

async def get_llm_analysis(data: FormData, score_info: dict) -> Optional[str]:
    """Obtiene análisis del LLM con timeout. Devuelve None si falla."""
    
    prompt = f"""Eres un asistente empático de bienestar emocional. Basándote en este test, da un consejo breve y cálido (2-3 frases en español).

RESULTADOS:
- Sentimiento actual: {data.q1}
- Clima emocional: {"soleado/positivo" if data.q2 == "positive" else "tormentoso/nublado"}
- Emoción dominante (24h): {data.q3}
- Paz mental (1-10): {data.q4}
- Síntomas físicos: {data.q5}
- Fuerza física (1-5): {data.q6}
- Lo que pide el cuerpo: {data.q7}
- Lo que quita la calma: {data.q8}
- Quién/qué drena energía: {data.q9}
- Qué es la felicidad: {data.q10}

PUNTUACIÓN: {score_info['percentage']}%

Da un consejo personalizado, cálido y breve:"""

    try:
        async with httpx.AsyncClient(timeout=LLM_TIMEOUT) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 150
                    }
                }
            )
            if response.status_code == 200:
                result = response.json()
                spanish_text = result.get("response", "").strip()
                if spanish_text:
                    # Traducir a euskera
                    basque_text = await translate_to_basque(spanish_text)
                    if basque_text:
                        return basque_text
                    return spanish_text  # Fallback a español si traducción falla
    except Exception as e:
        print(f"LLM error (fallback to score only): {e}")
    
    return None

@app.post("/api/analyze")
async def analyze(data: FormData):
    """Analiza el formulario: calcula score + intenta LLM."""
    
    # Calcular score numérico (siempre funciona)
    score_info = calculate_score(data)
    
    # Intentar análisis LLM (con timeout, puede fallar)
    llm_analysis = await get_llm_analysis(data, score_info)
    
    return {
        **score_info,
        "llm_analysis": llm_analysis,
        "llm_available": llm_analysis is not None
    }

@app.get("/api/health")
async def health():
    """Health check."""
    # Verificar si Ollama está disponible
    ollama_ok = False
    try:
        async with httpx.AsyncClient(timeout=2) as client:
            r = await client.get("http://localhost:11434/api/tags")
            ollama_ok = r.status_code == 200
    except:
        pass
    
    return {"status": "ok", "ollama": ollama_ok}

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
