"""11–15-mavzular: formatlash, raqamli materiallarni takomillashtirish, saqlash formatlari va zaxira nusxa.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 11
    {
        'type': 'A',
        'title': 'Matn va hujjatlarni tahrirlash hamda formatlash',
        'reja': ['Belgi (shrift) formatlash',
                 'Amaliy ish: abzats, ro‘yxat va uslublar bilan formatlash',
                 'Sahifani formatlash: hoshiya, sahifa raqami, kolontitul'],
        'maqsad': 'O‘quvchilarda hujjat matnini shrift, abzats, ro‘yxat va uslublar yordamida formatlash hamda sahifa '
                  'parametrlarini sozlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar tayyor matnni talablarga mos formatlaydi: sarlavhalarga uslub beradi, ro‘yxat tuzadi, '
                  'sahifa raqamini qo‘yadi va avtomatik mundarija yaratadi.',
        'vosita': 'Microsoft Word o‘rnatilgan kompyuterlar, formatlanmagan namunaviy matn fayli, proyektor',
        'bolimlar': [
            """
## Shrift parametrlari
- **Shrift** — harflar va belgilarning bir xil uslubdagi to‘plami (Times New Roman, Arial, Calibri).
- **Kegl** — shrift o‘lchami, punktlarda (pt) o‘lchanadi.
| Parametr | Tugmalar | Misol |
| Qalin | `Ctrl + B` | **muhim so‘z** |
| Kursiv (qiya) | `Ctrl + I` | atama yoki izoh |
| Tagiga chizilgan | `Ctrl + U` | havola |
| O‘lchamni kattalashtirish | `Ctrl + ]` | sarlavha |
| O‘lchamni kichraytirish | `Ctrl + [` | izoh |
Shrift rangini «Главная» → «Цвет шрифта» tugmasi, matn fonini esa «Цвет выделения текста» (marker) tugmasi orqali o‘zgartirish mumkin. Rasmiy hujjatlarda faqat qora rang ishlatiladi.
## «Format bo‘yicha namuna» asbobi
«Формат по образцу» (cho‘tka belgisi) bitta matn bo‘lagi formatini boshqasiga ko‘chiradi: avval namuna matnni ajrating, cho‘tkani bosing, so‘ng formatlanadigan matnni ajrating.
""",
            """
## Abzatsni formatlash
- **Abzats** — `Enter` tugmasi bosilgunga qadar yozilgan matn bo‘lagi.
- **Xatboshi** — abzats birinchi qatorining o‘ngga surilishi.
«Главная» → «Абзац» oynasida (kichik strelka) quyidagilar sozlanadi: tekislash, chap va o‘ng chekinish, birinchi qator chekinishi (xatboshi 1,25 sm), abzatsdan oldin va keyingi oraliq, qatorlar oralig‘i (1,0; 1,15; 1,5).
## Ishni bajarish tartibi
- **Qadam 1.** Namunaviy matnni oching va butun matnni ajratib (`Ctrl + A`), Times New Roman 14 pt, qatorlar oralig‘i 1,5 qiling.
- **Qadam 2.** Barcha abzatslarga 1,25 sm xatboshi bering va ikki tomondan tekislang.
- **Qadam 3.** Asosiy sarlavhaga «Заголовок 1», kichik sarlavhalarga «Заголовок 2» uslubini qo‘llang.
- **Qadam 4.** Sanab o‘tilgan qismni ajratib, «Маркеры» tugmasi bilan belgili ro‘yxatga aylantiring.
- **Qadam 5.** Ketma-ket bajariladigan bosqichlarni «Нумерация» tugmasi bilan raqamli ro‘yxatga aylantiring.
## Uslublar afzalligi
- **Uslub** — shrift va abzats parametrlarining nom bilan saqlangan to‘plami (masalan, «Заголовок 1»).
Uslub o‘zgartirilsa, u qo‘llangan barcha sarlavhalar bir zumda o‘zgaradi. Bundan tashqari sarlavha uslublari asosida avtomatik mundarija yaratiladi.
""",
            """
