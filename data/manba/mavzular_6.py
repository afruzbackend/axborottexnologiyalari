"""26–30-mavzular: axborot xavfsizligi qoidalari, raqamli muhitda xavfsiz ishlash, shaxsiy ma'lumotlar, parol va 2FA.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 26
    {
        'type': 'N',
        'title': 'Axborot xavfsizligining asosiy tushunchalari va qoidalari',
        'reja': ['Axborot xavfsizligi tushunchasi va uning tamoyillari',
                 'Axborotga tahdidlar va zararli dasturlar',
                 'Kompyuter va axborotni himoyalashning asosiy qoidalari'],
        'maqsad': 'O‘quvchilarga axborot xavfsizligi, maxfiylik, yaxlitlik, foydalanuvchanlik tamoyillari, axborotga '
                  'tahdidlar, zararli dastur turlari va kompyuterni himoyalashning asosiy qoidalarini tushuntirish.',
        'natija': 'O‘quvchilar axborot xavfsizligi tamoyillarini izohlaydi, zararli dastur turlarini farqlaydi va '
                  'kundalik ishda qo‘llaniladigan himoya qoidalarini sanaydi.',
        'bolimlar': [
            """
## Axborot xavfsizligi nima?
Kompyuterda saqlanadigan hujjatlar, fotosuratlar, parollar, bank kartasi ma’lumotlari va yozishmalar har kimning shaxsiy boyligidir. Ularni yo‘qotish, o‘g‘irlatish yoki o‘zgartirilishi katta zarar keltiradi.
- **Axborot xavfsizligi** — axborotni ruxsatsiz kirish, o‘zgartirish, yo‘q qilish va tarqatishdan himoyalangan holati.
- **Tahdid** — axborotga zarar yetkazishi mumkin bo‘lgan hodisa yoki harakat.
- **Zaiflik** — tizimdagi kamchilik bo‘lib, undan foydalanib hujum qilish mumkin.
## Uchta asosiy tamoyil
| Tamoyil | Ma’nosi | Buzilishiga misol |
| Maxfiylik (konfidensiallik) | Axborotni faqat ruxsati borlar ko‘radi | Begona odam parolingizni bilib oldi |
| Yaxlitlik | Axborot ruxsatsiz o‘zgartirilmaydi | Hujjatdagi raqamlar o‘zgartirildi |
| Foydalanuvchanlik | Axborotdan kerakli vaqtda foydalanish mumkin | Virus fayllarni qulflab qo‘ydi |
O‘zbekistonda bu soha «Axborotlashtirish to‘g‘risida», «Kiberxavfsizlik to‘g‘risida» va «Shaxsga doir ma’lumotlar to‘g‘risida»gi qonunlar bilan tartibga solinadi.
""",
            """
## Tahdid turlari
| Tahdid | Misol |
| Tabiiy va texnik | Elektr uzilishi, disk buzilishi, yong‘in |
| Inson xatosi | Faylni tasodifan o‘chirish, parolni aytib qo‘yish |
| Qasddan qilingan | Xakerlik hujumi, virus tarqatish, firibgarlik |
## Zararli dasturlar
- **Zararli dastur** — foydalanuvchi bilmagan holda kompyuterga zarar yetkazuvchi, ma’lumotlarni o‘g‘irlovchi yoki buzuvchi dastur.
- **Virus** — boshqa fayllarga yozilib, ular orqali ko‘payadigan zararli dastur.
- **Troyan** — foydali dastur qiyofasida kirib, yashirincha zararli ish bajaradigan dastur.
- **Chuvalchang** — tarmoq orqali o‘zini o‘zi tarqatadigan zararli dastur.
- **Shifrlovchi virus** — fayllarni shifrlab qulflaydigan va ochish uchun pul talab qiladigan zararli dastur.
- **Josus dastur** — foydalanuvchi harakatlari va parollarini yashirincha yig‘uvchi dastur.
## Virus belgilari
Kompyuter juda sekinlashsa, fayllar o‘z-o‘zidan yo‘qolsa yoki nomi o‘zgarsa, ekranda notanish reklama oynalari paydo bo‘lsa, fleshkada papkalar o‘rnida `.exe` fayllar ko‘rinsa, kompyuterni darhol antivirus bilan tekshirish kerak.
""",
            """
