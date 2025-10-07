# 🔄 Gerador Infinito de Arquivos - Teste de Storage

## 🎯 Propósito

Script para executar geração de arquivos em loop infinito, ideal para:
- **Popular storage** com dados de teste
- **Validar taxa de eficiência** de sistemas de armazenamento
- **Testar deduplicação** e compressão
- **Simular carga de trabalho** contínua
- **Benchmark de performance** de storage

## 📁 Arquivos

| Arquivo | Propósito |
|---------|-----------|
| `gerador_infinito.sh` | Script principal (loop infinito) |
| `teste_gerador.sh` | Script de teste (3 iterações) |
| `GERADOR_INFINITO.md` | Esta documentação |

## 🚀 Como Usar

### 1. Teste Inicial (Recomendado)
```bash
# Testar com 3 iterações primeiro
./teste_gerador.sh
```

### 2. Execução Infinita
```bash
# Executar em loop infinito
./gerador_infinito.sh
```

### 3. Executar em Background
```bash
# Executar em background (não bloqueia terminal)
nohup ./gerador_infinito.sh > gerador.log 2>&1 &

# Verificar se está rodando
ps aux | grep gerador_infinito

# Parar o processo
pkill -f gerador_infinito
```

## ⚙️ Configurações

### Parâmetros Editáveis no Script

```bash
# Configurações principais
PASTA_DESTINO="storage_teste"        # Pasta onde salvar arquivos
QUANTIDADE_ARQUIVOS=100              # Arquivos por iteração
TEMPLATE="equilibrado"               # Template de distribuição
```

### Templates Disponíveis
- `equilibrado` - Distribuição balanceada (padrão)
- `foco_imagens` - 60% imagens (JPEG/PNG)
- `foco_documentos` - 70% documentos (PDF/DOCX)
- `foco_dados` - 50% planilhas (XLSX)
- `minimal` - Apenas TXT e PDF

## 📊 Monitoramento

### Arquivos de Log
- `gerador_infinito.log` - Log detalhado de execução
- `estatisticas.txt` - CSV com estatísticas por iteração

### Estatísticas em Tempo Real
O script exibe estatísticas a cada 5 iterações:
```
╔══════════════════════════════════════════════════════════════╗
║                    ESTATÍSTICAS DO GERADOR                    ║
╠══════════════════════════════════════════════════════════════╣
║ Iteração: 25
║ Tempo de execução: 2h 15m 30s
║ Total de arquivos: 2500
║ Tamanho total: 1250 MB
║ Pasta: storage_teste
║ Template: equilibrado
║ Arquivos por iteração: 100
║ Média por iteração: 100 arquivos, 50 MB
╚══════════════════════════════════════════════════════════════╝
```

## 🛠️ Funcionalidades Avançadas

### 1. Verificação de Espaço
- Monitora espaço em disco automaticamente
- Alerta quando menos de 1GB disponível

### 2. Limpeza Automática
- Remove arquivos antigos a cada 10 iterações
- Mantém apenas os últimos 1000 arquivos
- Configurável no script

### 3. Recuperação de Erros
- Continua execução mesmo com erros
- Pausa de 5 segundos em caso de falha
- Log detalhado de erros

### 4. Interrupção Segura
- `Ctrl+C` para parar graciosamente
- Salva estatísticas finais
- Exibe resumo ao final

## 📈 Análise de Dados

### Arquivo de Estatísticas (CSV)
```csv
timestamp,iteracao,arquivos,tamanho_mb
2024-01-15 10:30:00,1,100,50
2024-01-15 10:32:00,2,200,100
2024-01-15 10:34:00,3,300,150
```

### Comandos Úteis para Análise
```bash
# Ver estatísticas em tempo real
tail -f estatisticas.txt

# Contar arquivos por tipo
find storage_teste -name "*.pdf" | wc -l
find storage_teste -name "*.jpeg" | wc -l
find storage_teste -name "*.png" | wc -l

# Tamanho por tipo
du -sh storage_teste/*.pdf
du -sh storage_teste/*.jpeg

# Taxa de crescimento
awk -F',' '{print $3}' estatisticas.txt | tail -10
```

## 🚨 Solução de Problemas

### Problema: "Permission denied"
```bash
# Dar permissão de execução
chmod +x gerador_infinito.sh
```

### Problema: "Ambiente virtual não encontrado"
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: "Espaço em disco insuficiente"
```bash
# Verificar espaço
df -h

# Limpar arquivos antigos
rm -rf storage_teste/*
```

### Problema: "Processo não para"
```bash
# Encontrar processo
ps aux | grep gerador_infinito

# Matar processo
pkill -f gerador_infinito
```

## 📋 Casos de Uso

### 1. Teste de Deduplicação
```bash
# Configurar para gerar muitos arquivos similares
QUANTIDADE_ARQUIVOS=1000
TEMPLATE="minimal"  # Apenas TXT e PDF
```

### 2. Teste de Compressão
```bash
# Gerar arquivos grandes
QUANTIDADE_ARQUIVOS=50
# Editar config.json para aumentar tamanhos
```

### 3. Teste de Performance
```bash
# Gerar muitos arquivos pequenos
QUANTIDADE_ARQUIVOS=500
TEMPLATE="minimal"
```

### 4. Simulação de Carga
```bash
# Executar em background
nohup ./gerador_infinito.sh > gerador.log 2>&1 &
```

## 🔧 Personalização

### Modificar Configurações
Edite as variáveis no início do script:
```bash
PASTA_DESTINO="meu_storage"
QUANTIDADE_ARQUIVOS=200
TEMPLATE="foco_imagens"
```

### Adicionar Novos Templates
Edite o `config.json` para adicionar novos templates de distribuição.

### Modificar Limpeza Automática
Altere a função `limpar_arquivos_antigos()` para ajustar:
- Frequência de limpeza
- Quantidade de arquivos mantidos
- Critérios de seleção

## 📊 Exemplo de Uso Completo

```bash
# 1. Testar primeiro
./teste_gerador.sh

# 2. Configurar para teste de storage
# Editar gerador_infinito.sh:
# PASTA_DESTINO="storage_teste"
# QUANTIDADE_ARQUIVOS=100
# TEMPLATE="equilibrado"

# 3. Executar em background
nohup ./gerador_infinito.sh > gerador.log 2>&1 &

# 4. Monitorar
tail -f gerador.log
tail -f estatisticas.txt

# 5. Parar quando necessário
pkill -f gerador_infinito
```

## 🎯 Resultados Esperados

### Para Teste de Deduplicação
- Arquivos com conteúdo similar
- Taxa de deduplicação mensurável
- Economia de espaço visível

### Para Teste de Compressão
- Diferentes tipos de arquivo
- Taxa de compressão variável
- Performance de compressão

### Para Teste de Performance
- Taxa de escrita constante
- Latência mensurável
- Throughput do storage

---

**🔄 Pronto para testar seu storage com carga contínua!**