## Sahifa parametrlari
| Sozlama | Qayerda | Odatiy qiymat |
| Hoshiyalar | «Макет» → «Поля» | Chap 3, o‘ng 1,5, yuqori 2, pastki 2 sm |
| Yo‘nalish | «Макет» → «Ориентация» | Kitob (portret) yoki albom |
| O‘lcham | «Макет» → «Размер» | A4 (21×29,7 sm) |
| Sahifa raqami | «Вставка» → «Номер страницы» | Pastki qism, markazda |
- **Kolontitul** — har bir sahifaning yuqori yoki pastki qismida takrorlanadigan matn (hujjat nomi, sahifa raqami).
## Avtomatik mundarija
- **Qadam 1.** Kursorni hujjat boshiga qo‘ying.
- **Qadam 2.** «Ссылки» → «Оглавление» → «Автособираемое оглавление» ni tanlang.
- **Qadam 3.** Matn o‘zgargach, mundarija ustida o‘ng tugma → «Обновить поле» orqali yangilang.
## Baholash
Ish quyidagi bandlar bo‘yicha baholanadi: shrift va abzats talablarga mos (1 ball), sarlavhalarga uslub berilgan (1 ball), ro‘yxatlar to‘g‘ri tuzilgan (1 ball), sahifa raqami qo‘yilgan (1 ball), avtomatik mundarija yaratilgan (1 ball).
""",
        ],
        'oldingi': ['Tahrirlash va formatlashning farqi nimada?',
                    'Almashinuv buferi nima?',
                    'Matn qanday ajratiladi?'],
        'savollar': ['Matnni qalin va kursiv qilish uchun qaysi tugmalar ishlatiladi?',
                     'Abzats va xatboshi nima?',
                     'Uslubdan foydalanishning qanday afzalliklari bor?',
                     'Sahifa raqami qanday qo‘yiladi?',
                     'Avtomatik mundarija qanday yaratiladi?'],
        'testlar': [
            ('Matnni qalin qiluvchi tugmalar birikmasi:',
             ['Ctrl + I', 'Ctrl + U', 'Ctrl + B', 'Ctrl + Q'], 'c'),
            ('Shrift o‘lchami qanday birlikda o‘lchanadi?',
             ['Punkt (pt)', 'Piksel', 'Santimetr', 'Bayt'], 'a'),
            ('Har bir sahifaning yuqori yoki pastki qismida takrorlanadigan matn:',
             ['Xatboshi', 'Uslub', 'Abzats', 'Kolontitul'], 'd'),
            ('Avtomatik mundarija qaysi yorliqda yaratiladi?',
             ['Главная', 'Ссылки', 'Вставка', 'Вид'], 'b'),
            ('Bir matn bo‘lagi formatini boshqasiga ko‘chiruvchi asbob:',
             ['Формат по образцу', 'Найти и заменить', 'Орфография', 'Таблица'], 'a'),
        ],
        'mustaqil': ['3–4 sahifali referat tayyorlab, unga sarlavha uslublari, sahifa raqami va avtomatik '
                     'mundarija qo‘shing.',
                     'Bitta matnni uch xil uslubda (rasmiy, e’lon, taklifnoma) formatlab, farqlarini izohlang.'],
    },
    # ------------------------------------------------------------------ 12
    {
        'type': 'A',
        'title': 'Raqamli materiallarni tahrirlash va takomillashtirish',
        'reja': ['Rasmlarni tahrirlash: qirqish, o‘lcham, aylantirish',
                 'Amaliy ish: taqdimotni tahrirlash va takomillashtirish',
                 'Raqamli material sifatini tekshirish mezonlari'],
        'maqsad': 'O‘quvchilarda tayyor rasm va taqdimotlarni tahrirlash — qirqish, o‘lchamini o‘zgartirish, '
                  'yorqinlikni sozlash, slaydlarni tartiblash, o‘tish effektlari va animatsiya qo‘shish ko‘nikmasini '
                  'shakllantirish.',
        'natija': 'O‘quvchilar rasmni qirqib, siqib saqlaydi, taqdimot slaydlarini qayta tartiblaydi, dizayn va '
                  'animatsiya qo‘shadi hamda material sifatini mezonlar bo‘yicha baholaydi.',
        'vosita': 'Paint, «Фотографии» ilovasi, PowerPoint, namunaviy rasm va taqdimot fayllari',
        'bolimlar': [
            """
