# The script of the game goes in this file.

define mc = Character("Della") #mcnya della
# define na = Character("Nadia")
define al = Character("Aldi")
define ds = Character("??")

default lab_is_solved = False
default class_is_solved = False
default aula_is_solved = False
default canteen_is_solved = False
image bg supeno = "images/bg/supeno.png"
image bg lobby = "images/bg/lobby.png"
image bg classroom = "images/bg/classroom.png"
image bg infor = "images/bg/infor.png"
image bg kcv = "images/bg/kcv.png"
image bg rpl = "images/bg/rpl.png"
image bg giga = "images/bg/giga.png"
image bg pkt = "images/bg/pkt.png"
image bg netics = "images/bg/netics.png"
image bg mci = "images/bg/mci.png"
image bg alpro = "images/bg/alpro.png"
image bg aula = "images/bg/aula.png"
image bg rooftop = "images/bg/rooftop.png"
image bg bathroom = "images/bg/bathroom.png"
image bg canteen = "images/bg/canteen.png"
image bg car parkinglot = "images/bg/car.png"
image bg aisle = "images/bg/aisle.png"
image bg aisle canteen = "images/bg/aisleeC.png"
image bg 111 = "images/bg/111.png"
image bg black = "images/bg/black.png"
image bg pintu 111 = "images/bg/pintu111.png"
image bg 105 = "images/bg/105.png"
image bg 107 = "images/bg/107.png"
image bg 101 = "images/bg/101.png"
image bg musholla = "images/bg/musholla.png"
image bg tu = "images/bg/tu.png"
image bg floor = "images/bg/floor.png"
image bg blackboard = "images/bg/blackboard.png"
image bg pcstart = "images/bg/pcstart.png"
image bg paper clue = "images/bg/paperclue.png"
image bg biner1 = "images/bg/biner1.png"
image bg biner2 = "images/bg/biner2.png"
image bg biner3 = "images/bg/biner3.png"
image bg biner4 = "images/bg/biner4.png"
image bg blackoutScreen = "images/bg/blackoutScreen.png"
image bg rScreen = "images/bg/rScreen.png"
image bg blankBlackboard = "images/bg/blankBlackboard.png"
# The game starts here.

label start:
    scene bg supeno
    show aldi at left
    al "Kamu... pernah dengar rumor kelas tengah malam di TC?"
    hide aldi
    show mc at right
    mc "Huh? Aku ngga pernah denger, tuh"
    mc "Jangan bilang kamu mau nyoba buktiin?"
    hide mc
    show aldi at left
    al "Ya iyalah, pasti. Kamu ikut kan?"
    hide aldi
    menu: 
        "Apa yang akan kamu pilih?" 

        "Ikut Aldi menyelidiki":
            show mc at right
            mc "Ayo, aku juga penasaran."
            hide mc
            show aldi at left
            al "Oke, kita kumpul di TC jam 23.12, ya"
            hide mc
            hide aldi
            $ is_investigating = True
        "Tidak mau menyelidiki":
            show mc
            mc "Kayaknya mending kita pulang aja deh. Perasaanku ga enak."
            $ is_investigating = False

if is_investigating:
    jump firstNight
else:
    scene bg classroom
    "Kamu merasa bahwa menyelidiki kampusmu di malam hari bukanlah pilihan yang tepat. Kamu tidak pernah tau apa yang terjadi sampai kamu lulus dari Teknik Informatika."
    return

label firstNight:
    scene bg infor 
    show mc at right
    mc "Kita beneran masuk, nih?"
    hide mc
    show aldi at left
    al "Yaiyalah ayo!"
    hide aldi

    scene bg car parkinglot
    "Malam semakin larut. Della dan Aldi memberanikan diri berjalan masuk ke parkiran mobil gedung departemen dengan berbekal senter dan handphone."
    show mc at right
    mc "Dari luar sih kayak biasanya."
    mc "Ayo kita jalan terus!"
    hide mc

    "Setelah sampai di parkiran mobil mereka melanjutkan berjalan lurus menuju Lobby yang tampak remang-remang di malam itu."

