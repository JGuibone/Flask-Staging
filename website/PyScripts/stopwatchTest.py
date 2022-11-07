# print(stopwords.words('english'))
DIC_LOCATION = "website/static/wordDic/wordninja_words.txt"



import wordninja
import time
import re
from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyPDF2 import PdfFileReader
from werkzeug.utils import secure_filename
from os.path import join

START_TIME = time.time()

def PdfToText (fileobj: str):
    pdf = PdfFileReader(fileobj)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return use_regex(text)

def use_regex(input_text):
    text = re.sub("[^\x00-\x7F]+","", input_text)
    text = re.sub("\W+", " ", text)
    return text
  
stop_words = set(stopwords.words('english'))

slicedwords = wordninja.split(PdfToText("website/uploads/2_textProc.pdf"))

filtered_sentence = [w.lower() for w in slicedwords if not w.lower() in stop_words]



lenUnclean = len(filtered_sentence)

filtered_sentence = list(set(filtered_sentence))

lenClean = len(filtered_sentence)

ENDTIME = time.time() - START_TIME
print(filtered_sentence)
print(f"{lenUnclean} {lenClean}, {ENDTIME}")

# def localTokenizer(preCleaned:list):
#     for word in preCleaned:

#         return 1
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
# def testFunc ():
#     return 1
# cleaned = ' '.join(wordninja.split(PdfToText("website/uploads/2_TextProc.pdf")))
# filtered_sentence = [w for w in cleaned if not w.lower() in stop_words]
# print(word_tokenize(PdfToText("website/uploads/2_TextProc.pdf")))
  
# print(cleaned)
# print(filtered_sentence)