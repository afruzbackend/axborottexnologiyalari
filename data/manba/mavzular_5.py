"""21–25-mavzular: zaxiralash usullari, internet va tarmoq xizmatlari, brauzer, elektron axborot almashinuvi.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 21
    {
        'type': 'A',
        'title': 'Ma’lumotlarni saqlash va zaxiralash usullaridan foydalanish',
        'reja': ['Zaxiralash turlari va jadvali',
                 'Amaliy ish: Google Disk va OneDrive bilan sinxronlash',
                 'Tizimni tiklash nuqtasi va disk tozalash'],
        'maqsad': 'O‘quvchilarda to‘liq va qo‘shimcha zaxiralash turlarini farqlash, bulutli xotira bilan '
                  'sinxronlash, fayllarni havola orqali ulashish, tizimni tiklash nuqtasini yaratish va diskni tozalash '
                  'ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar zaxiralash jadvalini tuzadi, faylni bulutga yuklab havola bilan ulashadi, tiklash '
                  'nuqtasini yaratadi va «Очистка диска» yordamida joy bo‘shatadi.',
        'vosita': 'Internetga ulangan kompyuterlar, o‘quv Google hisobi, OneDrive, administrator huquqi (o‘qituvchi)',
        'bolimlar': [
            """
## Zaxiralash turlari
- **To‘liq zaxiralash** — tanlangan barcha ma’lumotlarning to‘liq nusxasini yaratish.
- **Qo‘shimcha zaxiralash** — faqat oxirgi zaxira nusxadan keyin o‘zgargan yoki yangi fayllarni nusxalash (inkremental).
| Tur | Afzalligi | Kamchiligi |
| To‘liq | Tiklash oson va tez | Ko‘p vaqt va joy talab qiladi |
| Qo‘shimcha | Tez bajariladi, kam joy egallaydi | Tiklashda barcha nusxalar kerak |
| Sinxronlash (bulut) | Avtomatik, istalgan qurilmadan | Fayl o‘chirilsa, nusxasi ham o‘chadi |
Sinxronlash zaxiralashning to‘liq o‘rnini bosmaydi: kompyuterda fayl o‘chirilsa yoki virus uni shifrlasa, bulutdagi nusxa ham o‘zgaradi. Shu sababli Google Disk va OneDrive o‘chirilgan fayllarni 30 kun davomida «Корзина» da saqlaydi.
## Zaxiralash jadvali
| Ma’lumot | Qanchalik tez-tez | Qayerga |
| O‘quv hujjatlari | Har kuni (avtomatik) | Bulutli xotira |
| Fotosuratlar | Har hafta | Bulut va tashqi disk |
| Butun kompyuter | Har oy | Tashqi disk |
""",
            """
## Google Disk bilan ishlash
- **Qadam 1.** drive.google.com saytida o‘quv hisobingiz bilan kiring.
- **Qadam 2.** «Создать» → «Загрузить папку» orqali `01_Axborot_texnologiyalari` papkangizni yuklang.
- **Qadam 3.** Papka ustida o‘ng tugma → «Открыть доступ» ni tanlang.
- **Qadam 4.** «Общий доступ» bo‘limida «Все, у кого есть ссылка» va «Читатель» (faqat ko‘rish) huquqini tanlang.
- **Qadam 5.** «Копировать ссылку» tugmasini bosing va havolani o‘qituvchiga yuboring.
## Ulashish huquqlari
| Huquq | Nima qila oladi |
| Читатель (o‘quvchi) | Faqat ko‘radi va yuklab oladi |
| Комментатор | Ko‘radi va izoh qoldiradi |
| Редактор (muharrir) | O‘zgartiradi, o‘chiradi, boshqalarga ulashadi |
Faqat kerakli huquqni bering: muharrir huquqi berilgan kishi fayllarni o‘chirib yuborishi mumkin.
## OneDrive
Windows 10/11 da OneDrive o‘rnatilgan bo‘ladi. Unga Microsoft hisobi bilan kirilgach, Provodnik’da «OneDrive» papkasi paydo bo‘ladi: shu papkaga qo‘yilgan har bir fayl avtomatik bulutga yuklanadi. Fayl yonidagi yashil belgi uning sinxronlanganini, ko‘k bulut belgisi esa u faqat bulutda saqlanayotganini bildiradi.
""",
            """
