"""6–10-mavzular: dastur va qurilmalarni boshqarish, elektron hujjatlar, matnli hujjat va grafik materiallar yaratish.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 6
    {
        'type': 'A',
        'title': 'Operatsion tizim yordamida dastur va qurilmalarni boshqarish',
        'reja': ['Dasturlarni o‘rnatish, yangilash va o‘chirish',
                 'Amaliy ish: vazifalar dispetcheri va avtoyuklanish',
                 'Qurilmalar va drayverlarni boshqarish'],
        'maqsad': 'O‘quvchilarda Windows yordamida dasturlarni o‘rnatish va o‘chirish, osilib qolgan dasturni '
                  'yopish, avtoyuklanishni sozlash hamda qurilma va drayverlarni boshqarish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar dasturni rasmiy manbadan o‘rnatadi va o‘chiradi, vazifalar dispetcherida jarayonlarni '
                  'kuzatadi, qurilmani o‘chirib-yoqadi va drayverni yangilaydi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, o‘rnatish fayli (masalan, 7-Zip), printer yoki fleshka',
        'bolimlar': [
            """
## Dasturlarni o‘rnatish
Kompyuterga yangi dastur qo‘shish o‘rnatish (installyatsiya) deb ataladi. Dastur fayllari diskka ko‘chiriladi, «Пуск» menyusida va ish stolida yorliq paydo bo‘ladi.
- **O‘rnatish fayli** — dasturni kompyuterga o‘rnatuvchi `.exe` yoki `.msi` kengaytmali fayl.
- **Litsenziya** — dasturdan foydalanish shartlari va huquqini belgilovchi hujjat.
Dasturlarni faqat ishonchli manbalardan o‘rnatish kerak: ishlab chiqaruvchining rasmiy sayti yoki «Microsoft Store». Noma’lum saytlardan yuklangan «buzilgan» dasturlar ko‘pincha virus tarqatadi.
## Dasturni o‘chirish
Dasturni papkasini o‘chirib tashlash orqali emas, maxsus bo‘lim orqali o‘chirish kerak:
- **Qadam 1.** «Параметры» (`Win + I`) → «Приложения» → «Установленные приложения» bo‘limini oching.
- **Qadam 2.** Kerakli dastur yonidagi «…» belgisini bosib, «Удалить» (O‘chirish) ni tanlang.
- **Qadam 3.** O‘chirish ustasi ko‘rsatmalariga amal qiling.
""",
            """
## Vazifalar dispetcheri
- **Vazifalar dispetcheri** — ishlab turgan dasturlar, jarayonlar va kompyuter resurslari sarfini ko‘rsatuvchi tizim dasturi.
- **Jarayon** — tezkor xotirada bajarilayotgan dastur nusxasi.
Vazifalar dispetcherini `Ctrl + Shift + Esc` tugmalari bilan ochish mumkin.
## Ishni bajarish tartibi
- **Qadam 1.** Vazifalar dispetcherini oching va «Процессы» yorlig‘ida protsessor (ЦП) va xotira ustunlarini kuzating.
- **Qadam 2.** Bloknot dasturini oching, uni ro‘yxatdan toping va «Снять задачу» tugmasi bilan yoping.
- **Qadam 3.** «Производительность» yorlig‘ida protsessor, xotira va disk yuklanish grafiklarini ko‘ring.
- **Qadam 4.** «Автозагрузка» yorlig‘ida kompyuter yoqilganda avtomatik ishga tushadigan dasturlarni ko‘ring.
- **Qadam 5.** Keraksiz dasturni tanlab, «Отключить» tugmasi bilan avtoyuklanishdan olib tashlang.
| Ustun | Nimani ko‘rsatadi |
| ЦП (CPU) | Protsessorning necha foizi band |
| Память | Tezkor xotira sarfi |
| Диск | Diskka yozish va o‘qish tezligi |
| Сеть | Tarmoq orqali uzatilayotgan ma’lumotlar |
Avtoyuklanishdagi dasturlar soni kamaytirilsa, kompyuter tezroq yoqiladi. Lekin antivirus va tizim drayverlarini o‘chirish mumkin emas.
""",
            """
