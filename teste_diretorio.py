#!/usr/bin/env python3
"""
Script de teste para demonstrar a funcionalidade de diretório personalizado
"""

from geraArquivos import (
    ConfiguracaoArquivos, 
    gerar_arquivos, 
    gerar_arquivos_aleatorios,
    gerar_arquivos_por_quantidade
)

def testar_diretorio_personalizado():
    """Testa a funcionalidade de diretório personalizado"""
    
    print("🧪 Testando funcionalidade de diretório personalizado...")
    
    # Teste 1: Usando ConfiguracaoArquivos com diretório personalizado
    print("\n1️⃣ Teste com ConfiguracaoArquivos:")
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 2, "pdf": 1},
        diretorio_destino="teste_diretorio_1"
    )
    gerar_arquivos(config)
    
    # Teste 2: Usando função de conveniência
    print("\n2️⃣ Teste com função de conveniência:")
    gerar_arquivos_aleatorios(
        qtd=3, 
        tipos_ativados=["txt", "jpeg"], 
        diretorio_destino="teste_diretorio_2"
    )
    
    # Teste 3: Usando função por quantidade
    print("\n3️⃣ Teste com função por quantidade:")
    gerar_arquivos_por_quantidade(
        quantidade_total=4,
        tipos_ativados=["txt", "pdf", "docx"],
        diretorio_destino="teste_diretorio_3"
    )
    
    print("\n✅ Testes concluídos! Verifique os diretórios criados:")
    print("   - teste_diretorio_1/")
    print("   - teste_diretorio_2/")
    print("   - teste_diretorio_3/")

if __name__ == "__main__":
    testar_diretorio_personalizado()