## Tizimni tiklash nuqtasi
- **Tiklash nuqtasi** — operatsion tizim sozlamalari va tizim fayllarining ma’lum vaqtdagi holati; muammo yuz berganda kompyuterni shu holatga qaytarish mumkin.
- **Qadam 1.** «Пуск» qidiruviga «Создание точки восстановления» deb yozing.
- **Qadam 2.** «Защита системы» yorlig‘ida `C:` disk uchun himoya yoqilganini tekshiring.
- **Qadam 3.** «Создать» tugmasini bosib, nuqtaga nom bering: `Dars_21_oldin`.
Tiklash nuqtasi shaxsiy fayllarni (hujjat, rasm) saqlamaydi, u faqat tizim holatini qaytaradi. Shuning uchun u fayllar zaxirasining o‘rnini bosmaydi.
## Disk tozalash
Vaqtinchalik fayllar, brauzer keshi va savatdagi fayllar diskda ko‘p joy egallaydi.
- **Qadam 1.** «Пуск» qidiruviga «Очистка диска» deb yozing va `C:` diskni tanlang.
- **Qadam 2.** «Временные файлы», «Корзина», «Временные файлы Интернета» bandlarini belgilang.
- **Qadam 3.** «OK» → «Удалить файлы» tugmasini bosing va bo‘shatilgan joy hajmini yozib oling.
- **Kesh** — tez ochilishi uchun vaqtincha saqlab qo‘yiladigan ma’lumotlar (masalan, saytlar rasmlari).
""",
        ],
        'oldingi': ['«3-2-1» qoidasini tushuntiring.',
                    'Fleshkani qanday xavfsiz chiqarish kerak?',
                    'Bulutli xotira nima?'],
        'savollar': ['To‘liq va qo‘shimcha zaxiralash farqi nimada?',
                     'Nima uchun sinxronlash zaxiralash o‘rnini to‘liq bosa olmaydi?',
                     'Google Diskda faylni qanday ulashish mumkin?',
                     'Tiklash nuqtasi nimani saqlaydi va nimani saqlamaydi?',
                     'Diskni tozalash qanday bajariladi?'],
        'testlar': [
            ('Faqat oxirgi nusxadan keyin o‘zgargan fayllarni nusxalash:',
             ['To‘liq zaxiralash', 'Formatlash', 'Qo‘shimcha (inkremental) zaxiralash', 'Defragmentatsiya'], 'c'),
            ('Google Diskda faylni faqat ko‘rish huquqi:',
             ['Читатель', 'Редактор', 'Владелец', 'Администратор'], 'a'),
            ('Tiklash nuqtasi nimani saqlaydi?',
             ['Fotosuratlarni', 'Hujjatlarni', 'Musiqalarni', 'Tizim sozlamalari va tizim fayllarini'], 'd'),
            ('Vaqtinchalik fayllarni o‘chirib, joy bo‘shatuvchi Windows vositasi:',
             ['Paint', 'Очистка диска', 'Блокнот', 'Калькулятор'], 'b'),
            ('Google Disk o‘chirilgan fayllarni necha kun saqlaydi?',
             ['30 kun', '1 kun', '7 kun', '365 kun'], 'a'),
        ],
        'mustaqil': ['Oilangiz kompyuteri yoki telefonlari uchun zaxiralash jadvalini tuzing (nima, qachon, qayerga).',
                     'Google Diskda guruh uchun umumiy papka yarating va huquqlarni to‘g‘ri sozlab, natijani '
                     'skrinshot bilan ko‘rsating.'],
    },
    # ------------------------------------------------------------------ 22
    {
        'type': 'N',
        'title': 'Internet va tarmoq xizmatlarining asosiy imkoniyatlari',
        'reja': ['Kompyuter tarmog‘i va internet tushunchasi',
                 'Internetning ishlash tamoyili: IP-manzil, domen, provayder',
                 'Internetning asosiy xizmatlari'],
        'maqsad': 'O‘quvchilarga kompyuter tarmog‘i, lokal va global tarmoq, internet, IP-manzil, domen, provayder '
                  'tushunchalarini hamda internetning asosiy xizmatlarini tushuntirish.',
        'natija': 'O‘quvchilar tarmoq turlarini farqlaydi, sayt manzilining tuzilishini izohlaydi va kundalik hayotda '
                  'foydalaniladigan internet xizmatlarini sanaydi.',
        'bolimlar': [
            """