## Rasmni tahrirlash
Internetdan yoki fotoapparatdan olingan rasm ko‘pincha hujjatga to‘g‘ridan-to‘g‘ri mos kelmaydi: u juda katta, qorong‘i yoki ortiqcha qismlarga ega bo‘lishi mumkin.
- **Qirqish** — rasmning keraksiz chetlarini olib tashlash amali.
- **Ruxsat** — rasmning eni va bo‘yidagi piksellar soni (masalan, 1920×1080).
| Amal | Paint’da | «Фотографии» ilovasida |
| Qirqish | «Выделить» → «Обрезать» | «Изменить» → «Обрезка» |
| O‘lchamni o‘zgartirish | «Изменить размер» (foiz yoki piksel) | «…» → «Изменить размер» |
| Aylantirish | «Повернуть» | Aylantirish tugmasi |
| Yorqinlik va rang | Yo‘q | «Корректировка» bo‘limi |
Rasm o‘lchami kichraytirilsa, fayl hajmi ham kamayadi. Elektron pochta yoki saytga joylash uchun eni 1200–1600 piksel yetarli.
""",
            """
## Taqdimotni tahrirlash
- **Qadam 1.** Namunaviy taqdimotni oching va chap paneldagi slaydlarni sudrab, mantiqiy tartibga keltiring.
- **Qadam 2.** «Конструктор» yorlig‘ida yagona dizayn mavzusini tanlang: barcha slaydlar bir xil uslubda bo‘lsin.
- **Qadam 3.** Ortiqcha matnni qisqartiring: bitta slaydda 5–6 qatordan ko‘p matn bo‘lmasin.
- **Qadam 4.** Rasmni tanlab, «Формат рисунка» → «Обрезка» orqali qirqing va «Сжать рисунки» bilan siqing.
- **Qadam 5.** «Переходы» yorlig‘ida slaydlar o‘rtasidagi o‘tish effektini tanlang.
- **Qadam 6.** «Анимация» yorlig‘ida sarlavha va rasmlarga sodda animatsiya bering.
- **Qadam 7.** `F5` tugmasi bilan taqdimotni boshidan namoyish qilib tekshiring.
- **Animatsiya** — slayd ichidagi obyektning paydo bo‘lishi yoki harakatlanish effekti.
- **O‘tish effekti** — bir slayddan ikkinchisiga o‘tishdagi vizual effekt.
Effektlarni me’yorida ishlatish kerak: juda ko‘p harakat tinglovchining diqqatini mazmundan chalg‘itadi.
""",
            """
## Raqamli material sifati mezonlari
| Mezon | Savol |
| Mazmun | Ma’lumot to‘g‘ri, aniq va to‘liqmi? |
| Tuzilma | Sarlavha, asosiy qism va xulosa bormi? |
| Dizayn | Ranglar va shriftlar bir xilmi, matn o‘qiladimi? |
| Rasm sifati | Rasmlar tiniq, cho‘zilmagan, mavzuga mosmi? |
| Hajm | Fayl yuborish uchun haddan tashqari katta emasmi? |
| Mualliflik | Boshqa manbalardan olingan ma’lumotlarga havola berilganmi? |
## Takomillashtirish
- **Qadam.** Imlo xatolarini tuzating va qisqa, tushunarli jumlalar yozing.
- **Qadam.** Matnni sxema, jadval yoki diagramma bilan almashtiring: ko‘rgazmali material yaxshi esda qoladi.
- **Qadam.** Kontrastni tekshiring: oq fonda to‘q, to‘q fonda och rangli matn.
- **Qadam.** Oxirgi slaydga manbalar ro‘yxatini qo‘shing.
Juftlikdagi o‘quvchilar bir-birining taqdimotini jadvaldagi mezonlar bo‘yicha 5 ballik tizimda baholaydi va takomillashtirish bo‘yicha bitta taklif yozadi.
""",
        ],
        'oldingi': ['Paint dasturida qanday asboblar bor?',
                    'Rastr grafika nima?',
                    'Taqdimot va slayd tushunchalarini izohlang.'],
        'savollar': ['Rasmni qirqish nima uchun kerak?',
                     'Rasm o‘lchami kichraytirilsa, fayl hajmi qanday o‘zgaradi?',
                     'Animatsiya va o‘tish effekti farqi nimada?',
                     'Bitta slaydda qancha matn bo‘lishi tavsiya etiladi?',
                     'Raqamli material sifati qanday mezonlar bo‘yicha baholanadi?'],
        'testlar': [
            ('Rasmning keraksiz chetlarini olib tashlash amali:',
             ['Aylantirish', 'Qirqish', 'Siqish', 'Bo‘yash'], 'b'),
            ('Taqdimotni boshidan namoyish qiluvchi tugma:',
             ['F5', 'F1', 'F7', 'F12'], 'a'),
            ('Slayd ichidagi obyektning harakatlanish effekti:',
             ['O‘tish effekti', 'Dizayn mavzusi', 'Animatsiya', 'Kolontitul'], 'c'),
            ('Rasmning eni va bo‘yidagi piksellar soni qanday ataladi?',
             ['Format', 'Hajm', 'Kontrast', 'Ruxsat'], 'd'),
            ('PowerPoint’da rasmlar hajmini kamaytiruvchi buyruq:',
             ['Сжать рисунки', 'Обтекание текстом', 'Повторить', 'Группировать'], 'a'),
        ],
        'mustaqil': ['Avvalgi darsda tayyorlagan taqdimotingizni sifat mezonlari bo‘yicha takomillashtiring va '
                     '«oldin–keyin» farqlarini yozing.',
                     'Telefoningizdagi 3 ta rasmni qirqib, o‘lchamini kichraytiring va fayl hajmlarini solishtiring.'],
    },
    # ------------------------------------------------------------------ 13
    {
        'type': 'N',
        'title': 'Elektron hujjatlarni saqlash formatlari va usullari',
        'reja': ['Fayl formati va kengaytma tushunchasi',
                 'Hujjat, rasm, audio va video formatlari',
                 'Hujjatlarni saqlash usullari va joylari'],
        'maqsad': 'O‘quvchilarga fayl formati, kengaytma tushunchalari, eng ko‘p ishlatiladigan hujjat va multimedia '
                  'formatlari hamda hujjatlarni saqlash usullari va joylarini tushuntirish.',
        'natija': 'O‘quvchilar fayl formatini kengaytmasidan aniqlaydi, vazifaga mos formatni tanlaydi va hujjatni '
                  'qayerda saqlash qulay ekanini asoslaydi.',
        'bolimlar': [
            """