## Himoya vositalari
- **Antivirus** — zararli dasturlarni aniqlovchi, bloklovchi va o‘chiruvchi dastur.
- **Tarmoqlararo ekran** — kompyuter va tarmoq o‘rtasidagi ma’lumot oqimini nazorat qilib, xavfli ulanishlarni bloklovchi vosita (firewall).
- **Yangilanish** — dasturdagi xatolar va zaifliklarni tuzatuvchi yangi versiya.
Windows 10/11 da «Безопасность Windows» (Windows Security) ilovasi o‘rnatilgan bo‘lib, u antivirus va tarmoqlararo ekran vazifasini bajaradi.
## Asosiy xavfsizlik qoidalari
- Operatsion tizim va dasturlarni muntazam yangilang.
- Antivirusni o‘chirmang va bazasini yangilab turing.
- Dasturlarni faqat rasmiy manbalardan o‘rnating.
- Har bir hisob uchun alohida kuchli parol ishlating.
- Noma’lum havolalar va ilovalarni ochmang.
- Muhim fayllarning zaxira nusxasini oling.
- Kompyuterdan uzoqlashganda uni `Win + L` bilan qulflang.
Xavfsizlikda eng zaif bo‘g‘in ko‘pincha insonning o‘zi bo‘ladi. Shuning uchun texnik vositalar bilan birga ehtiyotkorlik va bilim ham zarur.
""",
        ],
        'oldingi': ['Elektron pochta orqali qanday fayl yuboriladi?',
                    'Spam nima?',
                    'Qanday messenjerlarni bilasiz?'],
        'savollar': ['Axborot xavfsizligi nima?',
                     'Maxfiylik, yaxlitlik va foydalanuvchanlik tamoyillarini misol bilan tushuntiring.',
                     'Virus va troyan o‘rtasida qanday farq bor?',
                     'Kompyuter virusga chalinganini qanday belgilardan bilish mumkin?',
                     'Kompyuterni himoyalashning asosiy qoidalarini sanang.'],
        'testlar': [
            ('Foydali dastur qiyofasida kirib, yashirincha zararli ish bajaradigan dastur:',
             ['Chuvalchang', 'Troyan', 'Antivirus', 'Drayver'], 'b'),
            ('Axborotni faqat ruxsati bor shaxslar ko‘ra olishi qaysi tamoyil?',
             ['Maxfiylik', 'Yaxlitlik', 'Foydalanuvchanlik', 'Hisobdorlik'], 'a'),
            ('Fayllarni qulflab, ochish uchun pul talab qiluvchi zararli dastur:',
             ['Josus dastur', 'Chuvalchang', 'Reklama dasturi', 'Shifrlovchi virus'], 'd'),
            ('Kompyuter va tarmoq o‘rtasidagi xavfli ulanishlarni bloklovchi vosita:',
             ['Arxivator', 'Brauzer', 'Tarmoqlararo ekran (firewall)', 'Matn muharriri'], 'c'),
            ('Tarmoq orqali o‘zini o‘zi tarqatadigan zararli dastur:',
             ['Chuvalchang', 'Troyan', 'Drayver', 'Yangilanish'], 'a'),
        ],
        'mustaqil': ['Zararli dastur turlari bo‘yicha «Klaster» chizmasini tuzing va har biriga real hayotdan misol '
                     'keltiring.',
                     'Kompyuteringizda «Безопасность Windows» ilovasini ochib, himoya holatini tekshiring va natijani '
                     'yozing.'],
    },
    # ------------------------------------------------------------------ 27
    {
        'type': 'A',
        'title': 'Internet va raqamli muhitda xavfsiz ishlash qoidalarini qo‘llash',
        'reja': ['Internetdagi asosiy xavflar: phishing va firibgarlik',
                 'Amaliy ish: havola va saytlarni tekshirish, antivirus bilan skanerlash',
                 'Ijtimoiy tarmoqlar va messenjerlarda xavfsizlik'],
        'maqsad': 'O‘quvchilarda phishing xatlar va soxta saytlarni aniqlash, shubhali havolani tekshirish, kompyuterni '
                  'antivirus bilan skanerlash va ijtimoiy tarmoqlarda maxfiylik sozlamalarini qo‘llash ko‘nikmasini '
                  'shakllantirish.',
        'natija': 'O‘quvchilar phishing belgilarini aniqlaydi, havolani VirusTotal’da tekshiradi, Windows Defender '
                  'bilan tez tekshiruv o‘tkazadi va Telegram maxfiylik sozlamalarini o‘rnatadi.',
        'vosita': 'Internetga ulangan kompyuterlar, «Безопасность Windows», virustotal.com, phishing xatlar namunalari',
        'bolimlar': [
            """
## Phishing
- **Phishing** — firibgarlar o‘zini bank, do‘kon yoki taniqli tashkilot qilib ko‘rsatib, login, parol va karta ma’lumotlarini aldov yo‘li bilan olishga urinishi.
- **Soxta sayt** — mashhur saytning tashqi ko‘rinishini nusxalab, boshqa manzilda joylashtirilgan firibgarlik sayti.
- **Ijtimoiy muhandislik** — insonning ishonuvchanligi, qo‘rquvi yoki qiziqishidan foydalanib, uni maxfiy ma’lumotni berishga majburlash usuli.
## Phishing belgilari
| Belgi | Misol |
| Shoshiltirish | «24 soat ichida tasdiqlamasangiz, hisobingiz bloklanadi!» |
| Juda yaxshi taklif | «Siz iPhone yutib oldingiz, faqat yetkazib berish uchun to‘lang» |
| Noto‘g‘ri manzil | `click-uz.net`, `paynne.uz`, `telegram-premium.ru` |
| Maxfiy ma’lumot so‘rash | SMS-kod, karta raqami va amal qilish muddatini so‘rash |
| Imlo xatolari | Rasmiy xatda grammatik xatolar |
Bank va to‘lov tizimlari hech qachon SMS-kod yoki kartaning orqa tomonidagi kodni so‘ramaydi. SMS-kodni hech kimga aytmang: u sizning raqamli imzoyingiz.
""",
            """
