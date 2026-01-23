#!/usr/bin/env python3
"""Tests unitarios para el API de estado anímico."""

import httpx
import sys

BASE_URL = "http://localhost:8096"
TIMEOUT = 45  # segundos (LLM puede tardar)

# Casos de prueba: (nombre, datos, score_esperado, level_esperado)
TEST_CASES = [
    (
        "Caso ÓPTIMO - Todo positivo",
        {
            "q1": "feliz, tranquilo, motivado",
            "q2": "positive",  # +10
            "q3": "alegría",
            "q4": 10,          # +10
            "q5": "positive",  # +10 (arnasa lasaiak)
            "q6": 5,           # +10
            "q7": "nada, estoy bien",
            "q8": "nada",
            "q9": "nadie",
            "q10": "estar con mi familia"
        },
        100,  # percentage esperado
        "great"
    ),
    (
        "Caso BAJO - Todo negativo",
        {
            "q1": "cansado, triste, agotado",
            "q2": "negative",  # +0
            "q3": "tristeza",
            "q4": 1,           # +1
            "q5": "negative",  # +0
            "q6": 1,           # +2
            "q7": "descansar mucho",
            "q8": "todo",
            "q9": "el trabajo",
            "q10": "no lo sé"
        },
        8,    # (0+1+0+2)/40 = 7.5% -> 8%
        "low"
    ),
    (
        "Caso MEDIO - Mixto",
        {
            "q1": "normal, algo cansado, bien",
            "q2": "positive",  # +10
            "q3": "calma",
            "q4": 5,           # +5
            "q5": "neutral",   # +5
            "q6": 3,           # +6
            "q7": "un paseo",
            "q8": "algunas preocupaciones",
            "q9": "nada especial",
            "q10": "momentos de paz"
        },
        65,   # (10+5+5+6)/40 = 65%
        "good"
    ),
    (
        "Caso BUENO - Mayoría positivo",
        {
            "q1": "animado, activo, contento",
            "q2": "positive",  # +10
            "q3": "motivación",
            "q4": 8,           # +8
            "q5": "positive",  # +10
            "q6": 4,           # +8
            "q7": "seguir así",
            "q8": "poca cosa",
            "q9": "nadie",
            "q10": "lograr mis metas"
        },
        90,   # (10+8+10+8)/40 = 90%
        "great"
    ),
    (
        "Caso MEDIO-BAJO - Tendencia negativa",
        {
            "q1": "estresado, preocupado, nervioso",
            "q2": "negative",  # +0
            "q3": "ansiedad",
            "q4": 3,           # +3
            "q5": "negative",  # +0
            "q6": 2,           # +4
            "q7": "respirar",
            "q8": "el futuro",
            "q9": "las noticias",
            "q10": "tranquilidad"
        },
        18,   # (0+3+0+4)/40 = 17.5% -> 18%
        "low"
    ),
]


def test_health():
    """Test del endpoint de health."""
    print("🔍 Test: Health endpoint...")
    try:
        r = httpx.get(f"{BASE_URL}/api/health", timeout=5)
        data = r.json()
        assert r.status_code == 200, f"Status code: {r.status_code}"
        assert data["status"] == "ok", f"Status: {data['status']}"
        ollama_status = "✅" if data["ollama"] else "⚠️ (no disponible)"
        print(f"   ✅ Health OK - Ollama: {ollama_status}")
        return True, data["ollama"]
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        return False, False


def test_analyze(name: str, data: dict, expected_pct: int, expected_level: str, check_llm: bool):
    """Test de un caso de análisis."""
    print(f"🔍 Test: {name}...")
    try:
        r = httpx.post(f"{BASE_URL}/api/analyze", json=data, timeout=TIMEOUT)
        result = r.json()
        
        assert r.status_code == 200, f"Status code: {r.status_code}"
        
        # Verificar score (con margen de ±2% por redondeo)
        pct = result["percentage"]
        assert abs(pct - expected_pct) <= 2, f"Percentage: {pct}% (esperado: {expected_pct}%)"
        
        # Verificar level
        level = result["level"]
        assert level == expected_level, f"Level: {level} (esperado: {expected_level})"
        
        # Info del LLM
        llm_info = ""
        if check_llm:
            if result.get("llm_available") and result.get("llm_analysis"):
                llm_preview = result["llm_analysis"][:60] + "..." if len(result["llm_analysis"]) > 60 else result["llm_analysis"]
                llm_info = f"\n      🤖 LLM: {llm_preview}"
            else:
                llm_info = "\n      ⚠️ LLM: No disponible (fallback OK)"
        
        print(f"   ✅ PASS - Score: {pct}% ({level}){llm_info}")
        return True
        
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
        return False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False


def main():
    print("=" * 60)
    print("🧪 TESTS UNITARIOS - Nolakoa Naiz Ni API")
    print("=" * 60)
    print()
    
    passed = 0
    failed = 0
    
    # Test health
    health_ok, ollama_available = test_health()
    if health_ok:
        passed += 1
    else:
        failed += 1
        print("\n❌ API no disponible. Abortando tests.")
        sys.exit(1)
    
    print()
    
    # Tests de análisis
    for name, data, expected_pct, expected_level in TEST_CASES:
        if test_analyze(name, data, expected_pct, expected_level, ollama_available):
            passed += 1
        else:
            failed += 1
    
    print()
    print("=" * 60)
    print(f"📊 RESULTADOS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed > 0:
        sys.exit(1)
    else:
        print("✅ Todos los tests pasaron!")
        sys.exit(0)


if __name__ == "__main__":
    main()
