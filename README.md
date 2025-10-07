# GeraArquivos - Gerador de Arquivos de Teste

Sistema parametrizável para geração de arquivos de teste em diferentes formatos (JPEG, PDF, DOCX, XLSX, TXT).

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

### Arquivos Essenciais:
- **`geraArquivos.py`**: Módulo principal com todas as funcionalidades
- **`config.json`**: Configurações centralizadas e personalizáveis
- **`requirements.txt`**: Lista de dependências Python
- **`README.md`**: Documentação completa do sistema

## 🚀 Funcionalidades

### ✅ **Controle de Tipos de Arquivo**
- Ative/desative tipos específicos de arquivo
- Suporte para: JPEG, PDF, DOCX, XLSX, TXT

### ✅ **Controle de Quantidade**
- Quantidade específica por tipo de arquivo
- Modo aleatório com distribuição automática
- Controle total sobre quantos arquivos de cada tipo gerar

### ✅ **Controle de Tamanho**
- Tamanho alvo em MB para cada tipo de arquivo
- Ajuste automático do conteúdo para atingir o tamanho desejado
- Configurações específicas por tipo (resolução, linhas, parágrafos, etc.)

## 📋 Uso Básico

### Geração Aleatória Simples
```python
from geraArquivos import gerar_arquivos_aleatorios

# Gerar 10 arquivos aleatórios
gerar_arquivos_aleatorios(10)

# Gerar apenas TXT e PDF
gerar_arquivos_aleatorios(5, ["txt", "pdf"])
```

### Geração com Quantidade Específica
```python
from geraArquivos import gerar_arquivos_por_tipo

# Gerar 2 TXT, 3 XLSX e 1 JPEG
gerar_arquivos_por_tipo({
    "txt": 2,
    "xlsx": 3, 
    "jpeg": 1
})
```

### Configuração Completa
```python
from geraArquivos import ConfiguracaoArquivos, gerar_arquivos

config = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx"],
    quantidade_por_tipo={"txt": 3, "pdf": 2, "docx": 1},
    tamanho_mb={"txt": 0.5, "pdf": 1.0, "docx": 0.8},
    config_especifica={
        "txt": {"linhas": 20, "caracteres_por_linha": 100},
        "pdf": {"linhas": 10, "caracteres_por_linha": 80},
        "docx": {"paragrafos": 8, "caracteres_por_paragrafo": 150}
    }
)

gerar_arquivos(config)
```

## ⚙️ Sistema de Configuração

### 📄 Arquivo config.json

O sistema agora utiliza um arquivo `config.json` centralizado para todas as configurações, permitindo personalização completa sem modificar o código.

#### Estrutura do config.json:

```json
{
  "configuracao_global": {
    "diretorio_padrao": "arquivos_teste",
    "locale_faker": "pt_BR",
    "encoding_padrao": "utf-8"
  },
  "tipos_arquivo_padrao": ["jpeg", "pdf", "docx", "xlsx", "txt"],
  "tamanhos_mb_padrao": {
    "jpeg": 0.5, "pdf": 1.0, "docx": 0.8, "xlsx": 0.3, "txt": 0.1
  },
  "configuracoes_especificas": {
    "jpeg": {"linhas_texto": 50, "resolucao": [800, 600], "qualidade": 85},
    "pdf": {"linhas": 5, "caracteres_por_linha": 80, "margem_esquerda": 100},
    "docx": {"paragrafos": 5, "caracteres_por_paragrafo": 120},
    "xlsx": {"linhas": 20, "colunas": 15, "ajustar_largura_colunas": true},
    "txt": {"linhas": 10, "caracteres_por_linha": 80, "incluir_cabecalho": true}
  }
}
```

### ConfiguracaoArquivos

| Parâmetro | Tipo | Descrição | Padrão |
|-----------|------|-----------|---------|
| `tipos_ativados` | List[str] | Tipos de arquivo a gerar | Carregado do config.json |
| `quantidade_por_tipo` | Dict[str, int] | Quantidade específica por tipo | `{}` |
| `tamanho_mb` | Dict[str, float] | Tamanho alvo em MB por tipo | Carregado do config.json |
| `config_especifica` | Dict[str, Dict] | Configurações específicas por tipo | Carregado do config.json |
| `diretorio_destino` | str | Diretório onde salvar arquivos | Carregado do config.json |

### 🎛️ Personalização via config.json

#### Modificando Configurações Globais:
```json
{
  "configuracao_global": {
    "diretorio_padrao": "meus_arquivos_teste",
    "locale_faker": "pt_BR",
    "encoding_padrao": "utf-8"
  }
}
```

#### Ajustando Tamanhos de Arquivo:
```json
{
  "tamanhos_mb_padrao": {
    "jpeg": 1.0,    // 1MB para imagens
    "pdf": 2.0,     // 2MB para PDFs
    "docx": 1.5,    // 1.5MB para documentos
    "xlsx": 0.5,    // 500KB para planilhas
    "txt": 0.2      // 200KB para textos
  }
}
```

#### Configurações Específicas por Tipo:

**JPEG:**
```json
{
  "jpeg": {
    "linhas_texto": 100,        // Caracteres do texto sobreposto
    "resolucao": [1920, 1080],  // Resolução da imagem
    "qualidade": 95,            // Qualidade JPEG (1-100)
    "formato_cor": "RGB"        // Formato de cor
  }
}
```

**PDF:**
```json
{
  "pdf": {
    "linhas": 10,               // Número de linhas
    "caracteres_por_linha": 100, // Limite de caracteres por linha
    "margem_esquerda": 50,       // Margem esquerda em pixels
    "margem_superior": 800,      // Margem superior em pixels
    "espacamento_linhas": 15,    // Espaçamento entre linhas
    "altura_minima_pagina": 100, // Altura mínima antes de nova página
    "fonte_tamanho": 14          // Tamanho da fonte
  }
}
```

**DOCX:**
```json
{
  "docx": {
    "paragrafos": 8,                    // Número de parágrafos
    "caracteres_por_paragrafo": 200,   // Caracteres por parágrafo
    "incluir_titulo": true,             // Incluir título do documento
    "incluir_informacoes": true,        // Incluir seção de informações
    "nivel_titulo": 0                    // Nível do título (0-6)
  }
}
```

**XLSX:**
```json
{
  "xlsx": {
    "linhas": 50,                    // Número de linhas de dados
    "colunas": 15,                    // Número de colunas
    "ajustar_largura_colunas": true,  // Ajustar largura automaticamente
    "largura_maxima_coluna": 50,      // Largura máxima de coluna
    "incluir_cabecalho": true,        // Incluir cabeçalho
    "nome_planilha": "Dados"          // Nome da planilha
  }
}
```

**TXT:**
```json
{
  "txt": {
    "linhas": 20,                    // Número de linhas
    "caracteres_por_linha": 100,     // Caracteres por linha
    "incluir_cabecalho": true,       // Incluir cabeçalho
    "incluir_rodape": true,          // Incluir rodapé
    "separador_linha": "=",          // Caractere separador
    "largura_separador": 80          // Largura do separador
  }
}
```

### Tamanhos Padrão (MB)
- **JPEG**: 0.5 MB
- **PDF**: 1.0 MB  
- **DOCX**: 0.8 MB
- **XLSX**: 0.3 MB
- **TXT**: 0.1 MB

### Configurações Específicas Padrão
```python
{
    "jpeg": {"linhas_texto": 50, "resolucao": (800, 600)},
    "pdf": {"linhas": 5, "caracteres_por_linha": 80},
    "docx": {"paragrafos": 5, "caracteres_por_paragrafo": 120},
    "xlsx": {"linhas": 20, "colunas": 3},
    "txt": {"linhas": 10, "caracteres_por_linha": 80}
}
```

## 📁 Estrutura dos Arquivos Gerados

### TXT
- Texto Lorem Ipsum profissional
- Cabeçalho e rodapé formatados
- Data de geração e ID único
- Controle de tamanho baseado em MB
- Codificação UTF-8

### PDF
- Texto Lorem Ipsum profissional
- Formato padrão A4 com quebra de página automática
- Quebra de linha inteligente (80 caracteres)
- Controle de tamanho baseado em MB

### DOCX
- Texto Lorem Ipsum em parágrafos
- Título e seção de informações
- Data de geração e ID único
- Formatação padrão do Word
- Controle de tamanho baseado em MB

### XLSX
- Planilha com 15 colunas de dados realistas
- Dados gerados com biblioteca Faker em português brasileiro
- Colunas incluem: ID, Nome, Email, Telefone, Endereço, Cidade, Estado, CEP, Data_Nascimento, Profissão, Empresa, Salário, Data_Contrato, Status, Observações
- Formatação automática de colunas
- Formato Excel padrão

### JPEG
- Imagem colorida aleatória
- Texto sobreposto
- Resolução ajustável

## 🧪 Exemplos Práticos

Execute `python exemplo_uso.py` para ver demonstrações completas de todas as funcionalidades.

## 🎭 Dados Realistas com Faker

Os arquivos XLSX agora utilizam a biblioteca **Faker** para gerar dados realistas em português brasileiro:

### Colunas Geradas Automaticamente:
- **ID**: Números únicos de 1000-9999
- **Nome**: Nomes completos brasileiros
- **Email**: Endereços de email realistas
- **Telefone**: Números de telefone no formato brasileiro
- **Endereço**: Endereços completos com bairro e cidade
- **Cidade**: Nomes de cidades brasileiras
- **Estado**: Estados brasileiros
- **CEP**: Códigos postais válidos
- **Data_Nascimento**: Datas de nascimento (18-80 anos)
- **Profissão**: Profissões diversas
- **Empresa**: Nomes de empresas
- **Salário**: Valores salariais (R$ 1.500 - R$ 15.000)
- **Data_Contrato**: Datas de contratação (últimos 5 anos)
- **Status**: Status do funcionário (Ativo, Inativo, Férias, Licença)
- **Observações**: Textos aleatórios de até 100 caracteres