## Havolani tekshirish
- **Qadam 1.** Shubhali havolani bosmang, sichqonchani uning ustiga olib boring va pastki burchakda haqiqiy manzilni o‘qing.
- **Qadam 2.** Manzilni oxiridan o‘qing: `my.gov.uz.login-check.com` aslida `login-check.com` saytiga olib boradi.
- **Qadam 3.** virustotal.com saytida «URL» yorlig‘ini tanlang va havolani nusxalab qo‘ying.
- **Qadam 4.** Natijani o‘qing: xavfli deb belgilagan antiviruslar soni ko‘rsatiladi.
- **Qadam 5.** Natijani topshiriq kartochkasiga yozing.
## Antivirus bilan tekshirish
- **Qadam 1.** «Безопасность Windows» → «Защита от вирусов и угроз» bo‘limini oching.
- **Qadam 2.** «Быстрая проверка» tugmasini bosing va tekshiruv tugashini kuting.
- **Qadam 3.** «Обновления защиты» bo‘limida antivirus bazasini yangilang.
- **Qadam 4.** «Брандмауэр и защита сети» bo‘limida barcha tarmoq profillarida himoya yoqilganligini tekshiring.
## Topshiriq kartochkasi
| № | Havola | Xavfli/xavfsiz | Belgilar |
| 1 | `https://my.gov.uz` | | |
| 2 | `http://my-gov-uz.free-bonus.top` | | |
| 3 | `https://payme.uz` | | |
| 4 | `https://click-uz.net/bonus` | | |
""",
            """
## Ijtimoiy tarmoq va messenjerlarda xavfsizlik
- Shaxsiy ma’lumotlar (uy manzili, pasport, karta) va geolokatsiyali rasmlarni ommaga joylamang.
- Notanish odamlarning do‘stlik so‘rovlarini va guruhga taklifini qabul qilmang.
- Do‘stingiz nomidan pul so‘ragan xabarni unga qo‘ng‘iroq qilib tekshiring: hisobi buzilgan bo‘lishi mumkin.
- Telegram’da notanish yuboruvchidan kelgan `.apk` yoki `.exe` fayllarni ochmang.
## Telegram maxfiylik sozlamalari
- **Qadam 1.** «Настройки» → «Конфиденциальность» bo‘limini oching.
- **Qadam 2.** «Номер телефона» bandida «Мои контакты» yoki «Никто» ni tanlang.
- **Qadam 3.** «Группы и каналы» bandida sizni guruhga kim qo‘sha olishini cheklang.
- **Qadam 4.** «Активные сеансы» bo‘limida begona qurilmalar bo‘lsa, ularni yakunlang.
## Raqamli iz
- **Raqamli iz** — foydalanuvchining internetda qoldirgan barcha ma’lumotlari: yozuvlari, rasmlari, izohlari va qidiruvlari.
Internetga bir marta joylangan ma’lumotni butunlay o‘chirish deyarli imkonsiz. Shuning uchun har bir yozuvni joylashdan oldin «Buni ota-onam yoki kelajakdagi ish beruvchim ko‘rsa nima bo‘ladi?» degan savolni o‘zingizga bering.
""",
        ],
        'oldingi': ['Axborot xavfsizligining uchta asosiy tamoyilini ayting.',
                    'Qanday zararli dastur turlarini bilasiz?',
                    'Antivirus nima?'],
        'savollar': ['Phishing nima?',
                     'Phishing xatning qanday belgilari bor?',
                     'Havola xavfsizligini qanday tekshirish mumkin?',
                     'Windows Defender bilan tez tekshiruv qanday o‘tkaziladi?',
                     'Raqamli iz nima va uni nega nazorat qilish kerak?'],
        'testlar': [
            ('Firibgarlarning taniqli tashkilot nomidan parol va karta ma’lumotlarini olishga urinishi:',
             ['Spam', 'Phishing', 'Sinxronlash', 'Arxivlash'], 'b'),
            ('`my.gov.uz.login-check.com` havolasi aslida qaysi saytga olib boradi?',
             ['my.gov.uz', 'gov.uz', 'login-check.com', 'uz.login'], 'c'),
            ('Havolani ko‘plab antiviruslar bilan onlayn tekshiruvchi xizmat:',
             ['VirusTotal', 'Canva', 'Google Disk', 'Paint'], 'a'),
            ('Bank xodimi deb tanishtirgan odam SMS-kodni so‘rasa nima qilish kerak?',
             ['Kodni aytish', 'Karta raqamini aytish', 'Kodni ijtimoiy tarmoqqa yozish',
              'Hech narsa aytmasdan bankning rasmiy raqamiga qo‘ng‘iroq qilish'], 'd'),
            ('Insonning ishonuvchanligidan foydalanib maxfiy ma’lumot olish usuli:',
             ['Ijtimoiy muhandislik', 'Formatlash', 'Shifrlash', 'Zaxiralash'], 'a'),
        ],
        'mustaqil': ['O‘zingiz yoki tanishlaringiz duch kelgan 3 ta internet firibgarligi holatini tasvirlab, '
                     'ularni qanday aniqlash mumkinligini yozing.',
                     'Ota-onangiz uchun «Internetda xavfsizlikning 7 ta qoidasi» eslatmasini tayyorlang.'],
    },
    # ------------------------------------------------------------------ 28
    {
        'type': 'N',
        'title': 'Shaxsiy va xizmat ma’lumotlarini himoya qilish usullari',
        'reja': ['Shaxsiy va xizmat ma’lumotlari tushunchasi',
                 'Ma’lumotlarni himoya qilishning tashkiliy va texnik usullari',
                 'Qonunchilik va ma’lumotlar sizib chiqqanda ko‘riladigan choralar'],
        'maqsad': 'O‘quvchilarga shaxsiy va xizmat ma’lumotlari tushunchalari, ularni himoya qilishning tashkiliy va '
                  'texnik usullari (kirish huquqlari, shifrlash, ekran qulfi, xavfsiz o‘chirish) hamda tegishli '
                  'qonunchilikni tushuntirish.',
        'natija': 'O‘quvchilar shaxsiy va xizmat ma’lumotlarini farqlaydi, ularni himoya qilish usullarini tanlaydi va '
                  'ma’lumot sizib chiqqanda ko‘riladigan choralarni izohlaydi.',
        'bolimlar': [
            """
