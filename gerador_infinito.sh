#!/bin/bash

# =============================================================================
# Gerador Infinito de Arquivos - Teste de Storage
# =============================================================================
# 
# Propósito: Executar geração de arquivos em loop infinito para:
# - Popular storage com dados de teste
# - Validar taxa de eficiência
# - Testar deduplicação e compressão
# - Simular carga de trabalho contínua
#
# Uso: ./gerador_infinito.sh
# =============================================================================

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configurações
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/venv"
LOG_FILE="$SCRIPT_DIR/gerador_infinito.log"
STATS_FILE="$SCRIPT_DIR/estatisticas.txt"
PASTA_DESTINO="storage_teste"
QUANTIDADE_ARQUIVOS=100
TEMPLATE="equilibrado"

# Contadores
ITERACAO=0
TOTAL_ARQUIVOS=0
TOTAL_MB=0
INICIO_EXECUCAO=$(date +%s)

# Função para log com timestamp
log() {
    local mensagem="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $mensagem" | tee -a "$LOG_FILE"
}

# Função para calcular estatísticas
calcular_estatisticas() {
    local pasta="$1"
    local arquivos=$(find "$pasta" -type f 2>/dev/null | wc -l)
    local tamanho_mb=$(du -sm "$pasta" 2>/dev/null | cut -f1)
    echo "$arquivos,$tamanho_mb"
}

# Função para exibir estatísticas
exibir_estatisticas() {
    local tempo_atual=$(date +%s)
    local tempo_decorrido=$((tempo_atual - INICIO_EXECUCAO))
    local horas=$((tempo_decorrido / 3600))
    local minutos=$(((tempo_decorrido % 3600) / 60))
    local segundos=$((tempo_decorrido % 60))
    
    local stats=$(calcular_estatisticas "$PASTA_DESTINO")
    local arquivos=$(echo "$stats" | cut -d',' -f1)
    local tamanho_mb=$(echo "$stats" | cut -d',' -f2)
    
    echo -e "\n${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                    ESTATÍSTICAS DO GERADOR                    ║${NC}"
    echo -e "${CYAN}╠══════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${CYAN}║${NC} Iteração: ${GREEN}$ITERACAO${NC}"
    echo -e "${CYAN}║${NC} Tempo de execução: ${GREEN}${horas}h ${minutos}m ${segundos}s${NC}"
    echo -e "${CYAN}║${NC} Total de arquivos: ${GREEN}$arquivos${NC}"
    echo -e "${CYAN}║${NC} Tamanho total: ${GREEN}${tamanho_mb} MB${NC}"
    echo -e "${CYAN}║${NC} Pasta: ${GREEN}$PASTA_DESTINO${NC}"
    echo -e "${CYAN}║${NC} Template: ${GREEN}$TEMPLATE${NC}"
    echo -e "${CYAN}║${NC} Arquivos por iteração: ${GREEN}$QUANTIDADE_ARQUIVOS${NC}"
    
    if [ $ITERACAO -gt 0 ]; then
        local media_arquivos=$((arquivos / ITERACAO))
        local media_mb=$((tamanho_mb / ITERACAO))
        echo -e "${CYAN}║${NC} Média por iteração: ${GREEN}${media_arquivos} arquivos, ${media_mb} MB${NC}"
    fi
    
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}\n"
}

# Função para salvar estatísticas em arquivo
salvar_estatisticas() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local stats=$(calcular_estatisticas "$PASTA_DESTINO")
    local arquivos=$(echo "$stats" | cut -d',' -f1)
    local tamanho_mb=$(echo "$stats" | cut -d',' -f2)
    
    echo "$timestamp,$ITERACAO,$arquivos,$tamanho_mb" >> "$STATS_FILE"
}

# Função para verificar espaço em disco
verificar_espaco() {
    local espaco_disponivel=$(df "$PASTA_DESTINO" 2>/dev/null | tail -1 | awk '{print $4}')
    local espaco_mb=$((espaco_disponivel / 1024))
    
    if [ $espaco_mb -lt 1000 ]; then
        log "${RED}⚠️  ATENÇÃO: Menos de 1GB de espaço disponível!${NC}"
        log "${YELLOW}Espaço restante: ${espaco_mb} MB${NC}"
    fi
}

# Função para limpar arquivos antigos (opcional)
limpar_arquivos_antigos() {
    if [ $ITERACAO -gt 0 ] && [ $((ITERACAO % 10)) -eq 0 ]; then
        log "${YELLOW}🧹 Limpeza automática (iteração $ITERACAO)${NC}"
        # Manter apenas os últimos 1000 arquivos
        find "$PASTA_DESTINO" -type f -name "*.txt" -o -name "*.pdf" -o -name "*.docx" -o -name "*.xlsx" -o -name "*.jpeg" -o -name "*.png" | \
        sort -r | tail -n +1001 | xargs rm -f 2>/dev/null
        log "${GREEN}✅ Limpeza concluída${NC}"
    fi
}

