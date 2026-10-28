"""16–20-mavzular: fayl va papkalar bilan ishlash, ma'lumotlarni saqlash vositalari, tashqi xotira.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 16
    {
        'type': 'N',
        'title': 'Fayl va papkalar bilan ishlashning asosiy qoidalari',
        'reja': ['Fayl, papka va fayl tizimi tushunchalari',
                 'Fayl yo‘li va papkalar daraxti',
                 'Provodnik dasturi va fayllar bilan ishlash qoidalari'],
        'maqsad': 'O‘quvchilarga fayl, papka, disk, fayl yo‘li, papkalar daraxti tushunchalarini, Provodnik dasturi '
                  'imkoniyatlarini va fayllar bilan ishlashning asosiy qoidalarini tushuntirish.',
        'natija': 'O‘quvchilar fayl va papkani farqlaydi, fayl yo‘lini o‘qiydi va yozadi, Provodnik’da kerakli faylni '
                  'topadi hamda fayllarni tartibli saqlash qoidalarini izohlaydi.',
        'bolimlar': [
            """
## Fayl va papka
Kompyuterdagi barcha ma’lumotlar (hujjat, rasm, dastur, musiqa) fayl ko‘rinishida saqlanadi. Fayllar ko‘p bo‘lgani uchun ular papkalarga guruhlanadi.
- **Fayl** — diskda nom bilan saqlanadigan ma’lumotlar to‘plami.
- **Papka** — fayllar va boshqa papkalarni guruhlab saqlash uchun mo‘ljallangan joy (katalog).
- **Disk** — kompyuterdagi xotira qurilmasi yoki uning qismi, harf bilan belgilanadi (`C:`, `D:`).
- **Ichki papka** — boshqa papka ichida joylashgan papka.
| Tushuncha | Hayotiy o‘xshatish |
| Disk | Kitob javoni |
| Papka | Javondagi qutilar va jildlar |
| Fayl | Jild ichidagi varaq |
## Fayl atributlari
Har bir fayl nomi va kengaytmasidan tashqari hajm, yaratilgan va o‘zgartirilgan sana, atributlarga ega. «Только чтение» (faqat o‘qish uchun) atributi faylni tasodifiy o‘zgartirishdan, «Скрытый» (yashirin) atributi esa uni ko‘rinishdan himoya qiladi.
""",
            """
## Fayl yo‘li
- **Fayl yo‘li** — faylning diskdagi joylashgan o‘rnini disk harfi va papkalar ketma-ketligi orqali ko‘rsatuvchi manzil.
Masalan: `D:\\Texnikum\\Axborot texnologiyalari\\Amaliy\\Ariza_Karimov.docx`. Bu yerda `D:` disk, `Texnikum`, `Axborot texnologiyalari`, `Amaliy` papkalar, `Ariza_Karimov.docx` esa fayl. Windows’da papkalar teskari qiya chiziq (`\\`) bilan ajratiladi, internet manzillari va Linux’da esa to‘g‘ri qiya chiziq (`/`) ishlatiladi.
## Papkalar daraxti
Papkalar bir-birining ichida joylashib, daraxtsimon tuzilmani hosil qiladi. Eng yuqori daraja disk bo‘lib, u ildiz papka deyiladi.
| Daraja | Misol |
| Ildiz (disk) | `D:\\` |
| 1-daraja | `D:\\Texnikum` |
| 2-daraja | `D:\\Texnikum\\Axborot texnologiyalari` |
| 3-daraja | `D:\\Texnikum\\Axborot texnologiyalari\\Amaliy` |
## Maxsus papkalar
Windows har bir foydalanuvchi uchun tayyor papkalar yaratadi: «Рабочий стол» (Ish stoli), «Документы», «Загрузки» (internetdan yuklanganlar), «Изображения», «Музыка», «Видео». Ular `C:\\Users\\Foydalanuvchi_nomi` ichida joylashadi.
""",
            """