## Kompyuter tarmog‘i
- **Kompyuter tarmog‘i** — ma’lumot almashish uchun aloqa kanallari orqali o‘zaro bog‘langan kompyuterlar va qurilmalar majmui.
- **Lokal tarmoq** — bir xona, bino yoki tashkilot ichidagi kompyuterlarni bog‘lovchi tarmoq (LAN).
- **Global tarmoq** — shaharlar, mamlakatlar va qit’alardagi tarmoqlarni bog‘lovchi katta tarmoq (WAN).
- **Internet** — butun dunyodagi millionlab tarmoqlarni yagona qoidalar asosida birlashtiruvchi global tarmoq.
| Tarmoq | Qamrovi | Misol |
| PAN (shaxsiy) | Bir necha metr | Telefon va Bluetooth quloqchin |
| LAN (lokal) | Xona, bino | Texnikumning kompyuter sinfi |
| MAN (shahar) | Shahar | Shahar provayderi tarmog‘i |
| WAN (global) | Mamlakat, dunyo | Internet |
## Tarmoq afzalliklari
Tarmoq orqali fayllar, printer va internet aloqasidan birgalikda foydalanish, xabar almashish va bir hujjat ustida birgalikda ishlash mumkin.
""",
            """
## Internet qanday ishlaydi?
- **Provayder** — foydalanuvchilarni internetga ulash xizmatini ko‘rsatuvchi tashkilot (masalan, Uztelecom).
- **IP-manzil** — tarmoqdagi har bir qurilmaning noyob raqamli manzili (masalan, `192.168.1.10`).
- **Domen nomi** — IP-manzilni eslab qolish oson bo‘lgan matnli ko‘rinishi (masalan, `ziyonet.uz`).
- **DNS** — domen nomlarini IP-manzillarga aylantiruvchi xizmat.
- **Protokol** — tarmoqda ma’lumot almashish qoidalari to‘plami (HTTP, HTTPS, SMTP).
## Sayt manzilining tuzilishi
Manzil `https://www.ziyonet.uz/uz/library` quyidagi qismlardan iborat:
| Qism | Ma’nosi |
| `https://` | Protokol (S — xavfsiz, shifrlangan ulanish) |
| `www` | Subdomen |
| `ziyonet` | Domen nomi |
| `.uz` | Yuqori darajali domen (davlat yoki soha) |
| `/uz/library` | Sayt ichidagi sahifa yo‘li |
Yuqori darajali domenlarga misollar: `.uz` — O‘zbekiston, `.ru` — Rossiya, `.com` — tijorat, `.org` — tashkilotlar, `.edu` — ta’lim. Kompyuter IP-manzilini bilish uchun buyruqlar satrida `ipconfig` buyrug‘ini berish mumkin.
""",
            """
