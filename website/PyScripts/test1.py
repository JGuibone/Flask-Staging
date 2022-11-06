from MainTextExtModule import PDFObject
from docx import Document
from pathlib import Path
from pptx import Presentation
import os

# document = Document(Path('website/PyScripts/testdoc1.docx'))
# docText = '\n\n'.join(
#     paragraph.text for paragraph in document.paragraphs
# )
# print(docText)


# def doc_to_text_catdoc(filename):
#     (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
#     fi.close()
#     retval = fo.read()
#     erroroutput = fe.read()
#     fo.close()
#     fe.close()
#     if not erroroutput:
#         return retval
#     else:
#         raise OSError("Executing the command caused an error: %s" % erroroutput)


def pptxToString(extLocation:str, fileobj: object):
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
        return outputFile.write(text)

text_runs = []


print(text_runs)

                
def PptxToText(extLocation:str, fileobj: object):
    FileName = Path(fileobj.filename).stem + '.txt'
    document = Document(Path('website/PyScripts/testdoc1.docx'))
    with Path(join(extLocation,secure_filename(FileName))).open(mode="w", encoding='utf-8') as outputFile:
        docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)
        docText = use_regex(docText)
        return outputFile.write(docText)

# import aspose.slides as slides

# # Instantiate a Presentation object that represents a PPTX file
# pres = slides.Presentation("PPTtoPPTX.ppt")

# # Saving the PPTX presentation to PPTX format
# pres.save("PPTtoPPTX_out.pptx", slides.export.SaveFormat.PPTX)

# similar doc_to_text_antiword()