## Provodnik dasturi
- **Provodnik** — Windows’da disklar, papkalar va fayllarni ko‘rish hamda boshqarish uchun mo‘ljallangan dastur (Проводник).
Provodnik `Win + E` tugmalari yoki vazifalar panelidagi sariq papka belgisi bilan ochiladi.
| Qism | Vazifasi |
| Manzil satri | Joriy papkaning yo‘li |
| Qidiruv maydoni | Joriy papkada nom bo‘yicha qidirish |
| Navigatsiya paneli | Disklar va tez kirish papkalari |
| Ish maydoni | Fayl va papkalar ro‘yxati |
| «Вид» menyusi | Belgilar o‘lchami, jadval ko‘rinishi, kengaytmalarni ko‘rsatish |
## Fayllar bilan ishlash qoidalari
- Har bir fan yoki loyiha uchun alohida papka yarating.
- Fayllarni «Загрузки» yoki ish stolida to‘plab qo‘ymang, darhol tegishli papkaga joylang.
- Tizim papkalari (`C:\\Windows`, `C:\\Program Files`) dagi fayllarni o‘chirmang va ko‘chirmang.
- Noma’lum manbadan kelgan faylni ochishdan oldin antivirus bilan tekshiring.
- Muhim fayllarning zaxira nusxasini muntazam oling.
Tartibli papkalar tizimi vaqtni tejaydi: kerakli fayl qidirilmaydi, balki darhol topiladi.
""",
        ],
        'oldingi': ['Zaxira nusxa nima?',
                    'Fayl kengaytmasi nima?',
                    'Fayl nomlashning qanday qoidalari bor?'],
        'savollar': ['Fayl va papka nima?',
                     'Fayl yo‘li qanday yoziladi? Misol keltiring.',
                     'Papkalar daraxti nima?',
                     'Provodnik qanday ochiladi va qanday qismlardan iborat?',
                     'Qaysi papkalardagi fayllarni o‘chirish mumkin emas?'],
        'testlar': [
            ('Faylning diskdagi o‘rnini ko‘rsatuvchi manzil:',
             ['Kengaytma', 'Atribut', 'Fayl yo‘li', 'Yorliq'], 'c'),
            ('Provodnik’ni ochuvchi tugmalar birikmasi:',
             ['Win + E', 'Win + D', 'Win + L', 'Win + R'], 'a'),
            ('Windows’da fayl yo‘lidagi papkalar qaysi belgi bilan ajratiladi?',
             ['/', '|', ':', '\\'], 'd'),
            ('Internetdan yuklangan fayllar odatda qaysi papkaga tushadi?',
             ['Документы', 'Загрузки', 'Музыка', 'Windows'], 'b'),
            ('Faylni tasodifiy o‘zgartirishdan himoya qiluvchi atribut:',
             ['Только чтение', 'Скрытый', 'Архивный', 'Системный'], 'a'),
        ],
        'mustaqil': ['O‘quv fanlaringiz uchun papkalar daraxtini chizing (kamida 3 daraja) va har bir papkaga misol '
                     'fayllar yozing.',
                     'Kompyuteringizdagi 5 ta faylning to‘liq yo‘lini manzil satridan nusxalab yozing.'],
    },
    # ------------------------------------------------------------------ 17
    {
        'type': 'A',
        'title': 'Fayl va papkalarni yaratish hamda nomlash',
        'reja': ['Papka va fayl yaratish usullari',
                 'Amaliy ish: o‘quv papkalar tizimini yaratish',
                 'Qayta nomlash, xususiyatlar va qidirish'],
        'maqsad': 'O‘quvchilarda Provodnik yordamida papka va fayllarni yaratish, ularni qoidalarga muvofiq nomlash va '
                  'qayta nomlash, xususiyatlarini ko‘rish va qidirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar ko‘p darajali papkalar tizimini yaratadi, fayllarni to‘g‘ri nomlaydi va qayta nomlaydi, '
                  'kerakli faylni qidiruv orqali topadi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, Provodnik, topshiriq kartochkasi',
        'bolimlar': [
            """
## Papka yaratish usullari
| Usul | Harakat |
| Kontekst menyu | Bo‘sh joyda o‘ng tugma → «Создать» → «Папку» |
| Tugmalar | `Ctrl + Shift + N` |
| Provodnik paneli | «Создать» tugmasi → «Папку» |
Yangi papka «Новая папка» nomi bilan paydo bo‘ladi va nomi ajratilgan holda turadi: darhol yangi nomni yozib, `Enter` bosish kifoya.
## Fayl yaratish usullari
- Dasturning o‘zida: Word’da yangi hujjat yaratib, «Сохранить как» orqali kerakli papkaga saqlash.
- Provodnik’da: o‘ng tugma → «Создать» → «Документ Microsoft Word» yoki «Текстовый документ».
- **Kontekst menyu** — sichqonchaning o‘ng tugmasi bosilganda chiqadigan, tanlangan obyekt uchun mos buyruqlar ro‘yxati.
""",
            """