## Shaxsiy ma’lumotlar
- **Shaxsga doir ma’lumotlar** — muayyan shaxsni aniqlash imkonini beruvchi har qanday ma’lumot: F.I.Sh., pasport, JShShIR, manzil, telefon, rasm.
- **Xizmat ma’lumotlari** — tashkilot faoliyatiga oid, faqat xodimlar foydalanishi mumkin bo‘lgan ma’lumotlar: hisobotlar, mijozlar ro‘yxati, ichki hujjatlar.
- **Maxfiy ma’lumot** — oshkor bo‘lishi shaxs yoki tashkilotga zarar keltirishi mumkin bo‘lgan, kirish cheklangan ma’lumot.
| Turi | Misollar | Oshkor bo‘lsa xavfi |
| Shaxsiy | Pasport rasmi, uy manzili, telefon | Firibgarlik, nomingizdan kredit olish |
| Moliyaviy | Karta raqami, SMS-kod | Pulni o‘g‘irlash |
| Tibbiy | Kasallik tarixi | Kamsitish, shantaj |
| Xizmat | Mijozlar bazasi, parollar | Tashkilot obro‘si va puli yo‘qoladi |
O‘zbekistonda shaxsiy ma’lumotlar «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (2019-yil, O‘RQ-547) bilan himoya qilinadi.
""",
            """
## Tashkiliy usullar
- Ma’lumotga kirish huquqini faqat kerakli xodimlarga berish.
- Xodimlarni xavfsizlik qoidalariga o‘qitish.
- Qog‘ozdagi maxfiy hujjatlarni qulflanadigan javonda saqlash va keraksizini maydalagichda yo‘q qilish.
- «Toza stol» qoidasi: ish joyidan ketayotganda stolda hujjat va parol yozilgan qog‘oz qoldirmaslik.
## Texnik usullar
- **Kirish huquqlari** — foydalanuvchi qaysi fayl yoki papkani ko‘rishi, o‘zgartirishi yoki o‘chirishi mumkinligini belgilovchi ruxsatlar.
- **Shifrlash** — ma’lumotni maxsus kalitsiz o‘qib bo‘lmaydigan ko‘rinishga keltirish.
- **Ekran qulfi** — foydalanuvchi uzoqlashganda kompyuter yoki telefonni parol, PIN yoki barmoq izi bilan qulflash.
| Usul | Qanday qo‘llaniladi |
| Alohida foydalanuvchi hisoblari | Har bir xodimning o‘z logini va paroli |
| Papka ruxsatlari | «Свойства» → «Безопасность» yorlig‘i |
| Disk shifrlash | Windows BitLocker, telefonlarda o‘rnatilgan shifrlash |
| Arxivni parollash | 7-Zip’da AES-256 shifrlash bilan arxiv |
| Xavfsiz o‘chirish | Diskni utilita bilan qayta yozib tozalash |
""",
            """
