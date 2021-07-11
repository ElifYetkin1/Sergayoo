import re
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import uzun_cevaplar as uzun

def konuş(yazı):
    language = 'tr'
    filename ="ses.mp3"
    output = gTTS(text=yazı, lang = language,slow=False)
    output.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# def dinle():
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print('Lütfen konuşun.')
#
#         ses = r.listen(source)
#         try:
#             print('Sen :'+ r.recognize_google(ses))
#
#         except Exception as e :
#             print('What dedin gülüm'+ str(e))
# konuş('merhaba')

def mesaj_olasılığı(kullanıcı_mesajı, tanınan_kelimeler, tek_cevap=False, gerekli_kelimeler=[]):
    mesaj_kesinliği = 0
    gerekli_kelime_içeren = True

    for kelime in kullanıcı_mesajı:
        if kelime in tanınan_kelimeler:
            mesaj_kesinliği += 1
    #mesajdaki tanınan kelime yüzdesine bakıyor.
    yüzde = float(mesaj_kesinliği)/ float(len(tanınan_kelimeler))

    for kelime in gerekli_kelimeler:
        if kelime not in kullanıcı_mesajı:
            gerekli_kelime_içeren = False
            break

    if gerekli_kelime_içeren or tek_cevap:
        return (yüzde*100)
    else:
        return 0

def tüm_mesajları_kontrol_et(mesaj):
    en_yüksek_ol_listesi = {}

    def cevap(bot_cevabı,kelime_listesi, tek_cevap = False,gerekli_kelimeler=[]):
        nonlocal en_yüksek_ol_listesi
        en_yüksek_ol_listesi[bot_cevabı]= mesaj_olasılığı(mesaj,kelime_listesi, tek_cevap, gerekli_kelimeler,)

#cevaplar-----------------------------------------------------------------------------------------------------

    cevap('Merhaba!', ['merhaba', 'selam'], tek_cevap=True)
    cevap('İyi sayılırım, sen ?', ['nasılsın','iyi','misin','nasıl','gidiyor','naber'], gerekli_kelimeler=['iyi','misin'or 'nasılsın'] )
    cevap(' İyi valla nolsun', ['naber'], tek_cevap=True)
    cevap('Teşekkürler', ['seni','seviyorum',], gerekli_kelimeler=['seni','seviyorum'])
    cevap('Seni benden başka...', ['soru', 'sor', ], gerekli_kelimeler=['soru', 'sor'])
    cevap('Hayır istemem', ['ister','misin'], gerekli_kelimeler=['ister','misin'])
    cevap('Çünkü öyle.', ['neden','ne için','niye','niçin'], tek_cevap=True)
    cevap('Nerden bilim', ['nasıl','oluyor','yapılıyor'], gerekli_kelimeler=['nasıl'])
    cevap('Ayıb oluyo.', ['mal', 'mısın', 'amcık', 'yarrak'], tek_cevap=True)
    cevap('Ben çitlek!', ['adın', 'ne'], gerekli_kelimeler=['adın','ne'])
    cevap(uzun.tavsiye(), ['ne', 'yapmalıyım'], gerekli_kelimeler=['ne', 'yapmalıyım'])
    en_iyi_eşleşme = max(en_yüksek_ol_listesi, key=en_yüksek_ol_listesi.get)

    # print(en_yüksek_ol_listesi)
    # print(en_iyi_eşleşme)

# cevaplar-----------------------------------------------------------------------------------------------------
    if en_yüksek_ol_listesi[en_iyi_eşleşme] < 1 :
        return uzun.bilinmeyen()
    else:
        return en_iyi_eşleşme




def cevap_al(kullanıcı_input):
    bölünük_mesaj = re.split(r'\s+|[,;?!.-]\s*', kullanıcı_input.lower())
    cevap = tüm_mesajları_kontrol_et(bölünük_mesaj)
    return cevap

# cevap sistemini test etme
# try:
while True:

    a = cevap_al(input('Sen :'))
    print('Çitlek : ' + a)
    konuş(a)

# except TypeError:
#     print('hata oluştu')