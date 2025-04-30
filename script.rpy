# The script of the game goes in this file.

define mc = Character("Della") #mcnya della
# define na = Character("Nadia")
define al = Character("Aldi")
define ds = Character("Dosen ??")
define ct = Character("Ibu Kantin")

default lab_is_solved = False
default class_is_solved = False
default aula_is_solved = False
default canteen_is_solved = False

image ct1 = "images/ct1.png"
image ct2 = "images/ct2.png"
image mc1 = "images/mc/mc.png"
image mc2 = "images/mc/mc1.png"
image mc3 = "images/mc/mc2.png"
image mc4 = "images/mc/mc3.png"
image mc5 = "images/mc/mc4.png"
image mc6 = "images/mc/mc5.png"
image mc7 = "images/mc/mc6.png"
image aldi1 = "images/aldi/aldi.png"
image aldi2 = "images/aldi/aldi2.png"
image aldi3 = "images/aldi/aldi3.png"
image ds = "images/char/ds.png"
image dss = "images/char/dss.png"
image bg supeno = "images/bg/supeno.png"
image bg lobby = "images/bg/lobby.jpg"
image bg classroom = "images/bg/classroom.jpg"
image bg infor = "images/bg/infor.jpg"
image bg kcv = "images/bg/kcv.jpg"
image bg rpl = "images/bg/rpl.jpg"
image bg giga = "images/bg/giga.jpg"
image bg netics = "images/bg/ajk.jpg"
image bg alpro = "images/bg/alpro.jpg"
image bg kbj = "images/bg/kbj.jpg"
image bg aula = "images/bg/aula.jpg"
image bg aula1 = "images/bg/aula1.png"
image bg aula2 = "images/bg/aula2.png"
image bg aula3 = "images/bg/aula3.png"
image bg canteen = "images/bg/canteen.jpg"
image bg car parkinglot = "images/bg/car.jpg"
image bg aisle = "images/bg/aisle.jpg"
image bg aisleC = "images/bg/aisleeC.jpg"
image bg 111 = "images/bg/111.jpg"
image bg black = "images/bg/black.jpg"
image bg pintu111 = "images/bg/pintu111.jpg"
image bg 105 = "images/bg/105.jpg"
image bg 107 = "images/bg/107.jpg"
image bg 101 = "images/bg/101.jpg"
image bg musholla = "images/bg/musholla.png"
image bg floor = "images/bg/floor.png"
image bg blackboard = "images/bg/blackboard.jpg"
image bg board = "images/bg/board.jpg"
image bg pcstart = "images/bg/pcstart.png"
image bg paper clue = "images/bg/paperclue.jpg"
image bg biner1 = "images/bg/biner1.png"
image bg biner2 = "images/bg/biner2.png"
image bg biner3 = "images/bg/biner3.png"
image bg blackoutScreen = "images/bg/blackoutScreen.png"
image bg rScreen = "images/bg/rScreen.png"
image bg blankBlackboard = "images/bg/blankBlackboard.png"
image bg bBlackboard = "images/bg/bBlackboard.png"
image bg staticElectricity = "imagess/bg/staticElectricity.jpg"
image bg fog = "images/bg/staticElectricity.jpg"
image bg white = "images/bg/white.jpg"
image bg class1 = "images/bg/class1.png"
image bg class2 = "images/bg/class2.png"
image bg class3 = "images/bg/class3.png"
image bg staircase = "images/bg/staircase.jpg"
image bg rbtc = "images/bg/rbtc.jpg"
image bg rbtc1 = "images/bg/rbtc1.jpg"
image bg rbtc2 = "images/bg/rbtc2.jpg"
# The game starts here.

