#!/bin/bash
# Tests unitarios para el API de estado anímico

BASE_URL="http://localhost:8096"
PASSED=0
FAILED=0

echo "============================================================"
echo "🧪 TESTS UNITARIOS - Nolakoa Naiz Ni API"
echo "============================================================"
echo

# Test Health
echo "🔍 Test: Health endpoint..."
HEALTH=$(curl -s "$BASE_URL/api/health")
if echo "$HEALTH" | grep -q '"status":"ok"'; then
    OLLAMA=$(echo "$HEALTH" | grep -o '"ollama":[^,}]*' | cut -d: -f2)
    echo "   ✅ Health OK - Ollama: $OLLAMA"
    ((PASSED++))
else
    echo "   ❌ FAILED: $HEALTH"
    ((FAILED++))
    echo "❌ API no disponible. Abortando."
    exit 1
fi

echo

# Función para testear análisis
test_case() {
    local name="$1"
    local data="$2"
    local expected_level="$3"
    
    echo "🔍 Test: $name..."
    
    RESULT=$(curl -s -X POST "$BASE_URL/api/analyze" \
        -H "Content-Type: application/json" \
        -d "$data" \
        --max-time 45)
    
    if [ -z "$RESULT" ]; then
        echo "   ❌ FAILED: Sin respuesta"
        ((FAILED++))
        return
    fi
    
    LEVEL=$(echo "$RESULT" | grep -o '"level":"[^"]*"' | cut -d'"' -f4)
    PCT=$(echo "$RESULT" | grep -o '"percentage":[0-9]*' | cut -d: -f2)
    LLM=$(echo "$RESULT" | grep -o '"llm_available":[^,}]*' | cut -d: -f2)
    
    if [ "$LEVEL" = "$expected_level" ]; then
        echo -n "   ✅ PASS - Score: ${PCT}% (${LEVEL})"
        if [ "$LLM" = "true" ]; then
            LLM_TEXT=$(echo "$RESULT" | grep -o '"llm_analysis":"[^"]*' | cut -d'"' -f4 | head -c 50)
            echo " 🤖 ${LLM_TEXT}..."
        else
            echo " (sin LLM)"
        fi
        ((PASSED++))
    else
        echo "   ❌ FAILED: Level=$LEVEL (esperado: $expected_level)"
        ((FAILED++))
    fi
}

# CASO 1: Óptimo - Todo positivo
test_case "Caso ÓPTIMO - Todo positivo" \
    '{"q1":"feliz, tranquilo, motivado","q2":"positive","q3":"alegría","q4":10,"q5":"positive","q6":5,"q7":"nada","q8":"nada","q9":"nadie","q10":"familia"}' \
    "great"

# CASO 2: Bajo - Todo negativo
test_case "Caso BAJO - Todo negativo" \
    '{"q1":"cansado, triste, agotado","q2":"negative","q3":"tristeza","q4":1,"q5":"negative","q6":1,"q7":"descansar","q8":"todo","q9":"trabajo","q10":"no sé"}' \
    "low"

# CASO 3: Medio - Mixto
test_case "Caso MEDIO - Mixto" \
    '{"q1":"normal, cansado, bien","q2":"positive","q3":"calma","q4":5,"q5":"neutral","q6":3,"q7":"paseo","q8":"preocupaciones","q9":"nada","q10":"paz"}' \
    "good"

# CASO 4: Bueno - Mayoría positivo  
test_case "Caso BUENO - Mayoría positivo" \
    '{"q1":"animado, activo, contento","q2":"positive","q3":"motivación","q4":8,"q5":"positive","q6":4,"q7":"seguir","q8":"poca cosa","q9":"nadie","q10":"metas"}' \
    "great"

# CASO 5: Medio-bajo
test_case "Caso MEDIO-BAJO - Tendencia negativa" \
    '{"q1":"estresado, nervioso, preocupado","q2":"negative","q3":"ansiedad","q4":3,"q5":"negative","q6":2,"q7":"respirar","q8":"futuro","q9":"noticias","q10":"tranquilidad"}' \
    "low"

echo
echo "============================================================"
echo "📊 RESULTADOS: $PASSED passed, $FAILED failed"
echo "============================================================"

if [ $FAILED -eq 0 ]; then
    echo "✅ Todos los tests pasaron!"
    exit 0
else
    exit 1
fi