label firstChoice:
    scene bg lobby
    "Kalian sampai di Lantai pertama Teknik Informatika."
    "Lantai pertama diisi dengan deretan kelas yang memiliki kuota yang berbeda."
    "Ruang kelas tampak sepi karena jadwal kelas biasanya hanya sampai pukul 17.20."
    "Kalian memilih untuk memulai penyelidikan dari sini."
    menu:
        "Ke arah mana kalian akan pergi?"
        "Kanan":
            "Kalian memilih untuk pergi ke arah kanan."
            menu:
                "Cek 107":
                    scene bg 107
                    show mc at right
                    mc "Nggak ada apa apa sih di sini. Mungkin aku harus cek kelas lain."
                    hide mc
                    $ is_check_107 = True
                "Kembali":
                    show mc at right
                    mc "Hmm... Sepertinya ini bukan arah yang tepat."
                    hide mc
                    $ is_check_107 = False
        "Kiri":
            "Kalian memilih untuk pergi ke arah kiri."
            menu:
                "Cek 111":
                    jump firstEvent
                "Kembali":
                    jump firstChoice

label secondChoice:
    if is_check_107:
        "Kalian memilih untuk mengecek kelas lainnya. Kelas apa yang akan kalian cek selanjutnya?"
        menu:
            "Cek 105":
                scene bg 105
                show aldi at left
                al "Di sini juga nggak ada apa apa. Sepertinya aku harus cek ruangan kelas lain."
                hide aldi
                jump secondChoice
            "Cek 101":
                scene bg 101
                al "Della! Aku lihat lampu di kelas seberang menyala!"
                show aldi at left
                hide aldi
                "Aldi dan Della melihat bahwa lampu kelas 111 menyala, seolah sedang ada kegiatan belajar mengajar yang dilakukan." 
                "Mereka pun segera berjalan menuju Kelas 111"
                # hide aldi
                menu:
                    "Cek 111":
                        jump firstEvent
    else:
        show mc at right
        mc "Hmm... Sepertinya ini bukan arah yang tepat."
        hide mc
        jump firstChoice

label firstEvent:
    scene bg 111
    "Sesampainya di sana, mereka mendengar suara bising dari dalam kelas."
    show aldi at left
    al "Tuh kan! Bener ada!"
    hide aldi
    show mc at right
    mc "Gila, kok bisaada suara jam segini."
    # hide mc
    "{i}Aku rasa kita harus menghentikan penyelidikan ini. Tapi... Kita sudah sejauh ini."
    hide mc
    "Della merasa semakin bimbang. Della merasa bahwa mereka harus menghentikan penyelidikan mereka di sini. Namun di sisi lain, Della juga penasaran atas kebenaran rumor tersebut."
    menu:
        "Ajak Aldi untuk masuk ke Kelas 111":
            show mc at right
            mc "Udah, lah. Kita nyoba masuk aja, yuk."
            hide mc
            jump event111

        "Minta Aldi untuk mengecek":
            show mc at right
            mc "Aku ngerasa ini ide buruk deh, Al."
            hide mc
            show aldi at left
            al "Ayolah, pengecut!"
            hide aldi
            jump event111
    
