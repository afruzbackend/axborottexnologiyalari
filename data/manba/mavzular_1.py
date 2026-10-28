"""1–5-mavzular: kompyuterning asosiy va qo'shimcha qurilmalari, operatsion tizim tuzilishi va interfeysi.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
«- **Atama** — ta'rif» ko'rinishidagi bandlar glossariyga avtomatik kiradi.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 1
    {
        'type': 'N',
        'title': 'Kompyuterning asosiy qurilmalari va ularning vazifalari',
        'reja': ['Kompyuter tushunchasi va uning ishlash tamoyili',
                 'Tizim bloki ichidagi asosiy qurilmalar',
                 'Kiritish va chiqarish uchun asosiy qurilmalar'],
        'maqsad': 'O‘quvchilarga kompyuterning tuzilishi, ishlash tamoyili hamda asosiy qurilmalari — protsessor, '
                  'tezkor xotira, ona plata, doimiy xotira, monitor, klaviatura va sichqonchaning vazifalarini tushuntirish.',
        'natija': 'O‘quvchilar kompyuterning asosiy qurilmalarini nomlaydi, ularning vazifasini izohlaydi va axborotni '
                  'kiritish, qayta ishlash, saqlash va chiqarish bosqichlarini misollar bilan tushuntiradi.',
        'bolimlar': [
            """
## Kompyuter nima?
Kompyuter inson topshirig‘iga ko‘ra axborotni qabul qiladigan, uni qayta ishlaydigan, saqlaydigan va natijani foydalanuvchiga taqdim etadigan elektron qurilmadir. Kompyuter faqat dastur asosida ishlaydi: dastur unga nima qilish kerakligini buyruqlar ketma-ketligi ko‘rinishida aytib turadi.
- **Kompyuter** — axborotni dastur asosida avtomatik qayta ishlovchi elektron qurilma.
- **Apparat ta’minoti** — kompyuterning qo‘l bilan ushlash mumkin bo‘lgan barcha fizik qurilmalari majmui.
- **Dasturiy ta’minot** — kompyuterda ishlaydigan operatsion tizim va amaliy dasturlar majmui.
## Kompyuterning ishlash tamoyili
Har qanday kompyuter, u stol kompyuteri, noutbuk yoki smartfon bo‘lishidan qat’i nazar, to‘rt bosqichda ishlaydi.
| Bosqich | Nima sodir bo‘ladi | Misol |
| Kiritish | Axborot kompyuterga beriladi | Klaviaturada matn yozish |
| Qayta ishlash | Protsessor axborot ustida amallar bajaradi | Matnni formatlash, hisoblash |
| Saqlash | Natija xotirada saqlanadi | Faylni diskka yozish |
| Chiqarish | Natija foydalanuvchiga ko‘rsatiladi | Monitorda ko‘rish, printerda chop etish |
Bu bosqichlarni bilish IT-servis mutaxassisiga nosozlikni tez topishga yordam beradi: masalan, ekranda tasvir yo‘q bo‘lsa, muammo chiqarish qurilmasida, kabelda yoki videokartada bo‘lishi mumkin.
""",
            """
## Tizim bloki
Tizim bloki kompyuterning «yuragi» bo‘lib, uning ichida axborotni qayta ishlovchi va saqlovchi asosiy qurilmalar joylashadi.
- **Ona plata** — kompyuterning barcha qurilmalarini o‘zaro bog‘lovchi asosiy elektron plata.
- **Protsessor** — dastur buyruqlarini bajaruvchi va hisob-kitoblarni amalga oshiruvchi markaziy qurilma (CPU).
- **Tezkor xotira** — ishlab turgan dasturlar va ma’lumotlar vaqtincha saqlanadigan tez xotira (RAM); kompyuter o‘chganda undagi ma’lumot yo‘qoladi.
- **Doimiy xotira** — fayllar va dasturlar uzoq muddat saqlanadigan qurilma (HDD yoki SSD); kompyuter o‘chganda ham ma’lumot saqlanadi.
- **Ta’minot bloki** — elektr tarmog‘idagi 220 V o‘zgaruvchan tokni kompyuter qurilmalari uchun kerakli past kuchlanishga aylantiruvchi qurilma.
- **Videokarta** — tasvirni hosil qilib, monitorga uzatuvchi qurilma.
## Asosiy ko‘rsatkichlar
| Qurilma | O‘lchov birligi | Odatiy qiymat |
| Protsessor | Chastota (GGs), yadrolar soni | 3,2 GGs, 6 yadro |
| Tezkor xotira | Gigabayt (GB) | 8–16 GB |
| Doimiy xotira | Gigabayt, terabayt (GB, TB) | 512 GB SSD, 1 TB HDD |
| Ta’minot bloki | Vatt (W) | 450–650 W |
Protsessor qizib ketmasligi uchun uning ustiga radiator va ventilyator (kuler) o‘rnatiladi. Tizim blokini changdan muntazam tozalash kompyuterning uzoq ishlashini ta’minlaydi.
""",
            """