## Topshiriq: o‘quv papkalar tizimi
`D:` diskda (yoki «Документы» da) quyidagi tuzilmani yarating:
| Daraja | Papka nomi |
| 1 | `Familiya_Ism` |
| 2 | `01_Axborot_texnologiyalari`, `02_Matematika`, `03_Ingliz_tili` |
| 3 (`01_Axborot_texnologiyalari` ichida) | `Nazariy`, `Amaliy`, `Mustaqil_ish` |
## Ishni bajarish tartibi
- **Qadam 1.** Provodnik’ni oching (`Win + E`) va `D:` diskka o‘ting.
- **Qadam 2.** `Ctrl + Shift + N` bilan `Familiya_Ism` papkasini yarating.
- **Qadam 3.** Papka ichiga kirib, uchta fan papkasini yarating; nomlar boshidagi raqam ularni tartiblab turadi.
- **Qadam 4.** `01_Axborot_texnologiyalari` ichida uchta ichki papka yarating.
- **Qadam 5.** `Amaliy` papkasida o‘ng tugma → «Создать» → «Текстовый документ» orqali `Amaliy_17_hisobot.txt` faylini yarating.
- **Qadam 6.** Faylni oching, bugungi sana va mavzu nomini yozib, `Ctrl + S` bilan saqlang.
- **Qadam 7.** Manzil satrini bosib, faylning to‘liq yo‘lini daftarga yozing.
""",
            """
## Qayta nomlash
- **Qadam.** Faylni tanlab `F2` tugmasini bosing, yangi nomni yozing va `Enter` ni bosing.
- **Qadam.** Kengaytmani o‘zgartirmang: `hisobot.txt` ni `hisobot.docx` qilib qayta nomlash fayl formatini o‘zgartirmaydi va u ochilmay qolishi mumkin.
- **Qadam.** Bir nechta faylni ajratib `F2` bossangiz, ular bir xil nom va tartib raqami bilan nomlanadi: `Rasm (1).jpg`, `Rasm (2).jpg`.
## Xususiyatlar
Papka ustida o‘ng tugma → «Свойства» oynasida papka ichidagi fayllar soni, umumiy hajm va joylashuv ko‘rsatiladi. Natijani topshiriq kartochkasiga yozing.
## Qidirish
- Provodnik’ning yuqori o‘ng qismidagi qidiruv maydoniga fayl nomining bir qismini yozing.
- Faqat ma’lum turdagi fayllarni topish uchun yulduzcha belgisidan foydalaning: `*.docx` barcha Word fayllarini topadi.
- `Win + S` tugmalari butun kompyuter bo‘yicha qidiruvni ochadi.
- **Shablon belgisi** — qidiruvda istalgan belgilar ketma-ketligini almashtiruvchi `*` yoki bitta belgini almashtiruvchi `?` belgisi.
Ish yakunida o‘qituvchi papkalar tuzilmasini, nomlarning to‘g‘riligini va topshiriq kartochkasini tekshiradi.
""",
        ],
        'oldingi': ['Fayl yo‘li nima?',
                    'Papkalar daraxtini tushuntiring.',
                    'Provodnik qanday qismlardan iborat?'],
        'savollar': ['Yangi papka yaratishning qanday usullari bor?',
                     'Faylni qayta nomlash uchun qaysi tugma bosiladi?',
                     'Nima uchun kengaytmani o‘zgartirib bo‘lmaydi?',
                     'Barcha Word fayllarini qanday qidirib topish mumkin?',
                     'Papka ichidagi fayllar sonini qayerdan bilish mumkin?'],
        'testlar': [
            ('Yangi papka yaratuvchi tugmalar birikmasi:',
             ['Ctrl + N', 'Ctrl + Shift + N', 'Alt + N', 'Win + N'], 'b'),
            ('Fayl yoki papkani qayta nomlash tugmasi:',
             ['F2', 'F5', 'F10', 'F12'], 'a'),
            ('Qidiruvda `*.docx` yozilsa nima topiladi?',
             ['Faqat bitta fayl', 'Barcha rasmlar', 'Barcha Word fayllari', 'Yashirin papkalar'], 'c'),
            ('Sichqonchaning o‘ng tugmasi bosilganda chiqadigan buyruqlar ro‘yxati:',
             ['Vazifalar paneli', 'Lenta', 'Holat satri', 'Kontekst menyu'], 'd'),
            ('Butun kompyuter bo‘yicha qidiruvni ochuvchi birikma:',
             ['Win + S', 'Ctrl + F4', 'Alt + S', 'Shift + S'], 'a'),
        ],
        'mustaqil': ['Uydagi kompyuter yoki telefoningizda o‘qish uchun papkalar tizimini yarating va uning '
                     'tuzilishini skrinshot bilan ko‘rsating.',
                     'Qidiruvda `*` va `?` shablon belgilaridan foydalanishga 5 ta misol yozing va sinab ko‘ring.'],
    },
    # ------------------------------------------------------------------ 18
    {
        'type': 'A',
        'title': 'Fayl va papkalarni nusxalash, ko‘chirish va o‘chirish',
        'reja': ['Nusxalash va ko‘chirishning farqi va usullari',
                 'Amaliy ish: fayllarni guruhlab ajratish, nusxalash va ko‘chirish',
                 'O‘chirish, savat va fayllarni tiklash'],
        'maqsad': 'O‘quvchilarda fayl va papkalarni bir nechta usulda nusxalash va ko‘chirish, bir nechta faylni '
                  'birdaniga ajratish, o‘chirish va savatdan tiklash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar fayllarni almashinuv buferi va sudrab tashlash orqali nusxalaydi va ko‘chiradi, '
                  'nom to‘qnashuvini to‘g‘ri hal qiladi, o‘chirilgan faylni savatdan tiklaydi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, 17-darsda yaratilgan papkalar, namunaviy fayllar to‘plami',
        'bolimlar': [
            """
