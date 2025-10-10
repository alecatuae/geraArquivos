#!/bin/bash

# Configurações
QUANTIDADE=100
CICLOS=10
BUFFER="buffer_temp"
DESTINO="tars_gerados"

echo "📦 Gerador Recorrente de TARs (SEM compressão)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Arquivos por tar: $QUANTIDADE"
echo "Ciclos: $CICLOS"
echo "Formato: .tar (sem compressão)"
echo "Destino: $DESTINO/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

source venv/bin/activate

for i in $(seq 1 $CICLOS); do
    echo "📦 Ciclo $i/$CICLOS"
    python -c "
from geraArquivos import gerar_buffer_e_empacotar
gerar_buffer_e_empacotar(
    quantidade=$QUANTIDADE,
    buffer='$BUFFER',
    destino='$DESTINO'
)
"
    echo ""
done

echo "✅ $CICLOS arquivos .tar criados em $DESTINO/"

