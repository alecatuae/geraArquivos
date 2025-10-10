# 📚 Como Usar o Gerador de Arquivos - Guia Completo

## 🎯 O que este programa faz?

Este programa cria arquivos de teste automaticamente para você. Ele gera diferentes tipos de arquivos (imagens, documentos, planilhas) com conteúdo realista, perfeito para testar sistemas ou fazer demonstrações.

## 🚀 Início Rápido (3 passos)

### Passo 1: Ativar o Ambiente
```bash
# No terminal, execute:
source venv/bin/activate
```

### Passo 2: Gerar Arquivos (Método Mais Simples)
```python
# Abra o Python e execute:
from geraArquivos import gerar
gerar(50)  # Gera 50 arquivos automaticamente
```

### Passo 3: Verificar os Arquivos
Os arquivos aparecerão na pasta `arquivos_teste/` com nomes únicos como:
- `a1b2c3d4e5f6789012345678901234567890abcd.pdf`
- `f9e8d7c6b5a4938271605948372615049382716.jpg`

## 📋 Tipos de Arquivos Gerados

| Tipo | Extensão | O que contém |
|------|----------|--------------|
| **JPEG** | `.jpg` | Imagens coloridas com palavras (wordcloud) |
| **PNG** | `.png` | Imagens com transparência e palavras |
| **PDF** | `.pdf` | Documentos com texto Lorem Ipsum |
| **DOCX** | `.docx` | Documentos Word com parágrafos |
| **XLSX** | `.xlsx` | Planilhas com dados de funcionários |
| **TXT** | `.txt` | Arquivos de texto simples |

## 🎨 Exemplos Práticos

### Exemplo 1: Gerar 20 arquivos básicos
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(20)"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 1 arquivos (5.0%)
   PNG: 3 arquivos (15.0%)
   PDF: 12 arquivos (60.0%)
   DOCX: 1 arquivos (5.0%)
   XLSX: 1 arquivos (5.0%)
   TXT: 2 arquivos (10.0%)

[OK] Gerado: arquivos_teste/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: arquivos_teste/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: arquivos_teste/... (mais 18 arquivos)

✅ Total de arquivos gerados: 20
```

**Resultado:** 20 arquivos misturados na pasta `arquivos_teste/`

### Exemplo 2: Gerar arquivos em pasta específica
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(30, 'equilibrado', 'minha_pasta')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 2 arquivos (6.7%)
   PNG: 5 arquivos (16.7%)
   PDF: 18 arquivos (60.0%)
   DOCX: 1 arquivos (3.3%)
   XLSX: 2 arquivos (6.7%)
   TXT: 2 arquivos (6.7%)

[OK] Gerado: minha_pasta/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: minha_pasta/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: minha_pasta/... (mais 28 arquivos)

✅ Total de arquivos gerados: 30
```

**Resultado:** 30 arquivos na pasta `minha_pasta/`

### Exemplo 3: Focar em imagens
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(25, 'foco_imagens', 'imagens_teste')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 8 arquivos (32.0%)
   PNG: 7 arquivos (28.0%)
   PDF: 5 arquivos (20.0%)
   DOCX: 2 arquivos (8.0%)
   XLSX: 2 arquivos (8.0%)
   TXT: 1 arquivos (4.0%)

[OK] Gerado: imagens_teste/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: imagens_teste/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: imagens_teste/... (mais 23 arquivos)

✅ Total de arquivos gerados: 25
```

**Resultado:** 25 arquivos com 60% sendo imagens (JPEG/PNG)

### Exemplo 4: Focar em documentos
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(40, 'foco_documentos', 'documentos')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   PDF: 16 arquivos (40.0%)
   DOCX: 12 arquivos (30.0%)
   TXT: 8 arquivos (20.0%)
   JPEG: 2 arquivos (5.0%)
   PNG: 1 arquivos (2.5%)
   XLSX: 1 arquivos (2.5%)

[OK] Gerado: documentos/a1b2c3d4e5f6789012345678901234567890abcd.pdf (0.52 MB)
[OK] Gerado: documentos/f9e8d7c6b5a4938271605948372615049382716.docx (0.14 MB)
[OK] Gerado: documentos/... (mais 38 arquivos)

✅ Total de arquivos gerados: 40
```