## Internet xizmatlari
- **Butunjahon o‘rgimchak to‘ri** — internetdagi bir-biriga havolalar orqali bog‘langan veb-sahifalar tizimi (WWW).
| Xizmat | Vazifasi | Misollar |
| Veb-saytlar | Ma’lumotlarni sahifalar ko‘rinishida taqdim etish | ziyonet.uz, uz.wikipedia.org |
| Qidiruv tizimlari | Kalit so‘z bo‘yicha ma’lumot topish | Google, Yandex |
| Elektron pochta | Xat va fayl yuborish | Gmail, Mail.ru |
| Messenjerlar | Tezkor xabar, qo‘ng‘iroq | Telegram, WhatsApp |
| Bulutli xizmatlar | Fayl saqlash va birga ishlash | Google Disk, OneDrive |
| Videoaloqa | Onlayn dars, uchrashuv | Zoom, Google Meet |
| Davlat xizmatlari | Ariza, ma’lumotnoma olish | my.gov.uz |
| Onlayn ta’lim | Video darslar, kurslar | YouTube, Coursera |
## Internetga ulanish usullari
Kompyuter internetga kabel (Ethernet), Wi-Fi yoki mobil internet (4G/5G) orqali ulanadi. Ulanish tezligi megabit sekundda (Mbit/s) o‘lchanadi. IT-servis mutaxassisi ulanish yo‘qolganda avval kabel va Wi-Fi holatini, keyin `ping google.com` buyrug‘i bilan aloqani tekshiradi.
""",
        ],
        'oldingi': ['Bulutli xotira qanday ishlaydi?',
                    'Faylni havola orqali qanday ulashish mumkin?',
                    'Router nima vazifani bajaradi?'],
        'savollar': ['Lokal va global tarmoq farqi nimada?',
                     'IP-manzil va domen nomi nima?',
                     'DNS xizmati nima uchun kerak?',
                     'Sayt manzili qanday qismlardan iborat?',
                     'Internetning qanday xizmatlarini bilasiz?'],
        'testlar': [
            ('Domen nomlarini IP-manzillarga aylantiruvchi xizmat:',
             ['HTTP', 'DNS', 'USB', 'LAN'], 'b'),
            ('Bitta bino ichidagi kompyuterlarni bog‘lovchi tarmoq:',
             ['WAN', 'MAN', 'Internet', 'LAN'], 'd'),
            ('Manzildagi «https» qismidagi «S» harfi nimani bildiradi?',
             ['Xavfsiz (shifrlangan) ulanish', 'Sayt', 'Server', 'Subdomen'], 'a'),
            ('O‘zbekistonning yuqori darajali domeni:',
             ['.uz', '.us', '.ua', '.uk'], 'a'),
            ('Kompyuterning IP-manzilini ko‘rsatuvchi buyruq:',
             ['winver', 'paint', 'ipconfig', 'notepad'], 'c'),
        ],
        'mustaqil': ['O‘zbekistondagi 10 ta foydali sayt (ta’lim, davlat xizmatlari, yangiliklar) manzilini yozib, '
                     'har birining qismlarini (protokol, domen, zona) ajrating.',
                     'Uyingiz yoki texnikumdagi internet ulanish turi va tezligini aniqlang (speedtest.net).'],
    },
    # ------------------------------------------------------------------ 23
    {
        'type': 'A',
        'title': 'Internet brauzerlari va qidiruv tizimlaridan foydalanish',
        'reja': ['Brauzer oynasi va asosiy imkoniyatlari',
                 'Amaliy ish: qidiruv tizimida samarali qidirish',
                 'Axborot ishonchliligini baholash va yuklab olish'],
        'maqsad': 'O‘quvchilarda brauzerda yorliqlar, xatcho‘plar va tarix bilan ishlash, qidiruv tizimida kalit '
                  'so‘zlar va operatorlar yordamida samarali qidirish hamda topilgan axborot ishonchliligini baholash '
                  'ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar brauzerni sozlaydi, kerakli saytni xatcho‘pga qo‘shadi, qidiruv operatorlari bilan '
                  'aniq natija oladi va manbaning ishonchliligini mezonlar bo‘yicha baholaydi.',
        'vosita': 'Internetga ulangan kompyuterlar, Google Chrome yoki Microsoft Edge brauzeri, topshiriq kartochkasi',
        'bolimlar': [
            """
## Brauzer
- **Brauzer** — internetdagi veb-sahifalarni ko‘rish va ular bilan ishlash uchun mo‘ljallangan dastur.
- **Xatcho‘p** — keyinchalik tez ochish uchun saqlab qo‘yilgan sayt havolasi (закладка).
- **Tarix** — brauzerda ochilgan sahifalarning sana bo‘yicha ro‘yxati.
Mashhur brauzerlar: Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, Yandex Browser.
| Amal | Tugmalar |
| Yangi yorliq (vkladka) | `Ctrl + T` |
| Yorliqni yopish | `Ctrl + W` |
| Yopilgan yorliqni qayta ochish | `Ctrl + Shift + T` |
| Xatcho‘pga qo‘shish | `Ctrl + D` |
| Tarix | `Ctrl + H` |
| Sahifani yangilash | `F5` |
| Sahifada so‘z qidirish | `Ctrl + F` |
| Inkognito oyna | `Ctrl + Shift + N` |
""",
            """
## Qidiruv tizimi
- **Qidiruv tizimi** — internetdagi sahifalarni kalit so‘zlar bo‘yicha topib beruvchi xizmat (Google, Yandex).
- **Kalit so‘z** — qidirilayotgan mavzuning asosiy mazmunini ifodalovchi so‘z yoki so‘z birikmasi.
## Qidiruv operatorlari
| Operator | Misol | Natija |
| Qo‘shtirnoq | `"axborot texnologiyalari"` | Aynan shu ibora |
| Minus | `kompyuter -o‘yin` | «o‘yin» so‘zisiz natijalar |
| site: | `ariza namunasi site:gov.uz` | Faqat gov.uz saytlaridan |
| filetype: | `informatika filetype:pdf` | Faqat PDF fayllar |
| OR | `fleshka OR USB` | Ikki so‘zdan biri bor sahifalar |
## Topshiriq
- **Qadam 1.** Brauzerda google.com saytini oching va interfeys tilini o‘zbek tiliga o‘zgartiring.
- **Qadam 2.** «Kompyuterning asosiy qurilmalari» mavzusini oddiy, so‘ng qo‘shtirnoqda qidiring; natijalar sonini solishtiring.
- **Qadam 3.** Faqat ziyonet.uz saytidan «informatika» bo‘yicha materiallarni toping.
- **Qadam 4.** «Axborot texnologiyalari» bo‘yicha PDF qo‘llanmani `filetype:pdf` bilan toping.
- **Qadam 5.** «Rasmlar» bo‘limida «Инструменты» → «Права на использование» orqali erkin foydalanish mumkin bo‘lgan rasmni toping.
- **Qadam 6.** Eng foydali sahifani `Ctrl + D` bilan xatcho‘pga qo‘shing.
""",
            """