## Qurilmani topshirish va sotish
Kompyuter yoki telefonni ta’mirga berish, sotish yoki boshqa xodimga topshirishdan oldin:
- muhim fayllarning zaxira nusxasini oling;
- barcha hisoblardan (Google, Telegram, bank ilovalari) chiqing;
- telefonni «Сброс до заводских настроек» bilan tozalang;
- kompyuterda disklarni xavfsiz tozalang yoki shifrlangan holda topshiring.
IT-servis mutaxassisi mijoz kompyuterini ta’mirlayotganda uning shaxsiy fayllarini ochmasligi, nusxalamasligi va hech kimga ko‘rsatmasligi shart. Bu kasb odobining asosiy talabidir.
## Ma’lumot sizib chiqqanda
- **Ma’lumotlar sizib chiqishi** — himoyalangan ma’lumotlarning ruxsatsiz shaxslar qo‘liga tushishi.
- **Qadam 1.** Buzilgan hisob parolini darhol o‘zgartiring va boshqa qurilmalardagi seanslarni yakunlang.
- **Qadam 2.** Bank kartasi ma’lumotlari bilan bog‘liq bo‘lsa, bank bilan bog‘lanib kartani bloklang.
- **Qadam 3.** Ikki bosqichli autentifikatsiyani yoqing.
- **Qadam 4.** Tashkilotda bo‘lsa, rahbariyat va axborot xavfsizligi bo‘limiga xabar bering.
- **Qadam 5.** Kiberjinoyat holatlari haqida ichki ishlar organlariga murojaat qiling.
Pochtangiz qaysidir ma’lumotlar sizib chiqishida qatnashganini haveibeenpwned.com saytida tekshirish mumkin.
""",
        ],
        'oldingi': ['Phishing nima?',
                    'Havola xavfsizligini qanday tekshirish mumkin?',
                    'Raqamli iz nima?'],
        'savollar': ['Shaxsga doir ma’lumotlarga nimalar kiradi?',
                     'Xizmat ma’lumotlari shaxsiy ma’lumotlardan qanday farq qiladi?',
                     'Ma’lumotlarni himoya qilishning tashkiliy usullarini sanang.',
                     'Shifrlash nima?',
                     'Ma’lumot sizib chiqqanda qanday choralar ko‘riladi?'],
        'testlar': [
            ('O‘zbekistonda shaxsiy ma’lumotlar qaysi qonun bilan himoya qilinadi?',
             ['«Ta’lim to‘g‘risida»gi Qonun', '«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun',
              '«Reklama to‘g‘risida»gi Qonun', 'Mehnat kodeksi'], 'b'),
            ('Ma’lumotni maxsus kalitsiz o‘qib bo‘lmaydigan ko‘rinishga keltirish:',
             ['Arxivlash', 'Formatlash', 'Shifrlash', 'Nusxalash'], 'c'),
            ('Windows’da diskni shifrlovchi o‘rnatilgan vosita:',
             ['BitLocker', 'Paint', 'WordPad', 'Defragmentator'], 'a'),
            ('«Toza stol» qoidasi nimani talab qiladi?',
             ['Stolni har kuni artish', 'Kompyuterni stolga qo‘ymaslik',
              'Faqat bitta monitor ishlatish', 'Stolda hujjat va parol yozilgan qog‘oz qoldirmaslik'], 'd'),
            ('Papka ruxsatlari qaysi yorliqda sozlanadi?',
             ['Безопасность', 'Общие', 'Настройка', 'Предыдущие версии'], 'a'),
        ],
        'mustaqil': ['Internetda ommaga joylanmasligi kerak bo‘lgan 10 ta shaxsiy ma’lumot turini yozib, har birining '
                     'oshkor bo‘lishi xavfini izohlang.',
                     '«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonunning asosiy tushunchalarini lex.uz saytidan '
                     'o‘qib, konspekt qiling.'],
    },
    # ------------------------------------------------------------------ 29
    {
        'type': 'A',
        'title': 'Kuchli parol va autentifikatsiya usullaridan foydalanish',
        'reja': ['Kuchli parol talablari va parol yaratish usullari',
                 'Amaliy ish: Windows va Google hisobida parol va PIN-kodni o‘zgartirish',
                 'Ikki bosqichli autentifikatsiyani yoqish'],
        'maqsad': 'O‘quvchilarda kuchli parol yaratish, uni xavfsiz saqlash, Windows va Google hisobida parolni '
                  'o‘zgartirish, PIN-kod o‘rnatish hamda ikki bosqichli autentifikatsiyani yoqish ko‘nikmasini '
                  'shakllantirish.',
        'natija': 'O‘quvchilar parol iborasi usulida kuchli parol yaratadi, o‘quv hisobida parolni almashtiradi, '
                  'Google va Telegram’da ikki bosqichli himoyani yoqadi.',
        'vosita': 'Internetga ulangan kompyuterlar, o‘quv Google hisoblari, telefon (Telegram), parollar talablari tarqatmasi',
        'bolimlar': [
            """
## Autentifikatsiya
- **Identifikatsiya** — foydalanuvchining o‘zini tanishtirishi, ya’ni login yoki ismini kiritishi.
- **Autentifikatsiya** — foydalanuvchi haqiqatan ham o‘zi aytgan shaxs ekanini tekshirish jarayoni.
- **Avtorizatsiya** — autentifikatsiyadan o‘tgan foydalanuvchiga tegishli huquqlarni berish.
| Usul | Misol |
| Bilgan narsasi | Parol, PIN-kod |
| Ega bo‘lgan narsasi | Telefon (SMS-kod), bank kartasi, ERI kaliti |
| O‘ziga xos belgisi (biometriya) | Barmoq izi, yuz tasviri |
## Kuchli parol talablari
- **Talab:** uzunligi kamida 12 belgi.
- **Talab:** katta va kichik harflar, raqamlar va maxsus belgilar (`! @ # $ %`) aralashgan.
- **Talab:** ism, tug‘ilgan sana, telefon raqami, `12345678`, `qwerty`, `parol` kabi oson taxmin qilinadigan so‘zlar ishlatilmaydi.
- **Talab:** har bir hisob uchun alohida parol: bitta parol sizib chiqsa, boshqa hisoblar xavfsiz qoladi.
| Parol | Baho |
| `123456` | Juda zaif: bir soniyada topiladi |
| `Ali2008` | Zaif: ism va yil |
| `Qovun!Yashil7Daraxt` | Kuchli: uzun, aralash belgilar |
""",
            """
