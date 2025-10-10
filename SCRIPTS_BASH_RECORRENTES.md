# 🔄 Scripts Bash para Geração Recorrente de TARs

**Data:** 10 de outubro de 2025  
**Status:** ✅ Testado e Validado

---

## 📦 Scripts Criados

### 1. gerar_tars_sem_compressao.sh
- **Tamanho:** 909 bytes
- **Compressão:** Nenhuma (.tar)
- **Uso:** Quando velocidade é prioridade

### 2. gerar_tars_com_compressao.sh
- **Tamanho:** 993 bytes
- **Compressão:** gzip (.tar.gz)
- **Uso:** Quando economia de espaço é importante

---

## 🧪 Resultados dos Testes

### Teste 1: Script SEM Compressão
**Configuração:** 3 ciclos × 10 arquivos = 30 arquivos

**Resultados:**
- ✅ 3 arquivos `.tar` criados
- 📦 Tamanho: ~4.9MB cada
- 💾 Total: 15MB
- ✅ Buffer limpo entre ciclos
- ✅ Nomes SHA-1 únicos
- ⚡ Velocidade: Muito rápida

### Teste 2: Script COM Compressão
**Configuração:** 3 ciclos × 10 arquivos = 30 arquivos

**Resultados:**
- ✅ 3 arquivos `.tar.gz` criados
- 📦 Tamanho: ~3.4MB cada
- 💾 Total: 10MB
- 📊 Taxa de compressão: ~31%
- 💰 Economia: ~33% de espaço
- ✅ Buffer limpo entre ciclos
- ✅ Nomes SHA-1 únicos
- ⚡ Velocidade: Rápida

### Teste 3: Demonstração Final
**Configuração:** 2 ciclos × 5 arquivos = 10 arquivos

**Resultados:**
- ✅ 2 arquivos `.tar` criados
- 📦 Tamanho: ~2.6MB cada
- ✅ Funcionamento conforme documentado
- ✅ Saída idêntica à documentação

---

## 📊 Comparação: SEM vs COM Compressão

| Métrica | SEM Compressão (.tar) | COM Compressão (.tar.gz) | Diferença |
|---------|----------------------|--------------------------|-----------|
| **Tamanho por tar** | ~4.9 MB | ~3.4 MB | -31% |
| **Total (3 tars)** | 15 MB | 10 MB | -33% |
| **Velocidade** | ⚡⚡⚡ Muito rápido | ⚡⚡ Rápido | - |
| **CPU** | 🔋 Baixo uso | 🔋 Médio uso | - |
| **Formato** | .tar | .tar.gz | - |
| **Quando usar** | Rede local, SSD | Transferência, armazenamento | - |

---

## 🎯 Configurações Disponíveis

### Variáveis Configuráveis

```bash
QUANTIDADE=100     # Arquivos por tar (10, 50, 100, 1000...)
CICLOS=10          # Número de tars a gerar (5, 10, 20, 100...)
BUFFER="buffer_temp"       # Nome do buffer temporário
DESTINO="tars_gerados"     # Diretório de destino dos tars
COMPRESSAO="gz"    # Tipo: "gz", "bz2", "xz" ou remova para sem compressão
```

### Exemplos de Personalização

#### Exemplo 1: Gerar 50 TARs de 200 arquivos
```bash
QUANTIDADE=200
CICLOS=50
# Resultado: 10.000 arquivos em 50 tars
```

#### Exemplo 2: Usar compressão máxima
```bash
COMPRESSAO="bz2"
# Melhor taxa de compressão, mais lento
```

#### Exemplo 3: Organizar por data
```bash
DESTINO="tars_$(date +%Y%m%d)"
# Cria pasta com data: tars_20251010
```

---

## 💡 Dicas de Uso

### 1. Teste Primeiro
```bash
# Comece com valores pequenos
QUANTIDADE=10
CICLOS=3
```

