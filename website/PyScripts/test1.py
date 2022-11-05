from MainTextExtModule import PDFObject
from docx import Document
from pathlib import Path
import os

document = Document(Path('website/PyScripts/testdoc1.docx'))
docText = '\n\n'.join(
    paragraph.text for paragraph in document.paragraphs
)
print(docText)


def doc_to_text_catdoc(filename):
    (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
    fi.close()
    retval = fo.read()
    erroroutput = fe.read()
    fo.close()
    fe.close()
    if not erroroutput:
        return retval
    else:
        raise OSError("Executing the command caused an error: %s" % erroroutput)

# import aspose.slides as slides

# # Instantiate a Presentation object that represents a PPTX file
# pres = slides.Presentation("PPTtoPPTX.ppt")

# # Saving the PPTX presentation to PPTX format
# pres.save("PPTtoPPTX_out.pptx", slides.export.SaveFormat.PPTX)

# similar doc_to_text_antiword()