label start:
    play music "<from 0.0 to 41.0>horrorMusic.mp3"
    scene bg supeno
    show aldi at left
    al "Kamu... pernah dengar rumor kelas tengah malam di TC?"
    hide aldi
    show mc1 at right
    mc "Huh? Aku ngga pernah denger, tuh"
    mc "Jangan bilang kamu mau nyoba buktiin?"
    hide mc1
    show aldi at left
    al "Ya iyalah, pasti. Kamu ikut kan?"
    hide aldi
    menu: 
        "Apa yang akan kamu pilih?" 

        "Ikut Aldi menyelidiki":
            show mc1 at right
            mc "Ayo, aku juga penasaran."
            hide mc1
            show aldi at left
            al "Oke, kita ketemu di TC jam 23.11, ya"
            hide mc1
            hide aldi
            $ is_investigating = True
        "Tidak mau menyelidiki":
            show mc1 at right
            mc "Kayaknya mending kita pulang aja deh. Perasaanku ga enak."
            $ is_investigating = False

if is_investigating:
    jump firstNight
else:
    scene bg infor
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
                    mc "Nggak ada apa apa sih di sini. Mungkin kita harus cek kelas lain."
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
                al "Di sini juga nggak ada apa apa. Sepertinya kita harus cek ruangan kelas lain."
                hide aldi
                jump secondChoice
            "Cek 101":
                scene bg 101
                al "Della! Aku lihat lampu di kelas seberang menyala!"
                show aldi1 at left
                hide aldi1
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
    # stop music fadeout 1.0
    scene bg 111
    "Sesampainya di sana, mereka mendengar suara bising dari dalam kelas."
    play sound "classNoise.mp3"
    ""
    stop sound
    show aldi at left
    al "Tuh kan! Bener ada!"
    hide aldi
    show mc4 at right
    mc "Gila, kok bisa ada suara jam segini."
    # hide mc
    mc "{i}Aku rasa kita harus menghentikan penyelidikan ini. Tapi... Kita sudah sejauh ini."
    hide mc4
    "Della merasa semakin bimbang. Della merasa bahwa mereka harus menghentikan penyelidikan mereka di sini. Namun di sisi lain, Della juga penasaran atas kebenaran rumor tersebut."
    menu:
        "Ajak Aldi untuk masuk ke Kelas 111":
            show mc at right
            mc "Udah, lah. Kita nyoba masuk aja, yuk."
            hide mc
            jump event111

        "Minta Aldi untuk mengecek":
            show mc6 at right
            mc "Aku ngerasa ini ide buruk deh, Al."
            hide mc6
            show aldi at left
            al "Ayolah, pengecut!"
            hide aldi
            jump event111
    