## Fayl formati
Bitta hujjatni bir necha xil ko‘rinishda saqlash mumkin. Masalan, ariza Word faylida tahrir qilinadi, PDF ko‘rinishida esa o‘zgartirib bo‘lmaydigan qilib yuboriladi.
- **Fayl formati** — fayldagi ma’lumotlarni kodlash va joylashtirish usuli; fayl qaysi dasturda ochilishini belgilaydi.
- **Kengaytma** — fayl nomidan keyin nuqta bilan yoziladigan va formatni ko‘rsatuvchi belgilar (`ariza.docx`).
Windows ba’zan kengaytmani yashiradi. Uni ko‘rish uchun Provodnik’da «Вид» → «Показать» → «Расширения имён файлов» bandini yoqing.
## Hujjat formatlari
| Kengaytma | Format | Qachon ishlatiladi |
| `.docx` | Word hujjati | Tahrirlanadigan matnli hujjatlar |
| `.pdf` | Portable Document Format | Yuborish, chop etish, o‘zgarmas ko‘rinish |
| `.txt` | Oddiy matn | Formatlashsiz matn, eslatmalar |
| `.rtf` | Boy matn formati | Turli dasturlar o‘rtasida almashish |
| `.odt` | OpenDocument matni | LibreOffice hujjatlari |
| `.xlsx` | Excel jadvali | Hisob-kitob, ro‘yxatlar |
| `.pptx` | PowerPoint taqdimoti | Slaydlar |
""",
            """
## Multimedia formatlari
| Turi | Kengaytmalar | Izoh |
| Rasm | `.jpg`, `.png`, `.gif`, `.bmp` | JPG — foto, PNG — sxema va skrinshot |
| Audio | `.mp3`, `.wav`, `.ogg` | MP3 — siqilgan, WAV — siqilmagan |
| Video | `.mp4`, `.avi`, `.mkv` | MP4 — eng ko‘p qo‘llaniladi |
| Arxiv | `.zip`, `.rar`, `.7z` | Bir nechta faylni bitta siqilgan faylga jamlash |
- **Siqish** — fayl hajmini kamaytirish uchun ma’lumotlarni maxsus algoritm bilan qayta kodlash.
- **Arxiv** — bir yoki bir nechta fayl siqilgan holda joylangan bitta fayl.
## Formatni tanlash qoidalari
- Hujjat hali tahrirlanadigan bo‘lsa — `.docx`.
- Hujjat rasmiy yuborilsa yoki chop etilsa — `.pdf`.
- Ko‘p faylni bitta xatda yuborish kerak bo‘lsa — `.zip` arxiv.
- Fotosurat — `.jpg`, ekran rasmi yoki sxema — `.png`.
""",
            """