label event111:
    hide aldi
    hide mc
    "Kalian memilih untuk masuk ke dalam kelas."
    scene bg pintu111
    #insert sound door knocking
    "{i}Tok... Tok... Tok.."
    ds "Masuk saja, pintunya tidak dikunci."
    scene bg black
    #insert sound door opening
    "Pintu dibuka secara perlahan. Di dalam, terlihat seorang dosen yang mengajar di depan banyak mahasiswa lain-"
    scene bg classroom
    #insert sound heartbeat
    # "{i}Deg... Deg.. Deg..."
    "-tetapi semua wajah mahasiswa di dalam terlihat kabur!"
    "{i}Deg... Deg.. Deg..."
    #insert sound chair being pulled
    "Melihat hal tersebut, Aldi yang {i} excited {/i} langsung mengambil bangku paling depan."
    show mc #focus on center, zoom
    "{i} AH! Aku harus pulang sekarang!. Tapi jika aku pergi siapa yang akan menemani Aldi?"
    hide mc
    menu:
        "Duduk bersama Aldi":
            show mc at right
            "{i}Kurasa tidak ada salahnya mencoba duduk sebentar. Siapa tau aku akan menemukan akar dari semua hal aneh ini."
            hide mc
            "Della dan Aldi menatap papan tulis untuk mengikuti materi yang tengah diajarkan oleh dosen misterius tersebut."
            show mc at right
            "{i}Aneh... Aku merasa hawa di sini semakin dingin."
            "{i}Indikator AC-nya tidak menyala, pintu dan jendela dikunci. Darimana asal hawa dingin yang kurasakan ini?"
            "{i}Materi yang diajarkan juga aneh. Mengapa kita diajarkan cara memakai disket 3.5 inchi untuk transfer data?"
            hide mc
            "Della menengok aldi yang serius mencatat materi yang dibawakan di ponsel miliknya."
            jump signOfStrangeness

        "Mengajak Aldi untuk pergi":
            show aldi at left
            al "Aku nggak mau pergi dari sini! Pokoknya aku harus usut semua ini sampai tuntas!"
            hide aldi
            "Della tidak punya pilihan selain ikut duduk menemani Aldi."
            jump signOfStrangeness

label signOfStrangeness:
    "Setelah beberapa menit berjalan, Della mencoba mengecek bangku kanan dan kirinya."
    show mc at right
    mc "{i}Kenapa semua orang tidak ada yang bergerak, ya?"
    #insert sound dosen voice distorted
    mc "{i}Suara dosen juga kadang terdistorsi seperti memakai mic yang memiliki daya rendah."
    mc "Ini kayak nggak bener, deh, Al. Ada yang aneh sama dosen itu."
    hide mc
    show aldi at left
    al "Iya, suasana kelasnya juga aneh."
    al "Jangan-jangan..."
    al "...mereka ini semua hantu!"
    hide aldi
    "Aldi tertawa dengan keras."
    #insert laughter
    show aldi at left
    al "HAHAHAHA"
    al "Nggak mungkin lah, Del. Jelas jelas penampilan mereka seperti manusia, kok!"
    hide aldi
    "Bulu kuduk Della berdiri. Insting Della menyuruhnya untuk segera pergi dari ruang kelas tersebut."
    menu:
        "Jatuhkan pulpen untuk mengecek":
            show mc at right
            mc "{i}Aku akan mengecek apakah mereka benar-benar manusia."
            hide mc
            #insert pen falling

            scene bg floor
            #insert bg floor with feet floating.
            "{i}Deg... Deg... DEG..."
            show mc
            mc "{i} MELAYANG!"
            hide mc

            scene bg classroom
            show mc at right
            mc "(Berbisik) Aldi, ayo buruan keluar. Entitas di depan kita nggak menapak tanah!"
            hide mc
            show aldi at left
            al "!!!"
            hide aldi
            "Menyadari kejanggalan tersebut, Della dan Aldi mencoba meminta izin pulang ke 'dosen' yang sedang mengajar."
            
            scene bg blackboard
            show mc at right
            mc "Permisi, Pak. Karena ini sudah malam, kami izin pulang terlebih dahulu."
            hide mc
            show ds #zoom on center
            "Dosen berhenti berbicara. Beliau menatap Della dan Aldi dengan tatapan kosong."
            #insert villain laughter <chuckle>
            ds "Sudah malam, atau sudah tahu?"
            show ds #make it closer or should we make it into background?
            hide ds
            jump blackout
        
        "Ajak Aldi Pulang":
            show mc at right
            mc "Aldi! Ayo keluar, kumohon!!!"
            hide mc
            show aldi at left
            al "Ah! Takut amat kamu!"
            hide aldi
            jump blackout


label blackout:
    scene bg black
    "Lampu ruang Kelas 111 mati secara tiba tiba."
    mc "Aku... pusing sekali."
    "Della dan Aldi terkapar di lantai tidak sadarkan diri."
    jump wokeUp

