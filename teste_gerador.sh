#!/bin/bash

# Script de teste para o gerador infinito
# Executa apenas 3 iterações para validar o funcionamento

echo "🧪 Testando Gerador Infinito (3 iterações)"
echo "=========================================="

# Ativar ambiente virtual
source venv/bin/activate

# Criar pasta de teste
mkdir -p storage_teste

# Executar 3 iterações
for i in {1..3}; do
    echo "🔄 Iteração $i/3"
    python -c "from geraArquivos import gerar; gerar(5, 'equilibrado', 'storage_teste')"
    
    # Mostrar estatísticas
    arquivos=$(find storage_teste -type f | wc -l)
    tamanho=$(du -sm storage_teste | cut -f1)
    echo "📊 Arquivos: $arquivos | Tamanho: ${tamanho}MB"
    echo "---"
done

echo "✅ Teste concluído!"
echo "📁 Arquivos gerados em: storage_teste/"
echo "📊 Total de arquivos: $(find storage_teste -type f | wc -l)"
echo "📊 Tamanho total: $(du -sm storage_teste | cut -f1)MB"
