from docx import Document

document = Document('Anais/anais_6.docx')
paras_text = []

for para in document.paragraphs:
    para_text = para.text.strip()
    if para_text:
        paras_text.append(para_text)

for para in paras_text[:500]:
    print(para)
    print()