## Axborot ishonchliligini baholash
Internetdagi har bir ma’lumot ham to‘g‘ri emas. Manbani baholash uchun quyidagi savollarga javob bering:
| Mezon | Savol |
| Muallif | Sahifani kim yozgan? Tashkilot yoki mutaxassismi? |
| Sana | Ma’lumot qachon e’lon qilingan, eskirmaganmi? |
| Manba | Rasmiy sayt (`.gov.uz`, `.edu`) yoki shaxsiy blogmi? |
| Tasdiq | Shu ma’lumot boshqa ishonchli saytlarda ham bormi? |
| Maqsad | Sahifa xabar beradimi yoki biror narsa sotmoqchimi? |
## Fayllarni yuklab olish
- Faylni faqat rasmiy saytlardan yuklab oling; «Скачать» degan yolg‘on reklama tugmalarini bosmang.
- Yuklangan fayllar odatda «Загрузки» papkasiga tushadi, ularni brauzerda `Ctrl + J` bilan ko‘rish mumkin.
- Yuklangan faylni ochishdan oldin uning kengaytmasini tekshiring: hujjat o‘rniga `.exe` kelsa, uni ochmang.
## Brauzer xavfsizligi
Manzil satridagi qulf belgisi ulanish shifrlanganini bildiradi. Begona kompyuterda inkognito oynadan foydalaning va ishdan keyin hisoblardan chiqing. Brauzer va uning kengaytmalarini muntazam yangilab turing.
""",
        ],
        'oldingi': ['Internet nima?',
                    'Sayt manzili qanday qismlardan iborat?',
                    'Qanday internet xizmatlarini bilasiz?'],
        'savollar': ['Qanday brauzerlarni bilasiz?',
                     'Xatcho‘p va tarixning farqi nimada?',
                     'Qo‘shtirnoq va site: operatorlari qanday ishlaydi?',
                     'Internetdagi ma’lumot ishonchliligini qanday tekshirasiz?',
                     'Yopilgan yorliqni qanday qayta ochish mumkin?'],
        'testlar': [
            ('Sahifani xatcho‘pga qo‘shuvchi tugmalar birikmasi:',
             ['Ctrl + H', 'Ctrl + D', 'Ctrl + J', 'Ctrl + W'], 'b'),
            ('Faqat PDF fayllarni qidirish uchun qaysi operator ishlatiladi?',
             ['site:', 'OR', 'filetype:', 'minus (-)'], 'c'),
            ('Aynan bir iborani qidirish uchun so‘zlar qanday yoziladi?',
             ['Qo‘shtirnoq ichida', 'Katta harflar bilan', 'Vergul bilan', 'Qavs ichida'], 'a'),
            ('Yopilgan yorliqni qayta ochuvchi birikma:',
             ['Ctrl + T', 'Ctrl + N', 'Ctrl + F5', 'Ctrl + Shift + T'], 'd'),
            ('Internetdagi sahifalarni ko‘rish uchun mo‘ljallangan dastur:',
             ['Brauzer', 'Arxivator', 'Drayver', 'Matn muharriri'], 'a'),
        ],
        'mustaqil': ['Qidiruv operatorlaridan foydalanib, «Axborot texnologiyalari» faniga oid 5 ta ishonchli manba '
                     'toping va har birini mezonlar bo‘yicha baholang.',
                     'Brauzeringizda o‘quv saytlari uchun xatcho‘plar papkasini yarating (kamida 8 ta sayt).'],
    },
    # ------------------------------------------------------------------ 24
    {
        'type': 'N',
        'title': 'Elektron axborot almashinuvi va uning vositalari',
        'reja': ['Elektron axborot almashinuvi tushunchasi',
                 'Elektron pochta va uning ishlash tamoyili',
                 'Messenjerlar, ijtimoiy tarmoqlar va elektron hujjat aylanishi tizimlari'],
        'maqsad': 'O‘quvchilarga elektron axborot almashinuvi tushunchasi, elektron pochta manzili tuzilishi va '
                  'ishlash tamoyili, messenjerlar, videoaloqa va elektron hujjat aylanishi tizimlarini tushuntirish.',
        'natija': 'O‘quvchilar axborot almashinuvi vositalarini taqqoslaydi, elektron pochta manzilini to‘g‘ri yozadi '
                  'va rasmiy hamda norasmiy yozishma uchun mos vositani tanlaydi.',
        'bolimlar': [
            """
