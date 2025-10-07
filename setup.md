# 🛠️ Setup do GeraArquivos - Guia de Instalação

## 📋 Pré-requisitos

### Sistema Operacional
- **Windows 10/11** (64-bit)
- **macOS 10.14+** (Mojave ou superior)
- **Linux** (Ubuntu 18.04+, CentOS 7+, Debian 9+)

### Python
- **Python 3.8+** (recomendado: Python 3.9 ou 3.10)
- **pip** (gerenciador de pacotes Python)

## 🔍 Verificação Inicial

### 1. Verificar se Python está instalado
```bash
# No terminal/prompt de comando:
python --version
# ou
python3 --version
```

**Saída esperada:**
```
Python 3.9.7
# ou versão 3.8+
```

### 2. Verificar se pip está instalado
```bash
pip --version
# ou
pip3 --version
```

**Saída esperada:**
```
pip 21.2.4 from /usr/lib/python3.9/site-packages/pip (python 3.9)
```

## 📦 Instalação do Python (se necessário)

### Windows

#### Opção 1: Download Oficial (Recomendado)
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente (3.9+)
3. **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação
4. Execute o instalador como administrador

#### Opção 2: Microsoft Store
1. Abra a Microsoft Store
2. Procure por "Python 3.9" ou "Python 3.10"
3. Instale a versão oficial

### macOS

#### Opção 1: Homebrew (Recomendado)
```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python@3.9
```

#### Opção 2: Download Oficial
1. Acesse: https://www.python.org/downloads/macos/
2. Baixe o instalador para sua versão do macOS
3. Execute o instalador

### Linux (Ubuntu/Debian)

```bash
# Atualizar sistema
sudo apt update

# Instalar Python e pip
sudo apt install python3 python3-pip python3-venv

# Verificar instalação
python3 --version
pip3 --version
```

### Linux (CentOS/RHEL)

```bash
# Instalar Python e pip
sudo yum install python3 python3-pip

# ou para versões mais novas
sudo dnf install python3 python3-pip

# Verificar instalação
python3 --version
pip3 --version
```

## 🚀 Setup do Projeto GeraArquivos

### 1. Baixar/Clonar o Projeto

#### Opção A: Download ZIP
1. Baixe o projeto como ZIP
2. Extraia em uma pasta (ex: `C:\Users\SeuNome\geraArquivos`)

#### Opção B: Git Clone (se tiver Git)
```bash
git clone <url-do-repositorio>
cd geraArquivos
```

### 2. Navegar para o Diretório do Projeto

```bash
# Windows
cd C:\caminho\para\geraArquivos

# macOS/Linux
cd /caminho/para/geraArquivos
```

### 3. Criar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv
# ou
python3 -m venv venv
```

**Saída esperada:**
```
# Deve criar uma pasta 'venv' no diretório
```

### 4. Ativar Ambiente Virtual

#### Windows (Command Prompt)
```cmd
venv\Scripts\activate
```

#### Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```

#### macOS/Linux
```bash
source venv/bin/activate
```

**Saída esperada:**
```
(venv) C:\caminho\para\geraArquivos>
# ou
(venv) usuario@computador:~/geraArquivos$
```

### 5. Atualizar pip (Recomendado)

```bash
python -m pip install --upgrade pip
```

**Saída esperada:**
```
Requirement already satisfied: pip in venv\lib\site-packages (21.2.4)
```

### 6. Instalar Dependências

```bash
pip install -r requirements.txt
```

**Saída esperada:**
```
Collecting Pillow>=10.0.0
  Downloading Pillow-10.0.0-cp39-cp39-win_amd64.whl (2.3 MB)
     |████████████████████████████████| 2.3 MB 1.2 MB/s
Collecting reportlab>=4.0.0
  Downloading reportlab-4.0.0-py3-none-any.whs (1.2 MB)
     |████████████████████████████████| 1.2 MB 1.5 MB/s
...
Successfully installed Pillow-10.0.0 reportlab-4.0.0 python-docx-0.8.11 pandas-2.0.0 openpyxl-3.1.0 faker-37.0.0 lorem-text-3.0.0 wordcloud-1.9.0 matplotlib-3.5.0 numpy-1.21.0
```

### 7. Verificar Instalação