label event111:
    hide aldi
    hide mc
    "Kalian memilih untuk masuk ke dalam kelas."
    scene bg pintu111
    play sound "doorknock.mp3"
    "{i}Tok... Tok... Tok.."
    stop sound
    ds "Masuk saja, pintunya tidak dikunci."
    scene bg black
    play sound "doorOpen.mp3"
    "Pintu dibuka secara perlahan. Di dalam, terlihat seorang dosen yang mengajar di depan banyak mahasiswa lain-"
    stop sound
    scene bg classroom
    "-tetapi semua wajah mahasiswa di dalam terlihat kabur!"
    play sound "heartbeat.mp3"
    "{i}Deg... Deg.. Deg..."
    #insert sound chair being pulled
    stop sound
    "Melihat hal tersebut, Aldi yang {i} excited {/i} langsung mengambil bangku paling depan."
    show mc6 at right #focus on center, zoom
    mc "{i} AH! Aku harus pulang sekarang!. Tapi jika aku pergi siapa yang akan menemani Aldi?"
    hide mc6
    menu:
        "Duduk bersama Aldi":
            show mc6 at right
            "{i}Kurasa tidak ada salahnya mencoba duduk sebentar. Siapa tau aku akan menemukan akar dari semua hal aneh ini."
            hide mc6
            # play music "<from 0.0 to 41.0>  volume 0.1 horrorMusic.mp3"
            "Della dan Aldi menatap papan tulis untuk mengikuti materi yang tengah diajarkan oleh dosen misterius tersebut."
            show mc6 at right
            mc "{i}Aneh... Aku merasa hawa di sini semakin dingin."
            mc "{i}Indikator AC-nya tidak menyala, pintu dan jendela dikunci. Darimana asal hawa dingin yang kurasakan ini?"
            mc "{i}Materi yang diajarkan juga aneh. Mengapa kita diajarkan cara memakai disket 3.5 inchi untuk transfer data?"
            hide mc6
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
    show mc6 at right
    mc "{i}Kenapa semua orang tidak ada yang bergerak, ya?"
    #insert sound dosen voice distorted
    mc "{i}Suara dosen juga kadang terdistorsi seperti memakai mic yang memiliki daya rendah."
    mc "Ini kayak nggak bener, deh, Al. Ada yang aneh sama dosen itu."
    hide mc6
    show aldi at left
    al "Iya, suasana kelasnya juga aneh."
    al "Jangan-jangan..."
    al "...mereka ini semua hantu!"
    hide aldi
    "Aldi tertawa dengan keras."
    play sound "man laugh 2.mp3"
    #insert laughter
    show aldi2 at left
    al "HAHAHAHA"
    stop sound
    al "Nggak mungkin lah, Del. Jelas jelas penampilan mereka seperti manusia, kok!"
    hide aldi2
    "Bulu kuduk Della berdiri. Insting Della menyuruhnya untuk segera pergi dari ruang kelas tersebut."
    menu:
        "Jatuhkan pulpen untuk mengecek":
            show mc at right
            mc "{i}Aku akan mengecek apakah mereka benar-benar manusia."
            play sound "pen_drop.mp3"
            hide mc

            scene bg floor
            #insert bg floor with feet floating.
            play sound "heartbeat.mp3"
            "{i}Deg... Deg... DEG..."
            show mc7
            mc "{i} MELAYANG!"
            hide mc7

            scene bg classroom
            show mc2 at right
            mc "(Berbisik) Aldi, ayo buruan keluar. Entitas di depan kita nggak menapak tanah!"
            hide mc2
            show aldi1 at left
            al "!!!"
            hide aldi1
            "Menyadari kejanggalan tersebut, Della dan Aldi mencoba meminta izin pulang ke 'dosen' yang sedang mengajar."
            
            scene bg blackboard
            show mc7 at right
            mc "Permisi, Pak. Karena ini sudah malam, kami izin pulang terlebih dahulu."
            hide mc7
            show ds #zoom on center
            "Dosen berhenti berbicara. Beliau menatap Della dan Aldi dengan tatapan kosong."
            hide ds
            #insert villain laughter <chuckle>
            scene bg board
            show dss
            stop music
            ds "Sudah malam, atau sudah tahu?"
            #show dss #make it closer or should we make it into background?
            hide dss
            jump blackout
        
        "Ajak Aldi Pulang":
            show mc6 at right
            stop music
            mc "Aldi! Ayo keluar, kumohon!!!"
            hide mc6
            show aldi at left
            al "Ah! Takut amat kamu!"
            hide aldi
            jump blackout


label blackout:
    scene bg black
    "Lampu ruang Kelas 111 mati secara tiba tiba."
    mc "Aku... pusing sekali."
    "Della terkapar di lantai tidak sadarkan diri."
    jump wokeUp