## Kiritish qurilmalari
Kiritish qurilmalari yordamida foydalanuvchi kompyuterga buyruq va ma’lumot beradi.
- **Klaviatura** — harflar, raqamlar va buyruqlarni kiritish uchun mo‘ljallangan tugmali qurilma.
- **Sichqoncha** — ekrandagi ko‘rsatkichni boshqarish va obyektlarni tanlash uchun qurilma.
Klaviatura tugmalari guruhlarga bo‘linadi: harf-raqam tugmalari, funksional tugmalar (`F1`–`F12`), boshqaruv tugmalari (`Ctrl`, `Alt`, `Shift`, `Win`), kursorni boshqarish tugmalari va raqamli blok.
## Chiqarish qurilmalari
- **Monitor** — kompyuter qayta ishlagan axborotni matn va tasvir ko‘rinishida ko‘rsatuvchi qurilma.
Monitorlar diagonali (dyuymda, masalan 24″), ruxsat etilgan o‘lchami (masalan, 1920×1080 piksel) va yangilanish chastotasi (Gs) bilan farqlanadi.
## Asosiy qurilmalarsiz kompyuter ishlaydimi?
Kompyuter ishga tushishi uchun kamida ona plata, protsessor, tezkor xotira, ta’minot bloki va doimiy xotira bo‘lishi shart. Tezkor xotira o‘rnatilmagan bo‘lsa, kompyuter yoqilganda signal beradi, lekin operatsion tizim yuklanmaydi. Monitor va klaviatura esa foydalanuvchi bilan muloqot uchun zarur. Shu sababli bu qurilmalar kompyuterning asosiy konfiguratsiyasi deb ataladi.
""",
        ],
        'oldingi': ['Kundalik hayotda qanday raqamli qurilmalardan foydalanasiz?',
                    'Kompyuter va smartfonning qanday o‘xshash tomonlari bor?',
                    'Kompyuter qanday ishlarda yordam beradi?'],
        'savollar': ['Kompyuterning ishlash tamoyili qanday bosqichlardan iborat?',
                     'Protsessor qanday vazifani bajaradi?',
                     'Tezkor xotira va doimiy xotira o‘rtasida qanday farq bor?',
                     'Ona plata nima uchun kerak?',
                     'Qaysi qurilmalar asosiy kiritish va chiqarish qurilmalari hisoblanadi?'],
        'testlar': [
            ('Dastur buyruqlarini bajaruvchi markaziy qurilma:',
             ['Monitor', 'Protsessor', 'Ta’minot bloki', 'Klaviatura'], 'b'),
            ('Kompyuter o‘chganda undagi ma’lumotlar yo‘qoladigan xotira:',
             ['SSD disk', 'Fleshka', 'Tezkor xotira (RAM)', 'Qattiq disk (HDD)'], 'c'),
            ('Barcha qurilmalarni o‘zaro bog‘lovchi asosiy plata:',
             ['Ona plata', 'Videokarta', 'Tovush kartasi', 'Tarmoq kartasi'], 'a'),
            ('Monitor qaysi turdagi qurilmaga kiradi?',
             ['Kiritish qurilmasi', 'Saqlash qurilmasi', 'Qayta ishlash qurilmasi', 'Chiqarish qurilmasi'], 'd'),
            ('Tezkor xotira hajmi qaysi birlikda o‘lchanadi?',
             ['Gigagers (GGs)', 'Gigabayt (GB)', 'Vatt (W)', 'Dyuym'], 'b'),
        ],
        'mustaqil': ['O‘z kompyuteringiz yoki texnikum kompyuterining asosiy qurilmalari va ularning ko‘rsatkichlarini '
                     '(protsessor, RAM, disk) jadval ko‘rinishida yozing.',
                     'Kompyuterning ishlash tamoyili (kiritish → qayta ishlash → saqlash → chiqarish) bo‘yicha '
                     'misollar bilan chizma tuzing.'],
    },
    # ------------------------------------------------------------------ 2
    {
        'type': 'N',
        'title': 'Kompyuterning qo‘shimcha qurilmalarini aniqlash va ularning vazifalari',
        'reja': ['Qo‘shimcha (periferik) qurilmalar tushunchasi',
                 'Qo‘shimcha kiritish va chiqarish qurilmalari',
                 'Aloqa va saqlash uchun qo‘shimcha qurilmalar'],
        'maqsad': 'O‘quvchilarga kompyuterning qo‘shimcha qurilmalari — printer, skaner, kolonka, mikrofon, veb-kamera, '
                  'proyektor, modem va tashqi xotira qurilmalarining vazifalari hamda ularni farqlashni o‘rgatish.',
        'natija': 'O‘quvchilar qo‘shimcha qurilmalarni asosiy qurilmalardan farqlaydi, ularni vazifasi bo‘yicha '
                  'guruhlaydi va kerakli ish uchun mos qurilmani tanlaydi.',
        'bolimlar': [
            """