## Qurilmalarni boshqarish
Qurilmalar dispetcheri (`Win + X` → «Диспетчер устройств») orqali quyidagi amallar bajariladi:
- **Drayverni yangilash.** Qurilma ustida o‘ng tugma → «Обновить драйвер» → «Автоматический поиск драйверов».
- **Qurilmani o‘chirish.** «Отключить устройство» bandi qurilmani vaqtincha ishdan chiqaradi.
- **Qurilmani yoqish.** «Включить устройство» bandi uni qayta ishga tushiradi.
- **Xususiyatlarni ko‘rish.** «Свойства» oynasida drayver versiyasi va ishlab chiqaruvchi ko‘rsatiladi.
## Printer va tashqi qurilmalar
«Параметры» → «Bluetooth и устройства» bo‘limida printer, sichqoncha, quloqchin kabi qurilmalarni qo‘shish va o‘chirish mumkin. Fleshkani kompyuterdan olishdan oldin vazifalar panelidagi «Безопасное извлечение» belgisini bosish kerak, aks holda yozilayotgan fayllar buzilishi mumkin.
## Nazorat topshirig‘i
| № | Amal | Bajarildi |
| 1 | Dastur o‘rnatildi va ishga tushirildi | ha / yo‘q |
| 2 | Dastur to‘g‘ri usulda o‘chirildi | ha / yo‘q |
| 3 | Osilgan dastur vazifalar dispetcherida yopildi | ha / yo‘q |
| 4 | Avtoyuklanishdan keraksiz dastur olib tashlandi | ha / yo‘q |
| 5 | Qurilma drayveri versiyasi aniqlandi | ha / yo‘q |
""",
        ],
        'oldingi': ['Windows ish stolida qanday elementlar bor?',
                    'Oynalar orasida qanday o‘tiladi?',
                    'Yorliq nima?'],
        'savollar': ['Dasturni to‘g‘ri o‘chirish tartibi qanday?',
                     'Vazifalar dispetcheri qanday ochiladi va u nimani ko‘rsatadi?',
                     'Avtoyuklanish nima va uni nega sozlash kerak?',
                     'Drayverni qanday yangilash mumkin?',
                     'Fleshkani nega «xavfsiz chiqarish» kerak?'],
        'testlar': [
            ('Vazifalar dispetcherini ochuvchi tugmalar birikmasi:',
             ['Ctrl + Alt + T', 'Win + R', 'Ctrl + Shift + Esc', 'Alt + Tab'], 'c'),
            ('Tezkor xotirada bajarilayotgan dastur nusxasi:',
             ['Jarayon', 'Fayl', 'Yorliq', 'Drayver'], 'a'),
            ('Dasturni kompyuterdan to‘g‘ri o‘chirish usuli:',
             ['Dastur papkasini savatga tashlash', 'Yorliqni o‘chirish',
              'Kompyuterni qayta yoqish', '«Параметры» → «Приложения» orqali o‘chirish'], 'd'),
            ('Kompyuter yoqilganda avtomatik ishga tushadigan dasturlar ro‘yxati qaysi yorliqda?',
             ['Процессы', 'Автозагрузка', 'Пользователи', 'Службы'], 'b'),
            ('Dasturlarni qayerdan yuklab olish xavfsiz?',
             ['Ishlab chiqaruvchining rasmiy saytidan', 'Noma’lum forumdan',
              'Reklama bannerlaridan', 'Ijtimoiy tarmoqdagi havoladan'], 'a'),
        ],
        'mustaqil': ['Kompyuteringizdagi avtoyuklanishdagi dasturlar ro‘yxatini yozing va ulardan qaysilari '
                     'kerakli, qaysilari keraksiz ekanligini asoslang.',
                     'Bepul va foydali 5 ta dastur (arxivator, PDF o‘qish, brauzer va h.k.) ro‘yxatini rasmiy '
                     'sayt manzillari bilan tuzing.'],
    },
    # ------------------------------------------------------------------ 7
    {
        'type': 'N',
        'title': 'Elektron hujjatlar va raqamli materiallarni yaratish asoslari',
        'reja': ['Elektron hujjat va raqamli material tushunchasi',
                 'Elektron hujjatlar yaratiladigan amaliy dasturlar',
                 'Elektron hujjat yaratish bosqichlari va talablari'],
        'maqsad': 'O‘quvchilarga elektron hujjat, raqamli material, amaliy dastur tushunchalarini, ofis dasturlari '
                  'turlarini hamda elektron hujjat yaratish bosqichlari va rasmiylashtirish talablarini tushuntirish.',
        'natija': 'O‘quvchilar elektron hujjat turlarini farqlaydi, vazifaga mos amaliy dasturni tanlaydi va hujjat '
                  'yaratish bosqichlarini izohlaydi.',
        'bolimlar': [
            """