label wokeUp:
    scene bg aisle
    show mc2 at right
    mc "Aldi?"
    mc "ALDI?"
    mc "ALDI DI MANA KAMU?"
    hide mc2
    "Tidak ada tanda Aldi dimanapun Della melihat. Tak lama, Della menyadari bahwa dia memegang secarik kertas."
    scene bg paper clue
    show mc2 at right
    mc "Kamu bisa keluar kalau menemukan 4 petunjuk."
    mc "Aldi... Aku tidak bisa menemukan Aldi..."
    mc "Dia hilang dan aku terjebak di sini!"
    hide mc2

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
        play music "music_box.mp3"
        "Tanpa membuang-buang waktu Della segera berjalan menuju lokasi yang dia pilih yaitu..."
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
                        show mc6 at right
                        mc "Ugh... Lab ini terkunci."
                        mc "Sepertinya aku harus mengecek lab lain."
                        hide mc6
                        jump labKCV
                    
                    "Lab. Teknologi Jaringan dan Keamanan Siber Cerdas":
                        scene bg netics
                        show mc6 at right
                        mc "Ugh... Lab ini terkunci."
                        mc "Sepertinya aku harus mengecek lab lain."
                        hide mc6
                        jump labGiga
            
            "Kelas":
                scene bg 107
                show mc at right
                mc "Kelas 107 dan 108 biasanya digunakan oleh IUP. Karena dosen tadi mengajar menggunakan bahasa Indonesia, sepertinya clue nya tidak berada di sini."
                hide mc
                
                "Della menyalakan senter ke pengaturan paling terang."
                "Dia melangkahkan kaki menuju kelas 105."

                scene bg 105
                show mc6 at right
                mc "Kelas ini memiliki kapasitas 100 orang. Clue pada kertas merujuk pada kelas dengan mahasiswa yang sedikit, sepertinya bukan ini kelas yang dimaksud."
                mc "Sepertinya aku harus menuju ke arah kelas paling ujung."
                hide mc6

                play sound "walk.mp3"
                "{i} Drap... Drap... Drap..."
                "Langkah kaki Della nyaring terdengar di tengah sunyinya kampus."
                scene bg 101
                "Kelas 101 merupakan kelas yang memiliki kapasitas 50 siswa. Kelas ini bersebelahan dengan Mushola dan berada di ujung paling dalam Teknik Informatika."
                show mc6 at right
                mc "Oke, aku akan mencoba membuka kelas ini."
                play sound "doorOpen.mp3"
                mc "Ah, terbuka!"
                stop sound
                hide mc6
                jump classEvent
        
            "Kantin":
                scene bg aisleC
                "Kantin Teknik Informatika terletak di sebelah parkiran mobil."
                "Untuk menuju kantin, Della dapat keluar dari Lobby, menuju ke tempat parkir mobil, lalu berjalan ke arah barat, atau melewati lorong di depan 111, lalu berjalan ke arah selatan."
                show mc at right
                mc "Sepertinya aku akan lewat lorong 111 untuk menghemat waktu."
                hide mc
                jump canteenEvent
            
            "Aula":
                scene bg aula
                "Aula Handayani berada di Lantai 2. Aula ini digunakan untuk kegiatan yang melibatkan 200 orang, seperti workshop, atau kelas besar."
                "Aula Handayani berada di sebelah Ruang Staff Tata Usaha"
                jump aulaEvent
            
label labKCV:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Komputasi Cerdas dan Visi":
            scene bg kcv
            show mc6 at right
            mc "Ugh... Lab ini terkunci juga."
            mc "Sepertinya aku harus mengecek lab lain."
            hide mc6
            jump labRPL
        "Kembali":
            jump labEvent

label labRPL:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Rekayasa Perangkat Lunak":
            scene bg rpl
            show mc4 at right
            mc "Lab ini terbuka!"
            mc "Sepertinya ini merupakan laboratorium yang tepat."
            hide mc4
            jump labHappening

        "Kembali":
            jump labKCV

label labGiga:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Grafika, Interaksi, Gim, dan Analitik":
            scene bg giga
            show mc6 at right
            mc "Lab ini juga terkunci."
            mc "Sepertinya aku harus mengecek lab lain."
            hide mc6
            jump labKBJ
        
        "Kembali":
            jump labEvent

label labKBJ:
    menu:
        "Kemanakah Della harus mengecek?"
        "Lab. Komputasi Berbasis Jaringan":
            scene bg kbj
            show mc6 at right
            mc "Ugh. Sepertinya aku harus kembali ke titik awal."
            hide mc6
            jump labKCV

