#!/usr/bin/env python3
"""
Script de teste para funcionalidade de TAR
Testa diferentes tipos de compressão e opções
"""

import os
import sys
import shutil
from geraArquivos import gerar_e_empacotar, criar_arquivo_tar, gerar, ConfiguracaoArquivos, gerar_arquivos

def limpar_testes():
    """Remove diretórios de teste anteriores"""
    diretorios = [
        "teste_tar_sem_compressao",
        "teste_tar_gz",
        "teste_tar_bz2",
        "teste_tar_xz",
        "teste_tar_limpar"
    ]
    
    for dir in diretorios:
        if os.path.exists(dir):
            shutil.rmtree(dir)
            print(f"🗑️  Removido: {dir}")
    
    # Remover arquivos .tar* soltos
    for arquivo in os.listdir("."):
        if arquivo.endswith((".tar", ".tar.gz", ".tar.bz2", ".tar.xz")):
            os.remove(arquivo)
            print(f"🗑️  Removido: {arquivo}")

def teste_1_sem_compressao():
    """Teste 1: TAR sem compressão (default)"""
    print("\n" + "="*70)
    print("TESTE 1: TAR sem compressão (default)")
    print("="*70)
    
    try:
        gerar_e_empacotar(
            quantidade=5,
            template="minimal",
            diretorio="teste_tar_sem_compressao",
            compressao=None
        )
        print("✅ Teste 1 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 1 falhou: {e}")
        return False

def teste_2_compressao_gz():
    """Teste 2: TAR com compressão gzip"""
    print("\n" + "="*70)
    print("TESTE 2: TAR com compressão gzip (.tar.gz)")
    print("="*70)
    
    try:
        gerar_e_empacotar(
            quantidade=5,
            template="minimal",
            diretorio="teste_tar_gz",
            compressao="gz"
        )
        print("✅ Teste 2 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 2 falhou: {e}")
        return False

def teste_3_compressao_bz2():
    """Teste 3: TAR com compressão bzip2"""
    print("\n" + "="*70)
    print("TESTE 3: TAR com compressão bzip2 (.tar.bz2)")
    print("="*70)
    
    try:
        gerar_e_empacotar(
            quantidade=5,
            template="minimal",
            diretorio="teste_tar_bz2",
            compressao="bz2"
        )
        print("✅ Teste 3 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 3 falhou: {e}")
        return False

def teste_4_compressao_xz():
    """Teste 4: TAR com compressão xz"""
    print("\n" + "="*70)
    print("TESTE 4: TAR com compressão xz (.tar.xz)")
    print("="*70)
    
    try:
        gerar_e_empacotar(
            quantidade=5,
            template="minimal",
            diretorio="teste_tar_xz",
            compressao="xz"
        )
        print("✅ Teste 4 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 4 falhou: {e}")
        return False

def teste_5_limpar_originais():
    """Teste 5: TAR com remoção dos arquivos originais"""
    print("\n" + "="*70)
    print("TESTE 5: TAR com remoção dos arquivos originais")
    print("="*70)
    
    try:
        gerar_e_empacotar(
            quantidade=5,
            template="minimal",
            diretorio="teste_tar_limpar",
            compressao="gz",
            limpar_originais=True
        )
        
        # Verificar se o diretório foi removido
        if os.path.exists("teste_tar_limpar"):
            print("❌ Teste 5 falhou: Diretório não foi removido")
            return False
        
        print("✅ Teste 5 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 5 falhou: {e}")
        return False

def teste_6_config_manual():
    """Teste 6: TAR com configuração manual"""
    print("\n" + "="*70)
    print("TESTE 6: TAR com configuração manual (ConfiguracaoArquivos)")
    print("="*70)
    
    try:
        config = ConfiguracaoArquivos()
        config.tipos_ativados = ["txt", "pdf"]
        config.quantidade_por_tipo = {"txt": 3, "pdf": 2}
        config.diretorio_destino = "teste_tar_manual"
        config.criar_tar = True
        config.tar_compressao = "gz"
        config.tar_limpar_originais = False
        
        from geraArquivos import gerar_arquivos
        gerar_arquivos(config)
        
        print("✅ Teste 6 passou!")
        return True
    except Exception as e:
        print(f"❌ Teste 6 falhou: {e}")
        return False
    finally:
        # Limpar
        if os.path.exists("teste_tar_manual"):
            shutil.rmtree("teste_tar_manual")

def teste_7_hash_sha1():
    """Teste 7: Verificar nomes com hash SHA-1"""
    print("\n" + "="*70)
    print("TESTE 7: Verificar nomes dos arquivos tar usam hash SHA-1")
    print("="*70)
    
    try:
        # Gerar alguns arquivos e tar
        gerar_e_empacotar(
            quantidade=3,
            template="minimal",
            diretorio="teste_tar_hash",
            compressao="gz"
        )
        
        # Procurar arquivos .tar.gz na raiz
        arquivos_tar = [f for f in os.listdir(".") if f.endswith(".tar.gz")]
        
        if not arquivos_tar:
            print("❌ Teste 7 falhou: Nenhum arquivo .tar.gz encontrado")
            return False
        
        # Verificar se o nome é um hash SHA-1 (40 caracteres hexadecimais)
        tar_mais_recente = arquivos_tar[-1]
        nome_sem_extensao = tar_mais_recente.replace(".tar.gz", "")
        
        print(f"   📄 Arquivo tar gerado: {tar_mais_recente}")
        print(f"   🔑 Hash SHA-1: {nome_sem_extensao}")
        
        # Validar se é um hash SHA-1 válido (40 caracteres hex)
        if len(nome_sem_extensao) == 40 and all(c in "0123456789abcdef" for c in nome_sem_extensao):
            print("✅ Teste 7 passou! Nome usa hash SHA-1 válido")
            return True
        else:
            print(f"❌ Teste 7 falhou: Nome não é hash SHA-1 válido")
            return False
    except Exception as e:
        print(f"❌ Teste 7 falhou: {e}")
        return False
    finally:
        # Limpar
        if os.path.exists("teste_tar_hash"):
            shutil.rmtree("teste_tar_hash")

def executar_todos_testes():
    """Executa todos os testes"""
    print("\n" + "="*70)
    print("🧪 INICIANDO TESTES DE FUNCIONALIDADE TAR")
    print("="*70)
    
    # Limpar testes anteriores
    limpar_testes()
    
    # Executar testes
    testes = [
        teste_1_sem_compressao,
        teste_2_compressao_gz,
        teste_3_compressao_bz2,
        teste_4_compressao_xz,
        teste_5_limpar_originais,
        teste_6_config_manual,
        teste_7_hash_sha1
    ]
    
    resultados = []
    for teste in testes:
        resultado = teste()
        resultados.append(resultado)
    
    # Resumo
    print("\n" + "="*70)
    print("📊 RESUMO DOS TESTES")
    print("="*70)
    
    total = len(resultados)
    passou = sum(resultados)
    falhou = total - passou
    
    print(f"✅ Testes que passaram: {passou}/{total}")
    print(f"❌ Testes que falharam: {falhou}/{total}")
    
    if falhou == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        return 0
    else:
        print(f"\n⚠️  {falhou} teste(s) falharam")
        return 1

if __name__ == "__main__":
    sys.exit(executar_todos_testes())

