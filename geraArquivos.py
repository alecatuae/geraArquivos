import os
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from docx import Document
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional

# Pasta onde salvar os arquivos
OUTPUT_DIR = "arquivos_teste"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@dataclass
class ConfiguracaoArquivos:
    """Configuração para geração de arquivos"""
    # Tipos de arquivo ativados
    tipos_ativados: List[str] = None
    
    # Quantidade de arquivos por tipo (None = aleatório)
    quantidade_por_tipo: Dict[str, int] = None
    
    # Tamanho alvo em MB para cada tipo
    tamanho_mb: Dict[str, float] = None
    
    # Configurações específicas por tipo
    config_especifica: Dict[str, Dict] = None
    
    def __post_init__(self):
        if self.tipos_ativados is None:
            self.tipos_ativados = ["jpeg", "pdf", "docx", "xlsx", "txt"]
        
        if self.quantidade_por_tipo is None:
            self.quantidade_por_tipo = {}
        
        if self.tamanho_mb is None:
            self.tamanho_mb = {
                "jpeg": 0.5,    # 500KB
                "pdf": 1.0,     # 1MB
                "docx": 0.8,    # 800KB
                "xlsx": 0.3,    # 300KB
                "txt": 0.1      # 100KB
            }
        
        if self.config_especifica is None:
            self.config_especifica = {
                "jpeg": {"linhas_texto": 50, "resolucao": (800, 600)},
                "pdf": {"linhas": 5, "caracteres_por_linha": 80},
                "docx": {"paragrafos": 5, "caracteres_por_paragrafo": 120},
                "xlsx": {"linhas": 20, "colunas": 3},
                "txt": {"linhas": 10, "caracteres_por_linha": 80}
            }

# Função para gerar texto aleatório
def texto_aleatorio(tamanho=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

# Funções auxiliares para controle de tamanho
def calcular_tamanho_arquivo(caminho_arquivo):
    """Calcula o tamanho do arquivo em MB"""
    return os.path.getsize(caminho_arquivo) / (1024 * 1024)

def ajustar_conteudo_para_tamanho(tipo_arquivo, tamanho_mb_alvo, config):
    """Ajusta o conteúdo baseado no tamanho alvo"""
    if tipo_arquivo == "txt":
        # Para TXT: ~1 caractere = 1 byte, então 1MB = ~1M caracteres
        caracteres_por_linha = config["caracteres_por_linha"]
        linhas_necessarias = int((tamanho_mb_alvo * 1024 * 1024) / caracteres_por_linha)
        return max(linhas_necessarias, 1)
    
    elif tipo_arquivo == "pdf":
        # Para PDF: estimativa baseada em linhas
        linhas_necessarias = int(tamanho_mb_alvo * 50)  # Aproximação
        return max(linhas_necessarias, 1)
    
    elif tipo_arquivo == "docx":
        # Para DOCX: estimativa baseada em parágrafos
        paragrafos_necessarios = int(tamanho_mb_alvo * 30)  # Aproximação
        return max(paragrafos_necessarios, 1)
    
    elif tipo_arquivo == "xlsx":
        # Para XLSX: estimativa baseada em linhas
        linhas_necessarias = int(tamanho_mb_alvo * 200)  # Aproximação
        return max(linhas_necessarias, 1)
    
    elif tipo_arquivo == "jpeg":
        # Para JPEG: ajustar resolução baseada no tamanho
        if tamanho_mb_alvo <= 0.1:
            return (400, 300)
        elif tamanho_mb_alvo <= 0.5:
            return (800, 600)
        elif tamanho_mb_alvo <= 1.0:
            return (1200, 900)
        else:
            return (1600, 1200)
    
    return config

# Gerar JPEG
def gerar_jpeg(nome, config, tamanho_mb_alvo=None):
    resolucao = config["resolucao"]
    if tamanho_mb_alvo:
        resolucao = ajustar_conteudo_para_tamanho("jpeg", tamanho_mb_alvo, config)
    
    img = Image.new("RGB", resolucao, color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), texto_aleatorio(config["linhas_texto"]), fill=(255,255,255))
    img.save(nome, "JPEG")

# Gerar PDF
def gerar_pdf(nome, config, tamanho_mb_alvo=None):
    linhas = config["linhas"]
    if tamanho_mb_alvo:
        linhas = ajustar_conteudo_para_tamanho("pdf", tamanho_mb_alvo, config)
    
    c = canvas.Canvas(nome)
    for i in range(linhas):
        c.drawString(100, 800 - i*100, texto_aleatorio(config["caracteres_por_linha"]))
    c.save()

# Gerar DOCX
def gerar_docx(nome, config, tamanho_mb_alvo=None):
    paragrafos = config["paragrafos"]
    if tamanho_mb_alvo:
        paragrafos = ajustar_conteudo_para_tamanho("docx", tamanho_mb_alvo, config)
    
    doc = Document()
    for i in range(paragrafos):
        doc.add_paragraph(texto_aleatorio(config["caracteres_por_paragrafo"]))
    doc.save(nome)

