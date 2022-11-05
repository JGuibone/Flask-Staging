from os.path import join
from PyPDF2 import PdfFileReader
from pathlib import Path
from werkzeug.utils import secure_filename
from docx import Document
import re

def use_regex(input_text):
    text = re.sub("\s+", ",", input_text)
    return text

def PDFObject (extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    pdf = PdfFileReader(fileobj)
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        text = use_regex(text)
        return outputFile.write(text)

def DocxToText(extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    document = Document(Path('website/PyScripts/testdoc1.docx'))
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)
        docText = use_regex(docText)
        return outputFile.write(docText)

