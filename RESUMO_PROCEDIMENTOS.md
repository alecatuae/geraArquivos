# 📋 Resumo dos Procedimentos - geraArquivos.py

## 🎯 Visão Geral

O sistema `geraArquivos.py` é um gerador completo de arquivos de teste com funcionalidades avançadas:

- ✅ **5 tipos de arquivo**: TXT, PDF, DOCX, XLSX, JPEG
- ✅ **Dados realistas**: Faker para XLSX (português brasileiro)
- ✅ **Texto profissional**: Lorem Ipsum para TXT, PDF, DOCX
- ✅ **Controle de tamanho**: Baseado em MB para cada tipo
- ✅ **Parametrização completa**: Quantidade, tipos, tamanhos
- ✅ **Scripts automáticos**: Execução simplificada

## 🚀 Execução Imediata

### 1. Execução Mais Simples
```bash
# Linux/Mac
./ativar_ambiente.sh

# Windows
ativar_ambiente.bat
```

### 2. Execução Manual
```bash
# Ativar ambiente
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Executar
python executar.py
```

## 📁 Estrutura de Arquivos

```
geraArquivos/
├── 🐍 geraArquivos.py          # Script principal
├── 🚀 executar.py              # Script de execução
├── 🔧 configuracao.py          # Configurações pré-definidas
├── 📋 INSTRUCOES_EXECUCAO.md   # Instruções detalhadas
├── 📖 README.md               # Documentação principal
├── 🎭 exemplo_faker.py        # Exemplos Faker
├── 📝 exemplo_lorem.py        # Exemplos Lorem Ipsum
├── 📊 exemplo_uso.py          # Exemplos básicos
├── 🐧 ativar_ambiente.sh      # Script Linux/Mac
├── 🪟 ativar_ambiente.bat     # Script Windows
├── 📦 requirements.txt        # Dependências
├── 🗂️ venv/                   # Ambiente virtual
└── 📁 arquivos_teste/         # Pasta de saída
```

## ⚙️ Configurações Disponíveis

### Configurações Pré-definidas
```python
from configuracao import obter_configuracao

# Pequena - testes rápidos
config = obter_configuracao('pequena')

# Média - testes normais  
config = obter_configuracao('media')

# Grande - testes de performance
config = obter_configuracao('grande')

# Dados realistas - apenas XLSX
config = obter_configuracao('dados_realistas')

# Lorem Ipsum - apenas texto
config = obter_configuracao('lorem_ipsum')
```

### Configuração Personalizada
```python
from geraArquivos import ConfiguracaoArquivos

config = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "xlsx"],
    quantidade_por_tipo={"txt": 3, "pdf": 2, "xlsx": 1},
    tamanho_mb={"txt": 0.2, "pdf": 0.4, "xlsx": 0.3}
)
```

## 🎨 Tipos de Arquivo e Funcionalidades

### 📄 TXT
- **Conteúdo**: Lorem Ipsum profissional
- **Formato**: Cabeçalho, parágrafos numerados, rodapé
- **Controle**: Preciso por MB (~1 caractere = 1 byte)

### 📋 PDF
- **Conteúdo**: Lorem Ipsum com quebra de página
- **Formato**: A4, quebra de linha inteligente (80 chars)
- **Controle**: Redução de 30% devido ao overhead

### 📝 DOCX
- **Conteúdo**: Lorem Ipsum em parágrafos
- **Formato**: Título, seção de informações
- **Controle**: Redução de 50% devido ao XML

### 📊 XLSX
- **Conteúdo**: Dados realistas com Faker
- **Colunas**: 15 colunas (ID, Nome, Email, etc.)
- **Controle**: ~2000 linhas por MB

### 🖼️ JPEG
- **Conteúdo**: Imagem colorida com texto
- **Formato**: Resolução ajustável por tamanho
- **Controle**: Resolução baseada no tamanho alvo

## 🔧 Comandos Úteis

### Verificar Ambiente
```bash
python -c "import geraArquivos; print('✅ Módulo carregado')"
```

### Teste Rápido
```bash
python -c "
from geraArquivos import gerar_arquivos_aleatorios
gerar_arquivos_aleatorios(1, ['txt'])
print('✅ Teste concluído')
"
```

### Verificar Arquivos Gerados
```bash
ls -la arquivos_teste/
du -sh arquivos_teste/
```

### Contar por Tipo
```bash
ls arquivos_teste/ | cut -d. -f2 | sort | uniq -c
```

## 📊 Exemplos de Saída

### Execução Padrão
```
🎯 PROCEDIMENTO PARA EXECUTAR GERAARQUIVOS.PY
============================================================
🔍 Verificando ambiente...
✅ Ambiente virtual ativo

📦 Instalando dependências...
✅ Dependências instaladas com sucesso

🚀 Executando geraArquivos.py...
[OK] Gerado: arquivos_teste/arquivo_1.txt (0.10 MB)
[OK] Gerado: arquivos_teste/arquivo_2.pdf (0.16 MB)
[OK] Gerado: arquivos_teste/arquivo_3.xlsx (0.11 MB)

📈 Estatísticas dos arquivos gerados:
📁 Total de arquivos: 10
💾 Tamanho total: 1.25 MB

🎉 PROCEDIMENTO CONCLUÍDO COM SUCESSO!
```

## 🐛 Solução de Problemas

### Problema: "ModuleNotFoundError"
```bash
pip install -r requirements.txt --force-reinstall
```

### Problema: "Permission denied" (Linux/Mac)
```bash
chmod +x ativar_ambiente.sh
```

### Problema: "Virtual environment not activated"
```bash
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### Problema: "No space left on device"
```bash
rm -rf arquivos_teste/*
```

## 🎯 Casos de Uso

### 1. Testes de Desenvolvimento
```python
# Arquivos pequenos para testes rápidos
from configuracao import obter_configuracao
config = obter_configuracao('pequena')
```

### 2. Testes de Performance
```python
# Arquivos grandes para testes de carga
config = obter_configuracao('grande')
```

### 3. Demonstrações
```python
# Dados realistas para apresentações
config = obter_configuracao('dados_realistas')
```

### 4. Testes de Texto
```python
# Apenas documentos de texto
config = obter_configuracao('lorem_ipsum')
```

## 📈 Monitoramento

### Verificar Tamanhos
```bash
ls -lh arquivos_teste/ | awk '{print $5, $9}'
```

### Verificar Conteúdo
```bash
head -5 arquivos_teste/arquivo_1.txt
```

### Estatísticas Detalhadas
```bash
find arquivos_teste/ -name "*.txt" -exec wc -l {} + | tail -1
```

## 🎉 Conclusão

O sistema `geraArquivos.py` oferece:

- ✅ **Execução simplificada** com scripts automáticos
- ✅ **Configuração flexível** com opções pré-definidas
- ✅ **Dados realistas** para testes profissionais
- ✅ **Controle preciso** de tamanho e quantidade
- ✅ **Documentação completa** com exemplos práticos
- ✅ **Solução de problemas** integrada

**Para começar imediatamente:**
```bash
./ativar_ambiente.sh  # Linux/Mac
# ou
ativar_ambiente.bat   # Windows
```
