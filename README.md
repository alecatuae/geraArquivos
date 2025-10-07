# GeraArquivos - Gerador de Arquivos de Teste

Sistema parametrizável para geração de arquivos de teste em diferentes formatos (JPEG, PNG, PDF, DOCX, XLSX, TXT) com wordclouds Lorem Ipsum.

## 📁 Estrutura do Projeto

```
geraArquivos/
├── geraArquivos.py          # Módulo principal com todas as funções
├── config.json              # Configurações centralizadas
├── requirements.txt         # Dependências Python
├── README.md               # Documentação completa
├── ativar_ambiente.sh      # Script de ativação (Linux/Mac)
├── ativar_ambiente.bat     # Script de ativação (Windows)
├── .gitignore              # Arquivos ignorados pelo Git
└── venv/                   # Ambiente virtual Python
```

## 🚀 Setup do Projeto

### Instalação Inicial

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt
```

### Execução Rápida

#### Opção 1: Script Automático (Recomendado)

**Linux/Mac:**
```bash
chmod +x ativar_ambiente.sh
./ativar_ambiente.sh
```

**Windows:**
```cmd
ativar_ambiente.bat
```

#### Opção 2: Execução Manual

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Usar o sistema
python -c "from geraArquivos import gerar_arquivos_aleatorios; gerar_arquivos_aleatorios(5)"
```

## ⚙️ Parametrização (config.json)

### Configurações Globais

```json
{
  "configuracao_global": {
    "diretorio_padrao": "arquivos_teste",
    "locale_faker": "pt_BR",
    "encoding_padrao": "utf-8"
  }
}
```

### Tipos de Arquivo e Tamanhos

```json
{
  "tipos_arquivo_padrao": ["jpeg", "pdf", "docx", "xlsx", "txt"],
  "tamanhos_mb_padrao": {
    "jpeg": 0.5,
    "pdf": 1.0,
    "docx": 0.8,
    "xlsx": 0.3,
    "txt": 0.1
  }
}
```

### Configurações Específicas por Tipo

#### JPEG
```json
{
  "jpeg": {
    "linhas_texto": 50,
    "resolucao": [800, 600],
    "qualidade": 85,
    "formato_cor": "RGB"
  }
}
```

#### PDF
```json
{
  "pdf": {
    "linhas": 5,
    "caracteres_por_linha": 80,
    "margem_esquerda": 100,
    "margem_superior": 800,
    "espacamento_linhas": 20,
    "altura_minima_pagina": 50,
    "fonte_tamanho": 12
  }
}
```

#### DOCX
```json
{
  "docx": {
    "paragrafos": 5,
    "caracteres_por_paragrafo": 120,
    "incluir_titulo": true,
    "incluir_informacoes": true,
    "nivel_titulo": 0
  }
}
```

#### XLSX
```json
{
  "xlsx": {
    "linhas": 20,
    "colunas": 15,
    "ajustar_largura_colunas": true,
    "largura_maxima_coluna": 50,
    "incluir_cabecalho": true,
    "nome_planilha": "Dados"
  }
}
```

#### TXT
```json
{
  "txt": {
    "linhas": 10,
    "caracteres_por_linha": 80,
    "incluir_cabecalho": true,
    "incluir_rodape": true,
    "separador_linha": "=",
    "largura_separador": 80
  }
}
```

## 🎯 Execução (geraArquivos.py)

### Uso Básico

```python
from geraArquivos import gerar_arquivos_aleatorios

# Gerar 10 arquivos aleatórios
gerar_arquivos_aleatorios(10)

# Gerar apenas TXT e PDF
gerar_arquivos_aleatorios(5, ["txt", "pdf"])

# Com diretório personalizado
gerar_arquivos_aleatorios(5, ["txt", "pdf"], "meus_arquivos")
```

### Configuração Avançada

```python
from geraArquivos import ConfiguracaoArquivos, gerar_arquivos

# Configuração personalizada
config = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx"],
    quantidade_por_tipo={"txt": 3, "pdf": 2, "docx": 1},
    tamanho_mb={"txt": 0.5, "pdf": 1.0, "docx": 0.8},
    diretorio_destino="meus_arquivos_teste"
)

gerar_arquivos(config)
```

### Funções Disponíveis

#### Geração Aleatória
```python
gerar_arquivos_aleatorios(qtd=20, tipos_ativados=None, diretorio_destino=None)
```

