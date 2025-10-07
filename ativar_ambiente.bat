@echo off
REM Script para ativar o ambiente virtual e executar o geraArquivos.py no Windows

echo 🎯 ATIVAÇÃO DO AMBIENTE VIRTUAL E EXECUÇÃO DO GERAARQUIVOS.PY
echo ==============================================================

REM Verificar se estamos no diretório correto
if not exist "geraArquivos.py" (
    echo ❌ Erro: geraArquivos.py não encontrado no diretório atual
    echo 💡 Certifique-se de estar no diretório correto
    pause
    exit /b 1
)

REM Verificar se o ambiente virtual existe
if not exist "venv" (
    echo ❌ Erro: Ambiente virtual 'venv' não encontrado
    echo 💡 Execute: python -m venv venv
    pause
    exit /b 1
)

REM Ativar ambiente virtual
echo 🔧 Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Verificar se a ativação foi bem-sucedida
if "%VIRTUAL_ENV%"=="" (
    echo ❌ Falha ao ativar ambiente virtual
    pause
    exit /b 1
) else (
    echo ✅ Ambiente virtual ativado: %VIRTUAL_ENV%
)

REM Instalar dependências se necessário
echo 📦 Verificando dependências...
pip install -r requirements.txt

REM Executar o script principal
echo 🚀 Executando geraArquivos.py...
python geraArquivos.py

REM Desativar ambiente virtual
echo 🔚 Desativando ambiente virtual...
call venv\Scripts\deactivate.bat

echo ✅ Procedimento concluído!
pause
