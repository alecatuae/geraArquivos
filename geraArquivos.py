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

# Gerar JPEG
def gerar_jpeg(nome):
    img = Image.new("RGB", (800, 600), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), texto_aleatorio(50), fill=(255,255,255))
    img.save(nome, "JPEG")

# Gerar PDF
def gerar_pdf(nome):
    c = canvas.Canvas(nome)
    for i in range(5):
        c.drawString(100, 800 - i*100, texto_aleatorio(80))
    c.save()

# Gerar DOCX
def gerar_docx(nome):
    doc = Document()
    for i in range(5):
        doc.add_paragraph(texto_aleatorio(120))
    doc.save(nome)

# Gerar XLSX
def gerar_xlsx(nome):
    df = pd.DataFrame({
        "Coluna1": [texto_aleatorio(10) for _ in range(20)],
        "Coluna2": [random.randint(1, 1000) for _ in range(20)],
        "Coluna3": [random.random() for _ in range(20)]
    })
    df.to_excel(nome, index=False)

# Gerar TXT
def gerar_txt(nome):
    with open(nome, 'w', encoding='utf-8') as arquivo:
        for i in range(10):  # 10 linhas de texto
            arquivo.write(f"Linha {i+1}: {texto_aleatorio(80)}\n")
        arquivo.write(f"\nData de geração: {random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2020, 2024)}\n")
        arquivo.write(f"ID do arquivo: {texto_aleatorio(16)}\n")

# Função principal
def gerar_arquivos(qtd=10):
    for i in range(qtd):
        tipo = random.choice(["jpeg", "pdf", "docx", "xlsx", "txt"])
        nome = os.path.join(OUTPUT_DIR, f"arquivo_{i+1}.{tipo}")
        if tipo == "jpeg":
            gerar_jpeg(nome)
        elif tipo == "pdf":
            gerar_pdf(nome)
        elif tipo == "docx":
            gerar_docx(nome)
        elif tipo == "xlsx":
            gerar_xlsx(nome)
        elif tipo == "txt":
            gerar_txt(nome)
        print(f"[OK] Gerado: {nome}")

if __name__ == "__main__":
    gerar_arquivos(20)  # quantidade de arquivos a gerar