## Elektron hujjat nima?
Bugungi kunda ariza, ma’lumotnoma, hisobot, buyruq va shartnomalar asosan kompyuterda tayyorlanadi va elektron shaklda yuboriladi. O‘zbekistonda elektron hujjatlar «Elektron hujjat aylanishi to‘g‘risida»gi Qonun bilan tartibga solinadi.
- **Elektron hujjat** — elektron shaklda qayd etilgan, rekvizitlarga ega va elektron raqamli imzo bilan tasdiqlanishi mumkin bo‘lgan axborot.
- **Raqamli material** — kompyuterda yaratilgan yoki raqamlashtirilgan matn, rasm, jadval, taqdimot, audio va video.
- **Rekvizit** — hujjatning majburiy qismlari: nomi, sanasi, raqami, imzosi, muhri.
- **Elektron raqamli imzo** — elektron hujjat muallifini aniqlash va hujjat o‘zgartirilmaganini tasdiqlash vositasi (ERI).
## Qog‘oz va elektron hujjat
| Belgi | Qog‘oz hujjat | Elektron hujjat |
| Tayyorlash | Qo‘lda yoki printerda | Kompyuter dasturida |
| Tahrirlash | Qayta yozish kerak | Istalgan vaqtda oson o‘zgartiriladi |
| Yuborish | Pochta, kuryer | Elektron pochta, bir necha soniyada |
| Saqlash | Javon, arxiv xonasi | Disk, bulut, kam joy egallaydi |
| Qidirish | Qo‘lda varaqlash | Kalit so‘z bo‘yicha tez topiladi |
""",
            """
## Amaliy dasturlar
- **Amaliy dastur** — foydalanuvchining muayyan vazifasini bajarish uchun mo‘ljallangan dastur: matn yozish, hisoblash, rasm chizish.
- **Ofis dasturlari to‘plami** — matn, jadval, taqdimot va boshqa hujjatlar bilan ishlash uchun dasturlar majmui.
| Hujjat turi | Microsoft Office | Bepul muqobil | Onlayn xizmat |
| Matnli hujjat | Word | LibreOffice Writer | Google Hujjatlar |
| Elektron jadval | Excel | LibreOffice Calc | Google Jadvallar |
| Taqdimot | PowerPoint | LibreOffice Impress | Google Slaydlar |
| Rasm | Paint | GIMP, Krita | Canva |
## Raqamli materiallar turlari
- Matnli: ariza, referat, hisobot (`.docx`, `.txt`, `.pdf`).
- Jadvalli: baholar qaydnomasi, hisob-kitob (`.xlsx`).
- Grafik: rasm, diagramma, sxema, plakat (`.png`, `.jpg`).
- Multimedia: taqdimot, audio, video (`.pptx`, `.mp3`, `.mp4`).
""",
            """