**Resultado:** 40 arquivos com 70% sendo documentos (PDF/DOCX)

## 📊 Templates Disponíveis

### 🎯 "equilibrado" (Padrão)
- **JPEG:** 7% | **PNG:** 16% | **PDF:** 61% | **DOCX:** 2% | **XLSX:** 7% | **TXT:** 7%
- **Uso:** Distribuição balanceada para testes gerais

### 📄 "foco_documentos"
- **PDF:** 40% | **DOCX:** 30% | **TXT:** 20% | **Outros:** 10%
- **Uso:** Quando você precisa principalmente de documentos

### 📊 "foco_dados"
- **XLSX:** 50% | **TXT:** 25% | **PDF:** 15% | **Outros:** 10%
- **Uso:** Para testar sistemas que trabalham com planilhas

### 🖼️ "foco_imagens"
- **JPEG:** 30% | **PNG:** 30% | **PDF:** 20% | **Outros:** 20%
- **Uso:** Para testar sistemas de imagens

### 📝 "minimal"
- **TXT:** 70% | **PDF:** 30%
- **Uso:** Apenas texto e PDF, ideal para testes simples

## 🛠️ Métodos Avançados

### Método 1: Quantidade Específica por Tipo
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_arquivos_por_tipo
gerar_arquivos_por_tipo(
    quantidade_por_tipo={'pdf': 5, 'jpeg': 3},
    diretorio_destino='meus_arquivos'
)
"
```

**Saída esperada:**
```
[OK] Gerado: meus_arquivos/a1b2c3d4e5f6789012345678901234567890abcd.pdf (0.52 MB)
[OK] Gerado: meus_arquivos/f9e8d7c6b5a4938271605948372615049382716.pdf (0.52 MB)
[OK] Gerado: meus_arquivos/... (mais 6 arquivos)

✅ Total de arquivos gerados: 8
```

### Método 2: Distribuição por Percentual
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_arquivos_por_percentual
gerar_arquivos_por_percentual(
    quantidade_total=20,
    percentual_por_tipo={'pdf': 60, 'outros': 40},
    tipos_ativados=['pdf', 'jpeg', 'txt'],
    diretorio_destino='documentos_mistos'
)
"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   PDF: 12 arquivos (60.0%)
   JPEG: 4 arquivos (20.0%)
   TXT: 4 arquivos (20.0%)

[OK] Gerado: documentos_mistos/a1b2c3d4e5f6789012345678901234567890abcd.pdf (0.52 MB)
[OK] Gerado: documentos_mistos/f9e8d7c6b5a4938271605948372615049382716.jpeg (0.12 MB)
[OK] Gerado: documentos_mistos/... (mais 18 arquivos)

✅ Total de arquivos gerados: 20
```

### Método 3: Geração Aleatória
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_arquivos_aleatorios
gerar_arquivos_aleatorios(
    qtd=15,
    tipos_ativados=['jpeg', 'png'],
    diretorio_destino='imagens_aleatorias'
)
"
```

**Saída esperada:**
```
[OK] Gerado: imagens_aleatorias/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: imagens_aleatorias/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: imagens_aleatorias/... (mais 13 arquivos)

✅ Total de arquivos gerados: 15
```

## ⚙️ Personalizando Tamanhos

### Alterar Tamanho dos Arquivos
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_arquivos_por_tipo
gerar_arquivos_por_tipo(
    quantidade_por_tipo={'pdf': 3, 'jpeg': 2},
    tamanhos_mb={'pdf': 2.0, 'jpeg': 1.0},
    diretorio_destino='arquivos_grandes'
)
"
```

**Saída esperada:**
```
[OK] Gerado: arquivos_grandes/a1b2c3d4e5f6789012345678901234567890abcd.pdf (2.1 MB)
[OK] Gerado: arquivos_grandes/f9e8d7c6b5a4938271605948372615049382716.pdf (2.0 MB)
[OK] Gerado: arquivos_grandes/... (mais 3 arquivos)

✅ Total de arquivos gerados: 5
```

## 📁 Estrutura de Pastas

```
seu_projeto/
├── arquivos_teste/          # Pasta padrão
├── minha_pasta/            # Pasta personalizada
├── imagens_teste/          # Pasta para imagens
└── documentos/             # Pasta para documentos
```