## Saqlash usullari
- **Сохранить** (`Ctrl + S`) — faylni joriy nomi va joyida saqlash; birinchi marta saqlashda nom so‘raladi.
- **Сохранить как** (`F12`) — faylni yangi nom, yangi joy yoki boshqa formatda saqlash.
- **Avtosaqlash** — dasturning hujjatni har bir necha daqiqada avtomatik saqlab borish imkoniyati.
## Saqlash joylari
| Joy | Afzalligi | Kamchiligi |
| Kompyuter diski (`C:`, `D:`) | Tez, internet kerak emas | Kompyuter buzilsa yo‘qolishi mumkin |
| Fleshka, tashqi disk | Ko‘chirish oson | Yo‘qolishi, buzilishi oson |
| Bulutli xotira (Google Disk, OneDrive) | Istalgan qurilmadan kirish, ulashish | Internet kerak |
| Tarmoq papkasi | Ofisda birgalikda ishlash | Faqat lokal tarmoqda |
Muhim hujjatlarni `C:` diskdagi ish stolida emas, alohida `D:` diskda yoki «Документы» papkasida saqlash tavsiya etiladi: operatsion tizim qayta o‘rnatilganda `C:` disk ko‘pincha tozalanadi.
""",
        ],
        'oldingi': ['Raqamli materiallarni qanday takomillashtirish mumkin?',
                    'Rasm o‘lchamini qanday kichraytirish mumkin?',
                    'Qanday hujjat turlarini bilasiz?'],
        'savollar': ['Fayl formati va kengaytma nima?',
                     'DOCX va PDF formatlarining farqi nimada?',
                     'Qachon faylni arxivlash kerak?',
                     '«Сохранить» va «Сохранить как» buyruqlarining farqi nimada?',
                     'Muhim hujjatlarni qayerda saqlash xavfsizroq?'],
        'testlar': [
            ('O‘zgarmas ko‘rinishda yuborish va chop etish uchun qulay format:',
             ['.txt', '.docx', '.pdf', '.mp3'], 'c'),
            ('Faylni yangi nom yoki formatda saqlash buyrug‘i:',
             ['Сохранить как', 'Открыть', 'Печать', 'Создать'], 'a'),
            ('Arxiv fayllarining kengaytmasi:',
             ['.png', '.zip', '.docx', '.mp4'], 'b'),
            ('Fayl nomidan keyin nuqta bilan yoziladigan va formatni ko‘rsatuvchi belgilar:',
             ['Atribut', 'Yo‘l', 'Yorliq', 'Kengaytma'], 'd'),
            ('Ekran rasmi va sxemalar uchun eng mos rasm formati:',
             ['PNG', 'MP3', 'AVI', 'TXT'], 'a'),
        ],
        'mustaqil': ['20 ta fayl kengaytmasini, ular qaysi turdagi fayl ekanini va qaysi dasturda ochilishini '
                     'jadvalga yozing.',
                     'Bitta hujjatni DOCX, PDF va TXT formatlarida saqlab, ularning hajmi va ko‘rinishini taqqoslang.'],
    },
    # ------------------------------------------------------------------ 14
    {
        'type': 'A',
        'title': 'Elektron hujjatlarni belgilangan formatlarda saqlash',
        'reja': ['Fayllarni to‘g‘ri nomlash qoidalari',
                 'Amaliy ish: hujjatni DOCX, PDF va boshqa formatlarda saqlash',
                 'Fayllarni arxivlash va hajmini tekshirish'],
        'maqsad': 'O‘quvchilarda elektron hujjatni to‘g‘ri nomlash, belgilangan formatlarda (DOCX, PDF, ODT, TXT) '
                  'saqlash, kengaytmalarni ko‘rsatish va fayllarni ZIP arxivga joylash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar bitta hujjatni bir nechta formatda saqlaydi, PDF faylni tekshiradi, fayllarni '
                  'arxivlaydi va fayl xususiyatlaridan hajmini aniqlaydi.',
        'vosita': 'Word, Provodnik, 7-Zip yoki Windows’ning o‘rnatilgan arxivatori, namunaviy hujjat',
        'bolimlar': [
            """
