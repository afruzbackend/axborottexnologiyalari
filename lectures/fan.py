"""Shu nusxadagi darslik (fan) ma'lumotlari.

Boshqa fan uchun sayt yasashda loyiha nusxalanadi va faqat shu fayl hamda data/maruza.docx almashtiriladi:
bo'limlar, har bir mavzuning 3D ko'rgazmasi, muallif, YouTube video darslari va materiallar shu yerda.
Bu fanning ma'ruza matnlari data/manba/ papkasida yozilgan (ishchi dasturda faqat mavzular ro'yxati bor edi).
"""
from pathlib import Path

SLUG = 'axborot-texnologiyalari'   # docx dagi fan nomidan: «UKM.2. Axborot texnologiyalari»
AUTHOR = 'Oydin Tashtemirova'

IMG = Path(__file__).resolve().parent / 'static' / 'lectures' / 'img'
PHOTO = IMG / 'muallif.jpg'   # ustoz (portret)
COVER = IMG / 'muqova.jpg'    # bosh sahifa foni: ustoz dars o'tayotgan payt

# docx muqovasida yo'q ma'lumotlar (modul, yo'nalish va soatlar docx'dan olinadi: 12 nazariy, 18 amaliy mavzu)
COURSE = {
    'subtitle': 'Interaktiv elektron darslik: 30 ta ma’ruza, 3D ko‘rgazmalar, video darslar, taqdimotlar, '
                '150 ta test va amaliy topshiriqlar.',
}

# (bo'lim nomi, birinchi mavzu, oxirgi mavzu, rang, belgi) — ishchi dasturdagi o'qitish natijalari bo'yicha
PARTS = [
    ('Kompyuter qurilmalari va operatsion tizim', 1, 6, '#24508F', 'cpu'),
    ('Elektron hujjatlar va raqamli materiallar', 7, 15, '#0E7C7B', 'file'),
    ('Fayl, papka va ma’lumotlarni saqlash vositalari', 16, 21, '#B07D1E', 'layers'),
    ('Internet va elektron axborot almashinuvi', 22, 25, '#C2562D', 'globe'),
    ('Axborot xavfsizligi va shaxsiy ma’lumotlar himoyasi', 26, 30, '#9E2A3A', 'shield'),
]

# mavzu raqami -> 3D ko'rgazma (lectures/scenes.py)
SCENES = {
    1: 'tower', 2: 'printer', 3: 'monitor', 4: 'layers', 5: 'os', 6: 'gear', 7: 'docs', 8: 'docs', 9: 'monitor',
    10: 'docs', 11: 'tools', 12: 'pulse', 13: 'disk', 14: 'docs', 15: 'cloud', 16: 'folder', 17: 'folder',
    18: 'folder', 19: 'disk', 20: 'usb', 21: 'cloud', 22: 'network', 23: 'browser', 24: 'mail', 25: 'mail',
    26: 'shield', 27: 'phish', 28: 'lock', 29: 'password', 30: 'lock',
}

# mavzu raqami -> [(YouTube video ID, tili)]   tanlov: mavzuga mosligi, o'zbek tilidagilar birinchi
VIDEOS = {
    1: [('_aG394NRckg', 'uz'), ('1yIEKUz4dCk', 'uz'), ('FSIwiEWSHyo', 'uz')],
    2: [('Twi2pXFimeo', 'uz'), ('dLtr-sJk6FM', 'uz'), ('-bHMIyrO58s', 'uz')],
    3: [('DMbuhZZFqsY', 'uz'), ('gvmLkv7xxmQ', 'uz'), ('OIUW4aIJqhw', 'uz')],
    4: [('jBYEKl-IoBg', 'uz'), ('Z6RWPikefd4', 'uz'), ('BHAW3mHGbm8', 'uz')],
    5: [('haTH7IiUwzk', 'uz'), ('csQ7113ALAg', 'uz'), ('CbfaDlgHQx0', 'uz')],
    6: [('gCY1LYsFGr8', 'uz'), ('doThHawqG8Q', 'uz'), ('RgGpjkbXv8c', 'uz')],
    7: [('INU6DMuePEw', 'uz'), ('U8W4ZvdVWqg', 'uz'), ('6WxcHqVTkew', 'uz')],
    8: [('A9GgVXfJLXM', 'uz'), ('6KP2SnBw-nc', 'uz'), ('4UmhbkHRnYM', 'uz')],
    9: [('l8AUOTHTY3Q', 'uz'), ('fiJAfE5bJ30', 'uz'), ('SneyokZM-KA', 'uz')],
    10: [('uEiF_cXvIh4', 'uz'), ('ZGG5k1y7dUE', 'uz'), ('Z9KrYaTM5wA', 'uz')],
    11: [('Yrkyik0yXOs', 'uz'), ('Ir4Nc9cWeUE', 'uz'), ('d5SXY0slSak', 'uz')],
    12: [('44GIvvTbhKk', 'uz'), ('7YWU3yUElEQ', 'uz'), ('dP0RMoOvPTo', 'uz')],
    13: [('d2BMOPStN4k', 'uz'), ('uH420cUgUTE', 'uz'), ('1Sda9Qdn-1Y', 'uz')],
    14: [('VjbSsR3fl34', 'uz'), ('blvrlHPGPUA', 'uz'), ('zREjXSumsMQ', 'uz')],
    15: [('NeWx67biwtI', 'uz'), ('i4Eqpq9Is4A', 'uz'), ('xWUbl6qt3Fg', 'uz')],
    16: [('ArnKGgK8llA', 'uz'), ('tz1Ivmvk3ns', 'uz'), ('GejPQXv2vkQ', 'uz')],
    17: [('nVUBOerLXGE', 'uz'), ('u15v5T1WuV8', 'uz'), ('xks08oXl0T4', 'uz')],
    18: [('2xc7Put--M8', 'uz'), ('eVppFnDb69A', 'uz'), ('9dgwVBbjrm8', 'uz')],
    19: [('AKA-x_lunJs', 'uz'), ('fEf5Ct2j7Fo', 'uz'), ('FC_2ljPpeSU', 'uz')],
    20: [('sZQGdD7t-x8', 'uz'), ('JtIbMrrGleg', 'uz'), ('SxzRRNRGfY8', 'uz')],
    21: [('n_hCeW_ohlo', 'uz'), ('18xNL4Q1Q28', 'uz'), ('j68xI37J0V4', 'uz')],
    22: [('t-JWCDNLn3Q', 'uz'), ('XXVHKbpknHg', 'uz'), ('r1Y1xJEXN5w', 'uz')],
    23: [('PzUaOs_8f8M', 'uz'), ('g-hohqaYrGM', 'uz'), ('3X0PpwylS-o', 'uz')],
    24: [('WzId8ys1YuQ', 'uz'), ('rDUwWGzwBl8', 'uz'), ('q6QttQmH68M', 'uz')],
    25: [('yA97xZJmhgk', 'uz'), ('52uN1WIcPCs', 'uz'), ('hAjp69liwXM', 'uz')],
    26: [('ESeGmFZsnXw', 'uz'), ('SfodEUc5hDc', 'uz'), ('nNsUIqY7ErQ', 'uz')],
    27: [('MatSa_r1ssY', 'uz'), ('fUgTf3ProxA', 'uz'), ('I9dADxL07xw', 'uz')],
    28: [('JD8m6T7tv7c', 'uz'), ('epI7NANklQA', 'uz'), ('BBt0lBldnLQ', 'uz')],
    29: [('yGqnzugayTQ', 'uz'), ('kew66LOiCpY', 'uz'), ('YFWAHJM2prs', 'uz')],
    30: [('T8zNebKq1gM', 'uz'), ('U9CQqCUpR8E', 'uz'), ('KnmbWUWWmBs', 'uz')],
}

