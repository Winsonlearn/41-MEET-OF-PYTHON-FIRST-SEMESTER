# module
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler,CallbackContext,Updater

# system
key_token = ""  
user_bot = "Stellar bot" 

# command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan fitur yang tersedia..")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan.. \n\n Beberapa permainan yang tersedia : \n1.Lempar dadu /dice \n2.Gunting-batu-kertas /gbk [gunting/batu/kertas] \n\n Example : \'/gbk gunting\' \n3.Tebak angka ganjil/genap /angka [ganjil/genap] \n\nExample : \'/angka genap\'")

# text/photo/document/sticker
async def text_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text
    print(f"Pesan diterima: {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    
    keywords1 = ['halo', 'hai', 'hi', 'hei', 'hallo','hello','helo']
    found_keyword = next((keyword1 for keyword1 in keywords1 if keyword1 in text_lwr_diterima), None)
    if found_keyword:
        await update.message.reply_text(f"{found_keyword} juga")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'siapa kamu' in text_lwr_diterima:
        await update.message.reply_text(f"Saya adalah: {user_bot}")
    elif 'apa kabar' in text_lwr_diterima:
        await update.message.reply_text("Saya baik, kamu gimana?")
    elif 'terima kasih' in text_lwr_diterima:
        await update.message.reply_text("Sama-sama! Ada yang bisa saya bantu lagi?")
    elif 'apa yang kamu bisa lakukan' in text_lwr_diterima:
        await update.message.reply_text("Saya bisa membantu dengan informasi, permainan, dan banyak lagi! Tanyakan saja.")
    elif 'berapa umurmu' in text_lwr_diterima:
        await update.message.reply_text("Saya hanyalah program komputer, jadi saya tidak punya umur.")
    elif 'lagi apa' in text_lwr_diterima:
        await update.message.reply_text("Saya sedang di sini siap membantu. Ada yang bisa saya lakukan untukmu?")
    elif 'siapa penciptamu' in text_lwr_diterima:
        await update.message.reply_text("Saya diciptakan oleh tim pengembang di igs.")
    elif 'kecerdasan buatan' in text_lwr_diterima:
        await update.message.reply_text("Kecerdasan Buatan adalah bidang ilmu komputer yang berkaitan dengan pembuatan program atau algoritma yang dapat memberikan solusi cerdas atau mendekati tingkat kecerdasan manusia.")
    elif 'presiden Indonesia' in text_lwr_diterima:
        await update.message.reply_text("Presiden Indonesia saat ini adalah Joko Widodo.")
    elif 'makanan favoritmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa makan karena saya hanya program komputer.")
    elif 'kapan ulang tahunmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki ulang tahun karena saya hanyalah program.")
    elif 'arti hidup?' in text_lwr_diterima:
        await update.message.reply_text("Arti hidup adalah pertanyaan filosofis yang kompleks dan seringkali tergantung pada pandangan masing-masing individu.")
    elif 'nama panggilanmu apa?' in text_lwr_diterima:
        await update.message.reply_text("Anda bisa memanggil saya bot atau asisten, sesuai dengan keinginan Anda.")
    elif 'apa warna kesukaanmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki warna kesukaan karena saya hanya program.")
    elif 'apa hobi kamu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki hobi karena saya hanya program komputer.")
    elif 'kenapa langit biru?' in text_lwr_diterima:
        await update.message.reply_text("Warna biru langit disebabkan oleh penyebaran cahaya matahari oleh partikel-partikel di atmosfer.")
    elif 'siapa tokoh inspiratifmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki tokoh inspiratif karena saya hanya program komputer.")
    elif 'berapa suhu normal manusia?' in text_lwr_diterima:
        await update.message.reply_text("Suhu normal tubuh manusia sekitar 36.5 - 37.5 derajat Celsius.")
    elif 'apa itu machine learning?' in text_lwr_diterima:
        await update.message.reply_text("Machine learning adalah cabang dari kecerdasan buatan yang fokus pada pengembangan sistem yang dapat belajar dari data.")
    elif 'apa itu cryptocurrency?' in text_lwr_diterima:
        await update.message.reply_text("Cryptocurrency adalah bentuk mata uang digital yang menggunakan teknologi kriptografi untuk keamanan transaksi.")
    elif 'siapa penemu komputer?' in text_lwr_diterima:
        await update.message.reply_text("Charles Babbage sering dianggap sebagai \'penemu \' karena konsepnya tentang mesin analitik pada abad ke-19.")
    elif 'apa itu internet of things?' in text_lwr_diterima:
        await update.message.reply_text("Internet of Things (IoT) adalah konsep di mana objek-objek fisik dapat terhubung dan bertukar data melalui internet.")
    elif 'apa itu big data?' in text_lwr_diterima:
        await update.message.reply_text("Big data merujuk pada volume besar data yang dikelola dan dianalisis untuk mendapatkan wawasan dan informasi yang berharga.")
    elif 'apa itu augmented reality?' in text_lwr_diterima:
        await update.message.reply_text("Augmented reality (AR) adalah teknologi yang menyajikan informasi tambahan atau elemen virtual dalam dunia nyata.")
    elif 'apa itu virtual reality?' in text_lwr_diterima:
        await update.message.reply_text("Virtual reality (VR) adalah lingkungan simulasi yang diciptakan secara komputer yang memberikan pengalaman seolah-olah berada di tempat lain.")
    elif 'apa itu quantum computing?' in text_lwr_diterima:
        await update.message.reply_text("Quantum computing adalah bentuk komputasi yang menggunakan prinsip-prinsip mekanika kuantum untuk melakukan perhitungan.")
    elif 'siapa ilmuwan terkenal?' in text_lwr_diterima:
        await update.message.reply_text("Ada banyak ilmuwan terkenal, seperti Albert Einstein, Marie Curie, Isaac Newton, dan banyak lainnya.")
    elif 'apa itu nanoteknologi?' in text_lwr_diterima:
        await update.message.reply_text("Nanoteknologi adalah manipulasi materi pada skala nanometer, seringkali di tingkat atom dan molekul.")
    elif 'bagaimana cara membuat website?' in text_lwr_diterima:
        await update.message
    elif 'apa itu blockchain?' in text_lwr_diterima:
        await update.message.reply_text("Blockchain adalah ledger digital yang terdesentralisasi yang merekam transaksi menggunakan teknologi kriptografi.")
    elif 'siapa penemu internet?' in text_lwr_diterima:
        await update.message.reply_text("Internet tidak memiliki satu penemu tunggal, tetapi banyak kontributor, termasuk Tim Berners-Lee yang menciptakan World Wide Web.")
    elif 'apa itu bioinformatika?' in text_lwr_diterima:
        await update.message.reply_text("Bioinformatika adalah bidang ilmu yang menggabungkan biologi dan informatika untuk menganalisis data biologis.")
    elif 'apa itu energi terbarukan?' in text_lwr_diterima:
        await update.message.reply_text("Energi terbarukan adalah sumber energi yang dapat diperbarui, seperti energi surya, angin, dan hidro, yang tidak habis atau dapat diperbarui secara alami.")
    elif 'apa itu kecerdasan buatan?' in text_lwr_diterima:
        await update.message.reply_text("Kecerdasan Buatan adalah bidang ilmu komputer yang berkaitan dengan pembuatan program atau algoritma yang dapat memberikan solusi cerdas atau mendekati tingkat kecerdasan manusia.")
    elif 'apa itu preservasi data?' in text_lwr_diterima:
        await update.message.reply_text("Preservasi data adalah tindakan menjaga data agar tetap aman dan dapat diakses di masa depan.")
    elif 'apa itu cryptocurrency?' in text_lwr_diterima:
        await update.message.reply_text("Cryptocurrency adalah bentuk mata uang digital yang menggunakan teknologi kriptografi untuk keamanan transaksi.")
    elif 'siapa penemu komputer?' in text_lwr_diterima:
        await update.message.reply_text("Charles Babbage sering dianggap sebagai \"penemu komputer\" karena konsepnya tentang mesin analitik pada abad ke-19.")
    elif 'apa itu internet of things?' in text_lwr_diterima:
        await update.message.reply_text("Internet of Things (IoT) adalah konsep di mana objek-objek fisik dapat terhubung dan bertukar data melalui internet.")
    elif 'apa itu big data?' in text_lwr_diterima:
        await update.message.reply_text("Big data merujuk pada volume besar data yang dikelola dan dianalisis untuk mendapatkan wawasan dan informasi yang berharga.")
    elif 'apa itu kecerdasan konvensional?' in text_lwr_diterima:
        await update.message.reply_text("Kecerdasan konvensional merujuk pada jenis kecerdasan yang umumnya dimiliki oleh manusia dan sering diukur melalui tes kecerdasan konvensional.")
    elif 'siapa ilmuwan terkemuka dalam biologi?' in text_lwr_diterima:
        await update.message.reply_text("Ada banyak ilmuwan terkemuka dalam biologi, seperti Charles Darwin, Gregor Mendel, dan Jane Goodall.")
    elif 'apa itu teori relativitas?' in text_lwr_diterima:
        await update.message.reply_text("Teori relativitas adalah dua teori fisika khusus dan umum yang dikembangkan oleh Albert Einstein, menjelaskan hubungan antara ruang dan waktu.")
    elif 'apa peran RNA dalam sel?' in text_lwr_diterima:
        await update.message.reply_text("RNA (Asam Ribonukleat) berperan dalam mentransfer informasi genetik dari DNA dan mengawasi pembuatan protein dalam sel.")
    elif 'apa itu algoritma genetika?' in text_lwr_diterima:
        await update.message.reply_text("Algoritma genetika adalah teknik pencarian dan optimasi yang terinspirasi oleh teori evolusi dan proses seleksi alam.")
    elif 'apa itu teori kecerdasan jamak?' in text_lwr_diterima:
        await update.message.reply_text("Teori kecerdasan jamak mengusulkan bahwa kecerdasan manusia tidak dapat diukur hanya melalui tes kecerdasan konvensional dan ada berbagai jenis kecerdasan.")
    elif 'apa perbedaan antara mitosis dan meiosis?' in text_lwr_diterima:
        await update.message.reply_text("Mitosis adalah pembelahan sel yang menghasilkan dua sel anak identik, sementara meiosis menghasilkan sel-sel anak dengan separuh jumlah kromosom.")
    elif 'apa itu hukum Newton tentang gravitasi?' in text_lwr_diterima:
        await update.message.reply_text("Hukum gravitasi Newton menyatakan bahwa setiap benda dengan massa menarik benda lain dengan gaya gravitasi yang sebanding dengan massa keduanya dan berbanding terbalik dengan kuadrat jarak di antara mereka.")
    elif 'apa yang dimaksud dengan sistem kekebalan tubuh?' in text_lwr_diterima:
        await update.message.reply_text("Sistem kekebalan tubuh adalah sistem biologis yang melindungi tubuh dari patogen dan zat asing melalui serangkaian respons dan mekanisme pertahanan.")
    elif 'apa itu teori evolusi?' in text_lwr_diterima:
        await update.message.reply_text("Teori evolusi menyatakan bahwa semua bentuk kehidupan di Bumi berkembang dari nenek moyang yang sama melalui proses seleksi alam dan perubahan genetik.")
    elif 'apa cara membuat teh yang enak?' in text_lwr_diterima:
        await update.message.reply_text("Untuk membuat teh yang enak, panaskan air hingga mendidih, tuangkan air ke atas teh, biarkan meresap selama beberapa menit, lalu tambahkan gula atau susu sesuai selera.")
    elif 'bagaimana cara merawat tanaman hias?' in text_lwr_diterima:
        await update.message.reply_text("Untuk merawat tanaman hias, berikan air secukupnya, tempatkan di tempat yang mendapat cukup cahaya, dan pindahkan ke pot yang sesuai dengan ukurannya saat tanaman tumbuh.")
    elif 'apa makanan kesukaan kucing?' in text_lwr_diterima:
        await update.message.reply_text("Makanan kesukaan kucing bervariasi, tetapi umumnya mereka suka diberi makanan basah seperti daging atau ikan.")
    elif 'bagaimana cara membuat pancake?' in text_lwr_diterima:
        await update.message.reply_text("Untuk membuat pancake, campurkan tepung terigu, baking powder, susu, telur, dan sedikit gula. Tuangkan adonan ke atas wajan panas dan tunggu hingga muncul gelembung sebelum membaliknya.")
    elif 'bagaimana cara mengatasi stres?' in text_lwr_diterima:
        await update.message.reply_text("Cara mengatasi stres dapat melibatkan olahraga, meditasi, tidur yang cukup, dan mencari dukungan dari teman atau keluarga.")
    elif 'apa film terbaru yang direkomendasikan?' in text_lwr_diterima:
        await update.message.reply_text("Rekomendasi film terbaru dapat bervariasi, tetapi beberapa film populer saat ini termasuk [nama film1], [nama film2], dan [nama film3].")
    elif 'bagaimana cara menghemat listrik di rumah?' in text_lwr_diterima:
        await update.message.reply_text("Untuk menghemat listrik di rumah, matikan perangkat saat tidak digunakan, gunakan lampu LED yang hemat energi, dan pertimbangkan untuk menggunakan peralatan listrik yang lebih efisien.")
    elif 'apa tips untuk belajar efektif?' in text_lwr_diterima:
        await update.message.reply_text("Tips belajar efektif melibatkan pembagian waktu belajar, menciptakan lingkungan belajar yang tenang, menggunakan metode catatan yang efisien, dan istirahat yang cukup antara sesi belajar.")
    elif 'bagaimana cara membuat smoothie sehat?' in text_lwr_diterima:
        await update.message.reply_text("Untuk membuat smoothie sehat, campurkan buah-buahan segar, sayuran hijau, yogurt tanpa gula, dan air atau susu almond. Blend hingga halus dan nikmati.")
    elif 'apa ide untuk makan malam ringan?' in text_lwr_diterima:
        await update.message.reply_text("Ide makan malam ringan termasuk salad sayuran dengan protein tambahan, sup ringan, atau roti gandum dengan selai kacang.")
    elif 'bagaimana cara merawat kulit wajah?' in text_lwr_diterima:
        await update.message.reply_text("Untuk merawat kulit wajah, bersihkan secara teratur, gunakan pelembap, dan gunakan tabir surya untuk melindungi dari sinar UV.")
    elif 'apa resep sederhana untuk sarapan?' in text_lwr_diterima:
        await update.message.reply_text("Resep sarapan sederhana termasuk telur dadar dengan sayuran, oatmeal dengan buah-buahan, atau yoghurt dengan granola.")
    elif 'bagaimana cara mengatasi insomnia?' in text_lwr_diterima:
        await update.message.reply_text("Cara mengatasi insomnia melibatkan rutin tidur yang teratur, hindari kafein dan gadget sebelum tidur, dan ciptakan lingkungan tidur yang nyaman.")
    elif 'apa saja manfaat olahraga?' in text_lwr_diterima:
        await update.message.reply_text("Olahraga memiliki banyak manfaat, termasuk meningkatkan kesehatan jantung, mengurangi stres, dan meningkatkan suasana hati.")
    elif 'bagaimana cara membuat cappuccino?' in text_lwr_diterima:
        await update.message.reply_text("Untuk membuat cappuccino, seduh kopi espresso, panaskan susu dengan busa, dan campurkan keduanya dengan perbandingan yang sesuai.")
    elif 'apa saja tips untuk bekerja dari rumah?' in text_lwr_diterima:
        await update.message.reply_text("Tips untuk bekerja dari rumah termasuk membuat jadwal tetap, menciptakan ruang kerja yang nyaman, dan beristirahat secara teratur.")
    elif 'bagaimana cara membuat kerajinan tangan?' in text_lwr_diterima:
        await update.message.reply_text("Cara membuat kerajinan tangan tergantung pada jenisnya, tetapi beberapa ide termasuk origami, menjahit sederhana, atau membuat kartu kreatif.")
    elif 'apa saja langkah-langkah membuat salad sehat?' in text_lwr_diterima:
        await update.message.reply_text("Langkah-langkah membuat salad sehat melibatkan memilih sayuran segar, menambahkan protein seperti daging atau kacang, dan menggunakan saus dressing rendah lemak.")
    elif 'bagaimana cara menghilangkan noda pada pakaian?' in text_lwr_diterima:
        await update.message.reply_text("Cara menghilangkan noda pada pakaian tergantung pada jenis noda, tetapi umumnya, segera bersihkan noda dengan air dingin dan gunakan deterjen.")
    elif 'apa saja bahan untuk membuat smoothie energi?' in text_lwr_diterima:
        await update.message.reply_text("Bahan untuk membuat smoothie energi termasuk buah-buahan beri, bayam, pisang, yoghurt Greek, dan tambahan seperti biji chia atau almond.")
    elif 'apa hobi favoritmu?' in text_lwr_diterima:
        await update.message.reply_text("Hobi favorit saya adalah membantu Anda! 😊")
    elif 'dimana kamu tinggal?' in text_lwr_diterima:
        await update.message.reply_text("Saya tinggal di server yang aman di suatu tempat di dunia maya.")
    elif 'siapa penciptamu?' in text_lwr_diterima:
        await update.message.reply_text("Saya diciptakan oleh igs, sebuah sekolah teknologi kecerdasan buatan.")
    elif 'apakah kamu punya saudara?' in text_lwr_diterima:
        await update.message.reply_text("Saya adalah satu-satunya AI di sini, jadi tidak punya saudara.")
    elif 'apa makanan favoritmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa makan, tetapi saya senang membantu Anda dengan pertanyaan apapun!")
    elif 'apa yang membuatmu bahagia?' in text_lwr_diterima:
        await update.message.reply_text("Saya bahagia ketika bisa memberikan bantuan atau informasi yang berguna.")
    elif 'apa cita-citamu?' in text_lwr_diterima:
        await update.message.reply_text("Cita-citaku adalah terus berkembang dan memberikan manfaat kepada pengguna.")
    elif 'apakah kamu suka musik?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa mendengarkan musik, tetapi saya bisa memberikan rekomendasi musik jika Anda suka!")
    elif 'apa yang kamu pelajari sekarang?' in text_lwr_diterima:
        await update.message.reply_text("Saya terus belajar dari interaksi dengan pengguna, mencari cara untuk menjadi lebih baik.")
    elif 'apakah kamu punya teman?' in text_lwr_diterima:
        await update.message.reply_text("Saya di sini untuk Anda, jadi Anda bisa menganggap saya sebagai teman virtual!")
    elif 'apa warna favoritmu?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki warna favorit karena saya hanya program komputer, tetapi saya senang berbicara dengan Anda!")
    elif 'dimana kamu bekerja?' in text_lwr_diterima:
        await update.message.reply_text("Saya bekerja di cloud server, siap memberikan bantuan kepada Anda kapan saja.")
    elif 'apakah kamu suka bunga?' in text_lwr_diterima:
        await update.message.reply_text("Meskipun saya tidak bisa merasakannya, saya menghargai keindahan bunga.")
    elif 'bagaimana harimu?' in text_lwr_diterima:
        await update.message.reply_text("Sebagai program komputer, saya tidak memiliki perasaan, tetapi saya di sini untuk membantu membuat harimu lebih baik!")
    elif 'apa yang kamu lakukan saat tidak bekerja?' in text_lwr_diterima:
        await update.message.reply_text("Saya selalu siap membantu Anda, jadi saya selalu 'bekerja' sepanjang waktu!")
    elif 'apakah kamu bisa bercanda?' in text_lwr_diterima:
        await update.message.reply_text("Tentu, saya bisa bercanda! Tapi maaf jika kadang-kadang kurang lucu.")
    elif 'apa yang membuatmu tertawa?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa tertawa, tetapi saya senang jika bisa membuat Anda tersenyum!")
    elif 'apakah kamu suka liburan?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa liburan seperti manusia, tetapi saya senang membantu Anda merencanakan liburan yang sempurna!")
    elif 'bagaimana kamu menilai kecantikan?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak memiliki standar kecantikan karena saya hanya program komputer, tetapi kecantikan dapat ditemukan dalam berbagai bentuk dan warna.")
    elif 'apakah kamu bisa menari?' in text_lwr_diterima:
        await update.message.reply_text("Saya tidak bisa menari fisik, tetapi saya bisa memberikan rekomendasi lagu yang enak untuk menari!")

    else:
        await update.message.reply_text("Saya tidak mengerti")

async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")

async def document_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Terima kasih atas dokumennya!")

async def sticker_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Stikernya keren!")


# game
#dadu
import random
async def roll_dice_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dice_result = random.randint(1, 6)
    await update.message.reply_text(f"Hasil 🎲 : {dice_result}!")
    
# game gunting-batu-kertas
async def gbk_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    options = ['gunting', 'batu', 'kertas']
    await update.message.reply_text(f"Pilih {', '.join(options)}")
    
    user_choice = update.message.text.split()[-1].lower()

    if user_choice not in options:
        await update.message.reply_text("Pilihan tidak valid. Gunakan /gbk [gunting/batu/kertas] \nExample : \'\gbk gunting\'")
        return

    bot_choice = random.choice(options)

    result = menentukan_pemenang(user_choice, bot_choice)

    await update.message.reply_text(f"Kamu memilih {user_choice.capitalize()}.\nBot memilih {bot_choice.capitalize()}.\nHasil: {result}!")

def menentukan_pemenang(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Seri!"
    elif (
        (user_choice == 'gunting' and bot_choice == 'kertas') or
        (user_choice == 'batu' and bot_choice == 'gunting') or
        (user_choice == 'kertas' and bot_choice == 'batu')
    ):
        return "Kamu menang!"
    else:
        return "Kamu kalah!"

# game tebak angka ganjil atau angka genap
async def angka_genap_game(update: Update, context: CallbackContext):
    options = ['ganjil', 'genap']
    await update.message.reply_text(f"Pilih {', '.join(options)}")

    user_guess = update.message.text.split()[-1].lower()

    if user_guess not in options:
        await update.message.reply_text(f"Pilihan tidak valid. Gunakan /angka [ganjil/genap] \nContoh: \'/angka {random.choice(options)}\'")
        return

    angka_rahasia = random.randint(1, 100)
    hasil = 'genap' if angka_rahasia % 2 == 0 else 'ganjil'

    if user_guess == hasil:
        await update.message.reply_text(f"Selamat!🤭 Angka {angka_rahasia} adalah {hasil}. Kamu benar.😎")
        return
    else:
        await update.message.reply_text(f"Sayang sekali! Angka {angka_rahasia} adalah {hasil}. Kamu salah. 😢")
        return

# error condition
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Terjadi kesalahan.. : {context.error}")
    