# Função para capturar sinais de interrupção
cleanup() {
    echo -e "\n${YELLOW}🛑 Interrompendo gerador...${NC}"
    log "${YELLOW}🛑 Gerador interrompido pelo usuário${NC}"
    exibir_estatisticas
    log "${GREEN}📊 Estatísticas finais salvas em: $STATS_FILE${NC}"
    exit 0
}

# Configurar captura de sinais
trap cleanup SIGINT SIGTERM

# =============================================================================
# INÍCIO DO SCRIPT
# =============================================================================

echo -e "${BLUE}🚀 Iniciando Gerador Infinito de Arquivos${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

# Verificar se estamos no diretório correto
if [ ! -f "geraArquivos.py" ]; then
    echo -e "${RED}❌ Erro: geraArquivos.py não encontrado!${NC}"
    echo -e "${YELLOW}Execute este script no diretório do projeto geraArquivos${NC}"
    exit 1
fi

# Verificar se o ambiente virtual existe
if [ ! -d "$VENV_PATH" ]; then
    echo -e "${RED}❌ Erro: Ambiente virtual não encontrado!${NC}"
    echo -e "${YELLOW}Execute primeiro: python -m venv venv${NC}"
    exit 1
fi

# Ativar ambiente virtual
echo -e "${YELLOW}🔧 Ativando ambiente virtual...${NC}"
source "$VENV_PATH/bin/activate"

# Verificar se o módulo funciona
echo -e "${YELLOW}🧪 Testando módulo geraArquivos...${NC}"
if ! python -c "from geraArquivos import gerar" 2>/dev/null; then
    echo -e "${RED}❌ Erro: Módulo geraArquivos não funciona!${NC}"
    echo -e "${YELLOW}Verifique se todas as dependências estão instaladas${NC}"
    exit 1
fi

# Criar pasta de destino
mkdir -p "$PASTA_DESTINO"

# Inicializar arquivos de log
echo "timestamp,iteracao,arquivos,tamanho_mb" > "$STATS_FILE"
log "${GREEN}✅ Gerador iniciado com sucesso!${NC}"
log "${BLUE}📁 Pasta de destino: $PASTA_DESTINO${NC}"
log "${BLUE}📊 Template: $TEMPLATE${NC}"
log "${BLUE}📦 Arquivos por iteração: $QUANTIDADE_ARQUIVOS${NC}"
log "${BLUE}📝 Log: $LOG_FILE${NC}"
log "${BLUE}📈 Estatísticas: $STATS_FILE${NC}"

# Exibir estatísticas iniciais
exibir_estatisticas

# =============================================================================
# LOOP INFINITO
# =============================================================================

while true; do
    ITERACAO=$((ITERACAO + 1))
    
    echo -e "${PURPLE}🔄 Iteração $ITERACAO iniciada...${NC}"
    log "${PURPLE}🔄 Iniciando iteração $ITERACAO${NC}"
    
    # Verificar espaço em disco
    verificar_espaco
    
    # Executar geração de arquivos
    echo -e "${YELLOW}📦 Gerando $QUANTIDADE_ARQUIVOS arquivos...${NC}"
    
    if python -c "from geraArquivos import gerar; gerar($QUANTIDADE_ARQUIVOS, '$TEMPLATE', '$PASTA_DESTINO')" 2>>"$LOG_FILE"; then
        echo -e "${GREEN}✅ Iteração $ITERACAO concluída com sucesso!${NC}"
        log "${GREEN}✅ Iteração $ITERACAO concluída${NC}"
    else
        echo -e "${RED}❌ Erro na iteração $ITERACAO!${NC}"
        log "${RED}❌ Erro na iteração $ITERACAO${NC}"
        echo -e "${YELLOW}🔄 Tentando novamente em 5 segundos...${NC}"
        sleep 5
        continue
    fi
    
    # Atualizar contadores
    TOTAL_ARQUIVOS=$((TOTAL_ARQUIVOS + QUANTIDADE_ARQUIVOS))
    
    # Salvar estatísticas
    salvar_estatisticas
    
    # Exibir estatísticas a cada 5 iterações
    if [ $((ITERACAO % 5)) -eq 0 ]; then
        exibir_estatisticas
    fi
    
    # Limpeza automática (opcional)
    limpar_arquivos_antigos
    
    # Pausa entre iterações (opcional)
    echo -e "${BLUE}⏳ Aguardando 2 segundos antes da próxima iteração...${NC}"
    sleep 2
done