# fanga oid foydali havolalar (Materiallar bo'limi): (nomi, havola, izoh, mavzu raqami yoki None)
MATERIALS = [
    ('«Axborotlashtirish to‘g‘risida»gi Qonun (560-II, 11.12.2003)', 'https://lex.uz/docs/82956',
     'Qonunning rasmiy matni · lex.uz', 26),
    ('«Elektron hujjat aylanishi to‘g‘risida»gi Qonun (611-II, 29.04.2004)', 'https://lex.uz/docs/165074',
     'Qonunning rasmiy matni · lex.uz', 7),
    ('«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (O‘RQ-547, 02.07.2019)', 'https://lex.uz/docs/4396419',
     'Qonunning rasmiy matni · lex.uz', 28),
    ('Windows bo‘yicha rasmiy yordam', 'https://support.microsoft.com/windows',
     'Microsoft: ish stoli, sozlamalar, qurilmalar va xavfsizlik bo‘yicha qo‘llanmalar', 5),
    ('Microsoft Word bo‘yicha rasmiy yordam', 'https://support.microsoft.com/word',
     'Hujjat yaratish, formatlash, jadval va saqlash bo‘yicha darsliklar', 8),
    ('LibreOffice — bepul ofis dasturlari to‘plami', 'https://www.libreoffice.org',
     'Writer, Calc, Impress: Microsoft Office’ning bepul muqobili', 7),
    ('Canva — onlayn grafik dizayn xizmati', 'https://www.canva.com',
     'E’lon, plakat va taqdimotlarni tayyor shablonlar asosida yaratish', 9),
    ('7-Zip — bepul arxivator', 'https://www.7-zip.org',
     'ZIP va 7z arxivlar yaratish, AES-256 bilan parollash', 14),
    ('Google Disk bo‘yicha yordam markazi', 'https://support.google.com/drive',
     'Fayllarni yuklash, sinxronlash va ulashish', 15),
    ('Google qidiruv operatorlari', 'https://support.google.com/websearch/answer/2466433',
     'Qo‘shtirnoq, minus, site: va boshqa operatorlardan foydalanish', 23),
    ('Gmail bo‘yicha yordam markazi', 'https://support.google.com/mail',
     'Xat yozish, fayl biriktirish, spam va xavfsizlik', 25),
    ('Yagona interaktiv davlat xizmatlari portali', 'https://my.gov.uz',
     'Davlat xizmatlaridan elektron foydalanish', 24),
    ('Kiberxavfsizlik markazi', 'https://csec.uz', 'Rasmiy tavsiyalar va ogohlantirishlar', 26),
    ('VirusTotal — fayl va havolalarni tekshirish', 'https://www.virustotal.com',
     '70 ga yaqin antivirus bilan onlayn tekshiruv', 27),
    ('Have I Been Pwned — pochta sizib chiqqanini tekshirish', 'https://haveibeenpwned.com',
     'Ma’lumotlar sizib chiqishida qatnashganini aniqlash', 28),
    ('Google xavfsizlik tekshiruvi', 'https://myaccount.google.com/security-checkup',
     'Google hisobi himoyasini bosqichma-bosqich tekshirish', 29),
    ('ZiyoNET ta’lim portali', 'https://ziyonet.uz', 'O‘quv materiallari va elektron kutubxona', None),
]