## Elektron hujjat yaratish bosqichlari
- **Rejalashtirish.** Hujjat maqsadi, turi va kimga mo‘ljallanganini aniqlash.
- **Matnni kiritish.** Matnni xatosiz, bir xil uslubda yozish.
- **Tahrirlash.** Xatolarni tuzatish, matnni qisqartirish yoki to‘ldirish.
- **Formatlash.** Shrift, abzats, sarlavha, jadval va rasmlarni bezash.
- **Tekshirish.** Imlo va mazmunni tekshirish, rekvizitlarni to‘ldirish.
- **Saqlash va yuborish.** Faylni to‘g‘ri nom va formatda saqlash, chop etish yoki elektron yuborish.
## Rasmiy hujjatlarga qo‘yiladigan talablar
| Ko‘rsatkich | Odatiy talab |
| Shrift | Times New Roman, 14 pt |
| Qatorlar oralig‘i | 1,0 yoki 1,5 |
| Hoshiyalar | Chap 3 sm, o‘ng 1,5 sm, yuqori va pastki 2 sm |
| Tekislash | Ikki tomondan (kenglik bo‘yicha) |
| Xatboshi | 1,25 sm |
Hujjat yaratishda mualliflik huquqiga rioya qilish kerak: boshqa manbadan olingan matn yoki rasm ishlatilganda manba ko‘rsatiladi.
""",
        ],
        'oldingi': ['Dastur qanday o‘rnatiladi?',
                    'Operatsion tizim va amaliy dastur farqi nimada?',
                    'Kundalik hayotda qanday hujjatlarni bilasiz?'],
        'savollar': ['Elektron hujjat qog‘oz hujjatdan qanday afzalliklarga ega?',
                     'Raqamli materiallarning qanday turlari bor?',
                     'Ofis dasturlari to‘plamiga qanday dasturlar kiradi?',
                     'Elektron hujjat yaratish qanday bosqichlardan iborat?',
                     'Rasmiy hujjat uchun qanday shrift va o‘lcham tavsiya etiladi?'],
        'testlar': [
            ('Elektron jadvallar bilan ishlash uchun mo‘ljallangan dastur:',
             ['Word', 'PowerPoint', 'Excel', 'Paint'], 'c'),
            ('Elektron hujjat muallifini aniqlash va o‘zgartirilmaganini tasdiqlash vositasi:',
             ['Elektron raqamli imzo', 'Shrift', 'Xatboshi', 'Rekvizit'], 'a'),
            ('Microsoft Word dasturining bepul muqobili:',
             ['GIMP', 'LibreOffice Writer', 'Excel', 'Paint'], 'b'),
            ('Rasmiy hujjatlarda odatda qaysi shrift ishlatiladi?',
             ['Comic Sans', 'Arial Black', 'Courier', 'Times New Roman'], 'd'),
            ('Hujjatning majburiy qismlari (nomi, sanasi, imzosi) qanday ataladi?',
             ['Rekvizitlar', 'Formatlar', 'Ilovalar', 'Shablonlar'], 'a'),
        ],
        'mustaqil': ['Kundalik hayotda uchraydigan 10 ta elektron hujjat va raqamli material turini, ular qaysi '
                     'dasturda yaratilishini jadvalga yozing.',
                     '«Elektron hujjat aylanishi to‘g‘risida»gi Qonunning asosiy tushunchalarini lex.uz saytidan '
                     'o‘qib, konspekt qiling.'],
    },
    # ------------------------------------------------------------------ 8
    {
        'type': 'A',
        'title': 'Matnli elektron hujjatlarni amaliy dasturlar yordamida yaratish',
        'reja': ['Matn muharriri oynasi va asosiy tushunchalar',
                 'Amaliy ish: ariza hujjatini yaratish',
                 'Hujjatga jadval va rasm qo‘shish'],
        'maqsad': 'O‘quvchilarda Microsoft Word (yoki LibreOffice Writer) dasturida yangi hujjat yaratish, matn kiritish, '
                  'jadval va rasm qo‘shish hamda hujjatni rasmiylashtirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar talablarga mos ariza hujjatini yaratadi, unga jadval va rasm qo‘shadi hamda hujjatni '
                  'to‘g‘ri nom bilan saqlaydi.',
        'vosita': 'Microsoft Word yoki LibreOffice Writer o‘rnatilgan kompyuterlar, namunaviy ariza matni, proyektor',
        'bolimlar': [
            """
## Word oynasi
- **Matn muharriri** — matnli hujjatlarni yaratish, tahrirlash va formatlash uchun mo‘ljallangan amaliy dastur.
- **Lenta** — Word oynasining yuqori qismidagi, buyruqlar yorliqlar bo‘yicha guruhlangan panel.
- **Kursor** — matn qayerga yozilishini ko‘rsatuvchi miltillovchi vertikal chiziq.
| Oyna qismi | Vazifasi |
| Tez murojaat paneli | Saqlash, bekor qilish, qaytarish tugmalari |
| «Главная» yorlig‘i | Shrift, abzats, uslublar |
| «Вставка» yorlig‘i | Jadval, rasm, shakl, sahifa raqami qo‘shish |
| «Макет» yorlig‘i | Hoshiyalar, sahifa yo‘nalishi va o‘lchami |
| Holat satri | Sahifa raqami, so‘zlar soni, til, masshtab |
## Matn kiritish qoidalari
- So‘zlar orasiga faqat bitta probel qo‘yiladi.
- Tinish belgisidan oldin probel qo‘yilmaydi, keyin qo‘yiladi.
- `Enter` tugmasi faqat yangi abzats boshlashda bosiladi, qator oxirida matn o‘zi keyingi qatorga o‘tadi.
- O‘zbek harflari «o‘», «g‘» uchun maxsus belgi (‘) ishlatiladi.
""",
            """