## Qo‘shimcha qurilmalar nima?
Kompyuter asosiy qurilmalarsiz ishlay olmaydi, lekin uning imkoniyatlarini kengaytirish uchun qo‘shimcha qurilmalar ulanadi. Ular tizim blokidan tashqarida joylashgani uchun periferik qurilmalar ham deyiladi.
- **Periferik qurilma** — kompyuterga tashqaridan ulanib, uning imkoniyatlarini kengaytiruvchi qo‘shimcha qurilma.
- **Drayver** — operatsion tizimga muayyan qurilma bilan ishlashni o‘rgatuvchi maxsus dastur.
## Qo‘shimcha qurilmalar guruhlari
| Guruh | Qurilmalar | Vazifasi |
| Kiritish | Skaner, mikrofon, veb-kamera, grafik planshet | Tasvir, tovush va harakatni kompyuterga kiritish |
| Chiqarish | Printer, kolonka, quloqchin, proyektor | Natijani qog‘ozga, tovush yoki katta ekranga chiqarish |
| Aloqa | Modem, Wi-Fi adapter, router | Kompyuterni tarmoq va internetga ulash |
| Saqlash | Fleshka, tashqi disk, xotira kartasi | Ma’lumotni ko‘chirish va zaxiralash |
""",
            """
## Qo‘shimcha kiritish qurilmalari
- **Skaner** — qog‘ozdagi matn yoki rasmni raqamli tasvirga aylantirib, kompyuterga kirituvchi qurilma.
- **Veb-kamera** — videoqo‘ng‘iroq va onlayn darslar uchun tasvirni real vaqtda kompyuterga uzatuvchi qurilma.
- **Mikrofon** — tovushni elektr signalga aylantirib, kompyuterga kirituvchi qurilma.
Shtrix-kod skaneri do‘konlarda, grafik planshet esa dizaynerlar ishida keng qo‘llaniladi.
## Qo‘shimcha chiqarish qurilmalari
- **Printer** — kompyuterdagi matn va tasvirni qog‘ozga chop etuvchi qurilma.
- **Proyektor** — kompyuter tasvirini katta ekran yoki devorga kattalashtirib tushiruvchi qurilma.
Printerlar ishlash usuliga ko‘ra uch turga bo‘linadi.
| Printer turi | Ishlash usuli | Qayerda qulay |
| Lazerli | Kukun (toner) issiqlik bilan qog‘ozga yopishtiriladi | Ofis, ko‘p hujjat chop etish |
| Purkagichli (struyli) | Mayda siyoh tomchilari purkaladi | Uy, rangli rasmlar |
| Matritsali | Ignalar lenta orqali qog‘ozga uriladi | Kassa cheklari, nusxali blankalar |
Ko‘p funksiyali qurilma (MFU) printer, skaner va nusxa ko‘chirish moslamasini bitta korpusda birlashtiradi.
""",
            """
