import random

def bilinmeyen():
     cevap = ['üzgünüm anlayamadım, başka şekilde söyleyebilir misin?',
              '...',
              'Bu ne demek?',
              'gerçekten anlaşılması zor birisin',
              '-_-',
              'Ne diyon ya!',
              'Sen ilkokul terksin herhalde.'][random.randrange(7)]
     return cevap

def tavsiye():
    tavsiye = ['Bizim köyde de öyle bir çocuk vardı öldü sonra, yapma.',
               'Bi daha mı geleceksin dünyaya yap gitsin',
               'Bak bence sen bunları çok düşünüyorsun, en iyisi bırak.',
               'Ben bi botum nereden bileyim?'][random.randrange(4)]
    return tavsiye

