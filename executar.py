#!/usr/bin/env python3
"""
Script principal para executar o geraArquivos.py
Procedimento completo para gerar arquivos de teste
"""

import os
import sys
import subprocess
from pathlib import Path

def verificar_ambiente():
    """Verifica se o ambiente virtual está ativo e as dependências estão instaladas"""
    print("🔍 Verificando ambiente...")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("geraArquivos.py"):
        print("❌ Erro: geraArquivos.py não encontrado no diretório atual")
        return False
    
    # Verificar se o ambiente virtual existe
    if not os.path.exists("venv"):
        print("❌ Erro: Ambiente virtual 'venv' não encontrado")
        print("💡 Execute: python -m venv venv")
        return False
    
    # Verificar se o ambiente virtual está ativo
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Aviso: Ambiente virtual não está ativo")
        print("💡 Execute: source venv/bin/activate (Linux/Mac) ou venv\\Scripts\\activate (Windows)")
        return False
    
    print("✅ Ambiente virtual ativo")
    return True

def instalar_dependencias():
    """Instala as dependências necessárias"""
    print("\n📦 Instalando dependências...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        print(f"Saída: {e.stdout}")
        print(f"Erro: {e.stderr}")
        return False

def criar_pasta_saida():
    """Cria a pasta de saída se não existir"""
    print("\n📁 Verificando pasta de saída...")
    
    pasta_saida = "arquivos_teste"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"✅ Pasta '{pasta_saida}' criada")
    else:
        print(f"✅ Pasta '{pasta_saida}' já existe")
    
    return True

def executar_gera_arquivos():
    """Executa o geraArquivos.py"""
    print("\n🚀 Executando geraArquivos.py...")
    
    try:
        # Importar e executar o módulo
        from geraArquivos import gerar_arquivos_aleatorios, gerar_arquivos_por_tipo, ConfiguracaoArquivos
        
        print("=" * 60)
        print("GERADOR DE ARQUIVOS DE TESTE")
        print("=" * 60)
        
        # Exemplo 1: Geração aleatória
        print("\n📄 Exemplo 1: Geração aleatória (10 arquivos)")
        gerar_arquivos_aleatorios(10)
        
        # Exemplo 2: Geração específica por tipo
        print("\n📊 Exemplo 2: Geração específica por tipo")
        gerar_arquivos_por_tipo(
            quantidade_por_tipo={"txt": 2, "pdf": 1, "docx": 1, "xlsx": 1, "jpeg": 1},
            tamanhos_mb={"txt": 0.2, "pdf": 0.3, "docx": 0.4, "xlsx": 0.1, "jpeg": 0.5}
        )
        
        # Exemplo 3: Configuração personalizada
        print("\n⚙️  Exemplo 3: Configuração personalizada")
        config = ConfiguracaoArquivos(
            tipos_ativados=["txt", "pdf", "xlsx"],
            quantidade_por_tipo={"txt": 3, "pdf": 2, "xlsx": 2},
            tamanho_mb={"txt": 0.15, "pdf": 0.25, "xlsx": 0.3}
        )
        from geraArquivos import gerar_arquivos
        gerar_arquivos(config)
        
        print("\n" + "=" * 60)
        print("✅ GERAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao executar geraArquivos.py: {e}")
        return False

def mostrar_estatisticas():
    """Mostra estatísticas dos arquivos gerados"""
    print("\n📈 Estatísticas dos arquivos gerados:")
    
    pasta_saida = "arquivos_teste"
    if not os.path.exists(pasta_saida):
        print("❌ Pasta de saída não encontrada")
        return
    
    arquivos = os.listdir(pasta_saida)
    if not arquivos:
        print("❌ Nenhum arquivo encontrado")
        return
    
    # Contar por tipo
    tipos = {}
    tamanho_total = 0
    
    for arquivo in arquivos:
        caminho = os.path.join(pasta_saida, arquivo)
        if os.path.isfile(caminho):
            extensao = arquivo.split('.')[-1].lower()
            tamanho = os.path.getsize(caminho) / (1024 * 1024)  # MB
            
            if extensao not in tipos:
                tipos[extensao] = {"quantidade": 0, "tamanho": 0}
            
            tipos[extensao]["quantidade"] += 1
            tipos[extensao]["tamanho"] += tamanho
            tamanho_total += tamanho
    
    print(f"📁 Total de arquivos: {len(arquivos)}")
    print(f"💾 Tamanho total: {tamanho_total:.2f} MB")
    print("\n📊 Por tipo:")
    
    for tipo, dados in sorted(tipos.items()):
        print(f"  {tipo.upper()}: {dados['quantidade']} arquivos ({dados['tamanho']:.2f} MB)")

def main():
    """Função principal"""
    print("🎯 PROCEDIMENTO PARA EXECUTAR GERAARQUIVOS.PY")
    print("=" * 60)
    
    # Passo 1: Verificar ambiente
    if not verificar_ambiente():
        print("\n❌ Falha na verificação do ambiente")
        return False
    
    # Passo 2: Instalar dependências
    if not instalar_dependencias():
        print("\n❌ Falha na instalação das dependências")
        return False
    
    # Passo 3: Criar pasta de saída
    if not criar_pasta_saida():
        print("\n❌ Falha na criação da pasta de saída")
        return False
    
    # Passo 4: Executar geraArquivos.py
    if not executar_gera_arquivos():
        print("\n❌ Falha na execução do geraArquivos.py")
        return False
    
    # Passo 5: Mostrar estatísticas
    mostrar_estatisticas()
    
    print("\n🎉 PROCEDIMENTO CONCLUÍDO COM SUCESSO!")
    print("📁 Verifique a pasta 'arquivos_teste' para ver os arquivos gerados")
    
    return True

if __name__ == "__main__":
    try:
        sucesso = main()
        sys.exit(0 if sucesso else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Execução interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