## Aloqa qurilmalari
- **Router** — bir nechta qurilmani lokal tarmoqqa birlashtirib, ularni internetga ulovchi qurilma.
- **Tarmoq kartasi** — kompyuterni kabel yoki simsiz aloqa orqali tarmoqqa ulovchi qurilma.
## Tashqi saqlash qurilmalari
Fleshka, tashqi qattiq disk va xotira kartalari ma’lumotlarni bir kompyuterdan boshqasiga ko‘chirish va zaxira nusxa saqlash uchun ishlatiladi. Ular USB porti yoki karta o‘quvchi (kartrider) orqali ulanadi.
## Qurilmani to‘g‘ri tanlash
IT-servis mutaxassisi mijozga qurilma tanlashda quyidagilarga e’tibor beradi:
- Ish turi: ko‘p hujjat chop etiladigan ofisga lazerli printer, foto chop etishga purkagichli printer mos keladi.
- Ulanish usuli: USB, Wi-Fi yoki Bluetooth.
- Operatsion tizim bilan mosligi va drayver mavjudligi.
- Narxi va xizmat ko‘rsatish xarajatlari (kartrij, toner, siyoh).
Har qanday yangi qurilma ulanganda Windows uni avtomatik aniqlaydi va drayver o‘rnatadi. Agar drayver topilmasa, uni ishlab chiqaruvchining rasmiy saytidan yuklab olish kerak.
""",
        ],
        'oldingi': ['Kompyuterning asosiy qurilmalarini sanab bering.',
                    'Tezkor xotira va doimiy xotira farqi nimada?',
                    'Monitor qaysi turdagi qurilma?'],
        'savollar': ['Qo‘shimcha qurilmalar nima uchun periferik qurilmalar deb ataladi?',
                     'Drayver nima va u nima uchun kerak?',
                     'Lazerli va purkagichli printerlarning farqi nimada?',
                     'Skaner qanday vazifani bajaradi?',
                     'Ko‘p funksiyali qurilma (MFU) qanday imkoniyatlarni birlashtiradi?'],
        'testlar': [
            ('Qog‘ozdagi matn yoki rasmni raqamli tasvirga aylantiruvchi qurilma:',
             ['Printer', 'Proyektor', 'Skaner', 'Kolonka'], 'c'),
            ('Operatsion tizimga qurilma bilan ishlashni o‘rgatuvchi dastur:',
             ['Drayver', 'Brauzer', 'Antivirus', 'Arxivator'], 'a'),
            ('Toner (kukun) yordamida chop etuvchi printer turi:',
             ['Purkagichli', 'Matritsali', 'Termoprinter', 'Lazerli'], 'd'),
            ('Bir nechta qurilmani tarmoqqa birlashtirib, internetga ulovchi qurilma:',
             ['Skaner', 'Router', 'Mikrofon', 'Veb-kamera'], 'b'),
            ('Quyidagilardan qaysi biri qo‘shimcha kiritish qurilmasi?',
             ['Kolonka', 'Proyektor', 'Printer', 'Mikrofon'], 'd'),
        ],
        'mustaqil': ['Uyingizdagi yoki texnikumdagi qo‘shimcha qurilmalarni guruhlarga (kiritish, chiqarish, aloqa, '
                     'saqlash) ajratib jadval tuzing.',
                     'Kichik ofis uchun printer tanlash bo‘yicha tavsiya yozing: qaysi turni va nima uchun tanlaysiz?'],
    },
    # ------------------------------------------------------------------ 3
    {
        'type': 'A',
        'title': 'Asosiy va qo‘shimcha qurilmalarni aniqlash, ulash va ishlatish',
        'reja': ['Kompyuter portlari va ulash kabellari',
                 'Amaliy ish: qurilmalarni ulash va ishga tushirish',
                 'Qurilma ishlashini tekshirish va natijani rasmiylashtirish'],
        'maqsad': 'O‘quvchilarda kompyuter portlarini tanish, asosiy va qo‘shimcha qurilmalarni xavfsiz ulash, '
                  'ishga tushirish va ularning ishlashini tekshirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar monitor, klaviatura, sichqoncha, printer va kolonkani to‘g‘ri portga ulaydi, '
                  '«Qurilmalar dispetcheri»da ularni aniqlaydi va nazorat varag‘ini to‘ldiradi.',
        'vosita': 'Tizim bloklari, monitorlar, klaviatura, sichqoncha, printer, kolonka, HDMI/VGA/USB kabellar, nazorat varag‘i',
        'bolimlar': [
            """
## Port nima?
Qurilmalar tizim blokiga maxsus ulagichlar orqali ulanadi. Har bir port faqat o‘ziga mos kabel uchun mo‘ljallangan, shuning uchun kabelni kuch bilan tiqish mumkin emas.
- **Port** — tashqi qurilmani kompyuterga ulash uchun mo‘ljallangan ulagich (raz’yom).
## Asosiy portlar
| Port | Ko‘rinishi | Nima ulanadi |
| USB (Type-A, Type-C) | To‘rtburchak yoki oval, yassi | Klaviatura, sichqoncha, fleshka, printer |
| HDMI | Trapetsiya shaklida | Monitor, televizor, proyektor (tasvir va tovush) |
| VGA | Ko‘k rangli, 15 ta ignali | Eski monitor va proyektorlar |
| DisplayPort | Bir burchagi qiya | Zamonaviy monitorlar |
| RJ-45 (LAN) | Plastik ilmoqli keng uya | Tarmoq kabeli |
| Audio 3,5 mm | Yashil — chiqish, pushti — mikrofon | Kolonka, quloqchin, mikrofon |
| Elektr ulagichi | Uch kontaktli | Ta’minot bloki kabeli |
Zamonaviy kompyuterlarda tasvir ulagichlari ikki joyda bo‘lishi mumkin: ona platada va alohida videokartada. Alohida videokarta bo‘lsa, monitor kabeli albatta videokartaga ulanadi.
""",
            """