## Nusxalash va ko‘chirish
- **Nusxalash** — faylning asli o‘z joyida qolgan holda yangi joyda uning aynan nusxasini yaratish.
- **Ko‘chirish** — faylni eski joyidan olib, yangi joyga o‘tkazish; eski joyda fayl qolmaydi.
| Amal | Tugmalar | Sudrab tashlash |
| Nusxalash | `Ctrl + C`, keyin `Ctrl + V` | Boshqa diskka sudrash yoki `Ctrl` bosib turib sudrash |
| Ko‘chirish | `Ctrl + X`, keyin `Ctrl + V` | Shu disk ichida sudrash yoki `Shift` bosib turib sudrash |
O‘ng tugma bilan sudrab, qo‘yib yuborilganda menyu chiqadi: «Копировать», «Переместить» yoki «Создать ярлыки». Bu eng xavfsiz usul, chunki nima sodir bo‘lishini o‘zingiz tanlaysiz.
## Bir nechta faylni ajratish
| Usul | Natija |
| `Ctrl` + bosish | Tartibsiz joylashgan fayllarni birma-bir tanlash |
| `Shift` + bosish | Birinchi va oxirgi fayl orasidagi hammasini tanlash |
| `Ctrl + A` | Papkadagi barcha fayllar |
| Sichqoncha bilan to‘rtburchak chizish | Hudud ichidagi fayllar |
""",
            """
## Ishni bajarish tartibi
O‘qituvchi bergan `Aralash_fayllar` papkasida hujjatlar, rasmlar va musiqa fayllari aralash holda turibdi.
- **Qadam 1.** `Aralash_fayllar` ichida `Hujjatlar`, `Rasmlar`, `Audio` papkalarini yarating.
- **Qadam 2.** «Вид» → «Таблица» (jadval) ko‘rinishini yoqing va «Тип» ustuni bo‘yicha saralang.
- **Qadam 3.** Barcha `.docx` va `.pdf` fayllarni `Shift` bilan ajratib, `Ctrl + X` bilan qirqing va `Hujjatlar` papkasiga qo‘ying.
- **Qadam 4.** Rasmlarni `Rasmlar` papkasiga sichqoncha bilan sudrab ko‘chiring.
- **Qadam 5.** `Hujjatlar` papkasini o‘z papkangizdagi `Mustaqil_ish` ga `Ctrl` bosib sudrab nusxalang.
- **Qadam 6.** Shu papkani yana bir marta nusxalang: Windows «Замена или пропуск файлов» oynasini ko‘rsatadi.
## Nom to‘qnashuvi
| Variant | Nima bo‘ladi |
| «Заменить файлы в папке назначения» | Eski fayl yangisi bilan almashtiriladi |
| «Пропустить эти файлы» | Mavjud fayllar o‘zgarmaydi |
| «Выбрать для каждого файла» | Har bir fayl uchun alohida qaror qabul qilinadi |
Muhim faylni almashtirishdan oldin ikkala versiyaning sanasi va hajmini solishtiring.
""",
            """