## 🔧 Configurações Avançadas

### Arquivo config.json
Você pode personalizar o comportamento editando o arquivo `config.json`:

```json
{
  "configuracao_global": {
    "diretorio_padrao": "arquivos_teste",
    "locale_faker": "pt_BR"
  },
  "tamanhos_mb_padrao": {
    "jpeg": 0.5,
    "png": 0.6,
    "pdf": 1.0,
    "docx": 0.8,
    "xlsx": 0.3,
    "txt": 0.1
  }
}
```

## 🚨 Solução de Problemas

### Problema: "Arquivo não encontrado"
```bash
# Solução: Ative o ambiente primeiro
source venv/bin/activate
```

### Problema: "Erro de permissão"
```bash
# Solução: Verifique se tem permissão para criar pastas
mkdir teste_permissao
```

### Problema: "Muitos arquivos gerados"
```python
# Solução: Use quantidades menores
gerar(5)  # Em vez de gerar(1000)
```

## 📈 Exemplos de Uso Real

### Cenário 1: Teste de Sistema de Upload
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(100, 'equilibrado', 'teste_upload')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 7 arquivos (7.0%)
   PNG: 16 arquivos (16.0%)
   PDF: 61 arquivos (61.0%)
   DOCX: 2 arquivos (2.0%)
   XLSX: 7 arquivos (7.0%)
   TXT: 7 arquivos (7.0%)

[OK] Gerado: teste_upload/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: teste_upload/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: teste_upload/... (mais 98 arquivos)

✅ Total de arquivos gerados: 100
```

### Cenário 2: Demonstração de Relatórios
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(50, 'foco_documentos', 'apresentacao')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   PDF: 20 arquivos (40.0%)
   DOCX: 15 arquivos (30.0%)
   TXT: 10 arquivos (20.0%)
   JPEG: 3 arquivos (6.0%)
   PNG: 1 arquivos (2.0%)
   XLSX: 1 arquivos (2.0%)

[OK] Gerado: apresentacao/a1b2c3d4e5f6789012345678901234567890abcd.pdf (0.52 MB)
[OK] Gerado: apresentacao/f9e8d7c6b5a4938271605948372615049382716.docx (0.14 MB)
[OK] Gerado: apresentacao/... (mais 48 arquivos)

✅ Total de arquivos gerados: 50
```

### Cenário 3: Teste de Performance
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(500, 'minimal', 'teste_performance')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   TXT: 350 arquivos (70.0%)
   PDF: 150 arquivos (30.0%)

[OK] Gerado: teste_performance/a1b2c3d4e5f6789012345678901234567890abcd.txt (0.10 MB)
[OK] Gerado: teste_performance/f9e8d7c6b5a4938271605948372615049382716.pdf (0.52 MB)
[OK] Gerado: teste_performance/... (mais 498 arquivos)

✅ Total de arquivos gerados: 500
```

### Cenário 4: Desenvolvimento de Sistema de Imagens
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(30, 'foco_imagens', 'sistema_imagens')"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 9 arquivos (30.0%)
   PNG: 9 arquivos (30.0%)
   PDF: 6 arquivos (20.0%)
   DOCX: 3 arquivos (10.0%)
   XLSX: 2 arquivos (6.7%)
   TXT: 1 arquivos (3.3%)

[OK] Gerado: sistema_imagens/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
[OK] Gerado: sistema_imagens/f9e8d7c6b5a4938271605948372615049382716.png (0.18 MB)
[OK] Gerado: sistema_imagens/... (mais 28 arquivos)

✅ Total de arquivos gerados: 30
```

## 📦 Geração com Empacotamento TAR (Novo!)

### O que é TAR?
TAR é um formato de arquivamento que permite empacotar múltiplos arquivos em um único arquivo, com ou sem compressão. Ideal para:
- Transferir múltiplos arquivos de uma vez
- Economizar espaço com compressão
- Organizar arquivos de teste

### Exemplo 1: TAR sem compressão (mais rápido)
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(20)"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 1 arquivos (5.0%)
   PNG: 3 arquivos (15.0%)
   PDF: 12 arquivos (60.0%)
   ...