## Elektron axborot almashinuvi
- **Elektron axborot almashinuvi** — matn, hujjat, rasm, ovoz va videoni tarmoq orqali elektron ko‘rinishda yuborish va qabul qilish.
Axborot almashinuvi ikki xil bo‘ladi: real vaqtda (qo‘ng‘iroq, videoaloqa, chat) va kechiktirilgan (elektron pochta, xabar qoldirish).
| Vosita | Tezligi | Qayerda qulay |
| Elektron pochta | Bir necha soniya | Rasmiy yozishma, hujjat yuborish |
| Messenjer | Darhol | Tezkor muloqot, guruh suhbatlari |
| Videoaloqa | Real vaqt | Onlayn dars, yig‘ilish |
| Bulutli hujjatlar | Real vaqt | Hujjat ustida birga ishlash |
| Elektron hujjat aylanishi tizimlari | Darhol | Tashkilotlar orasidagi rasmiy hujjatlar |
""",
            """
## Elektron pochta
- **Elektron pochta** — internet orqali xat va fayllarni yuborish va qabul qilish xizmati (e-mail).
- **Pochta qutisi** — pochta serverida foydalanuvchining xatlari saqlanadigan shaxsiy joy.
## Pochta manzilining tuzilishi
Manzil `karimov.ali@gmail.com` uch qismdan iborat:
| Qism | Ma’nosi |
| `karimov.ali` | Foydalanuvchi nomi (login) |
| `@` | «Kuchukcha» (at) belgisi, «da» degan ma’noni beradi |
| `gmail.com` | Pochta xizmati domeni |
Manzilda probel, kirill harflari va o‘zbekcha `‘` belgisi ishlatilmaydi. Rasmiy yozishma uchun ism va familiyadan iborat manzil tanlanadi, `superboy2008` kabi nomlar emas.
## Xat qismlari
| Maydon | Vazifasi |
| Кому (To) | Asosiy qabul qiluvchi manzili |
| Копия (Cc) | Xabardor bo‘lishi kerak bo‘lgan qabul qiluvchilar |
| Скрытая копия (Bcc) | Boshqalarga ko‘rinmaydigan qabul qiluvchilar |
| Тема (Mavzu) | Xatning qisqa mazmuni |
| Matn | Xatning asosiy qismi |
| Ilova (qisqich belgisi) | Biriktirilgan fayllar |
""",
            """