## O‘chirish va savat
- **Savat** — o‘chirilgan fayllar butunlay yo‘qolmasdan oldin vaqtincha saqlanadigan maxsus papka (Корзина).
| Amal | Tugmalar | Natija |
| O‘chirish | `Delete` | Fayl savatga tushadi |
| Butunlay o‘chirish | `Shift + Delete` | Fayl savatni chetlab o‘tadi, tiklash qiyin |
| Tiklash | Savatda o‘ng tugma → «Восстановить» | Fayl asl joyiga qaytadi |
| Savatni tozalash | Savat ustida o‘ng tugma → «Очистить корзину» | Ichidagi barcha fayllar butunlay o‘chadi |
Fleshka va tarmoq papkalaridan o‘chirilgan fayllar savatga tushmaydi, ular darhol o‘chadi. Shuning uchun fleshkadagi fayllarni o‘chirishda ayniqsa ehtiyot bo‘lish kerak.
## Mashq
- **Qadam 1.** `Audio` papkasidagi bitta faylni `Delete` bilan o‘chiring.
- **Qadam 2.** Ish stolidagi «Корзина» ni oching, faylni toping va «Восстановить» ni bosing.
- **Qadam 3.** Fayl asl papkasiga qaytganini tekshiring.
O‘qituvchi har bir o‘quvchining papkalarida fayllar to‘g‘ri saralanganini, nusxa va ko‘chirish amallari to‘g‘ri bajarilganini tekshirib baholaydi.
""",
        ],
        'oldingi': ['Papka qanday yaratiladi?',
                    'Faylni qayta nomlash tugmasi qaysi?',
                    'Almashinuv buferi nima?'],
        'savollar': ['Nusxalash va ko‘chirishning farqi nimada?',
                     'Bir nechta faylni qanday ajratish mumkin?',
                     'Nom to‘qnashuvida qanday variantlar taklif qilinadi?',
                     'Shift + Delete tugmalari nima qiladi?',
                     'O‘chirilgan faylni qanday tiklash mumkin?'],
        'testlar': [
            ('Faylni savatni chetlab o‘tib o‘chiruvchi birikma:',
             ['Ctrl + Delete', 'Alt + Delete', 'Shift + Delete', 'Win + Delete'], 'c'),
            ('Birinchi va oxirgi fayl orasidagi barcha fayllarni ajratish uchun qaysi tugma bosib turiladi?',
             ['Shift', 'Ctrl', 'Alt', 'Tab'], 'a'),
            ('Faylning asli joyida qolib, yangi joyda nusxasi paydo bo‘ladigan amal:',
             ['Ko‘chirish', 'Nusxalash', 'O‘chirish', 'Qayta nomlash'], 'b'),
            ('Fleshkadan o‘chirilgan fayl qayerga tushadi?',
             ['Savatga', 'Загрузки papkasiga', 'Ish stoliga', 'Hech qayerga, darhol o‘chadi'], 'd'),
            ('Savatdagi faylni asl joyiga qaytaruvchi buyruq:',
             ['Восстановить', 'Очистить', 'Вырезать', 'Переименовать'], 'a'),
        ],
        'mustaqil': ['«Загрузки» papkangizdagi fayllarni turlari bo‘yicha papkalarga saralang va natijani '
                     'skrinshot bilan ko‘rsating.',
                     'Nusxalash va ko‘chirish amallarining barcha usullarini (tugmalar, menyu, sudrash) jadvalga yozing.'],
    },
    # ------------------------------------------------------------------ 19
    {
        'type': 'N',
        'title': 'Ma’lumotlarni saqlash vositalari va ularning turlari',
        'reja': ['Xotira turlari va axborot o‘lchov birliklari',
                 'Ichki va tashqi saqlash qurilmalari',
                 'Bulutli saqlash va saqlash vositasini tanlash'],
        'maqsad': 'O‘quvchilarga ichki va tashqi xotira, HDD, SSD, fleshka, xotira kartasi, optik disk va bulutli '
                  'saqlash vositalarining ishlash tamoyili, afzallik va kamchiliklarini tushuntirish.',
        'natija': 'O‘quvchilar saqlash vositalarini turlarga ajratadi, ularning hajmi va tezligini taqqoslaydi hamda '
                  'vazifaga mos saqlash vositasini tanlaydi.',
        'bolimlar': [
            """