## Ishni bajarish tartibi
- **Qadam 1.** Word dasturini oching va «Новый документ» (Yangi hujjat) ni tanlang.
- **Qadam 2.** «Макет» → «Поля» bo‘limida hoshiyalarni o‘rnating: chap 3 sm, o‘ng 1,5 sm, yuqori va pastki 2 sm.
- **Qadam 3.** «Главная» yorlig‘ida Times New Roman shriftini va 14 o‘lchamini tanlang.
- **Qadam 4.** O‘ng yuqori qismga kimga yozilayotganini kiriting: «Piskent tuman 1-son texnikumi direktori ...ga».
- **Qadam 5.** Sahifa o‘rtasiga «ARIZA» so‘zini yozing va uni markazga tekislang (`Ctrl + E`).
- **Qadam 6.** Ariza matnini yozing va uni ikki tomondan tekislang (`Ctrl + J`).
- **Qadam 7.** Pastki qismga sana va imzo uchun joy qoldiring.
- **Qadam 8.** `Ctrl + S` tugmalarini bosib, hujjatni «Ariza_Familiya» nomi bilan saqlang.
## Tekislash tugmalari
| Tugmalar | Tekislash |
| `Ctrl + L` | Chapga |
| `Ctrl + E` | Markazga |
| `Ctrl + R` | O‘ngga |
| `Ctrl + J` | Ikki tomondan (kenglik bo‘yicha) |
""",
            """
## Jadval qo‘shish
- **Qadam 1.** Kursorni jadval kerak bo‘lgan joyga qo‘ying.
- **Qadam 2.** «Вставка» → «Таблица» bo‘limida kerakli ustun va qatorlar sonini belgilang (masalan, 3×4).
- **Qadam 3.** Jadval kataklariga ma’lumot kiriting; kataklar orasida `Tab` tugmasi bilan o‘ting.
- **Qadam 4.** «Конструктор таблиц» yorlig‘ida jadval uslubini tanlang.
## Rasm qo‘shish
- **Qadam 1.** «Вставка» → «Рисунки» → «Это устройство» orqali kompyuterdagi rasmni tanlang.
- **Qadam 2.** Rasm burchaklaridagi nuqtalarni tortib o‘lchamini o‘zgartiring.
- **Qadam 3.** «Формат рисунка» → «Обтекание текстом» orqali matn rasm atrofida qanday joylashishini tanlang.
## Baholash mezonlari
| Mezon | Ball |
| Hoshiyalar va shrift talabga mos | 1 |
| Sarlavha markazda, matn ikki tomondan tekislangan | 1 |
| Imlo xatolari yo‘q | 1 |
| Jadval to‘g‘ri tuzilgan | 1 |
| Hujjat to‘g‘ri nom bilan saqlangan | 1 |
""",
        ],
        'oldingi': ['Elektron hujjat nima?',
                    'Qanday ofis dasturlarini bilasiz?',
                    'Rasmiy hujjat uchun qanday talablar qo‘yiladi?'],
        'savollar': ['Word oynasining asosiy qismlarini sanang.',
                     'Matnni markazga tekislash uchun qaysi tugmalar bosiladi?',
                     'Hujjatga jadval qanday qo‘shiladi?',
                     'Hoshiyalar qayerda sozlanadi?',
                     'Matn kiritishda qanday qoidalarga amal qilish kerak?'],
        'testlar': [
            ('Matnni ikki tomondan (kenglik bo‘yicha) tekislovchi birikma:',
             ['Ctrl + E', 'Ctrl + L', 'Ctrl + J', 'Ctrl + R'], 'c'),
            ('Word’da jadval qaysi yorliq orqali qo‘shiladi?',
             ['Вставка', 'Главная', 'Рецензирование', 'Вид'], 'a'),
            ('Hujjatni tez saqlash uchun qaysi tugmalar bosiladi?',
             ['Ctrl + P', 'Ctrl + N', 'Ctrl + O', 'Ctrl + S'], 'd'),
            ('Jadval kataklari orasida keyingisiga o‘tish uchun qaysi tugma ishlatiladi?',
             ['Enter', 'Tab', 'Esc', 'Shift'], 'b'),
            ('Word oynasining yuqori qismidagi buyruqlar paneli qanday ataladi?',
             ['Holat satri', 'Lenta', 'Vazifalar paneli', 'Savat'], 'b'),
        ],
        'mustaqil': ['O‘zingiz haqingizda tarjimai hol (avtobiografiya) hujjatini rasmiy hujjat talablariga mos '
                     'holda tayyorlang.',
                     'Haftalik dars jadvalingizni Word’da jadval ko‘rinishida tuzing va uslub bering.'],
    },
    # ------------------------------------------------------------------ 9
    {
        'type': 'A',
        'title': 'Grafik va raqamli materiallarni yaratish',
        'reja': ['Kompyuter grafikasi va grafik fayl turlari',
                 'Amaliy ish: Paint dasturida rasm va sxema yaratish',
                 'Taqdimot slaydi va e’lon (plakat) tayyorlash'],
        'maqsad': 'O‘quvchilarda kompyuter grafikasi turlarini farqlash, Paint dasturida rasm va sxema yaratish, '
                  'PowerPoint yoki Canva yordamida slayd va e’lon tayyorlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar oddiy sxema chizadi, rasmga matn qo‘shadi, bir slaydli taqdimot va e’lon tayyorlab, '
                  'ularni PNG va PPTX formatlarida saqlaydi.',
        'vosita': 'Paint, PowerPoint (yoki LibreOffice Impress), internet (Canva), namunaviy rasmlar',
        'bolimlar': [
            """