label wokeUp:
    scene bg aisle
    show mc at right
    mc "Aldi?"
    mc "ALDI?"
    mc "ALDI DI MANA KAMU?"
    hide mc
    "Tidak ada tanda Aldi dimanapun Della melihat. Tak lama, Della menyadari bahwa dia memegang secarik kertas."
    scene bg paper clue
    show mc at right
    mc "Kamu bisa keluar kalau menemukan 4 petunjuk."
    mc "Aldi... Aku tidak bisa menemukan Aldi..."
    mc "Dia hilang dan aku terjebak di sini!"
    hide mc

    #transition
    scene bg mission #word mission with bg black. like this: mission n/ Cari 4 Petunjuk dan Selamatkan Aldi
    jump exploration

#paper = map?
label exploration:
    scene bg aisle
    if lab_is_solved and class_is_solved and aula_is_solved and canteen_is_solved:
        jump finalPuzzle
    else:
        "Petunjuk di kertas mengarah ke 4 tempat utama. Kantin, Aula, Kelas, dan Lab."
        "Tanpa membuang-buang waktu Della segera berjalan menuju lokasi pertamanya yaitu..."
        menu:
            "Lab":
                label labEvent:
                scene bg kcv
                "Lokasi laboratorium berada di lantai 3."
                "Teknik Informatika memiliki 8 Lab, yaitu Lab. Rekayasa Perangkat Lunak, Lab Komputasi berbasis Jaringan,"
                "Lab. Komputasi Cerdas dan Visi, Lab. Teknologi Jaringan dan Keamanan Siber Cerdas,"
                "Lab. Grafika, Interaksi, Gim, dan Analitik, Lab. Algoritma dan Pemrograman,"
                "Lab Manajemen Cerdas Informasi, serta Lab. Pemodelan dan Komputasi Terapan."
                show mc at right
                mc "Ah! Apakah aku harus mengintip ke dalam lab ini satu persatu?"
                hide mc
                menu:
                    "Kemanakah Della harus mengecek?"
                    "Lab. Algoritma dan Pemrograman":
                        scene bg alpro
                        show mc at right
                        mc "Ugh... Lab ini terkunci."
                        mc "Sepertinya aku harus mengecek lab lain."
                        hide mc
                        jump labKCV
                    
                    "Lab. Teknologi Jaringan dan Keamanan Siber Cerdas":
                        scene bg netics
                        show mc at right
                        mc "Ugh... Lab ini terkunci."
                        mc "Sepertinya aku harus mengecek lab lain."
                        hide mc
                        jump labGiga
            
            "Kelas":
                scene bg 107
                show mc at right
                mc "Kelas 107 dan 108 biasanya digunakan oleh IUP. Karena dosen tadi mengajar menggunakan bahasa Indonesia, sepertinya clue nya tidak berada di sini."
                hide mc
                
                "Della menyalakan senter ke pengaturan paling terang."
                "Dia melangkahkan kaki menuju kelas 105."

                scene bg 105
                show mc at right
                mc "Kelas ini memiliki kapasitas 100 orang. Clue pada kertas merujuk pada kelas dengan mahasiswa yang sedikit, sepertinya bukan ini kelas yang dimaksud."
                mc "Sepertinya aku harus menuju ke arah kelas paling ujung."
                hide mc

                "{i} Drap... Drap... Drap..."
                #sound person walking
                "Langkah kaki Della nyaring terdengar di tengah sunyinya kampus."
                scene bg 101
                "Kelas 101 merupakan kelas yang memiliki kapasitas 50 siswa. Kelas ini bersebelahan dengan Mushola dan berada di ujung paling dalam Teknik Informatika."
                show mc at right
                mc "Oke, aku akan mencoba membuka kelas ini."
                #insert doorknob sound
                mc "Ah, terbuka!"
                hide mc
                jump classEvent
        
            "Kantin":
                scene bg aisleeC
                "Kantin Teknik Informatika terletak di sebelah parkiran mobil."
                "Untuk menuju kantin, Della dapat keluar dari Lobby, menuju ke tempat parkir mobil, lalu berjalan ke arah barat, atau melewati lorong di depan 111, lalu berjalan ke arah selatan."
                show mc at right
                mc "Sepertinya aku akan lewat lorong 101 untuk menghemat waktu."
                hide mc
                jump canteenEvent
            
            "Aula":
                scene bg aula
                "Aula Handayani berada di Lantai 2. Aula ini digunakan untuk kegiatan yang melibatkan 200 orang, seperti workshop, atau kelas besar."
                "Aula Handayani berada di sebelah ... (gatau)"
                jump aulaEvent
            