label labHappening:
    scene bg rpl
    show mc6 at right
    mc "Komputer-komputer disini tidak seperti biasanya."
    mc "Model ini sepertinya sudah sangat lama"
    hide mc6

    scene bg biner1
    show mc4 at right
    mc "Hah? Kenapa komputer ini menyala sendiri?"
    hide mc4

    "Pada komputer di depan pintu masuk, muncul layar penuh kode biner mengalir."

    show mc at right
    mc "Layar tersebut seolah membujukku untuk mendekat."
    hide mc

    "Della mendekati komputer tersebut dan menyadari bahwa salah satu komputer menampilkan hal yang berbeda."

    show mc6 at right
    mc "Apa ini?"
    mc "Pilih jalur dengan rotasi kanan?"
    mc "01010010 dan 01001100"
    mc "Apa maksudnya?"
    mc "Apakah aku disuruh untuk memilih ini secara acak?"
    mc "Apa yang terjadi jika aku salah memilih?"
    mc "Hmm."
    mc "Kalau dihitung valuenya, bit 0 melambangkan 0."
    mc "Lalu bit 1 melambangkan 2 pangkat n yang dimulai dari urutan 0 dan dibaca dari kanan. Kemudian semuanya dijumlahkan."
    mc "Jadi 01010010 memiliki nilai 0 2 0 0 16 0 64 0, 82 yaitu value ASCII dari R!"
    mc "01001100 memiliki nilai 0 0 4 8 0 0 64 0, 76 yaitu value ASCII dari L!"
    hide mc6

    "Setelah mengetahui arti dari kode tersebut, Della merasa semakin putus asa."

    show mc at right
    mc "'Pilih jalur dengan rotasi kanan'"
    mc "Rotasi Kanan?"
    mc "Hmm... {i}Right Rotation{/i}... Pada Bitwise Shift rotasi ke kanan berarti {i}Right Shift{/i}..."
    mc "Hmm... {i}Right{/i}..."
    hide mc

    scene bg biner1
    menu:
        "Jawaban mana yang benar?"
        "01010010":
            show mc4 at right
            mc "Kata kuncinya di RIGHT! Jawabannya R!"
            hide mc4
            scene bg biner2
            play sound "bzzt.mp3"
            #scene bg rScreen
            show mc5 at right
            stop sound
            mc "Yes! Aku berhasil mendapatkan clue!"
            hide mc5
            $ lab_is_solved = True
            jump exploration

        "01001100":
            scene bg biner3
            show mc2 at right
            play sound "bzzt.mp3"
            mc "AH! Layarnya meledak!"
            play sound "gasp.mp3"
            hide mc2
            #insert gibberish sound
            stop sound
            "Bayangan kelam muncul dari dalam monitor dan berusaha menarik Della ke dalamnya."
            show mc3 at right
            #insert no
            play sound "afraid.mp3" volume 0.5
            mc "TIDAK!!!"
            stop sound
            hide mc3
            scene bg black
            $ lab_is_solved = False
            jump exploration

label classEvent:
    scene bg classroom
    "Ruangan kelas 101 masih memiliki kursi kayu jati tergabung meja yang sama."
    show mc6 at right
    #sound light chuckle
    mc "Tapi papan tulisnya model lama yang menggunakan kapur."
    hide mc6

    scene bg class1
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
            "Coretan pada papan perlahan lenyap."
            scene bg class2
            show mc5 at right
            mc "Berhasil! Aku memilih jawaban yang tepat!"
            hide mc5
            $ class_is_solved = True
            jump exploration
        
        "Graf Cycle":
            show mc at right
            mc "Aku rasa Graf Cycle merupakan jawaban yang benar."
            mc "Graf Cycle bisa menghubungkan dua dunia juga, kan?"
            hide mc
            scene bg class3
            "Semua coretan di papan hidup."
            "Coretan-coretan tersebut berubah menjadi tangan-tangan panjang yang mencoba menangkan Della."
            show mc3 at right
            play sound "gasp.mp3"
            mc "AH! Apa yang terjadi?"
            mc "Jawabanku benar!"
            hide mc3
            "Della menghindari tangan-tangan yang ingin menariknya. Dengan panik dia berlari menuju ke pintu."
            scene bg 101
            show mc2 at right
            play sound "run.mp3"
            mc "Ayo cepat terbuka!!!"
            stop sound
            play sound "heartbeat.mp3"
            mc "Tolong terbukalah!!!"
            stop sound
            hide mc2
            "Pintu ruang kelas nyaris tak bisa dibuka. Setelah beberapa kali percobaan akhirnya dia berhasil keluar dari ruangan tersebut."
            $ class_is_solved = False
            jump exploration