## Kompyuter grafikasi
- **Kompyuter grafikasi** — kompyuter yordamida tasvirlarni yaratish va qayta ishlash sohasi.
- **Rastr grafika** — tasvir mayda nuqtalar (piksellar) dan tashkil topgan grafika; kattalashtirilganda sifati pasayadi.
- **Vektor grafika** — tasvir chiziq, aylana, egri chiziq kabi geometrik obyektlardan iborat grafika; istalgancha kattalashtirilsa ham sifati saqlanadi.
- **Piksel** — rastr tasvirning eng kichik rangli nuqtasi.
| Format | Grafika turi | Xususiyati |
| JPG (JPEG) | Rastr | Fotosuratlar, hajmi kichik, sifati biroz yo‘qoladi |
| PNG | Rastr | Sifat yo‘qolmaydi, shaffof fonni qo‘llaydi |
| GIF | Rastr | Oddiy animatsiya, 256 rang |
| SVG | Vektor | Logotip va belgilar, saytlar uchun |
| PDF | Aralash | Chop etish va ulashish uchun |
""",
            """
## Paint dasturi
Paint Windows tarkibidagi oddiy rastr grafik muharrir. Uni «Пуск» → qidiruvga `paint` deb yozib ochish mumkin.
| Asbob | Vazifasi |
| Karandash | Erkin chiziq chizish |
| Cho‘tka | Turli qalinlikdagi chiziqlar |
| Shakllar | To‘g‘ri chiziq, to‘rtburchak, aylana, strelka |
| Bo‘yash (chelak) | Yopiq sohani rang bilan to‘ldirish |
| Matn (A) | Rasmga yozuv qo‘shish |
| Ajratish | Rasm qismini tanlash, nusxalash, ko‘chirish |
## Ishni bajarish tartibi
- **Qadam 1.** Paint’ni oching va «Изменить размер» orqali tuval o‘lchamini 1280×720 pikselga o‘rnating.
- **Qadam 2.** «Фигуры» asbobi bilan uchta to‘rtburchak chizing va ularni strelkalar bilan bog‘lang.
- **Qadam 3.** To‘rtburchaklar ichiga «Kiritish», «Qayta ishlash», «Chiqarish» so‘zlarini «A» asbobi bilan yozing.
- **Qadam 4.** Bo‘yash asbobi bilan har bir to‘rtburchakni boshqa rangga bo‘yang.
- **Qadam 5.** «Файл» → «Сохранить как» → «PNG» orqali «Sxema_Familiya.png» nomi bilan saqlang.
""",
            """