## Fayl nomlash qoidalari
Fayl nomi uning mazmunini aniq aks ettirishi kerak. «Yangi hujjat (3).docx» kabi nomlar keyinchalik faylni topishni qiyinlashtiradi.
- **Talab:** nomda hujjat turi, mavzu yoki egasi va sana bo‘lsin: `Hisobot_Oktabr_2026.docx`.
- **Talab:** probel o‘rniga pastki chiziq (_) yoki tire (-) ishlatilsin.
- **Talab:** `\\ / : * ? " < > |` belgilari Windows’da fayl nomida taqiqlangan.
- **Talab:** nom juda uzun bo‘lmasin (30–40 belgigacha).
- **Talab:** bir xil turdagi fayllar bir xil tartibda nomlansin: `01_Kirish`, `02_Asosiy`, `03_Xulosa`.
| Yomon nom | Yaxshi nom |
| `Документ1.docx` | `Ariza_Karimov_A.docx` |
| `yangi yangi oxirgi.docx` | `Referat_OT_v2.docx` |
| `rasm.png` | `Sxema_kompyuter_qurilmalari.png` |
""",
            """
## Ishni bajarish tartibi
- **Qadam 1.** Provodnik’da «Вид» → «Показать» → «Расширения имён файлов» bandini yoqing.
- **Qadam 2.** «Документы» ichida `Amaliy_14_Familiya` papkasini yarating.
- **Qadam 3.** Word’da avvalgi darsdagi arizangizni oching va `F12` tugmasini bosing.
- **Qadam 4.** «Тип файла» ro‘yxatidan «Документ Word (*.docx)» ni tanlab, `Ariza_Familiya.docx` nomi bilan saqlang.
- **Qadam 5.** Yana `F12` ni bosib, «PDF (*.pdf)» turini tanlang va saqlang. PDF faylni ochib, ko‘rinishini tekshiring.
- **Qadam 6.** Shu hujjatni «Текст OpenDocument (*.odt)» va «Обычный текст (*.txt)» formatlarida ham saqlang.
- **Qadam 7.** TXT faylni Bloknot’da ochib, formatlash (shrift, jadval) yo‘qolganini kuzating.
## Formatlarni solishtirish
| Format | Tahrir qilinadimi | Formatlash saqlanadimi | Hajmi |
| DOCX | ha | ha | o‘rtacha |
| PDF | yo‘q (maxsus dasturda) | ha | o‘rtacha |
| ODT | ha | ha | kichik |
| TXT | ha | yo‘q | eng kichik |
""",
            """