label canteenEvent:
    scene bg aisleC
    show mc2 at right
    play sound "gasp.mp3"
    mc "Ugh... Kenapa lampunya senternya mati..."
    hide mc2
    "Satu-satunya penerangan yang dimiliki oleh Della mati tiba-tiba."
    "Mata Della berusaha keras untuk menyesuaikan dengan kegelapan."
    stop music
    scene bg canteen
    "Tak lama, ia berjumpa dengan seseorang yang memakai pakaian layaknya ibu kantin."
    "Wanita tersebut berdiri diam dengan senyum yang kosong"
    "Senyumnya melebar ketika dia melihat Della mendekat"
    play music "whistle.mp3" fadein 0.5
    show mc6 at right
    mc "Halo, apakah kamu tadi melihat seorang laki-laki seumuranku dengan baju putih?"
    mc "Halo? Apakah kamu mendengarku?"
    hide mc6
    show ct at left
    ct "..."
    hide ct
    "Tak mendapat jawaban yang diinginkan, Della memfokuskan pandangannya ke daftar menu di meja."
    "Tertulis 5 menu di kertas tersebut: Nasi goreng, Mi goreng, Nasi campur, Ketoprak, dan Tungtungtungsahur."
    show mc6 at right
    mc "{i} Kenapa ada tungtungtungsahur di sini?"
    hide mc6
    show ct at left
    ct "Kamu perlu percaya pada logika..."
    hide ct
    "Suara Ibu Kantin terdengar sangat halus dan dingin. Della berpikir keras untuk mengartikan perkataan tersebut."
    menu:
        "Apa yang akan kamu pilih?"
        "Nasi Goreng":
            $ canteen_is_solved = False
            jump canteenMenu
        "Mi Goreng":
            $ canteen_is_solved = False
            jump canteenMenu
        "Nasi Campur":
            $ canteen_is_solved = False
            jump canteenMenu
        "Ketoprak":
            $ canteen_is_solved = False
            jump canteenMenu
        "Tungtungtungsahur":
            scene bg canteen
            "Ibu kantin perlahan menghilang seperti kabut"
            show ct2
            stop music
            ct "Pilihan yang tepat."
            hide ct2 with Dissolve(3)
            $ canteen_is_solved = True
            scene bg white
            jump exploration

label canteenMenu:
    scene bg canteen
    show mc7 at right
    play sound "breathing_fast.mp3"
    mc "APA YANG TERJADI?"
    stop sound
    play sound "gasp.mp3"
    mc "AHH!!!"    
    hide mc7
    "Ibu kantin menyeringai dan matanya berubah menjadi merah."
    show ct1
    play sound "possessed.mp3"
    ct "HII... HIIIIIIIIIIIIII"
    hide ct1
    scene bg canteen
    show mc2 at right
    stop sound
    play sound "run.mp3"
    mc "Aku harus segera pergi dari sini!!!" 
    stop sound
    hide mc2
    stop music
    "Della berlari menuju ke lorong awal"
    scene bg black
    jump exploration