## Xavfsizlik qoidalari
- **Talab:** ulashdan oldin kompyuter va monitor elektr tarmog‘idan uzilgan bo‘lishi kerak.
- **Talab:** kabellarni siqmasdan, egmasdan, ulagich shakliga mos holda ulash kerak.
- **Talab:** elektr kabeli eng oxirida ulanadi va eng birinchi uziladi.
## Ishni bajarish tartibi
- **Qadam 1.** Tizim blokining orqa panelidagi portlarni ko‘rib chiqing va ularni jadval bilan solishtiring.
- **Qadam 2.** Monitorni HDMI (yoki VGA) kabeli bilan videokartaga ulang, monitor elektr kabelini ulang.
- **Qadam 3.** Klaviatura va sichqonchani USB portlarga ulang.
- **Qadam 4.** Kolonkani yashil rangli audio uyaga ulang.
- **Qadam 5.** Printerni USB kabel bilan ulang va uning elektr kabelini rozetkaga ulang.
- **Qadam 6.** Tizim blokining elektr kabelini ulang, avval monitorni, keyin kompyuterni yoqing.
- **Qadam 7.** Operatsion tizim yuklangach, yangi qurilmalar aniqlanganligi haqidagi xabarlarni kuzating.
Tugmalar `Caps Lock` va `Num Lock` bosilganda klaviaturadagi chiroqchalar yonishi klaviatura ishlayotganini ko‘rsatadi.
""",
            """
## Qurilmalarni tekshirish
Windows tizimida ulangan qurilmalarni ko‘rishning eng qulay usuli — «Qurilmalar dispetcheri».
- `Win + X` tugmalarini bosing va «Диспетчер устройств» (Qurilmalar dispetcheri) bandini tanlang.
- Ro‘yxatda «Клавиатуры», «Мыши», «Мониторы», «Очереди печати» bo‘limlarini oching.
- Sariq undov belgisi bilan ko‘rsatilgan qurilma uchun drayver o‘rnatilmagan yoki u noto‘g‘ri ishlayapti.
Printerni tekshirish uchun «Параметры» → «Bluetooth и устройства» → «Принтеры и сканеры» bo‘limida printerni tanlab, «Печать пробной страницы» (sinov sahifasini chop etish) tugmasini bosing. Kolonkani tekshirish uchun vazifalar panelidagi tovush belgisini bosib, ovoz balandligini o‘zgartiring.
## Nazorat varag‘i
| № | Qurilma | Port | Ishladi | Izoh |
| 1 | Monitor | HDMI / VGA | ha / yo‘q | |
| 2 | Klaviatura | USB | ha / yo‘q | Caps Lock chirog‘i |
| 3 | Sichqoncha | USB | ha / yo‘q | |
| 4 | Kolonka | Audio 3,5 mm | ha / yo‘q | |
| 5 | Printer | USB | ha / yo‘q | sinov sahifasi |
Ish yakunida qurilmalar teskari tartibda o‘chiriladi: avval operatsion tizim «Завершение работы» orqali o‘chiriladi, keyin elektr kabellari uziladi.
""",
        ],
        'oldingi': ['Qo‘shimcha qurilmalarga misollar keltiring.',
                    'Drayver nima uchun kerak?',
                    'Printerlarning qanday turlarini bilasiz?'],
        'savollar': ['Monitor qaysi portlar orqali ulanadi?',
                     'Nima uchun elektr kabeli eng oxirida ulanadi?',
                     'Qurilmalar dispetcherini qanday ochish mumkin?',
                     'Sariq undov belgisi nimani bildiradi?',
                     'Printer ishlashini qanday tekshirasiz?'],
        'testlar': [
            ('Tasvir va tovushni bitta kabel orqali uzatuvchi port:',
             ['VGA', 'HDMI', 'RJ-45', 'PS/2'], 'b'),
            ('Tarmoq kabeli ulanadigan port:',
             ['USB', 'Audio 3,5 mm', 'RJ-45', 'DisplayPort'], 'c'),
            ('Kolonka odatda qaysi rangdagi audio uyaga ulanadi?',
             ['Yashil', 'Pushti', 'Ko‘k', 'Qora'], 'a'),
            ('Qurilmalar dispetcherini ochish uchun qaysi tugmalar birikmasi ishlatiladi?',
             ['Ctrl + Z', 'Alt + Tab', 'Win + D', 'Win + X'], 'd'),
            ('Qurilmalar dispetcherida sariq undov belgisi nimani bildiradi?',
             ['Qurilma yangi', 'Qurilmada muammo yoki drayver yo‘q', 'Qurilma o‘chirilgan', 'Qurilma tez ishlaydi'], 'b'),
        ],
        'mustaqil': ['O‘zingiz foydalanadigan kompyuter yoki noutbukdagi barcha portlarni rasmga olib, har biriga '
                     'nom va vazifasini yozing.',
                     'Qurilmalar dispetcherida kompyuteringiz qurilmalarini ko‘rib, 10 tasini ro‘yxat qiling.'],
    },
    # ------------------------------------------------------------------ 4
    {
        'type': 'N',
        'title': 'Operatsion tizimning tuzilishi va asosiy imkoniyatlari',
        'reja': ['Operatsion tizim tushunchasi va vazifalari',
                 'Operatsion tizimning tuzilishi',
                 'Zamonaviy operatsion tizimlar va ularning imkoniyatlari'],
        'maqsad': 'O‘quvchilarga operatsion tizim tushunchasi, uning vazifalari, tarkibiy qismlari (yadro, drayverlar, '
                  'fayl tizimi, interfeys) hamda zamonaviy operatsion tizimlarning imkoniyatlarini tushuntirish.',
        'natija': 'O‘quvchilar operatsion tizimning vazifalarini sanaydi, uning tuzilishini izohlaydi va Windows, '
                  'Linux, macOS, Android tizimlarini taqqoslaydi.',
        'bolimlar': [
            """
