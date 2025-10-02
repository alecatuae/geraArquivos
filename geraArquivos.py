import os
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from docx import Document
import pandas as pd

# Pasta onde salvar os arquivos
OUTPUT_DIR = "arquivos_teste"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

# Função principal
def gerar_arquivos(qtd=10):
    for i in range(qtd):
        tipo = random.choice(["jpeg", "pdf", "docx", "xlsx"])
        nome = os.path.join(OUTPUT_DIR, f"arquivo_{i+1}.{tipo}")
        if tipo == "jpeg":
            gerar_jpeg(nome)
        elif tipo == "pdf":
            gerar_pdf(nome)
        elif tipo == "docx":
            gerar_docx(nome)
        elif tipo == "xlsx":
            gerar_xlsx(nome)
        print(f"[OK] Gerado: {nome}")

if __name__ == "__main__":
    gerar_arquivos(20)  # quantidade de arquivos a gerar