```bash
python -c "from geraArquivos import gerar; print('✅ Instalação bem-sucedida!')"
```

**Saída esperada:**
```
✅ Instalação bem-sucedida!
```

## 🧪 Teste de Funcionamento

### Teste Básico
```bash
python -c "from geraArquivos import gerar; gerar(3)"
```

**Saída esperada:**
```
📊 Distribuição por percentual:
   JPEG: 0 arquivos (0.0%)
   PNG: 0 arquivos (0.0%)
   PDF: 3 arquivos (100.0%)
   DOCX: 0 arquivos (0.0%)
   XLSX: 0 arquivos (0.0%)
   TXT: 0 arquivos (0.0%)

[OK] Gerado: arquivos_teste/a1b2c3d4e5f6789012345678901234567890abcd.pdf (0.52 MB)
[OK] Gerado: arquivos_teste/f9e8d7c6b5a4938271605948372615049382716.pdf (0.52 MB)
[OK] Gerado: arquivos_teste/... (mais 1 arquivo)

✅ Total de arquivos gerados: 3
```

## 🔧 Scripts de Ativação Automática

### Windows (ativar_ambiente.bat)
```batch
@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate
echo Ambiente ativado! Executando geraArquivos.py...
python geraArquivos.py
pause
```

### macOS/Linux (ativar_ambiente.sh)
```bash
#!/bin/bash
echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "Ambiente ativado! Executando geraArquivos.py..."
python geraArquivos.py
```

**Para usar os scripts:**
```bash
# Windows
ativar_ambiente.bat

# macOS/Linux
chmod +x ativar_ambiente.sh
./ativar_ambiente.sh
```

## 🚨 Solução de Problemas

### Problema: "python não é reconhecido"
**Solução:**
1. Reinstale Python marcando "Add Python to PATH"
2. Reinicie o terminal
3. Teste: `python --version`

### Problema: "pip não é reconhecido"
**Solução:**
```bash
# Instalar pip manualmente
python -m ensurepip --upgrade
```

### Problema: "Erro de permissão no Windows"
**Solução:**
1. Execute o terminal como administrador
2. Ou use PowerShell com: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Problema: "Erro ao instalar dependências"
**Solução:**
```bash
# Atualizar pip primeiro
python -m pip install --upgrade pip

# Instalar dependências uma por uma
pip install Pillow
pip install reportlab
pip install python-docx
pip install pandas
pip install openpyxl
pip install faker
pip install lorem-text
pip install wordcloud
pip install matplotlib
pip install numpy
```

### Problema: "Erro de compilação no Linux"
**Solução:**
```bash
# Ubuntu/Debian
sudo apt install python3-dev build-essential

# CentOS/RHEL
sudo yum install python3-devel gcc
```

### Problema: "Erro de matplotlib no macOS"
**Solução:**
```bash
# Instalar dependências do sistema
brew install pkg-config freetype
pip install --upgrade matplotlib
```

## 📋 Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] pip funcionando
- [ ] Projeto baixado/clonado
- [ ] Ambiente virtual criado
- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Teste básico funcionando
- [ ] Scripts de ativação funcionando

## 🎯 Próximos Passos

Após completar o setup:

1. **Leia o [README.md](README.md)** - Visão geral do projeto
2. **Siga o [howto.md](howto.md)** - Guia de uso prático
3. **Teste com poucos arquivos** - Comece com `gerar(5)`
4. **Explore os templates** - Teste diferentes distribuições

## 🆘 Precisa de Ajuda?

### Recursos Úteis
- **Documentação Python**: https://docs.python.org/
- **Tutorial pip**: https://pip.pypa.io/en/stable/user_guide/
- **Ambientes virtuais**: https://docs.python.org/3/tutorial/venv.html

### Comandos de Diagnóstico
```bash
# Verificar Python
python --version

# Verificar pip
pip --version

# Verificar ambiente virtual
echo $VIRTUAL_ENV  # macOS/Linux
echo %VIRTUAL_ENV%  # Windows

# Listar pacotes instalados
pip list

# Verificar dependências específicas
python -c "import PIL; print('Pillow OK')"
python -c "import reportlab; print('ReportLab OK')"
python -c "import pandas; print('Pandas OK')"
```

---

**🎉 Setup completo! Agora você pode usar o GeraArquivos!**
