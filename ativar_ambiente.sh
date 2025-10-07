#!/bin/bash
# Script para ativar o ambiente virtual e executar o geraArquivos.py

echo "🎯 ATIVAÇÃO DO AMBIENTE VIRTUAL E EXECUÇÃO DO GERAARQUIVOS.PY"
echo "=============================================================="

# Verificar se estamos no diretório correto
if [ ! -f "geraArquivos.py" ]; then
    echo "❌ Erro: geraArquivos.py não encontrado no diretório atual"
    echo "💡 Certifique-se de estar no diretório correto"
    exit 1
fi

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Erro: Ambiente virtual 'venv' não encontrado"
    echo "💡 Execute: python -m venv venv"
    exit 1
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se a ativação foi bem-sucedida
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "✅ Ambiente virtual ativado: $VIRTUAL_ENV"
else
    echo "❌ Falha ao ativar ambiente virtual"
    exit 1
fi

# Instalar dependências se necessário
echo "📦 Verificando dependências..."
pip install -r requirements.txt

# Executar o script principal
echo "🚀 Executando geraArquivos.py..."
python geraArquivos.py

# Desativar ambiente virtual
echo "🔚 Desativando ambiente virtual..."
deactivate

echo "✅ Procedimento concluído!"