## Arxivga joylash
- **Qadam 1.** Papkadagi barcha fayllarni ajrating (`Ctrl + A`).
- **Qadam 2.** O‘ng tugma → «Сжать в ZIP-файл» (Windows 11) yoki «Отправить» → «Сжатая ZIP-папка» ni tanlang.
- **Qadam 3.** Arxivga `Amaliy_14_Familiya.zip` nomini bering.
- **Qadam 4.** Arxivni ikki marta bosib ichidagi fayllarni ko‘ring; arxivdan chiqarish uchun o‘ng tugma → «Извлечь все».
## Fayl hajmini aniqlash
Fayl ustida o‘ng tugma → «Свойства» oynasida fayl hajmi, turi, yaratilgan va o‘zgartirilgan sanasi ko‘rsatiladi.
| Birlik | Qiymati |
| 1 bayt | 8 bit |
| 1 KB (kilobayt) | 1024 bayt |
| 1 MB (megabayt) | 1024 KB |
| 1 GB (gigabayt) | 1024 MB |
| 1 TB (terabayt) | 1024 GB |
Natijalar daftarga yoziladi: har bir format uchun fayl hajmi va arxivdan oldingi hamda keyingi umumiy hajm. O‘qituvchi papkani tekshirib, nomlash qoidalariga rioya qilinganini baholaydi.
""",
        ],
        'oldingi': ['Kengaytma nima?',
                    'PDF formatining afzalligi nimada?',
                    'Arxiv nima uchun kerak?'],
        'savollar': ['Fayl nomida qaysi belgilar ishlatilmaydi?',
                     'Hujjatni PDF formatida qanday saqlash mumkin?',
                     'TXT formatida saqlanganda nima yo‘qoladi?',
                     'Fayllarni ZIP arxivga qanday joylash mumkin?',
                     'Fayl hajmini qayerdan bilish mumkin?'],
        'testlar': [
            ('Windows’da fayl nomida ishlatib bo‘lmaydigan belgi:',
             ['_', '-', '?', '2'], 'c'),
            ('Word’da «Сохранить как» oynasini ochuvchi tugma:',
             ['F12', 'F5', 'F7', 'F1'], 'a'),
            ('Formatlashni saqlamaydigan format:',
             ['DOCX', 'PDF', 'ODT', 'TXT'], 'd'),
            ('1 MB necha KB ga teng?',
             ['1000', '1024', '512', '8'], 'b'),
            ('Fayl hajmi va yaratilgan sanasini ko‘rsatuvchi oyna:',
             ['Свойства', 'Открыть с помощью', 'Переименовать', 'Вырезать'], 'a'),
        ],
        'mustaqil': ['O‘quv fanlaringiz bo‘yicha fayllar uchun yagona nomlash tizimini ishlab chiqing va 10 ta '
                     'misol yozing.',
                     'Bir nechta rasm va hujjatni ZIP arxivga joylab, siqilishdan oldingi va keyingi hajmlarini '
                     'taqqoslang.'],
    },
    # ------------------------------------------------------------------ 15
    {
        'type': 'A',
        'title': 'Raqamli materiallarning zaxira nusxasini yaratish',
        'reja': ['Zaxira nusxa tushunchasi va «3-2-1» qoidasi',
                 'Amaliy ish: fleshka va bulutga zaxira nusxa olish',
                 'Fayl tarixi va zaxira nusxadan tiklash'],
        'maqsad': 'O‘quvchilarda muhim fayllarning zaxira nusxasini tashqi qurilma va bulutli xotirada yaratish, '
                  'Windows «Fayl tarixi»ni sozlash hamda zaxira nusxadan faylni tiklash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar «3-2-1» qoidasini tushuntiradi, fayllarni fleshka va Google Diskka zaxiralaydi, '
                  'o‘chirilgan faylni zaxiradan tiklaydi.',
        'vosita': 'Internetga ulangan kompyuterlar, fleshka, Google hisobi (o‘quv), Windows «История файлов»',
        'bolimlar': [
            """
## Zaxira nusxa nima uchun kerak?
Disk buzilishi, virus, kompyuterning o‘g‘irlanishi yoki faylni tasodifan o‘chirib yuborish — bularning barchasi ma’lumot yo‘qolishiga olib keladi. Yo‘qolgan diplom ishi yoki hisobotni qayta yozish ko‘p vaqt oladi, ba’zan esa umuman imkonsiz bo‘ladi.
- **Zaxira nusxa** — asosiy ma’lumot yo‘qolganda uni tiklash uchun alohida joyda saqlanadigan nusxa (backup).
- **Tiklash** — zaxira nusxadagi fayllarni asl joyiga yoki yangi joyga qaytarish jarayoni.
## «3-2-1» qoidasi
| Raqam | Ma’nosi | Misol |
| 3 | Muhim ma’lumotning kamida 3 ta nusxasi bo‘lsin | Kompyuterda asl fayl + 2 ta zaxira |
| 2 | Nusxalar kamida 2 xil qurilmada saqlansin | Kompyuter diski va fleshka |
| 1 | Bitta nusxa boshqa joyda (masalan, bulutda) bo‘lsin | Google Disk yoki OneDrive |
Zaxira nusxa muntazam olinishi kerak: haftada bir marta yoki muhim ish tugagandan so‘ng darhol.
""",
            """
## Fleshkaga zaxira nusxa olish
- **Qadam 1.** Fleshkani ulang va Provodnik’da uning harfini aniqlang (masalan, `E:`).
- **Qadam 2.** Fleshkada `Zaxira_2026-10-28` kabi sanali papka yarating.
- **Qadam 3.** «Документы» dagi o‘quv papkangizni nusxalang (`Ctrl + C`) va zaxira papkaga qo‘ying (`Ctrl + V`).
- **Qadam 4.** Nusxalash tugagach, fayllar soni va umumiy hajmini «Свойства» oynasida asl papka bilan solishtiring.
- **Qadam 5.** Fleshkani «Безопасное извлечение» orqali chiqaring.
## Bulutga zaxira nusxa olish
- **Bulutli xotira** — fayllar internet orqali ishlab chiqaruvchining serverlarida saqlanadigan xizmat.
- **Sinxronlash** — bir nechta qurilmadagi fayllarni avtomatik bir xil holatga keltirish.
- **Qadam 1.** Brauzerda drive.google.com saytini oching va o‘quv hisobingiz bilan kiring.
- **Qadam 2.** «Создать» → «Папка» orqali `Zaxira` papkasini yarating.
- **Qadam 3.** Papkani oching va fayllarni brauzer oynasiga sudrab tashlang yoki «Загрузить файлы» ni bosing.
- **Qadam 4.** Yuklash tugaganini pastki o‘ng burchakdagi xabardan tekshiring.
Google Disk bepul 15 GB, OneDrive esa 5 GB joy beradi.
""",
            """