## Xotira turlari
Kompyuterda ikki xil xotira mavjud: biri tezkor, lekin vaqtincha, ikkinchisi sekinroq, lekin doimiy.
- **Ichki xotira** — tizim bloki ichiga o‘rnatilgan xotira qurilmalari (RAM, HDD, SSD).
- **Tashqi xotira** — kompyuterga tashqaridan ulanadigan va olib yurish mumkin bo‘lgan saqlash vositalari.
- **Bit** — axborotning eng kichik o‘lchov birligi, 0 yoki 1 qiymatini oladi.
- **Bayt** — 8 bitdan iborat axborot birligi; bitta belgini saqlash uchun yetarli.
## Hajmni his qilish
| Hajm | Taxminan nimaga yetadi |
| 1 KB | Yarim sahifa oddiy matn |
| 1 MB | Bitta sifatli fotosurat yoki 1 daqiqalik MP3 |
| 1 GB | 1 soatlik o‘rta sifatli video |
| 1 TB | 250 000 ta fotosurat |
""",
            """
## Ichki saqlash qurilmalari
- **Qattiq disk** — ma’lumotni aylanuvchi magnit plastinalarda saqlovchi qurilma (HDD).
- **SSD** — ma’lumotni harakatlanuvchi qismlarsiz flesh-xotira mikrosxemalarida saqlovchi tez disk.
| Ko‘rsatkich | HDD | SSD |
| Tezlik | 100–200 MB/s | 500–7000 MB/s |
| Harakatlanuvchi qismlar | Bor (plastina, kallak) | Yo‘q |
| Zarbaga chidamliligi | Past | Yuqori |
| Shovqin | Bor | Yo‘q |
| 1 GB narxi | Arzon | Qimmatroq |
Ko‘pincha operatsion tizim tez ishlashi uchun SSD ga, katta hajmdagi arxiv fayllar esa arzon HDD ga yoziladi.
## Tashqi saqlash qurilmalari
| Qurilma | Hajm | Ulanishi | Qo‘llanishi |
| Fleshka | 8–256 GB | USB | Fayllarni ko‘chirish |
| Xotira kartasi (microSD) | 16–512 GB | Kartrider, telefon | Telefon, fotoapparat |
| Tashqi HDD/SSD | 500 GB – 5 TB | USB | Zaxira nusxa, katta arxiv |
| Optik disk (CD/DVD) | 700 MB / 4,7 GB | DVD diskovod | Eski arxivlar, dasturlar |
""",
            """
