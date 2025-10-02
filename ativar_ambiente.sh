#!/bin/bash
# Script para ativar o ambiente virtual do projeto geraArquivos

echo "🚀 Ativando ambiente virtual Python..."
source venv/bin/activate

echo "✅ Ambiente virtual ativado!"
echo "📦 Dependências instaladas:"
pip list | grep -E "(Pillow|reportlab|python-docx|pandas|openpyxl)"

echo ""
echo "💡 Para executar o script:"
echo "   python geraArquivos.py"
echo ""
echo "💡 Para desativar o ambiente:"
echo "   deactivate"