## Taqdimot slaydi
- **Taqdimot** — ma’lumotni slaydlar ketma-ketligi ko‘rinishida namoyish etuvchi raqamli material.
- **Slayd** — taqdimotning matn, rasm va boshqa obyektlardan iborat alohida sahifasi.
- **Qadam 1.** PowerPoint’da yangi taqdimot oching va «Конструктор» yorlig‘idan mavzu (dizayn) tanlang.
- **Qadam 2.** Sarlavha maydoniga «Kompyuterning asosiy qurilmalari» deb yozing.
- **Qadam 3.** «Вставка» → «Рисунки» orqali Paint’da chizgan sxemangizni qo‘shing.
- **Qadam 4.** Hujjatni «Slayd_Familiya.pptx» nomi bilan saqlang.
## E’lon (plakat) tayyorlash
E’lonni PowerPoint yoki Canva (canva.com) xizmatida tayyorlash mumkin. Yaxshi e’lon qisqa, aniq va o‘qishga qulay bo‘ladi.
- Asosiy sarlavha katta harflar bilan va uzoqdan ko‘rinadigan bo‘lsin.
- Ranglar soni 2–3 tadan oshmasin; matn va fon rangi bir-biridan aniq ajralib tursin.
- Sana, vaqt va joy albatta ko‘rsatilsin.
- Boshqa muallifning rasmi ishlatilsa, ruxsat berilgan (bepul litsenziyali) rasmlardan foydalaning.
""",
        ],
        'oldingi': ['Word’da hujjatga rasm qanday qo‘shiladi?',
                    'Raqamli materiallarning qanday turlari bor?',
                    'Qanday grafik dasturlarni bilasiz?'],
        'savollar': ['Rastr va vektor grafikaning farqi nimada?',
                     'Piksel nima?',
                     'PNG va JPG formatlari qanday farq qiladi?',
                     'Paint’da rasmga matn qanday qo‘shiladi?',
                     'Yaxshi e’lon qanday talablarga javob berishi kerak?'],
        'testlar': [
            ('Kattalashtirilganda ham sifati saqlanadigan grafika turi:',
             ['Rastr', 'Piksel', 'Vektor', 'Fotografik'], 'c'),
            ('Shaffof fonni qo‘llaydigan, sifat yo‘qotmaydigan rastr format:',
             ['PNG', 'JPG', 'DOCX', 'MP3'], 'a'),
            ('Rastr tasvirning eng kichik rangli nuqtasi:',
             ['Slayd', 'Piksel', 'Vektor', 'Shrift'], 'b'),
            ('Paint’da yopiq sohani rang bilan to‘ldiruvchi asbob:',
             ['Karandash', 'Matn', 'Ajratish', 'Bo‘yash (chelak)'], 'd'),
            ('Taqdimotning alohida sahifasi qanday ataladi?',
             ['Slayd', 'Katak', 'Abzats', 'Varaq'], 'a'),
        ],
        'mustaqil': ['Paint’da kompyuterning ishlash tamoyili sxemasini chizib, PNG formatida saqlang.',
                     'Canva yoki PowerPoint’da texnikumdagi biror tadbir uchun e’lon tayyorlang.'],
    },
    # ------------------------------------------------------------------ 10
    {
        'type': 'N',
        'title': 'Elektron hujjatlarni tahrirlash usullari',
        'reja': ['Tahrirlash va formatlash tushunchalari',
                 'Matnni ajratish, nusxalash, ko‘chirish va o‘chirish usullari',
                 'Qidirish, almashtirish, imlo tekshirish va o‘zgarishlarni kuzatish'],
        'maqsad': 'O‘quvchilarga elektron hujjatni tahrirlash usullari — matnni ajratish, nusxalash, qirqish, qo‘yish, '
                  'bekor qilish, qidirish va almashtirish, imlo tekshirish va o‘zgarishlarni kuzatishni tushuntirish.',
        'natija': 'O‘quvchilar tahrirlash va formatlashni farqlaydi, almashinuv buferi bilan ishlash tamoyilini '
                  'izohlaydi va tahrirlashning tezkor usullarini qo‘llaydi.',
        'bolimlar': [
            """
## Tahrirlash va formatlash
Hujjat ustida ishlash ikki xil amalni o‘z ichiga oladi. Ularni farqlay olish ishni tez va to‘g‘ri bajarishga yordam beradi.
- **Tahrirlash** — hujjat mazmunini o‘zgartirish: matn qo‘shish, o‘chirish, ko‘chirish, xatolarni tuzatish.
- **Formatlash** — hujjatning tashqi ko‘rinishini o‘zgartirish: shrift, rang, abzats, hoshiya.
| Amal | Tahrirlash | Formatlash |
| Xato so‘zni tuzatish | ha | |
| Abzatsni boshqa joyga ko‘chirish | ha | |
| Sarlavhani qalin qilish | | ha |
| Qatorlar oralig‘ini o‘zgartirish | | ha |
## Kursorni tez harakatlantirish
| Tugma | Kursor qayerga o‘tadi |
| `Home` / `End` | Qator boshi / oxiri |
| `Ctrl + Home` | Hujjat boshi |
| `Ctrl + End` | Hujjat oxiri |
| `Ctrl + ←` / `→` | Bir so‘z chapga / o‘ngga |
| `Backspace` / `Delete` | Kursordan chapdagi / o‘ngdagi belgini o‘chirish |
""",
            """