### Controle de Tamanho:
- **0.1 MB**: ~200 linhas
- **0.5 MB**: ~1000 linhas  
- **1.0 MB**: ~2000 linhas

Execute `python exemplo_faker.py` para ver demonstrações específicas da funcionalidade Faker.

## 📝 Texto Lorem Ipsum

Os arquivos **TXT**, **PDF** e **DOCX** agora utilizam a biblioteca **lorem-text** para gerar texto Lorem Ipsum profissional:

### Características do Lorem Ipsum:
- **Texto clássico**: Lorem ipsum dolor sit amet, consectetur adipiscing elit...
- **Parágrafos variados**: Tamanho aleatório entre 50-200 palavras
- **Quebra inteligente**: Linhas respeitam limite de caracteres
- **Formatação profissional**: Cabeçalhos, rodapés e estrutura organizada

### Controle de Tamanho por Tipo:
- **TXT**: ~1 caractere = 1 byte (controle preciso)
- **PDF**: Redução de 30% devido ao overhead de formatação
- **DOCX**: Redução de 50% devido ao overhead de XML

### Estrutura dos Arquivos:
- **TXT**: Cabeçalho, parágrafos numerados, rodapé com informações
- **PDF**: Quebra de página automática, quebra de linha em 80 caracteres
- **DOCX**: Título, parágrafos Lorem Ipsum, seção de informações

Execute `python exemplo_lorem.py` para ver demonstrações específicas da funcionalidade Lorem Ipsum.

## 📋 Arquivos de Procedimento

### Scripts de Execução
- **`executar.py`**: Script principal com verificação de ambiente e exemplos
- **`ativar_ambiente.sh`**: Script automático para Linux/Mac
- **`ativar_ambiente.bat`**: Script automático para Windows
- **`configuracao.py`**: Configurações pré-definidas e personalização

### Documentação
- **`INSTRUCOES_EXECUCAO.md`**: Instruções detalhadas de execução
- **`exemplo_uso.py`**: Exemplos básicos de uso
- **`exemplo_faker.py`**: Exemplos específicos para XLSX com Faker
- **`exemplo_lorem.py`**: Exemplos específicos para Lorem Ipsum

### Uso das Configurações
```python
from configuracao import obter_configuracao
from geraArquivos import gerar_arquivos

# Usar configuração pré-definida
config = obter_configuracao('media')
gerar_arquivos(config)

# Configurações disponíveis: 'padrao', 'pequena', 'media', 'grande', 
# 'dados_realistas', 'lorem_ipsum', 'percentual_pdf', 
# 'percentual_equilibrada', 'percentual_especifica'
```

## 📊 Controle de Quantidade e Percentual

### Quantidade Total de Arquivos
```python
from geraArquivos import gerar_arquivos_por_quantidade

# Gerar 50 arquivos aleatoriamente
gerar_arquivos_por_quantidade(50, ["txt", "pdf", "docx"])
```

### Distribuição por Percentual
```python
from geraArquivos import gerar_arquivos_por_percentual

# 70% PDF, 30% outros tipos
gerar_arquivos_por_percentual(
    quantidade_total=100,
    percentual_por_tipo={"pdf": 70, "outros": 30},
    tipos_ativados=["txt", "pdf", "docx", "xlsx"]
)

# Percentuais específicos para cada tipo
gerar_arquivos_por_percentual(
    quantidade_total=24,
    percentual_por_tipo={"txt": 25, "pdf": 25, "docx": 25, "xlsx": 25}
)
```

### Configuração Completa com Percentuais
```python
from geraArquivos import ConfiguracaoArquivos

config = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx"],
    quantidade_total=30,
    percentual_por_tipo={"pdf": 60, "txt": 25, "outros": 15},
    tamanho_mb={"txt": 0.2, "pdf": 0.4, "docx": 0.3}
)
gerar_arquivos(config)
```

## 📦 Dependências

- PIL (Pillow)
- reportlab
- python-docx
- pandas
- openpyxl
- faker
- lorem-text

## 🚀 Execução Rápida

### Opção 1: Script Automático (Recomendado)

#### Linux/Mac:
```bash
chmod +x ativar_ambiente.sh
./ativar_ambiente.sh
```

#### Windows:
```cmd
ativar_ambiente.bat
```

### Opção 2: Execução Manual

#### Passo 1: Ativar Ambiente Virtual
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

#### Passo 3: Usar o Sistema
```python
from geraArquivos import gerar_arquivos_aleatorios

# Gerar 10 arquivos aleatórios
gerar_arquivos_aleatorios(10)
```

## 🔧 Instalação Inicial (Primeira Vez)

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Usar o sistema
python -c "from geraArquivos import gerar_arquivos_aleatorios; gerar_arquivos_aleatorios(5)"
```

## 📊 Saída

O sistema exibe informações detalhadas sobre cada arquivo gerado:
```
[OK] Gerado: arquivos_teste/arquivo_1.txt (0.23 MB)
[OK] Gerado: arquivos_teste/arquivo_2.pdf (0.45 MB)
```

Arquivos são salvos na pasta `arquivos_teste/` por padrão.