label labKCV:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Komputasi Cerdas dan Visi":
            scene bg kcv
            show mc at right
            mc "Ugh... Lab ini terkunci juga."
            mc "Sepertinya aku harus mengecek lab lain."
            hide mc
            jump labRPL
        "Kembali":
            jump labEvent

label labRPL:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Rekayasa Perangkat Lunak":
            scene bg rpl
            show mc at right
            mc "Lab ini terbuka!"
            mc "Sepertinya ini merupakan laboratorium yang tepat."
            hide mc
            jump labHappening

        "Kembali":
            jump labKCV

label labGiga:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Grafika, Interaksi, Gim, dan Analitik":
            scene bg giga
            show mc at right
            mc "Lab ini juga terkunci."
            mc "Sepertinya aku harus mengecek lab lain."
            hide mc
            jump labMCI
        
        "Kembali":
            jump labEvent

label labMCI:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Manajemen Cerdas Informasi":
            scene bg mci
            show mc at right
            mc "Tidak ada harapan. Lab ini tidak bisa dibuka."
            mc "Sepertinya aku harus mengecek lab lain."
            hide mc
            jump labPKT
        
        "Kembali":
            jump labGiga

label labPKT:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Pemodelan dan Komputasi Terapan":
            scene bg pkt
            show mc at right
            mc "Ugh. Sepertinya aku harus kembali ke titik awal."
            hide mc
            jump labMCI

label labHappening:
    scene bg rpl
    show mc at right
    mc "Komputer-komputer disini tidak seperti biasanya."
    mc "Model ini sepertinya dari tahun ...."
    hide mc

    scene bg biner1
    show mc at right
    mc "Hah? Kenapa komputer ini menyala sendiri?"
    hide mc
    scene bg biner2
    scene bg biner3
    scene bg biner4

    "Pada komputer di depan pintu masuk, muncul layar penuh kode biner mengalir."

    show mc at right
    mc "Layar tersebut seolah membujukku untuk mendekat."
    hide mc

    "Della mengecek komputer tersebut dan menyadari bahwa terdapat dua pilihan yang terpampang."

    show mc at right
    mc "01010010 dan 01001100"
    mc "Kalau dihitung valuenya, bit 0 melambangkan 0."
    mc "Lalu bit 1 melambangkan 2 pangkat n yang dimulai dari urutan 0 dan dibaca dari kanan. Kemudian semuanya dijumlahkan."
    mc "Jadi 01010010 memiliki nilai 0 2 0 0 16 0 64 0, 82 yaitu value ASCII dari R!"
    mc "01001100 memiliki nilai 0 0 4 8 0 0 64 0, 82 yaitu value ASCII dari L!"
    hide mc

    "Setelah mengetahui arti dari kode tersebut, Della merasa semakin putus asa."

    show mc at right
    mc "Apakah aku disuruh untuk memilih ini secara acak?"
    mc "Apa yang terjadi jika aku salah memilih?"
    mc "Sepertinya aku harus mencari clue lanjutan."
    hide mc

    scene bg rpl
    "Bertekad bulat untuk menyelesaikan puzzle tersebut, Della merogoh satu-persatu laci meja di lab tersebut."
    "Tak berselang lama, della menemukan secarik kertas putih di meja ujung."

    show mc at right
    mc "'Pilih jalur dengan rotasi kanan'"
    mc "Rotasi Kanan?"
    mc "Hmm... {i}Right Rotation{/i}... Pada Bitwise Shift rotasi ke kanan berarti {i}Right Shift{/i}..."
    mc "Hmm... {i}Right{/i}..."
    hide mc

    scene bg biner4
    menu:
        "Jawaban mana yang benar?"
        "01010010":
            show mc at right
            mc "Kata kuncinya di RIGHT! Jawabannya R!"
            hide mc
            show bg blackoutScreen
            #insert sound bzztt
            show bg rScreen
            show mc at right
            mc "Yes! Aku berhasil mendapatkan clue!"
            hide mc
            $ lab_is_solved = True
            jump exploration

        "01001100":
            show mc at right
            #insert sound bzztt
            mc "AH! Layarnya meledak!"
            hide mc
            #insert gibberish sound
            "Bayangan kelam muncul dari dalam monitor dan berusaha menarik Della ke dalamnya."
            show mc at right
            #insert no
            mc "TIDAK!!!"
            hide mc
            scene bg black
            $ lab_is_solved = False
            jump exploration