## Operatsion tizim nima?
Kompyuter yoqilgandan so‘ng ekranda ish stoli paydo bo‘lguncha bir necha soniya o‘tadi. Shu vaqt ichida diskdan operatsion tizim yuklanadi. Operatsion tizimsiz kompyuter shunchaki temir qutidir: foydalanuvchi u bilan muloqot qila olmaydi.
- **Operatsion tizim** — kompyuter qurilmalarini boshqaruvchi, dasturlar ishini tashkil etuvchi va foydalanuvchi bilan muloqotni ta’minlovchi dasturlar majmui.
- **Yuklanish** — kompyuter yoqilganda operatsion tizimning diskdan tezkor xotiraga o‘qilib, ishga tushish jarayoni.
## Operatsion tizimning vazifalari
| Vazifa | Mazmuni |
| Qurilmalarni boshqarish | Protsessor, xotira, disk, printer ishini muvofiqlashtiradi |
| Dasturlarni ishga tushirish | Dasturlarni xotiraga yuklaydi, ularga resurs ajratadi |
| Fayllarni boshqarish | Fayl va papkalarni yaratish, saqlash, nusxalash, o‘chirishni ta’minlaydi |
| Foydalanuvchi bilan muloqot | Oyna, belgi, menyu orqali buyruq qabul qiladi |
| Xavfsizlikni ta’minlash | Foydalanuvchi hisoblari, parollar, kirish huquqlari |
""",
            """
## Operatsion tizimning tuzilishi
Operatsion tizim bir-biri bilan bog‘langan bir necha qismdan iborat. Ularni qatlamlar ko‘rinishida tasavvur qilish qulay: eng pastda apparat ta’minoti, eng yuqorida foydalanuvchi dasturlari.
- **Yadro** — operatsion tizimning markaziy qismi bo‘lib, protsessor, xotira va qurilmalarni bevosita boshqaradi.
- **Fayl tizimi** — diskdagi ma’lumotlarni fayl va papkalar ko‘rinishida tartiblash usuli (NTFS, FAT32, exFAT).
- **Interfeys** — foydalanuvchi va kompyuter o‘rtasidagi muloqot vositasi.
- **Grafik interfeys** — oyna, belgi, menyu va sichqoncha yordamida boshqariladigan interfeys.
Bundan tashqari operatsion tizim tarkibiga drayverlar va xizmat dasturlari (utilitlar) kiradi: disk tozalash, defragmentatsiya, zaxira nusxa olish dasturlari shular jumlasidan.
## Interfeys turlari
| Interfeys | Boshqarish usuli | Misol |
| Buyruqlar satri | Buyruqlar klaviaturada yoziladi | `cmd`, PowerShell, Linux terminali |
| Grafik | Sichqoncha, oynalar, belgilar | Windows ish stoli |
| Sensorli | Barmoq bilan ekranga tegish | Android, iOS |
""",
            """