## Windows «Fayl tarixi»
- **Fayl tarixi** — tanlangan papkalar nusxasini tashqi diskka avtomatik saqlab boruvchi Windows vositasi.
Uni yoqish uchun: «Панель управления» → «История файлов» → tashqi diskni tanlang → «Включить». Shundan so‘ng Windows har soatda o‘zgargan fayllarni nusxalaydi va faylning eski versiyasiga qaytish imkonini beradi.
## Zaxiradan tiklashni sinash
- **Qadam 1.** O‘quv papkangizdagi bitta faylni o‘chiring va savatni ham tozalang (faqat o‘quv fayli!).
- **Qadam 2.** Fleshkadagi zaxira papkadan shu faylni topib, asl joyiga nusxalang.
- **Qadam 3.** Faylni ochib, uning to‘liq tiklanganiga ishonch hosil qiling.
## Nazorat varag‘i
| № | Bajarilgan amal | Natija |
| 1 | Fleshkaga sanali zaxira papka yaratildi | ha / yo‘q |
| 2 | Fayllar soni va hajmi solishtirildi | ha / yo‘q |
| 3 | Fayllar Google Diskka yuklandi | ha / yo‘q |
| 4 | O‘chirilgan fayl zaxiradan tiklandi | ha / yo‘q |
Zaxira nusxani tekshirmaslik eng ko‘p uchraydigan xato: nusxa olingan, lekin u bo‘sh yoki buzilgan bo‘lib chiqishi mumkin. Shuning uchun vaqti-vaqti bilan tiklashni sinab ko‘rish kerak.
""",
        ],
        'oldingi': ['Hujjat qaysi formatlarda saqlanishi mumkin?',
                    'Fayllarni qayerlarda saqlash mumkin?',
                    'Arxiv nima?'],
        'savollar': ['Zaxira nusxa nima va u nima uchun kerak?',
                     '«3-2-1» qoidasini tushuntiring.',
                     'Bulutli xotiraning afzalligi nimada?',
                     'Windows «Fayl tarixi» qanday ishlaydi?',
                     'Zaxira nusxani nega tekshirib turish kerak?'],
        'testlar': [
            ('«3-2-1» qoidasida «1» nimani bildiradi?',
             ['Bitta fleshka', 'Bitta nusxa boshqa joyda (bulutda) saqlanadi',
              'Bir kunda bir marta', 'Bitta parol'], 'b'),
            ('Bir nechta qurilmadagi fayllarni avtomatik bir xil holatga keltirish:',
             ['Sinxronlash', 'Formatlash', 'Arxivlash', 'Defragmentatsiya'], 'a'),
            ('Google Disk bepul qancha joy beradi?',
             ['1 GB', '5 GB', '100 GB', '15 GB'], 'd'),
            ('Windows’da tanlangan papkalar nusxasini avtomatik saqlovchi vosita:',
             ['Vazifalar dispetcheri', 'Paint', 'История файлов (Fayl tarixi)', 'Bloknot'], 'c'),
            ('Zaxira nusxadagi fayllarni asl joyiga qaytarish jarayoni:',
             ['Tiklash', 'O‘chirish', 'Siqish', 'Nomlash'], 'a'),
        ],
        'mustaqil': ['Shaxsiy fayllaringiz uchun «3-2-1» qoidasiga asoslangan zaxira nusxa rejasini (nima, qayerga, '
                     'qanchalik tez-tez) tuzing.',
                     'Telefoningizdagi rasmlarni Google Foto yoki boshqa bulutli xizmatga zaxiralashni sozlang va '
                     'bosqichlarini yozing.'],
    },
]