label classEvent:
    scene bg classroom
    "Ruangan kelas 101 masih memiliki kursi kayu jati tergabung meja yang sama."
    show mc at right
    #sound light chuckle
    mc "Jika aku tidak melihat komputer tua dan papan tulis hitam di depan, aku akan mengira ruang kelas ini masih ruang kelas di tahun 2025."
    hide mc

    scene bg blackboard
    show mc at right
    mc "Network graph yang tergambar di papan tulis ini sama dengan yang aku lihat di Kelas 111 sebelum aku dan Aldi terpisah."
    hide mc
    "Pada papan tergambar dua jenis graf, yaitu Graf Bipartite (B) dan Graf Cycle (C)"
    show mc at right
    mc "Hubungkan dua dunia yang berbeda?"
    mc "Hmm... Aku rasa ini merujuk pada jenis grafnya, deh."
    mc "Graf Bipartite itu graf yang simpul-simpulnya bisa dibagi ke dalam dua grup berbeda, dan setiap sisi cuma menghubungkan simpul dari grup yang berbeda."
    mc "Artinya, tidak ada sisi yang menghubungkan simpul dari grup yang sama."
    mc "Sedangkan Graf Cycle adalah graf yang membentuk siklus tertutup."
    mc "Setiap simpul terhubung sedemikian rupa sehingga kalau aku mengikuti jalurnya, aku akan kembali ke simpul awal tanpa mengulangi sisi yang sama."
    hide mc

    menu:
        "Manakah yang kamu pilih?"
        "Graf Bipartite":
            show mc at right
            mc "Aku rasa jawaban yang benar adalah Bipartite soalnya menghubungkan DUA grup"
            mc "Kata kuncinya juga merujuk pada angka dua."
            hide mc
            scene bg blankBlackboard
            "Coretan pada papan perlahan lenyap."
            scene bg bBlackboard
            show mc at right
            mc "Berhasil! Aku memilih jawaban yang tepat!"
            hide mc
            $ class_is_solved = True
            jump exploration
        
        "Graf Cycle":
            show mc at right
            mc "Aku rasa Graf Cycle merupakan jawaban yang benar."
            mc "Graf Cycle bisa menghubungkan dua dunia juga, kan?"
            hide mc
            "Semua coretan di papan hidup."
            "Coretan-coretan tersebut berubah menjadi tangan-tangan panjang yang mencoba menangkan Della."
            show mc at right
            mc "AH! Apa yang terjadi?"
            mc "Jawabanku benar!"
            hide mc
            "Della menghindari tangan-tangan yang ingin menariknya. Dengan panik dia berlari menuju ke pintu."
            scene bg 101
            show mc at right
            mc "Ayo cepat terbuka!!!"
            hide mc
            "Pintu ruang kelas nyaris tak bisa dibuka. Setelah beberapa kali percobaan akhirnya dia berhasil keluar dari ruangan tersebut."
            $ class_is_solved = False
            jump exploration

label canteenEvent:
    $ canteen_is_solved = False
    "start"

label aulaEvent:
    $ aula_is_solved = False
    "start"

return