[OK] Gerado: arquivos_teste/a1b2c3d4e5f6789012345678901234567890abcd.jpeg (0.12 MB)
...
✅ Total de arquivos gerados: 20

📦 Criando arquivo tar...
   📁 Diretório: arquivos_teste
   📄 Arquivo tar: f9e8d7c6b5a4938271605948372615049382716.tar
   🗜️  Compressão: Nenhuma (default)
   📊 Arquivos a empacotar: 20
   ✅ Tamanho original: 15.50 MB
   ✅ Tamanho do tar: 15.60 MB

✅ Arquivo tar criado com sucesso: f9e8d7c6b5a4938271605948372615049382716.tar
```

**Resultado:** Arquivo `.tar` com todos os arquivos (nome em hash SHA-1)

### Exemplo 2: TAR com compressão gzip (recomendado)
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(30, compressao='gz')"
```

**Saída esperada:**
```
...
✅ Total de arquivos gerados: 30

📦 Criando arquivo tar...
   📄 Arquivo tar: 1234567890abcdef1234567890abcdef12345678.tar.gz
   🗜️  Compressão: gz
   📊 Arquivos a empacotar: 30
   ✅ Tamanho original: 23.40 MB
   ✅ Tamanho do tar: 11.70 MB
   ✅ Taxa de compressão: 50.0%

✅ Arquivo tar criado com sucesso: 1234567890abcdef1234567890abcdef12345678.tar.gz
```

**Resultado:** Arquivo `.tar.gz` comprimido (economiza ~50% de espaço)

### Exemplo 3: TAR com compressão máxima
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(25, compressao='bz2')"
```

**Saída esperada:**
```
...
📦 Criando arquivo tar...
   📄 Arquivo tar: abcdef1234567890abcdef1234567890abcdef12.tar.bz2
   🗜️  Compressão: bz2
   ✅ Taxa de compressão: 54.0%
```

**Resultado:** Arquivo `.tar.bz2` com melhor compressão

### Exemplo 4: TAR e remover arquivos originais
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(20, compressao='gz', limpar_originais=True)"
```

**Saída esperada:**
```
...
✅ Tamanho do tar: 7.80 MB
   ✅ Taxa de compressão: 49.6%
   🗑️  Removendo arquivos originais...
   ✅ Diretório removido: arquivos_teste

✅ Arquivo tar criado com sucesso: ...tar.gz
```

**Resultado:** Apenas o arquivo `.tar.gz` permanece (arquivos individuais removidos)

### Exemplo 5: TAR com diretório personalizado
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(15, 'foco_imagens', 'minhas_imagens', 'xz')"
```

**Resultado:** Arquivos gerados em `minhas_imagens/` e empacotados em `.tar.xz`

### 📊 Tipos de Compressão Disponíveis

| Tipo | Extensão | Velocidade | Compressão | Uso Recomendado |
|------|----------|------------|------------|-----------------|
| **Nenhum** | `.tar` | ⚡⚡⚡ Muito rápido | ❌ 0% | Transferência local rápida |
| **gzip (gz)** | `.tar.gz` | ⚡⚡ Rápido | ✅ ~50% | Uso geral (recomendado) |
| **bzip2 (bz2)** | `.tar.bz2` | ⚡ Médio | ✅✅ ~54% | Arquivos grandes |
| **xz** | `.tar.xz` | 🐌 Lento | ✅✅✅ ~52% | Armazenamento longo prazo |

### 🎯 Quando Usar TAR?

✅ **Use TAR quando:**
- Precisa transferir muitos arquivos
- Quer economizar espaço em disco
- Precisa fazer backup de arquivos de teste
- Vai enviar arquivos por email ou upload

❌ **Não use TAR quando:**
- Precisa acessar arquivos individuais frequentemente
- Está apenas testando localmente
- Quer ver os arquivos diretamente no explorador

### 💻 Comandos Práticos Prontos

```bash
# Gerar 50 arquivos e empacotar sem compressão
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(50)"

# Gerar 30 arquivos e empacotar com gzip (recomendado)
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(30, compressao='gz')"

# Gerar 40 arquivos, empacotar e limpar originais
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(40, compressao='gz', limpar_originais=True)"