## Parol iborasi usuli
- **Parol iborasi** — bir-biriga bog‘liq bo‘lmagan bir nechta so‘zdan tuzilgan, eslab qolish oson, lekin taxmin qilish qiyin bo‘lgan uzun parol.
Masalan, «Mening mushugim 3 marta tarvuz yedi» gapidan `MeningMushugim3martaTarvuzYedi!` paroli hosil bo‘ladi. Darsda misol tariqasida ko‘rsatilgan parollarni haqiqiy hisoblarda ishlatmang.
## Windows’da parol va PIN-kod
- **Qadam 1.** «Параметры» (`Win + I`) → «Учётные записи» → «Варианты входа» bo‘limini oching.
- **Qadam 2.** «Пароль» → «Изменить» tugmasini bosing, joriy parolni, so‘ng yangi parolni ikki marta kiriting.
- **Qadam 3.** «PIN-код (Windows Hello)» bandida PIN-kod o‘rnating: u faqat shu kompyuterda ishlaydi.
- **Qadam 4.** «Динамическая блокировка» va avtomatik ekran qulfini yoqing.
## Google hisobida parolni almashtirish
- **Qadam 1.** myaccount.google.com → «Безопасность» bo‘limini oching.
- **Qadam 2.** «Пароль» bandini tanlang, joriy parolni tasdiqlang va yangi kuchli parolni kiriting.
- **Qadam 3.** «Проверка безопасности» (Xavfsizlik tekshiruvi) ni ishga tushirib, tavsiyalarni bajaring.
## Parolni saqlash
- **Parol menejeri** — parollarni shifrlangan holda saqlovchi va kuchli parol yaratib beruvchi dastur (Bitwarden, Google parollar menejeri).
Parolni qog‘ozga yozib monitorga yopishtirmang, uni messenjer orqali yubormang.
""",
            """
