# 📋 Instruções de Execução - geraArquivos.py

Este documento contém as instruções completas para executar o sistema de geração de arquivos de teste.

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

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

#### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

#### Passo 3: Executar
```bash
python executar.py
```

## 🔧 Configuração Inicial (Primeira Vez)

### 1. Criar Ambiente Virtual
```bash
python -m venv venv
```

### 2. Ativar Ambiente Virtual
**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

## 📁 Estrutura de Arquivos

```
geraArquivos/
├── geraArquivos.py          # Script principal
├── executar.py              # Script de execução
├── ativar_ambiente.sh       # Script Linux/Mac
├── ativar_ambiente.bat      # Script Windows
├── requirements.txt         # Dependências
├── README.md               # Documentação
├── exemplo_uso.py          # Exemplos de uso
├── exemplo_faker.py        # Exemplos Faker
├── exemplo_lorem.py        # Exemplos Lorem Ipsum
├── venv/                   # Ambiente virtual
└── arquivos_teste/         # Pasta de saída
```

## 🎯 Tipos de Execução

### 1. Execução Padrão
```python
python executar.py
```
- Gera 10 arquivos aleatórios
- Exemplos de configuração específica
- Mostra estatísticas finais

### 2. Execução Personalizada
```python
python -c "
from geraArquivos import gerar_arquivos_por_tipo
gerar_arquivos_por_tipo({'txt': 2, 'pdf': 1}, {'txt': 0.5, 'pdf': 0.3})
"
```

### 3. Execução com Configuração Completa
```python
python -c "
from geraArquivos import ConfiguracaoArquivos, gerar_arquivos
config = ConfiguracaoArquivos(
    tipos_ativados=['txt', 'pdf', 'xlsx'],
    quantidade_por_tipo={'txt': 3, 'pdf': 2, 'xlsx': 1},
    tamanho_mb={'txt': 0.2, 'pdf': 0.4, 'xlsx': 0.3}
)
gerar_arquivos(config)
"
```

## 📊 Exemplos de Uso

### Gerar Apenas TXT
```python
from geraArquivos import gerar_arquivos_aleatorios
gerar_arquivos_aleatorios(5, ['txt'])
```

### Gerar Apenas XLSX com Dados Realistas
```python
from geraArquivos import gerar_arquivos_por_tipo
gerar_arquivos_por_tipo({'xlsx': 3}, {'xlsx': 0.5})
```

### Gerar Arquivos Grandes
```python
from geraArquivos import gerar_arquivos_por_tipo
gerar_arquivos_por_tipo(
    {'txt': 1, 'pdf': 1, 'docx': 1}, 
    {'txt': 2.0, 'pdf': 1.5, 'docx': 1.0}
)
```

## 🔍 Verificação de Funcionamento

### 1. Verificar Ambiente
```bash
python -c "import sys; print('Python:', sys.version)"
python -c "import geraArquivos; print('Módulo carregado com sucesso')"
```

### 2. Verificar Dependências
```bash
pip list | grep -E "(faker|lorem-text|pandas|openpyxl|reportlab|python-docx|Pillow)"
```

### 3. Teste Rápido
```bash
python -c "
from geraArquivos import gerar_arquivos_aleatorios
gerar_arquivos_aleatorios(1, ['txt'])
print('Teste concluído com sucesso!')
"
```

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### Erro: "Permission denied" (Linux/Mac)
```bash
chmod +x ativar_ambiente.sh
```

### Erro: "Virtual environment not activated"
```bash
# Verificar se o ambiente está ativo
echo $VIRTUAL_ENV  # Linux/Mac
echo %VIRTUAL_ENV%  # Windows
```

### Erro: "No space left on device"
```bash
# Limpar arquivos antigos
rm -rf arquivos_teste/*
```

## 📈 Monitoramento

### Verificar Arquivos Gerados
```bash
ls -la arquivos_teste/
du -sh arquivos_teste/
```

### Contar por Tipo
```bash
ls arquivos_teste/ | cut -d. -f2 | sort | uniq -c
```

### Verificar Tamanhos
```bash
ls -lh arquivos_teste/ | awk '{print $5, $9}'
```

## 🎛️ Configurações Avançadas

### Modificar Tamanhos Padrão
Edite o arquivo `geraArquivos.py` na classe `ConfiguracaoArquivos`:

```python
tamanho_mb = {
    "jpeg": 0.5,    # 500KB
    "pdf": 1.0,     # 1MB
    "docx": 0.8,    # 800KB
    "xlsx": 0.3,    # 300KB
    "txt": 0.1      # 100KB
}
```

### Modificar Tipos Ativados
```python
tipos_ativados = ["txt", "pdf", "docx", "xlsx", "jpeg"]
```

## 📞 Suporte

Se encontrar problemas:

1. Verifique se todas as dependências estão instaladas
2. Confirme que o ambiente virtual está ativo
3. Execute o teste rápido para verificar funcionamento
4. Consulte os logs de erro para mais detalhes

## 🎉 Conclusão

Após seguir estas instruções, você terá:
- ✅ Ambiente configurado e funcionando
- ✅ Arquivos de teste gerados na pasta `arquivos_teste/`
- ✅ Controle total sobre tipos e tamanhos de arquivo
- ✅ Dados realistas (Faker) e texto profissional (Lorem Ipsum)