# Focar em imagens e empacotar com máxima compressão
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(25, 'foco_imagens', 'imagens', 'bz2')"
```

## 🔄 Fluxo Buffer → TAR → Destino (Novo!)

### O que é o Fluxo Buffer?
Um padrão avançado onde os arquivos são gerados em um **buffer temporário**, empacotados em tar, movidos para o **destino final** e o buffer é **automaticamente limpo**. Ideal para:
- Processar arquivos em lotes (batches)
- Gerar múltiplos tars em ciclos
- Manter o sistema organizado (buffer sempre limpo)
- Simulações de pipelines de dados

### Fluxo Completo
```
1️⃣  Arquivos (JPEG, PNG, PDF, etc.) → BUFFER temporário
2️⃣  Arquivos do buffer → Encapsulados em .tar
3️⃣  Arquivo .tar → Movido para DESTINO final
4️⃣  Buffer → LIMPO automaticamente (pronto para novo ciclo)
```

### Exemplo 1: Fluxo Básico
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_buffer_e_empacotar; gerar_buffer_e_empacotar(30)"
```

**Saída esperada:**
```
======================================================================
🔄 FLUXO BUFFER → TAR → DESTINO
======================================================================
1️⃣  Gerando arquivos no buffer: buffer_temp/
2️⃣  Criando arquivo tar
3️⃣  Movendo tar para destino: arquivos_tar/
4️⃣  Limpando buffer
======================================================================

[OK] Gerado: buffer_temp/xxxxx.pdf (0.52 MB)
...

✅ Total de arquivos gerados: 30

📦 Criando arquivo tar...
   📁 Buffer (origem): buffer_temp
   📄 Arquivo tar: abc123...xyz.tar
   📂 Destino do tar: arquivos_tar
   🗑️  Removendo arquivos originais...
   ✅ Diretório removido: buffer_temp

✅ CICLO COMPLETO:
   📁 Buffer usado: buffer_temp/
   📦 Tar criado em: arquivos_tar/
   🧹 Buffer limpo e pronto para novo ciclo
```

**Resultado:** 
- Tar criado em `arquivos_tar/abc123...xyz.tar`
- Buffer `buffer_temp/` foi completamente removido
- Sistema pronto para novo ciclo

### Exemplo 2: Com Compressão e Diretórios Personalizados
```bash
# No terminal, execute:
source venv/bin/activate
python -c "from geraArquivos import gerar_buffer_e_empacotar; gerar_buffer_e_empacotar(50, 'equilibrado', 'meu_buffer', 'meus_tars', 'gz')"
```

**Resultado:**
- 50 arquivos gerados em `meu_buffer/`
- Tar com gzip: `meus_tars/xxxxx.tar.gz`
- `meu_buffer/` limpo automaticamente

### Exemplo 3: Ciclos Múltiplos (Processamento em Lote)
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_buffer_e_empacotar

# Gerar 5 lotes de arquivos
for i in range(5):
    print(f'\n📦 Lote {i+1}/5')
    gerar_buffer_e_empacotar(
        quantidade=20,
        buffer='buffer_processamento',
        destino='saida_lotes',
        compressao='gz'
    )
"
```

**Resultado:**
- 5 tars criados em `saida_lotes/`
- Buffer reutilizado e limpo a cada ciclo
- Processamento eficiente em lotes

### Exemplo 4: Pipeline de Dados
```bash
# No terminal, execute:
source venv/bin/activate
python -c "
from geraArquivos import gerar_buffer_e_empacotar

# Simular pipeline: diferentes tipos de dados
templates = ['foco_imagens', 'foco_documentos', 'foco_dados']

for template in templates:
    print(f'\n📊 Processando: {template}')
    gerar_buffer_e_empacotar(
        quantidade=30,
        template=template,
        buffer='pipeline_buffer',
        destino='pipeline_output',
        compressao='bz2'
    )