## Zamonaviy operatsion tizimlar
| Operatsion tizim | Ishlab chiquvchi | Qayerda ishlatiladi |
| Windows 10/11 | Microsoft | Stol kompyuterlari, noutbuklar, ofislar |
| Linux (Ubuntu va boshq.) | Erkin hamjamiyat | Serverlar, dasturchilar kompyuterlari |
| macOS | Apple | Apple kompyuterlari (iMac, MacBook) |
| Android | Google | Smartfon va planshetlar |
| iOS | Apple | iPhone smartfonlari |
- **Erkin dasturiy ta’minot** — manba kodi ochiq bo‘lib, bepul foydalanish, o‘zgartirish va tarqatish mumkin bo‘lgan dastur.
## Windows imkoniyatlari
- Bir vaqtning o‘zida bir nechta dasturda ishlash (ko‘p vazifalilik).
- Bir nechta foydalanuvchi hisobini yaratish.
- Tarmoq va internetga ulanish, fayllarni ulashish.
- O‘rnatilgan himoya vositasi «Безопасность Windows» (antivirus va tarmoqlararo ekran).
- Avtomatik yangilanish va tizimni tiklash nuqtalari.
Operatsion tizim versiyasini bilish uchun `Win + R` tugmalarini bosib, `winver` buyrug‘ini kiriting. IT-servis mutaxassisi har bir kompyuterda qaysi tizim o‘rnatilganini bilishi kerak, chunki dastur va drayverlar tizim versiyasiga mos tanlanadi.
""",
        ],
        'oldingi': ['Kompyuterning asosiy qurilmalarini aytib bering.',
                    'Drayver nima?',
                    'Dasturiy ta’minot deganda nimani tushunasiz?'],
        'savollar': ['Operatsion tizim qanday vazifalarni bajaradi?',
                     'Operatsion tizim yadrosi nima?',
                     'Grafik interfeys buyruqlar satridan qanday farq qiladi?',
                     'Qanday zamonaviy operatsion tizimlarni bilasiz?',
                     'Windows versiyasini qanday aniqlash mumkin?'],
        'testlar': [
            ('Operatsion tizimning protsessor va xotirani bevosita boshqaruvchi markaziy qismi:',
             ['Interfeys', 'Drayver', 'Yadro', 'Brauzer'], 'c'),
            ('Smartfonlarda eng ko‘p tarqalgan operatsion tizim:',
             ['Android', 'Windows XP', 'MS-DOS', 'macOS'], 'a'),
            ('Diskdagi ma’lumotlarni fayl va papkalarga tartiblash usuli:',
             ['Yadro', 'Fayl tizimi', 'Yuklanish', 'Ish stoli'], 'b'),
            ('Windows versiyasini ko‘rsatuvchi buyruq:',
             ['ping', 'cls', 'dir', 'winver'], 'd'),
            ('Manba kodi ochiq, bepul tarqatiladigan operatsion tizim:',
             ['Windows 11', 'iOS', 'Linux', 'macOS'], 'c'),
        ],
        'mustaqil': ['Windows, Linux, macOS va Android operatsion tizimlarini 5 ta mezon bo‘yicha taqqoslovchi '
                     'jadval tuzing.',
                     'Kompyuteringizda `winver` va `systeminfo` buyruqlari yordamida operatsion tizim haqidagi '
                     'ma’lumotlarni aniqlab, yozib oling.'],
    },
    # ------------------------------------------------------------------ 5
    {
        'type': 'A',
        'title': 'Operatsion tizim interfeysi va ish stolini boshqarish',
        'reja': ['Windows ish stoli va uning elementlari',
                 'Amaliy ish: oynalar va ish stolini boshqarish',
                 'Ish stolini shaxsiylashtirish va tartibga keltirish'],
        'maqsad': 'O‘quvchilarda Windows ish stoli elementlari, oynalar, «Пуск» menyusi va vazifalar paneli bilan '
                  'ishlash hamda ish stolini sozlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar oynalarni ochadi, yopadi, kichraytiradi, joylashtiradi, ish stoli belgilarini '
                  'tartiblaydi va fon rasmi hamda mavzuni o‘zgartiradi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, proyektor, tugmalar birikmalari ro‘yxati tarqatmasi',
        'bolimlar': [
            """
## Ish stoli elementlari
Operatsion tizim yuklangandan keyin ekranda ko‘rinadigan asosiy ish maydoni ish stoli deb ataladi.
- **Ish stoli** — operatsion tizim yuklangandan so‘ng ekranda paydo bo‘ladigan, belgilar va oynalar joylashadigan asosiy ish maydoni.
- **Belgi** — fayl, papka yoki dasturni ifodalovchi kichik rasm (ikonka).
- **Yorliq** — fayl yoki dasturning o‘zi emas, unga tez murojaat qilish uchun havola; chap pastki burchagida strelka bo‘ladi.
- **Vazifalar paneli** — ekranning pastki qismidagi, ochiq dasturlar, soat va bildirishnomalar ko‘rsatiladigan panel.
| Element | Joylashuvi | Vazifasi |
| «Пуск» tugmasi | Vazifalar panelining chap yoki o‘rta qismi | Dasturlar ro‘yxati, sozlamalar, o‘chirish |
| Qidiruv maydoni | «Пуск» yonida | Dastur va fayllarni nomi bo‘yicha topish |
| Bildirishnomalar sohasi | O‘ng pastki burchak | Soat, til, tovush, tarmoq, batareya |
| Savat (Корзина) | Ish stolida | O‘chirilgan fayllar vaqtincha saqlanadi |
""",
            """