#### Geração por Tipo
```python
gerar_arquivos_por_tipo(
    quantidade_por_tipo={"txt": 2, "pdf": 3}, 
    tamanhos_mb=None, 
    diretorio_destino=None
)
```

#### Geração por Quantidade Total
```python
gerar_arquivos_por_quantidade(
    quantidade_total=15, 
    tipos_ativados=["txt", "pdf", "docx"], 
    diretorio_destino=None
)
```

#### Geração por Percentual
```python
gerar_arquivos_por_percentual(
    quantidade_total=100,
    percentual_por_tipo={"pdf": 70, "outros": 30},
    tipos_ativados=["txt", "pdf", "docx", "xlsx"],
    tamanhos_mb={"txt": 0.1, "pdf": 0.3, "docx": 0.2, "xlsx": 0.1},
    diretorio_destino=None
)
```

#### Geração por Template (Novo!)
```python
# Usar templates pré-definidos do config.json
gerar_arquivos_por_template(100, "equilibrado")
gerar_arquivos_por_template(50, "foco_documentos")
gerar_arquivos_por_template(30, "foco_dados", diretorio_destino="meus_arquivos")
```

### 🎯 Templates de Percentual Disponíveis

| Template | Descrição | Distribuição |
|----------|-----------|--------------|
| `equilibrado` | Distribuição igual entre todos os tipos | ~17% cada tipo (6 tipos) |
| `foco_documentos` | Foco em documentos | PDF 40%, DOCX 30%, TXT 20%, outros 10% |
| `foco_dados` | Foco em planilhas e dados | XLSX 50%, TXT 25%, PDF 15%, outros 10% |
| `foco_imagens` | Foco em imagens | JPEG 30%, PNG 30%, PDF 20%, outros 20% |
| `minimal` | Apenas texto e PDF | TXT 70%, PDF 30% |

## 📦 Dependências

- PIL (Pillow)
- reportlab
- python-docx
- pandas
- openpyxl
- faker
- lorem-text
- wordcloud
- matplotlib

## 📊 Saída

O sistema exibe informações detalhadas sobre cada arquivo gerado:
```
[OK] Gerado: arquivos_teste/a1b2c3d4e5f6789012345678901234567890abcd.txt (0.23 MB)
[OK] Gerado: arquivos_teste/f9e8d7c6b5a4938271605948372615049382716.pdf (0.45 MB)

✅ Total de arquivos gerados: 2
```

### 🔐 Nomes Únicos com SHA-1

Os arquivos são gerados com nomes únicos baseados em hash SHA-1, garantindo:
- ✅ **Sem conflitos**: Nomes únicos mesmo em execuções simultâneas
- ✅ **Sem contadores**: Não há necessidade de gerenciar contadores globais
- ✅ **Identificação única**: Cada arquivo tem um identificador único de 40 caracteres
- ✅ **Compatibilidade**: Funciona com todos os tipos de arquivo

**Formato dos nomes**: `{hash_sha1}.{extensao}`
- Exemplo: `a1b2c3d4e5f6789012345678901234567890abcd.txt`

Arquivos são salvos na pasta `arquivos_teste/` por padrão (configurável via config.json).

### 🎨 Wordclouds Lorem Ipsum

Os arquivos JPEG e PNG agora são gerados como **wordclouds coloridos** com palavras do Lorem Ipsum:

#### ✨ **Características dos Wordclouds:**
- **Palavras Lorem Ipsum**: Texto clássico em latim
- **Frequências Variadas**: Palavras com tamanhos diferentes baseados na frequência
- **Cores Vibrantes**: Mapas de cores aleatórios (viridis, plasma, inferno, etc.)
- **Layout Dinâmico**: Orientação otimizada para legibilidade
- **Configurável**: Tamanhos, cores e palavras personalizáveis

#### 🎯 **Configurações de Wordcloud:**
```json
"wordcloud": {
  "max_palavras": 100,
  "largura": 800,
  "altura": 600,
  "background_color": "white",
  "colormap": "viridis",
  "max_font_size": 100,
  "min_font_size": 10,
  "relative_scaling": 0.5,
  "prefer_horizontal": 0.9
}
```

#### 🖼️ **Diferenças JPEG vs PNG:**
- **JPEG**: Fundo sólido, cores vibrantes, ideal para fotos
- **PNG**: Suporte a transparência, cores mais suaves, ideal para gráficos