label aulaEvent:
    scene bg aula
    show mc6 at right
    mc "{i}Harusnya di sini nggak ada apa-apa kan ya?"
    play sound "heartbeat.mp3"
    mc "{i}Kenapa jantungku berdebar semakin keras..."
    mc "{i}Perasaanku semakin nggak enak..."
    hide mc6
    play sound "doorOpen.mp3"
    "Pintu aula terbuka dengan sendirinya. Lampu-lampu berkedip dengan sendirinya. Penerangan yang biasanya memberi suasana nyaman kini terasa mencekik."
    "Della memberanikan diri untuk mendekati pantulan dari layar proyektor yang menampilkan kode aneh."
    stop sound
    scene bg aula1
    show mc6 at right
    mc "Apa artinya ini?"
    mc "Apakah aku disuruh untuk menulis output?"
    hide mc6
    play sound "rumble.mp3"
    "Terdengar suara samar-samar yang menggema dari arah luar aula."
    "Suara tersebut terus mengulang hal yang sama."
    "Bak berbisik di telinga Della, suara tersebut mengucapkan suatu kalimat-"
    stop sound
    "'Pilih asal mula dari segalanya...'"
    "Muncul 4 pilihan di depan Della."
    show mc6 at right
    mc "Asal mula dari segalanya?"
    hide mc6
    show mc at right
    mc "{i}Oke. Aku mengerti. Apakah maksudnya bahasa pemrograman yang sesuai?"
    mc "{i}Thank God{/i}. Aku tahu jawabannya."
    hide mc

    menu:
        "Kotlin":
            $ aula_is_solved = False
            jump aulaMenu
        "Java":
            $ aula_is_solved = False
            jump aulaMenu
        "Python":
            $ aula_is_solved = False
            jump aulaMenu
        "C":
            show mc at right
            mc "{i}Hmm... Aku akan memilih C."
            hide mc
            "Layar seketika memerah."
            play sound "gasp.mp3"
            scene bg aula2
            "'C' terpampang di layar proyektor."
            show mc5 at right
            play sound "fyuh.mp3"
            mc "Hore! Sepertinya ini jawaban yang benar!"
            hide mc5
            show black
            $ aula_is_solved = True
            jump exploration

label aulaMenu:
    scene bg aula3
    show mc7 at right
    play sound "gasp.mp3"
    mc "APA YANG TERJADI?"
    play sound "afraid.mp3" volume 0.3  
    mc "AHH!!!"
    stop sound
    hide mc7
    play sound "bzzt.mp3"
    "Layar menunjukkan ribuan error."
    stop sound
    scene bg aula3
    show mc2 at right
    play sound "run.mp3"
    mc "Aku harus segera pergi dari sini!!!"    
    hide mc2
    stop sound
    "Della berlari menuju ke lorong awal"
    scene bg black
    jump exploration