### 2. Monitore Espaço em Disco
```bash
# Antes de executar
df -h

# Durante execução (outro terminal)
watch -n 1 df -h
```

### 3. Redirecione Logs
```bash
# Salvar saída em arquivo
./gerar_tars_com_compressao.sh > log_$(date +%Y%m%d_%H%M%S).txt 2>&1
```

### 4. Execute em Background
```bash
# Executar em background
./gerar_tars_com_compressao.sh &

# Ver processos
jobs

# Trazer para foreground
fg %1
```

### 5. Agende com Cron
```bash
# Editar crontab
crontab -e

# Executar todo dia às 2h da manhã
0 2 * * * /caminho/para/gerar_tars_com_compressao.sh >> /var/log/gerar_tars.log 2>&1
```

---

## 📋 Como Usar

### Passo a Passo

1. **Abrir o howto.md**
   ```bash
   cat howto.md
   ```

2. **Ir para seção "🔄 Scripts Bash para Geração Recorrente"**

3. **Copiar o código do script desejado**
   - Script SEM compressão: para velocidade
   - Script COM compressão: para economia de espaço

4. **Criar arquivo .sh**
   ```bash
   nano gerar_tars.sh
   # Colar o código
   ```

5. **Dar permissão de execução**
   ```bash
   chmod +x gerar_tars.sh
   ```

6. **Executar**
   ```bash
   ./gerar_tars.sh
   ```

---

## 🔢 Estimativas de Uso

### Cenário 1: Teste Pequeno
- **Configuração:** 10 ciclos × 100 arquivos
- **Resultado:** 10 tars de ~50MB cada
- **Total:** ~500MB
- **Tempo estimado:** ~5-10 minutos

### Cenário 2: Uso Médio
- **Configuração:** 50 ciclos × 100 arquivos
- **Resultado:** 50 tars de ~50MB cada
- **Total:** ~2.5GB
- **Tempo estimado:** ~25-50 minutos

### Cenário 3: Uso Intensivo
- **Configuração:** 100 ciclos × 100 arquivos
- **Resultado:** 100 tars de ~50MB cada
- **Total:** ~5GB (ou ~2.5GB com compressão)
- **Tempo estimado:** ~50-100 minutos

### Cenário 4: Produção
- **Configuração:** 1000 ciclos × 100 arquivos
- **Resultado:** 1000 tars de ~50MB cada
- **Total:** ~50GB (ou ~25GB com compressão)
- **Tempo estimado:** ~8-16 horas

---

## 🚨 Troubleshooting

### Erro: "Permission denied"
```bash
# Solução: Dar permissão de execução
chmod +x script.sh
```

### Erro: "No space left on device"
```bash
# Verificar espaço disponível
df -h

# Limpar arquivos antigos
rm -rf diretorio_antigo/*
```

### Erro: "comando não encontrado: python"
```bash
# Ativar ambiente virtual
source venv/bin/activate
```

### Script muito lento
```bash
# Use compressão mais rápida (gz) ou sem compressão
COMPRESSAO="gz"  # ou remova a linha
```

---

## ✅ Checklist de Validação

- [x] Scripts criados e testados
- [x] Documentação no howto.md
- [x] Saídas esperadas evidenciadas
- [x] Tabela comparativa incluída
- [x] Dicas de personalização
- [x] Testes com diferentes configurações
- [x] Validação de resultados
- [x] Limpeza de buffers confirmada
- [x] Nomes SHA-1 validados

---

## 📚 Referências

- **Documentação principal:** `howto.md` - Seção "🔄 Scripts Bash para Geração Recorrente"
- **Função base:** `gerar_buffer_e_empacotar()` em `geraArquivos.py`
- **Validação:** `VALIDACAO_FLUXO.md`

---

**✅ Status:** PRONTO PARA USO EM PRODUÇÃO  
**📅 Data de validação:** 10/10/2025