# Gerar XLSX
def gerar_xlsx(nome, config, tamanho_mb_alvo=None):
    linhas = config["linhas"]
    if tamanho_mb_alvo:
        linhas = ajustar_conteudo_para_tamanho("xlsx", tamanho_mb_alvo, config)
    
    df = pd.DataFrame({
        "Coluna1": [texto_aleatorio(10) for _ in range(linhas)],
        "Coluna2": [random.randint(1, 1000) for _ in range(linhas)],
        "Coluna3": [random.random() for _ in range(linhas)]
    })
    df.to_excel(nome, index=False)

# Gerar TXT
def gerar_txt(nome, config, tamanho_mb_alvo=None):
    linhas = config["linhas"]
    if tamanho_mb_alvo:
        linhas = ajustar_conteudo_para_tamanho("txt", tamanho_mb_alvo, config)
    
    with open(nome, 'w', encoding='utf-8') as arquivo:
        for i in range(linhas):
            arquivo.write(f"Linha {i+1}: {texto_aleatorio(config['caracteres_por_linha'])}\n")
        arquivo.write(f"\nData de geração: {random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2020, 2024)}\n")
        arquivo.write(f"ID do arquivo: {texto_aleatorio(16)}\n")

# Função principal
def gerar_arquivos(config: ConfiguracaoArquivos = None, qtd_total=None):
    """
    Gera arquivos baseado na configuração fornecida
    
    Args:
        config: ConfiguracaoArquivos com parâmetros de geração
        qtd_total: Quantidade total de arquivos (ignora quantidade_por_tipo se especificado)
    """
    if config is None:
        config = ConfiguracaoArquivos()
    
    # Determinar quantos arquivos gerar de cada tipo
    arquivos_para_gerar = {}
    
    if qtd_total is not None:
        # Modo aleatório: distribuir qtd_total entre tipos ativados
        for i in range(qtd_total):
            tipo = random.choice(config.tipos_ativados)
            arquivos_para_gerar[tipo] = arquivos_para_gerar.get(tipo, 0) + 1
    else:
        # Modo controlado: usar quantidade_por_tipo
        for tipo in config.tipos_ativados:
            if tipo in config.quantidade_por_tipo:
                arquivos_para_gerar[tipo] = config.quantidade_por_tipo[tipo]
            else:
                # Se não especificado, gerar 1 arquivo do tipo
                arquivos_para_gerar[tipo] = 1
    
    # Gerar os arquivos
    contador_global = 1
    for tipo, quantidade in arquivos_para_gerar.items():
        for i in range(quantidade):
            nome = os.path.join(OUTPUT_DIR, f"arquivo_{contador_global}.{tipo}")
            tamanho_alvo = config.tamanho_mb.get(tipo, 0.5)
            config_tipo = config.config_especifica.get(tipo, {})
            
            try:
                if tipo == "jpeg":
                    gerar_jpeg(nome, config_tipo, tamanho_alvo)
                elif tipo == "pdf":
                    gerar_pdf(nome, config_tipo, tamanho_alvo)
                elif tipo == "docx":
                    gerar_docx(nome, config_tipo, tamanho_alvo)
                elif tipo == "xlsx":
                    gerar_xlsx(nome, config_tipo, tamanho_alvo)
                elif tipo == "txt":
                    gerar_txt(nome, config_tipo, tamanho_alvo)
                
                tamanho_real = calcular_tamanho_arquivo(nome)
                print(f"[OK] Gerado: {nome} ({tamanho_real:.2f} MB)")
                contador_global += 1
                
            except Exception as e:
                print(f"[ERRO] Falha ao gerar {nome}: {e}")

# Funções de conveniência para configurações comuns
def gerar_arquivos_aleatorios(qtd=20, tipos_ativados=None):
    """Gera arquivos aleatoriamente"""
    config = ConfiguracaoArquivos()
    if tipos_ativados:
        config.tipos_ativados = tipos_ativados
    gerar_arquivos(config, qtd)

def gerar_arquivos_por_tipo(quantidade_por_tipo, tamanhos_mb=None):
    """Gera arquivos com quantidade específica por tipo"""
    config = ConfiguracaoArquivos()
    config.quantidade_por_tipo = quantidade_por_tipo
    if tamanhos_mb:
        config.tamanho_mb.update(tamanhos_mb)
    gerar_arquivos(config)

if __name__ == "__main__":
    # Exemplo de uso com configuração personalizada
    print("=== Gerando arquivos com configuração personalizada ===")
    
    # Configuração 1: Apenas TXT e PDF, tamanhos específicos
    config1 = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 3, "pdf": 2},
        tamanho_mb={"txt": 0.2, "pdf": 0.5}
    )
    gerar_arquivos(config1)
    
    print("\n=== Gerando arquivos aleatoriamente ===")
    # Configuração 2: Modo aleatório
    gerar_arquivos_aleatorios(10, ["jpeg", "xlsx", "txt"])