label finalPuzzle:
    scene bg 111
    show mc6 at right
    mc "Ugh.. Aku sudah menemukan keempat clue yang dimaksud."
    mc "Apa yang harus kulakukan dengan ini?"
    mc "Di masing-masing tempat aku menemukan huruf-huruf berupa C, B, T, dan R."
    mc "Apakah aku diminta untuk menggabungkan semuanya?"
    mc "Tapi tidak ada kata yang bisa dibentuk. Bahkan tidak ada huruf vokal..."
    mc "Ah, sebentar"
    hide mc6
    show mc4 at right
    mc "R-B-T-C."
    play sound "gasp.mp3"
    mc "Huruf-huruf ini bisa dikombinasikan menjadi RBTC!"
    hide mc4
    show mc at right
    stop music
    mc "Haruskah aku ke sana?"

    menu:
        "Pergi":
            play music "<from 70.0 to 122.0>horrorMusic.mp3"
            mc "Oke. Aku sudah mendapatkan semua cluenya. Tidak ada alasan untuk aku tidak pergi."
            play sound "run.mp3"
            scene bg staircase
            mc "Apakah aku harus menyelesaikan puzzle lagi?"
            mc "Aku masih perlu mencari Aldi... Aku khawatir padanya"
            hide mc
            stop sound
            "Della yang khawatir dengan Aldi bergegas menaiki tangga menuju RBTC."
            play sound "walk.mp3"
            "Terlihat Aldi yang terbujur lemas di balik ruang kelas."
            stop sound
            scene bg rbtc1
            show mc7 at right
            play sound "run.mp3"
            mc "ALDI!!"
            mc "Aldi! Bangun! Ayo kita keluar!!"
            stop sound
            mc "ALDI!!"
            play sound "door_banging.mp3"
            mc "Ahh!! Pintunya tidak bisa terbuka!!!"
            stop sound
            mc "Apa yang harus kulakukan..."
            hide mc7
            "Dari pojok pandangnya, Della melihat tangan Aldi menunjuk ke arah depan."
            show mc6 at right
            mc "Apakah aku diminta untuk mengecek loker-loker ini?"
            hide mc6
            stop music
            "Dari kertas yang tergeletak di atas meja tertulis clue untuk menyelesaikan puzzle terakhir."
            scene bg rbtc
            show mc6 at right
            mc "'Kamu hanya bisa memilih satu loker.'"
            mc "'Tempat pertama kamu ragu, waktu adalah pintu'."
            mc "Tempat pertama aku ragu?"
            show mc4 at right
            mc "Apakah itu saat aku berpikir untuk melanjutkan penyelidikan tentang rumor ini?"
            mc "Saat itu Aldi mengajak bertemu pada pukul 23.11."
            hide mc4
            show mc at right
            mc "Jadi... 2? 3? atau 1?"
            mc "Semua kejadian ini bermula dari kelas 111"
            mc "Jadi mungkin..."
            mc "Aku harus memilih loker 1?"
            mc "Oke. Aku tidak peduli ini benar atau salah. Aku akan mencoba untuk membuka loker 1."
            hide mc
            "Dengan segera, Della membuka loker 1 yang menyimpan sebuah kunci."
            play sound "locker.mp3"
            mc "Terbuka!"
            stop sound
            show mc5 at right
            mc "Kunci! Apakah ini kunci untuk membuka ruang kelas RBTC?"
            hide mc5
            "Della berhasil membuka RBTC dengan kunci yang ditemukannya di loker 1."
            scene bg rbtc2
            show mc4 at right
            play sound "key.mp3"
            mc "TERBUKA!"
            stop sound
            mc "ALDI! Ayo kita pergi dari sini!"
            hide mc4
            show aldi3 at left
            al "Della? Apa yang terjadi? Kenapa aku di sini?"
            al "Aku mengalami mimpi buruk dimana aku-"
            hide aldi3
            show mc6 at right
            mc "Kita bisa bicarakan itu nanti. Ayo kita keluar sekarang."
            mc "Kita tidak punya banyak waktu"
            play sound "run.mp3"
            hide mc6
            scene bg infor
            "Della dan Aldi berhasil keluar dari Gedung Departemen Informatika. Malam ini merupakan malam yang tidak akan pernah dilupakan oleh mereka berdua."
            stop sound
            "Terima kasih telah mengikuti cerita kami."
            return
        
        "Memikirkan ulang":
            mc "Mengingat kejadian-kejadian aneh yang aku alami, sepertinya memikirkan ulang merupakan keputusan terbaik."
            play sound "walk.mp3"
            mc "Suara apa itu?"
            hide mc
            show mc2 at right
            stop sound
            play sound "heartbeat.mp3"
            mc "{i}Dosen 111? Sejak kapan dia berdiri di sampingku?"
            mc "{i}Aku akan pergi dari sini secara diam diam."
            hide mc2
            show dss at left
            play sound "dosen111.mp3"
            ds "...Ma...U...Ke...Ma...Na...?"
            ds "...SUDAAAAAAAHHH...TAAAAUUU...YA...."
            stop sound
            hide dss
            show black
            "Della tidak berhasil menghindari cengkraman dosen tersebut."
            "Ketika dia kembali sadar, dia sudah berada di titik awal pencarian dan harus memulai semuanya dari awal."
            $ class_is_solved = False
            $ aula_is_solved = False
            $ lab_is_solved = False
            $ canteen_is_solved = False
            jump exploration