## Ikki bosqichli autentifikatsiya
- **Ikki bosqichli autentifikatsiya** — parol bilan birga ikkinchi tasdiqlash (SMS-kod, ilova kodi, telefonda tasdiqlash) talab qilinadigan himoya usuli (2FA).
Parol o‘g‘irlansa ham, firibgar sizning telefoningizsiz hisobga kira olmaydi.
## Google hisobida 2FA ni yoqish
- **Qadam 1.** myaccount.google.com → «Безопасность» → «Двухэтапная аутентификация» bandini oching.
- **Qadam 2.** «Начать» tugmasini bosing va telefon raqamingizni tasdiqlang.
- **Qadam 3.** SMS orqali kelgan kodni kiriting va «Включить» tugmasini bosing.
- **Qadam 4.** «Резервные коды» (zaxira kodlar) ni yuklab olib, xavfsiz joyda saqlang: telefon yo‘qolsa, ular yordam beradi.
## Telegram’da bulutli parol
- **Qadam 1.** «Настройки» → «Конфиденциальность» → «Облачный пароль» bandini oching.
- **Qadam 2.** Qo‘shimcha parol o‘ylab toping va kiriting.
- **Qadam 3.** Tiklash uchun elektron pochta manzilingizni ko‘rsating va tasdiqlang.
Shundan so‘ng yangi qurilmadan Telegram’ga kirishda SMS-koddan tashqari shu parol ham so‘raladi. Bu SMS-kodni aldov yo‘li bilan olgan firibgarlardan himoya qiladi.
## Nazorat varag‘i
| № | Amal | Bajarildi |
| 1 | Parol iborasi usulida kuchli parol tuzildi | ha / yo‘q |
| 2 | O‘quv hisobida parol almashtirildi | ha / yo‘q |
| 3 | Windows PIN-kod o‘rnatildi | ha / yo‘q |
| 4 | Google 2FA yoqildi, zaxira kodlar saqlandi | ha / yo‘q |
| 5 | Telegram bulutli paroli o‘rnatildi | ha / yo‘q |
""",
        ],
        'oldingi': ['Shaxsga doir ma’lumotlarga nimalar kiradi?',
                    'Shifrlash nima?',
                    'Ma’lumot sizib chiqqanda nima qilish kerak?'],
        'savollar': ['Identifikatsiya, autentifikatsiya va avtorizatsiya farqi nimada?',
                     'Kuchli parol qanday talablarga javob berishi kerak?',
                     'Parol iborasi usulini tushuntiring.',
                     'Ikki bosqichli autentifikatsiya qanday himoya beradi?',
                     'Parollarni qanday xavfsiz saqlash mumkin?'],
        'testlar': [
            ('Quyidagi parollardan eng kuchlisi:',
             ['123456789', 'Ali2008', 'Qovun!Yashil7Daraxt', 'qwerty'], 'c'),
            ('Foydalanuvchi haqiqatan ham o‘zi aytgan shaxs ekanini tekshirish:',
             ['Autentifikatsiya', 'Identifikatsiya', 'Avtorizatsiya', 'Formatlash'], 'a'),
            ('Barmoq izi va yuz tasviri qaysi autentifikatsiya usuliga kiradi?',
             ['Bilgan narsasi', 'Ega bo‘lgan narsasi', 'Parol', 'Biometriya'], 'd'),
            ('Kuchli parolning tavsiya etilgan minimal uzunligi:',
             ['4 belgi', '12 belgi', '6 belgi', '8 belgi'], 'b'),
            ('Telegram’da yangi qurilmadan kirishda SMS-koddan tashqari so‘raladigan parol:',
             ['Bulutli parol (Облачный пароль)', 'PIN-kod', 'Wi-Fi paroli', 'Windows paroli'], 'a'),
        ],
        'mustaqil': ['Parol iborasi usulida 3 ta kuchli parol tuzing (haqiqiy hisoblaringizda ishlatmang) va nima '
                     'uchun ular kuchli ekanini izohlang.',
                     'O‘zingiz foydalanadigan barcha hisoblar ro‘yxatini tuzib, qaysilarida 2FA yoqilganini belgilang '
                     'va qolganlarida yoqing.'],
    },
    # ------------------------------------------------------------------ 30
    {
        'type': 'A',
        'title': 'Shaxsiy ma’lumotlarni himoyalash choralarini amalda qo‘llash',
        'reja': ['Smartfon va kompyuterda maxfiylik sozlamalari',
                 'Amaliy ish: hujjatni parol bilan himoyalash va shifrlangan arxiv yaratish',
                 'Shaxsiy xavfsizlik auditini o‘tkazish'],
        'maqsad': 'O‘quvchilarda ilovalar ruxsatlari va joylashuv sozlamalarini boshqarish, Word hujjatini parol bilan '
                  'himoyalash, shifrlangan arxiv yaratish, brauzer ma’lumotlarini tozalash va shaxsiy xavfsizlik auditini '
                  'o‘tkazish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar telefondagi ilova ruxsatlarini tekshiradi, parolli hujjat va shifrlangan arxiv yaratadi, '
                  'brauzer ma’lumotlarini tozalaydi va shaxsiy xavfsizlik auditi natijasini rasmiylashtiradi.',
        'vosita': 'Internetga ulangan kompyuterlar, Word, 7-Zip, o‘quvchilarning smartfonlari, audit varag‘i',
        'bolimlar': [
            """
## Ilovalar ruxsatlari
Ko‘plab ilovalar ishlashi uchun kerak bo‘lmagan ruxsatlarni so‘raydi: fonarik ilovasi kontaktlarga, o‘yin esa mikrofonga kirishni so‘rashi xavfli belgi.
- **Ilova ruxsati** — ilovaga kamera, mikrofon, kontaktlar, joylashuv kabi qurilma imkoniyatlaridan foydalanishga berilgan huquq.
- **Geolokatsiya** — qurilmaning joylashgan o‘rnini GPS va tarmoq orqali aniqlash.
## Telefonda tekshirish (Android)
- **Qadam 1.** «Настройки» → «Конфиденциальность» → «Диспетчер разрешений» bo‘limini oching.
- **Qadam 2.** «Местоположение», «Камера», «Микрофон» bandlari bo‘yicha qaysi ilovalarga ruxsat berilganini ko‘ring.
- **Qadam 3.** Keraksiz ruxsatlarni «Запретить» yoki «Только во время использования» ga o‘zgartiring.
## Kompyuterda tekshirish (Windows)
«Параметры» → «Конфиденциальность и защита» bo‘limida kamera, mikrofon va joylashuvga kirish huquqini har bir ilova uchun alohida o‘chirish mumkin. Veb-kamerani ishlatmaganda yopib qo‘yish uchun maxsus qopqoqdan foydalaning.
""",
            """