## Bulutli saqlash
Bulutli xotirada fayllar foydalanuvchining kompyuterida emas, xizmat ko‘rsatuvchi kompaniyaning ma’lumotlar markazidagi serverlarda saqlanadi.
| Xizmat | Bepul hajm | Kompaniya |
| Google Disk | 15 GB | Google |
| OneDrive | 5 GB | Microsoft |
| iCloud | 5 GB | Apple |
| Yandex Disk | 5 GB | Yandex |
Afzalliklari: istalgan qurilmadan kirish, fayllarni havola orqali ulashish, qurilma buzilsa ham ma’lumot saqlanadi. Kamchiliklari: internet zarur, bepul hajm cheklangan, hisob paroli o‘g‘irlansa fayllar ham xavf ostida qoladi.
## Saqlash vositasini tanlash
- Darsdan uyga hujjat olib ketish uchun — fleshka yoki bulut.
- Butun kompyuterning zaxira nusxasi uchun — tashqi disk.
- Guruhdoshlar bilan birgalikda ishlash uchun — bulutli xotira.
- Telefondagi rasmlarni saqlash uchun — bulut va xotira kartasi.
Hech bir saqlash vositasi abadiy emas: fleshka va disklar ham buziladi. Shu sababli muhim ma’lumot kamida ikki xil vositada saqlanadi.
""",
        ],
        'oldingi': ['Faylni qanday nusxalash va ko‘chirish mumkin?',
                    'Savat nima?',
                    'Fayl hajmi qanday birliklarda o‘lchanadi?'],
        'savollar': ['Ichki va tashqi xotira farqi nimada?',
                     'Bit va bayt nima?',
                     'HDD va SSD ning afzallik va kamchiliklarini ayting.',
                     'Qanday bulutli saqlash xizmatlarini bilasiz?',
                     'Zaxira nusxa uchun qaysi saqlash vositasi qulay?'],
        'testlar': [
            ('Harakatlanuvchi qismlari yo‘q, tez ishlaydigan disk:',
             ['HDD', 'SSD', 'CD', 'Disketa'], 'b'),
            ('Axborotning eng kichik o‘lchov birligi:',
             ['Bayt', 'Kilobayt', 'Bit', 'Megabayt'], 'c'),
            ('1 bayt necha bitga teng?',
             ['8', '2', '10', '1024'], 'a'),
            ('Microsoft kompaniyasining bulutli saqlash xizmati:',
             ['iCloud', 'Google Disk', 'Yandex Disk', 'OneDrive'], 'd'),
            ('DVD diskning odatiy hajmi:',
             ['700 MB', '4,7 GB', '1 TB', '15 GB'], 'b'),
        ],
        'mustaqil': ['Do‘konlar saytlaridan 3 ta fleshka, 2 ta tashqi disk va 2 ta SSD narxini topib, 1 GB '
                     'narxini hisoblang va jadvalga yozing.',
                     'Telefoningiz va kompyuteringizdagi xotira hajmi va band joyni aniqlab, natijani yozing.'],
    },
    # ------------------------------------------------------------------ 20
    {
        'type': 'A',
        'title': 'Fayllarni tashqi xotira qurilmalariga ko‘chirish',
        'reja': ['Tashqi qurilmani ulash va xavfsiz tekshirish',
                 'Amaliy ish: fayllarni fleshkaga ko‘chirish va xavfsiz chiqarish',
                 'Fleshkani formatlash va fayl tizimini tanlash'],
        'maqsad': 'O‘quvchilarda fleshka va xotira kartasini ulash, antivirus bilan tekshirish, fayllarni ko‘chirish, '
                  'xavfsiz chiqarish hamda zarur hollarda formatlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar fleshkadagi bo‘sh joyni aniqlaydi, uni antivirus bilan tekshiradi, fayllarni ko‘chiradi, '
                  'xavfsiz chiqaradi va fayl tizimini (FAT32, exFAT, NTFS) to‘g‘ri tanlaydi.',
        'vosita': 'Kompyuterlar, o‘quv fleshkalari (ichida muhim ma’lumot yo‘q), kartrider, Windows Defender',
        'bolimlar': [
            """
## Fleshkani ulash
Fleshka USB portga ulanganda Windows uni avtomatik aniqlaydi va Provodnik’da yangi disk harfi bilan ko‘rsatadi (masalan, `E:`). Ekranning pastki o‘ng burchagida «Съемный диск» xabari chiqadi.
## Xavfsizlik qoidalari
- **Talab:** begona fleshkani ochishdan oldin antivirus bilan tekshiring.
- **Talab:** fleshkadagi noma’lum `.exe`, `.bat`, `.vbs` fayllarni ishga tushirmang.
- **Talab:** fleshkadagi papka belgisi `.exe` kengaytmali bo‘lsa, bu virus belgisi bo‘lishi mumkin.
- **Talab:** fleshkani nusxalash tugamasdan sug‘urib olmang.
## Antivirus bilan tekshirish
- **Qadam 1.** Provodnik’da fleshka ustida o‘ng tugmani bosing.
- **Qadam 2.** «Проверить с помощью Microsoft Defender» (Windows 11 da «Показать дополнительные параметры» ichida) ni tanlang.
- **Qadam 3.** Tekshiruv natijasida «Угроз не найдено» xabari chiqishini kuting.
## Bo‘sh joyni aniqlash
«Этот компьютер» oynasida har bir disk ostida chiziqli ko‘rsatkich bo‘ladi: unda umumiy va bo‘sh hajm yoziladi. Aniqroq ma’lumot uchun fleshka ustida o‘ng tugma → «Свойства».
""",
            """
## Ishni bajarish tartibi
- **Qadam 1.** Fleshkani ulang va «Этот компьютер» oynasida uning harfi, umumiy va bo‘sh hajmini yozib oling.
- **Qadam 2.** Fleshkani antivirus bilan tekshiring.
- **Qadam 3.** Fleshkada `Familiya_20_amaliy` papkasini yarating.
- **Qadam 4.** O‘z papkangizdagi `01_Axborot_texnologiyalari` papkasini ajrating va fleshkadagi papkaga sudrab tashlang. Boshqa diskka sudralgani uchun fayllar nusxalanadi.
- **Qadam 5.** Nusxalash oynasidagi tezlik (MB/s) va qolgan vaqtni kuzating.
- **Qadam 6.** Nusxa tugagach, asl va nusxa papkalarining «Свойства» oynasidagi fayllar soni va hajmini solishtiring.
- **Qadam 7.** Vazifalar panelidagi fleshka belgisini bosib, «Извлечь» ni tanlang. «Оборудование может быть извлечено» xabaridan keyingina fleshkani sug‘uring.
## Xavfsiz chiqarish nega kerak?
- **Xavfsiz chiqarish** — tashqi qurilmaga yozish jarayonlarini tugatib, uni kompyuterdan xavfsiz uzish amali.
Windows tezlik uchun ma’lumotni avval xotirada to‘plab, keyin fleshkaga yozadi. Fleshka vaqtidan oldin sug‘urilsa, fayl to‘liq yozilmay qoladi yoki fleshka fayl tizimi buziladi.
""",
            """