"
```

**Resultado:**
- 3 tars categorizados em `pipeline_output/`
- Buffer limpo entre cada categoria
- Pipeline automatizado

### 🎯 Quando Usar o Fluxo Buffer?

✅ **Use Fluxo Buffer quando:**
- Precisa gerar múltiplos lotes/batches
- Quer manter o sistema organizado (sem arquivos soltos)
- Está simulando pipelines de dados
- Precisa de processamento cíclico
- Quer separar geração (buffer) de armazenamento (destino)

❌ **Use gerar_e_empacotar() quando:**
- Precisa gerar apenas um tar
- Quer manter os arquivos originais
- Não precisa de ciclos múltiplos

### 📊 Comparação: gerar_e_empacotar vs gerar_buffer_e_empacotar

| Característica | gerar_e_empacotar() | gerar_buffer_e_empacotar() |
|----------------|---------------------|---------------------------|
| **Limpeza automática** | Opcional | Sempre |
| **Buffer separado** | Não | Sim |
| **Destino configurável** | Pasta pai | Diretório específico |
| **Ciclos múltiplos** | Manual | Otimizado |
| **Uso recomendado** | Tar único | Processamento em lotes |

### 💡 Dicas para Fluxo Buffer

1. **Buffer temporário**: Use nomes como `temp`, `buffer`, `staging`
2. **Destino organizado**: Use nomes como `output`, `tars`, `final`
3. **Compressão gzip**: Melhor equilíbrio para lotes
4. **Ciclos**: O buffer é automaticamente limpo entre ciclos
5. **Monitoramento**: Acompanhe o diretório de destino

## 💡 Dicas Importantes

1. **Comece Simples:** Use `gerar(10)` para testar primeiro
2. **Escolha a Pasta:** Sempre especifique uma pasta para não bagunçar
3. **Quantidade Razoável:** Comece com 10-50 arquivos, não milhares
4. **Verifique o Espaço:** Arquivos grandes ocupam espaço no disco
5. **Use Templates:** Os templates já vêm com distribuições testadas
6. **Compressão gzip:** É o melhor equilíbrio entre velocidade e tamanho
7. **Nomes SHA-1:** Os arquivos tar usam hash SHA-1, igual aos arquivos gerados

## 🎯 Resumo dos Comandos Essenciais

### Geração Normal (sem TAR)
```bash
# Comando mais simples
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(20)"

# Com pasta específica
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(30, 'equilibrado', 'minha_pasta')"

# Focar em imagens
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(25, 'foco_imagens', 'imagens')"

# Focar em documentos
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(40, 'foco_documentos', 'documentos')"

# Apenas texto e PDF
source venv/bin/activate
python -c "from geraArquivos import gerar; gerar(15, 'minimal', 'simples')"
```

### Geração com TAR
```bash
# TAR sem compressão
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(30)"

# TAR com compressão gzip (recomendado)
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(30, compressao='gz')"

# TAR e remover originais
source venv/bin/activate
python -c "from geraArquivos import gerar_e_empacotar; gerar_e_empacotar(30, compressao='gz', limpar_originais=True)"
```

### Fluxo Buffer → TAR → Destino (Novo!)
```bash
# Fluxo básico
source venv/bin/activate
python -c "from geraArquivos import gerar_buffer_e_empacotar; gerar_buffer_e_empacotar(30)"

# Com compressão e diretórios personalizados
source venv/bin/activate
python -c "from geraArquivos import gerar_buffer_e_empacotar; gerar_buffer_e_empacotar(50, buffer='temp', destino='output', compressao='gz')"

# Ciclos múltiplos (processamento em lote)
source venv/bin/activate
python -c "
from geraArquivos import gerar_buffer_e_empacotar
for i in range(5):
    gerar_buffer_e_empacotar(20, buffer='buffer', destino='tars', compressao='gz')
"
```

## ✅ Checklist de Uso

- [ ] Ambiente ativado (`source venv/bin/activate`)
- [ ] Pasta de destino escolhida
- [ ] Quantidade definida (comece com 10-20)
- [ ] Template escolhido (ou use "equilibrado")
- [ ] Verificar se há espaço suficiente no disco

## 🆘 Precisa de Ajuda?

Se algo não funcionar:

1. **Verifique o ambiente:** `source venv/bin/activate`
2. **Teste com poucos arquivos:** `gerar(5)`
3. **Verifique as permissões:** Pode criar pastas?
4. **Consulte os exemplos:** Use os códigos acima como base

---

**🎉 Pronto! Agora você pode gerar arquivos de teste facilmente!**