## Messenjerlar va ijtimoiy tarmoqlar
- **Messenjer** — internet orqali tezkor matnli, ovozli va video xabar almashish dasturi (Telegram, WhatsApp).
O‘zbekistonda eng ko‘p ishlatiladigan messenjer Telegram: unda shaxsiy suhbatlar, guruhlar (200 000 a’zogacha) va kanallar mavjud. Telegram orqali 2 GB gacha bo‘lgan fayllarni yuborish mumkin.
## Elektron hujjat aylanishi tizimlari
Davlat tashkilotlari va korxonalarda rasmiy hujjatlar maxsus tizimlar orqali yuboriladi. O‘zbekistonda «E-hujjat» (Ijro.gov.uz) tizimi va «Yagona interaktiv davlat xizmatlari portali» (my.gov.uz) shunday vositalardir. Ularda hujjatlar elektron raqamli imzo bilan tasdiqlanadi.
## Elektron muloqot odobi
- **Netiket** — internetda muloqot qilishning odob-axloq qoidalari.
- Xatda salomlashish, o‘zini tanishtirish va xayrlashish bo‘lsin.
- Mavzu maydonini albatta to‘ldiring: «Amaliy ish 25 – Karimov A.».
- Faqat katta harflar bilan yozmang: bu baqirish deb qabul qilinadi.
- Ilova faylning hajmi va nomini tekshiring, uni xat matnida eslating.
- Kechasi va dam olish kunlari rasmiy xabar yubormaslikka harakat qiling.
""",
        ],
        'oldingi': ['Brauzerda xatcho‘p qanday qo‘shiladi?',
                    'Qidiruv operatorlariga misol keltiring.',
                    'Internetning qanday xizmatlarini bilasiz?'],
        'savollar': ['Elektron axborot almashinuvining qanday vositalari bor?',
                     'Elektron pochta manzili qanday qismlardan iborat?',
                     'Копия va Скрытая копия maydonlarining farqi nimada?',
                     'Messenjer elektron pochtadan qanday farq qiladi?',
                     'Netiket qoidalaridan beshtasini ayting.'],
        'testlar': [
            ('Elektron pochta manzilida foydalanuvchi nomi va domenni ajratuvchi belgi:',
             ['#', '@', '&', '%'], 'b'),
            ('Boshqa qabul qiluvchilarga ko‘rinmaydigan nusxa maydoni:',
             ['Кому', 'Тема', 'Копия', 'Скрытая копия'], 'd'),
            ('Internetda muloqot qilishning odob-axloq qoidalari:',
             ['Netiket', 'Protokol', 'Domen', 'Brauzer'], 'a'),
            ('Quyidagilardan qaysi biri messenjer?',
             ['Gmail', 'Google Disk', 'Telegram', 'Paint'], 'c'),
            ('Davlat xizmatlaridan elektron foydalanish portali:',
             ['my.gov.uz', 'youtube.com', 'wikipedia.org', 'canva.com'], 'a'),
        ],
        'mustaqil': ['Elektron pochta, messenjer va videoaloqa vositalarini 5 ta mezon bo‘yicha taqqoslovchi jadval '
                     'tuzing.',
                     'Rasmiy elektron xat namunasini (o‘qituvchiga amaliy ish yuborish) netiket qoidalariga mos yozing.'],
    },
    # ------------------------------------------------------------------ 25
    {
        'type': 'A',
        'title': 'Elektron pochta va boshqa vositalar orqali axborot almashish',
        'reja': ['Elektron pochta qutisini ochish va sozlash',
                 'Amaliy ish: ilovali xat yuborish, javob berish va yo‘naltirish',
                 'Telegram va bulutli havola orqali fayl almashish'],
        'maqsad': 'O‘quvchilarda elektron pochta qutisini ochish, xat yozish, fayl biriktirish, xatga javob berish, '
                  'yo‘naltirish, papkalar bilan ishlash hamda messenjer va bulutli havola orqali fayl almashish '
                  'ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar o‘qituvchiga ilovali rasmiy xat yuboradi, kelgan xatga javob beradi, katta faylni '
                  'bulutli havola orqali ulashadi va spam xatlarni ajratadi.',
        'vosita': 'Internetga ulangan kompyuterlar, Gmail (o‘quv hisoblari), Telegram Desktop, Google Disk',
        'bolimlar': [
            """
## Pochta qutisini ochish
- **Qadam 1.** accounts.google.com saytida «Создать аккаунт» → «Для себя» ni tanlang.
- **Qadam 2.** Ism, familiya va tug‘ilgan sanani kiriting.
- **Qadam 3.** Ism va familiyadan iborat manzil tanlang: `ali.karimov.2026@gmail.com`.
- **Qadam 4.** Kamida 12 belgili kuchli parol o‘ylab toping (bu haqda 29-mavzuda batafsil).
- **Qadam 5.** Telefon raqamingizni qo‘shing: parol unutilganda hisobni shu orqali tiklaysiz.
16 yoshga to‘lmagan o‘quvchilar hisobni ota-ona ruxsati bilan ochadi. Darsda o‘qituvchi tayyorlab qo‘ygan o‘quv hisoblaridan foydalanish ham mumkin.
## Gmail oynasi
| Papka | Vazifasi |
| Входящие (Kiruvchi) | Kelgan xatlar |
| Отправленные (Yuborilgan) | Siz yuborgan xatlar |
| Черновики (Qoralama) | Tugallanmagan xatlar |
| Спам | Shubhali va reklama xatlari |
| Корзина | O‘chirilgan xatlar (30 kun saqlanadi) |
""",
            """
