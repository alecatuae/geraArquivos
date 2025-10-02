# GeraArquivos - Gerador de Arquivos de Teste

Sistema parametrizável para geração de arquivos de teste em diferentes formatos (JPEG, PDF, DOCX, XLSX, TXT).

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

## ⚙️ Parâmetros de Configuração

### ConfiguracaoArquivos

| Parâmetro | Tipo | Descrição | Padrão |
|-----------|------|-----------|---------|
| `tipos_ativados` | List[str] | Tipos de arquivo a gerar | `["jpeg", "pdf", "docx", "xlsx", "txt"]` |
| `quantidade_por_tipo` | Dict[str, int] | Quantidade específica por tipo | `{}` |
| `tamanho_mb` | Dict[str, float] | Tamanho alvo em MB por tipo | Ver valores padrão abaixo |
| `config_especifica` | Dict[str, Dict] | Configurações específicas por tipo | Ver valores padrão abaixo |

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
- Linhas de texto aleatório
- Data de geração
- ID único do arquivo
- Codificação UTF-8

### PDF
- Múltiplas linhas de texto
- Formato padrão A4
- Texto posicionado verticalmente

### DOCX
- Múltiplos parágrafos
- Texto aleatório em cada parágrafo
- Formatação padrão do Word

### XLSX
- Planilha com 3 colunas
- Dados aleatórios (texto, números, decimais)
- Formato Excel padrão

### JPEG
- Imagem colorida aleatória
- Texto sobreposto
- Resolução ajustável

## 🧪 Exemplos Práticos

Execute `python exemplo_uso.py` para ver demonstrações completas de todas as funcionalidades.

## 📦 Dependências

- PIL (Pillow)
- reportlab
- python-docx
- pandas
- openpyxl

## 🔧 Instalação

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python geraArquivos.py
```

## 📊 Saída

O sistema exibe informações detalhadas sobre cada arquivo gerado:
```
[OK] Gerado: arquivos_teste/arquivo_1.txt (0.23 MB)
[OK] Gerado: arquivos_teste/arquivo_2.pdf (0.45 MB)
```

Arquivos são salvos na pasta `arquivos_teste/` por padrão.