## Matnni ajratish
Matn ustida amal bajarishdan oldin uni ajratish (belgilash) kerak.
| Usul | Nima ajratiladi |
| So‘z ustida ikki marta bosish | Bitta so‘z |
| Uch marta bosish | Butun abzats |
| `Shift` + strelkalar | Belgilar bo‘yicha |
| `Ctrl + A` | Butun hujjat |
## Almashinuv buferi
- **Almashinuv buferi** — nusxalangan yoki qirqilgan ma’lumot vaqtincha saqlanadigan xotira sohasi.
| Amal | Tugmalar | Natija |
| Nusxalash | `Ctrl + C` | Matn joyida qoladi, nusxasi buferga tushadi |
| Qirqish | `Ctrl + X` | Matn joyidan olinib, buferga tushadi |
| Qo‘yish | `Ctrl + V` | Bufer mazmuni kursor turgan joyga qo‘yiladi |
| Bekor qilish | `Ctrl + Z` | Oxirgi amal bekor qilinadi |
| Qaytarish | `Ctrl + Y` | Bekor qilingan amal qaytariladi |
Windows 10/11 da `Win + V` tugmalari almashinuv buferi tarixini ochadi: oxirgi nusxalangan bir nechta matnni tanlab qo‘yish mumkin.
""",
            """
## Qidirish va almashtirish
Katta hujjatda biror so‘zni topish yoki uni hamma joyda boshqasiga almashtirish uchun maxsus buyruqlar bor.
- `Ctrl + F` — navigatsiya panelida so‘zni qidirish.
- `Ctrl + H` — «Найти и заменить» oynasida so‘zni boshqa so‘zga almashtirish; «Заменить все» tugmasi barcha uchrashuvlarni bir zumda almashtiradi.
## Imlo tekshirish
Word noto‘g‘ri yozilgan so‘zlar ostiga qizil to‘lqinli chiziq tortadi. So‘z ustida o‘ng tugmani bosib, to‘g‘ri variantni tanlash mumkin. `F7` tugmasi butun hujjatni tekshirishni boshlaydi. O‘zbek tili lug‘ati o‘rnatilmagan bo‘lsa, dastur o‘zbekcha so‘zlarni ham xato deb ko‘rsatishi mumkin, shuning uchun yakuniy tekshiruvni o‘zingiz bajaring.
## O‘zgarishlarni kuzatish
- **Rezenziyalash** — hujjatga boshqa shaxs tomonidan kiritilgan o‘zgarishlar va izohlarni ko‘rsatish rejimi.
«Рецензирование» → «Исправления» rejimi yoqilganda har bir o‘zgarish rangli belgilanadi. Hujjat muallifi o‘zgarishlarni qabul qilishi yoki rad etishi mumkin. Bu rejim hisobot va buyruqlarni bir nechta xodim birgalikda tayyorlaganda juda qulay.
""",
        ],
        'oldingi': ['Word’da yangi hujjat qanday yaratiladi?',
                    'Matn qanday tekislanadi?',
                    'Rastr va vektor grafikaning farqi nimada?'],
        'savollar': ['Tahrirlash va formatlash farqini misol bilan tushuntiring.',
                     'Almashinuv buferi nima?',
                     'Nusxalash va qirqish o‘rtasida qanday farq bor?',
                     'So‘zni butun hujjatda boshqasiga qanday almashtirish mumkin?',
                     'O‘zgarishlarni kuzatish rejimi nima uchun kerak?'],
        'testlar': [
            ('Oxirgi amalni bekor qiluvchi tugmalar birikmasi:',
             ['Ctrl + Y', 'Ctrl + Z', 'Ctrl + X', 'Ctrl + A'], 'b'),
            ('Matnni joyidan olib, almashinuv buferiga joylovchi amal:',
             ['Qirqish (Ctrl + X)', 'Nusxalash (Ctrl + C)', 'Qo‘yish (Ctrl + V)', 'Saqlash (Ctrl + S)'], 'a'),
            ('So‘zni hujjat bo‘yicha boshqa so‘zga almashtirish oynasini ochuvchi birikma:',
             ['Ctrl + F', 'Ctrl + P', 'Ctrl + H', 'Ctrl + E'], 'c'),
            ('Quyidagilardan qaysi biri formatlash amali?',
             ['Xato so‘zni tuzatish', 'Abzatsni o‘chirish', 'Yangi gap qo‘shish', 'Sarlavhani qalin qilish'], 'd'),
            ('Butun hujjatni ajratuvchi birikma:',
             ['Ctrl + A', 'Ctrl + End', 'Shift + Home', 'Alt + A'], 'a'),
        ],
        'mustaqil': ['Matn muharririda tahrirlash uchun ishlatiladigan 15 ta tugmalar birikmasi jadvalini tuzing.',
                     'Do‘stingiz bilan bitta hujjatni «Исправления» rejimida tahrirlab, o‘zgarishlarni qabul qiling.'],
    },
]