## Ilovali xat yuborish
- **Qadam 1.** «Написать» (Xat yozish) tugmasini bosing.
- **Qadam 2.** «Кому» maydoniga o‘qituvchining manzilini yozing.
- **Qadam 3.** «Тема» maydoniga yozing: `Amaliy ish 25 – Familiya Ism`.
- **Qadam 4.** Xat matnini yozing: salomlashish, xat maqsadi, xayrlashish va imzo.
- **Qadam 5.** Qisqich belgili «Прикрепить файл» tugmasi orqali 14-darsda saqlagan `Ariza_Familiya.pdf` faylini biriktiring.
- **Qadam 6.** Fayl to‘liq yuklanganini tekshirib, «Отправить» tugmasini bosing.
## Xat namunasi
| Qism | Matn |
| Salom | Assalomu alaykum, hurmatli Oydin opa! |
| Asosiy qism | 25-amaliy ish bo‘yicha arizamni PDF formatida ilova qilib yubormoqdaman. |
| Xayrlashish | Hurmat bilan, |
| Imzo | Karimov Ali, 1-kurs, KT-25 guruh |
## Javob berish va yo‘naltirish
- **Javob berish** — kelgan xat muallifiga shu xat davomida javob yozish (Ответить).
- **Yo‘naltirish** — kelgan xatni uchinchi shaxsga qayta yuborish (Переслать).
«Ответить всем» tugmasi xatni olgan barcha qabul qiluvchilarga javob yuboradi. Uni ehtiyotkorlik bilan ishlating.
Gmail’da 25 MB dan katta fayllar avtomatik Google Disk havolasiga aylantiriladi.
""",
            """
## Telegram orqali fayl almashish
- **Qadam 1.** Telegram Desktop’da o‘qituvchi bilan shaxsiy suhbatni yoki guruh chatini oching.
- **Qadam 2.** Qisqich belgisini bosib, «Файл» ni tanlang va hujjatni yuboring. Rasmni sifati yo‘qolmasligi uchun «siqmasdan» (fayl sifatida) yuboring.
- **Qadam 3.** «Избранное» (Saqlanganlar) suhbatidan o‘zingizga eslatma va fayllar saqlash uchun foydalaning.
## Bulutli havola orqali ulashish
Katta hajmdagi video yoki ko‘p fayllarni xatga biriktirish o‘rniga Google Diskka yuklab, havolasini yuboring. Havola uchun «Читатель» huquqini tanlang.
## Spam va shubhali xatlar
- **Spam** — oluvchining roziligisiz ommaviy yuboriladigan reklama yoki firibgarlik xatlari.
- Notanish yuboruvchidan kelgan ilovani ochmang.
- «Siz yutdingiz», «hisobingiz bloklandi» kabi xatlardagi havolalarni bosmang.
- Shubhali xatni «Пожаловаться на спам» tugmasi bilan spamga yuboring.
## Baholash
Ish quyidagilar bo‘yicha baholanadi: mavzu maydoni to‘g‘ri (1 ball), xat odob qoidalariga mos (1 ball), fayl biriktirilgan (1 ball), kelgan xatga javob berilgan (1 ball), bulutli havola to‘g‘ri huquq bilan ulashilgan (1 ball).
""",
        ],
        'oldingi': ['Elektron pochta manzili qanday qismlardan iborat?',
                    'Netiket nima?',
                    'Копия va Скрытая копия farqi nimada?'],
        'savollar': ['Gmail’da qanday papkalar bor?',
                     'Xatga fayl qanday biriktiriladi?',
                     '«Ответить» va «Переслать» farqi nimada?',
                     'Katta hajmdagi faylni qanday yuborish qulay?',
                     'Spam xatni qanday aniqlash va unga qanday munosabatda bo‘lish kerak?'],
        'testlar': [
            ('Kelgan xatni uchinchi shaxsga qayta yuborish:',
             ['Ответить', 'Переслать', 'Удалить', 'Архивировать'], 'b'),
            ('Tugallanmagan xatlar saqlanadigan papka:',
             ['Входящие', 'Спам', 'Отправленные', 'Черновики'], 'd'),
            ('Gmail’da qanday hajmdan katta fayllar Google Disk havolasiga aylanadi?',
             ['1 MB', '5 MB', '25 MB', '2 GB'], 'c'),
            ('Oluvchining roziligisiz ommaviy yuboriladigan reklama xatlari:',
             ['Spam', 'Qoralama', 'Ilova', 'Netiket'], 'a'),
            ('Xatga fayl biriktirish tugmasining belgisi:',
             ['Qisqich', 'Lupa', 'Yulduzcha', 'Savat'], 'a'),
        ],
        'mustaqil': ['Do‘stingiz bilan elektron pochta orqali yozishma o‘tkazing: ilovali xat, javob va yo‘naltirish; '
                     'natijani skrinshotlar bilan ko‘rsating.',
                     'Gmail’da «O‘qish» va «Shaxsiy» yorliqlarini (papkalarini) yarating va xatlarni saralang.'],
    },
]