## Formatlash
- **Diskni formatlash** — xotira qurilmasini yangi fayl tizimi bilan tayyorlash jarayoni; bunda undagi barcha ma’lumotlar o‘chadi.
Formatlash fleshka ochilmay qolganda, «Диск нужно отформатировать» xabari chiqqanda yoki fayl tizimini o‘zgartirish kerak bo‘lganda bajariladi.
| Fayl tizimi | Maksimal fayl hajmi | Qayerda qulay |
| FAT32 | 4 GB | Eski qurilmalar, televizor, avtomagnitola |
| exFAT | Deyarli cheklanmagan | Fleshka va xotira kartalari, Windows va macOS |
| NTFS | Deyarli cheklanmagan | Windows ichki disklari, tashqi disklar |
## Formatlash tartibi (faqat o‘quv fleshkasida!)
- **Qadam 1.** Fleshkadagi kerakli fayllarni kompyuterga nusxalab oling.
- **Qadam 2.** «Этот компьютер» da fleshka ustida o‘ng tugma → «Форматировать».
- **Qadam 3.** «Файловая система» ro‘yxatidan exFAT ni tanlang, «Метка тома» maydoniga nom yozing.
- **Qadam 4.** «Быстрое форматирование» belgisini qoldirib, «Начать» tugmasini bosing va ogohlantirishni tasdiqlang.
Hech qachon `C:` diskni yoki noma’lum diskni formatlamang. Formatlashdan oldin disk harfi va nomini ikki marta tekshiring.
""",
        ],
        'oldingi': ['Qanday tashqi saqlash qurilmalarini bilasiz?',
                    'HDD va SSD farqi nimada?',
                    'Fayllarni nusxalash usullarini ayting.'],
        'savollar': ['Begona fleshkani ochishdan oldin nima qilish kerak?',
                     'Fleshkadagi bo‘sh joyni qayerdan bilish mumkin?',
                     'Fleshkani nima uchun xavfsiz chiqarish kerak?',
                     'Formatlash nima va unda nima sodir bo‘ladi?',
                     'FAT32 fayl tizimining asosiy cheklovi nima?'],
        'testlar': [
            ('FAT32 fayl tizimida saqlanadigan bitta faylning maksimal hajmi:',
             ['1 GB', '16 GB', 'Cheklanmagan', '4 GB'], 'd'),
            ('Xotira qurilmasini yangi fayl tizimi bilan tayyorlash, unda ma’lumotlar o‘chadi:',
             ['Formatlash', 'Defragmentatsiya', 'Arxivlash', 'Sinxronlash'], 'a'),
            ('Fleshkani kompyuterdan uzishning to‘g‘ri usuli:',
             ['To‘g‘ridan-to‘g‘ri sug‘urish', 'Kompyuterni o‘chirib yoqish',
              '«Извлечь» (xavfsiz chiqarish) buyrug‘idan keyin sug‘urish', 'Savatni tozalash'], 'c'),
            ('Fleshka va xotira kartalari uchun eng qulay zamonaviy fayl tizimi:',
             ['FAT16', 'exFAT', 'CDFS', 'EXT2'], 'b'),
            ('Fleshkada qaysi fayl turi xavfli bo‘lishi mumkin?',
             ['Noma’lum .exe fayl', 'Rasm .jpg', 'Matn .txt', 'Hujjat .pdf'], 'a'),
        ],
        'mustaqil': ['Fleshkadagi viruslarning odatiy belgilari va ulardan himoyalanish choralari bo‘yicha eslatma '
                     'tayyorlang.',
                     'FAT32, exFAT va NTFS fayl tizimlarini 4 ta mezon bo‘yicha taqqoslovchi jadval tuzing.'],
    },
]
