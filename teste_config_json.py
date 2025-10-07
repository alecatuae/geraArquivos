#!/usr/bin/env python3
"""
Script de teste para demonstrar o novo sistema de configuração via config.json
"""

from geraArquivos import (
    ConfiguracaoArquivos, 
    gerar_arquivos, 
    gerar_arquivos_aleatorios,
    carregar_configuracao
)

def testar_sistema_config_json():
    """Testa o novo sistema de configuração via config.json"""
    
    print("🧪 Testando sistema de configuração via config.json...")
    
    # Teste 1: Verificar carregamento do config.json
    print("\n1️⃣ Teste de carregamento do config.json:")
    config_carregada = carregar_configuracao()
    if config_carregada:
        print("✅ Config.json carregado com sucesso!")
        print(f"   - Diretório padrão: {config_carregada.get('configuracao_global', {}).get('diretorio_padrao', 'N/A')}")
        print(f"   - Locale Faker: {config_carregada.get('configuracao_global', {}).get('locale_faker', 'N/A')}")
        print(f"   - Tipos padrão: {config_carregada.get('tipos_arquivo_padrao', [])}")
    else:
        print("⚠️  Config.json não encontrado, usando configurações padrão")
    
    # Teste 2: Usando ConfiguracaoArquivos com config.json
    print("\n2️⃣ Teste com ConfiguracaoArquivos (carrega do config.json):")
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 2, "pdf": 1},
        diretorio_destino="teste_config_json_1"
    )
    gerar_arquivos(config)
    
    # Teste 3: Função de conveniência com diretório personalizado
    print("\n3️⃣ Teste com função de conveniência:")
    gerar_arquivos_aleatorios(
        qtd=3, 
        tipos_ativados=["txt", "jpeg"], 
        diretorio_destino="teste_config_json_2"
    )
    
    # Teste 4: Verificar se as configurações do JSON foram aplicadas
    print("\n4️⃣ Verificando configurações aplicadas:")
    print(f"   - Tipos ativados padrão: {config.tipos_ativados}")
    print(f"   - Tamanhos MB padrão: {config.tamanho_mb}")
    print(f"   - Configurações específicas: {list(config.config_especifica.keys())}")
    
    print("\n✅ Testes concluídos! Verifique os diretórios criados:")
    print("   - teste_config_json_1/")
    print("   - teste_config_json_2/")

if __name__ == "__main__":
    testar_sistema_config_json()
