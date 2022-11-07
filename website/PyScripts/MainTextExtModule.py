from os.path import join
from PyPDF2 import PdfFileReader
from pathlib import Path
from werkzeug.utils import secure_filename
from docx import Document
from pptx import Presentation
import re

def use_regex(input_text):
    text = re.sub("[^\x00-\x7F]+","", input_text)
    text = re.sub("\W+", ",", text)
    return text
    
def PdfToText (extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    pdf = PdfFileReader(fileobj)
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        # text = use_regex(text)
        return outputFile.write(text)

def DocxToText(extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    document = Document(fileobj)
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        docText = '\n\n'.join(paragraph.text + "," for paragraph in document.paragraphs)
        # docText = use_regex(docText)
        return outputFile.write(docText)

def pptxToTxt(extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    prs = Presentation(fileobj)
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        text = ''
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        text += run.text + " "
        text = use_regex(text)
        return outputFile.write(text)