## Oyna bilan ishlash
Har bir dastur yoki papka alohida oynada ochiladi. Oynaning yuqori qismida sarlavha satri, o‘ng yuqori burchagida esa uchta boshqaruv tugmasi bo‘ladi: kichraytirish (—), yoyish (□) va yopish (×).
## Ishni bajarish tartibi
- **Qadam 1.** «Пуск» menyusini oching, «Блокнот» (Bloknot) va «Калькулятор» dasturlarini ishga tushiring.
- **Qadam 2.** Bloknot oynasini sarlavha satridan ushlab ekran bo‘ylab suring, oyna chegarasini tortib o‘lchamini o‘zgartiring.
- **Qadam 3.** `Alt + Tab` tugmalari bilan oynalar orasida o‘ting.
- **Qadam 4.** `Win + ←` va `Win + →` tugmalari bilan ikki oynani ekranning ikki yarmiga joylashtiring.
- **Qadam 5.** `Win + D` tugmalari bilan barcha oynalarni yashirib, ish stolini ko‘rsating, yana bosib qaytaring.
- **Qadam 6.** Kalkulyator belgisini sichqonchaning o‘ng tugmasi bilan bosib, «Закрепить на панели задач» orqali vazifalar paneliga mahkamlang.
## Foydali tugmalar birikmalari
| Birikma | Vazifasi |
| `Win` | «Пуск» menyusini ochish |
| `Win + E` | Provodnik (fayllar boshqaruvchisi)ni ochish |
| `Alt + F4` | Faol oynani yopish |
| `Win + L` | Kompyuterni qulflash |
| `Ctrl + Shift + Esc` | Vazifalar dispetcherini ochish |
""",
            """
## Ish stolini shaxsiylashtirish
Ish stolining bo‘sh joyida sichqonchaning o‘ng tugmasini bosib, «Персонализация» (Shaxsiylashtirish) bandini tanlang.
- **Fon.** «Фон» bo‘limida tayyor rasmlardan birini yoki o‘zingizning rasmingizni tanlang.
- **Ranglar.** «Цвета» bo‘limida yorug‘ yoki qorong‘i rejimni va asosiy rangni tanlang.
- **Ekran qulfi.** «Экран блокировки» bo‘limida qulflangan ekran rasmini o‘zgartiring.
- **Vazifalar paneli.** «Панель задач» bo‘limida panel tugmalarini sozlang.
## Ish stolini tartibga keltirish
Ish stolida juda ko‘p fayl saqlash kompyuterni sekinlashtiradi va kerakli faylni topishni qiyinlashtiradi. Shuning uchun:
- belgilarni o‘ng tugma → «Сортировка» → «Имя» orqali nom bo‘yicha tartiblang;
- bir xil turdagi fayllarni alohida papkalarga yig‘ing;
- ish stolida faqat tez-tez ishlatiladigan dasturlar yorliqlarini qoldiring.
## Ish natijasini baholash
O‘qituvchi har bir o‘quvchidan oynalarni ikki tomonga joylashtirish, ish stolini ko‘rsatish va fon rasmini o‘zgartirishni bajarib ko‘rsatishni so‘raydi. Barcha amallar 10 daqiqada bajarilsa, ish a’lo baholanadi.
""",
        ],
        'oldingi': ['Operatsion tizim qanday vazifalarni bajaradi?',
                    'Grafik interfeys nima?',
                    'Qanday operatsion tizimlarni bilasiz?'],
        'savollar': ['Ish stolida qanday elementlar bor?',
                     'Yorliq faylning o‘zidan qanday farq qiladi?',
                     'Oynani ekranning yarmiga qanday joylashtirish mumkin?',
                     'Alt + Tab tugmalari qanday vazifani bajaradi?',
                     'Ish stoli fonini qanday o‘zgartirasiz?'],
        'testlar': [
            ('Faylning o‘zi emas, unga tez murojaat qilish uchun havola:',
             ['Papka', 'Yorliq', 'Oyna', 'Savat'], 'b'),
            ('Barcha oynalarni yashirib, ish stolini ko‘rsatuvchi birikma:',
             ['Win + D', 'Alt + F4', 'Ctrl + C', 'Win + E'], 'a'),
            ('Ochiq oynalar orasida almashish uchun qaysi tugmalar ishlatiladi?',
             ['Ctrl + V', 'Win + L', 'Alt + Tab', 'Shift + Del'], 'c'),
            ('Ekranning pastki qismidagi ochiq dasturlar va soat ko‘rsatiladigan panel:',
             ['Sarlavha satri', 'Menyu satri', 'Asboblar paneli', 'Vazifalar paneli'], 'd'),
            ('Ish stoli fonini o‘zgartirish uchun qaysi bo‘lim ochiladi?',
             ['Персонализация', 'Диспетчер задач', 'Корзина', 'Проводник'], 'a'),
        ],
        'mustaqil': ['Windowsning 15 ta foydali tugmalar birikmasini yozib, har birini kompyuterda sinab ko‘ring.',
                     'Ish stolingizni tartibga keltiring: fayllarni papkalarga ajrating va natijani «oldin» va '
                     '«keyin» skrinshotlari bilan ko‘rsating.'],
    },
]