## Word hujjatini parol bilan himoyalash
- **Qadam 1.** Word’da `Shaxsiy_malumot_Familiya.docx` faylini yarating va unga o‘quv ma’lumotlarini yozing.
- **Qadam 2.** «Файл» → «Сведения» → «Защита документа» → «Зашифровать с использованием пароля» ni tanlang.
- **Qadam 3.** Kuchli parol kiriting va tasdiqlang, so‘ng hujjatni saqlang.
- **Qadam 4.** Hujjatni yopib, qayta oching: parol so‘ralishini tekshiring.
Parolni unutsangiz, hujjatni ochib bo‘lmaydi. Shuning uchun parolni parol menejerida saqlang.
## Shifrlangan arxiv yaratish (7-Zip)
- **Qadam 1.** Himoyalanadigan fayllarni ajrating va o‘ng tugma → «7-Zip» → «Добавить к архиву» ni tanlang.
- **Qadam 2.** «Формат архива» bandida `zip` yoki `7z` ni tanlang.
- **Qadam 3.** «Шифрование» bo‘limida parolni ikki marta kiriting va «Метод шифрования» da AES-256 ni tanlang.
- **Qadam 4.** `7z` formatida «Шифровать имена файлов» belgisini qo‘ying: shunda arxiv ichidagi fayl nomlari ham ko‘rinmaydi.
- **Qadam 5.** «OK» ni bosing va arxivni ochib, parol so‘ralishini tekshiring.
Parolli arxivni elektron pochta orqali yuborsangiz, parolni boshqa kanal (masalan, telefon qo‘ng‘irog‘i) orqali ayting.
## Brauzer ma’lumotlarini tozalash
Begona kompyuterda ishlagandan keyin `Ctrl + Shift + Delete` tugmalari bilan tarix, cookie fayllar va kesh tozalanadi.
- **Cookie** — sayt brauzerda saqlab qo‘yadigan kichik fayl: unda kirish holati va sozlamalar saqlanadi.
""",
            """
## Shaxsiy xavfsizlik auditi
Har bir o‘quvchi o‘z qurilmalari va hisoblari bo‘yicha quyidagi audit varag‘ini to‘ldiradi.
| № | Tekshiruv bandi | Holat |
| 1 | Telefon va kompyuterda ekran qulfi bor | ha / yo‘q |
| 2 | Operatsion tizim va ilovalar yangilangan | ha / yo‘q |
| 3 | Antivirus yoqilgan | ha / yo‘q |
| 4 | Asosiy hisoblarda (pochta, Telegram) 2FA yoqilgan | ha / yo‘q |
| 5 | Har bir hisobda alohida kuchli parol | ha / yo‘q |
| 6 | Ilovalarda keraksiz ruxsatlar yo‘q | ha / yo‘q |
| 7 | Ijtimoiy tarmoqlarda profil yopiq, telefon raqami ko‘rinmaydi | ha / yo‘q |
| 8 | Muhim fayllarning zaxira nusxasi bor | ha / yo‘q |
## Natijani baholash
- **7–8 ta «ha»** — xavfsizlik darajasi yuqori.
- **5–6 ta «ha»** — o‘rtacha, kamchiliklarni bir hafta ichida tuzating.
- **4 ta va kam** — xavfli, darhol choralar ko‘ring.
## Xulosa
Fan davomida biz kompyuter qurilmalari va operatsion tizim, elektron hujjatlar, fayllar va ularni saqlash, internet va elektron axborot almashinuvi hamda axborot xavfsizligi bilan tanishdik. Bu bilimlar har qanday kasbda, ayniqsa kompyuter tarmoqlari va IT-servis mutaxassisi ishida kundalik zaruratdir. Shaxsiy ma’lumotlarni himoyalash bir martalik ish emas: har oy o‘z audit varag‘ingizni qayta tekshirib turing.
""",
        ],
        'oldingi': ['Kuchli parol qanday talablarga javob beradi?',
                    'Ikki bosqichli autentifikatsiya nima?',
                    'Shaxsiy ma’lumotlarni himoyalashning qanday usullarini bilasiz?'],
        'savollar': ['Ilova ruxsatlarini nega tekshirib turish kerak?',
                     'Word hujjatini parol bilan qanday himoyalash mumkin?',
                     'Shifrlangan arxiv qanday yaratiladi?',
                     'Cookie nima va brauzer ma’lumotlari qanday tozalanadi?',
                     'Shaxsiy xavfsizlik auditi qanday bandlardan iborat?'],
        'testlar': [
            ('Word hujjatiga parol qo‘yish yo‘li:',
             ['«Вставка» → «Таблица»', '«Файл» → «Сведения» → «Защита документа»',
              '«Главная» → «Шрифт»', '«Вид» → «Масштаб»'], 'b'),
            ('7-Zip’da tavsiya etiladigan shifrlash usuli:',
             ['AES-256', 'FAT32', 'MP3', 'HTTP'], 'a'),
            ('Brauzer tarixi va keshini tozalash oynasini ochuvchi birikma:',
             ['Ctrl + D', 'Ctrl + T', 'Ctrl + J', 'Ctrl + Shift + Delete'], 'd'),
            ('Sayt brauzerda saqlab qo‘yadigan, kirish holatini eslab qoluvchi kichik fayl:',
             ['Kesh', 'Arxiv', 'Cookie', 'Drayver'], 'c'),
            ('Fonarik ilovasi kontaktlarga kirishni so‘rasa nima qilish kerak?',
             ['Ruxsat bermaslik', 'Darhol ruxsat berish', 'Telefonni formatlash', 'Ilovani ulashish'], 'a'),
        ],
        'mustaqil': ['Shaxsiy xavfsizlik auditini oila a’zolaringizdan birining telefoni bo‘yicha (uning roziligi bilan) '
                     'o‘tkazing va tavsiyalar yozing.',
                     'Fan bo‘yicha o‘rgangan bilimlaringiz asosida «Raqamli savodxonlik» mavzusida 5–7 slaydli taqdimot '
                     'tayyorlang.'],
    },
]
