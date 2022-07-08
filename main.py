import os
import zodiak
os.system('cls')

nama_bulan = ['januari','februari' , 'maret' , 'april' , 'mei' , 'juni' , 'juli' , 'agustus' , 'september' , 'oktober' , 'november' , 'desember']

stats = True
menu = {
    1: 'Check Ramalan Zodiak',
    2: 'Exit'
}

back = {
    1: 'Kembali ke Menu',
    2: 'Exit'
}

def print_menu():
    for key in menu.keys():
        print (key, '', menu[key] )

def print_back():
    for key in back.keys():
        print (key, '', back[key] )

def back_menu():
    print('\n============================')
    print_back()
    print('============================')
    
    option = input('Enter your choice: ')
    back_func(option)

def back_func(option):
    if option == '1':
        os.system('cls')
        main_menu()
    elif option == '2':
        print('Thanks for using the app!')
        exit()
    else:
        print('Please enter a number 1 or 2.')
    return back_menu()

def check_zodiak(nama, day, month):
    if month == 'desember':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Sagitarius.
{zodiak.sagitarius[0]}
Keuangan    : Masih dapat dikontrol sejauh ini.
Pelajaran   : Tugas mulai numpuk tuh.
Asmara      : Kalo jomblo ya jomblo aja.
Kesehatan   : Makin gendut aja bos.""" if (day < 22) else f"""
Hai, {nama}. Zodiakmu adalah Capricorn.
{zodiak.Capricorn}
Keuangan    : Minggu ini lagi krisis.
Pelajaran   : kerjakan selagi bisa kamu kerjakan.
Asmara      : Si dia kurang perhatian banget tuh.
Kesehatan   : Badan pada lemes semua.""" 
        
    elif month == 'januari':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Capricorn.
{zodiak.Capricorn}
Keuangan    : Minggu ini lagi krisis.
Pelajaran   : kerjakan selagi bisa kamu kerjakan.
Asmara      : Si dia kurang perhatian banget tuh.
Kesehatan   : Badan pada lemes semua."""  if (day < 20) else f"""
Hai, {nama}. Zodiakmu adalah Aquarius.
{zodiak.Aquarius}
Keuangan    : Hari ini kamu lagi beruntung.
Pelajaran   : Kamu bakal dapat tugas yang banyak.
Asmara      : Buat kamu yang jomblo bakal dapat gebetan baru.
Kesehatan   : Flu datang menghampiri mu."""

    elif month == 'februari':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Aquarius.
{zodiak.Aquarius}
Keuangan    : Hari ini kamu lagi beruntung.
Pelajaran   : Kamu bakal dapat tugas yang banyak.
Asmara      : Buat kamu yang jomblo bakal dapat gebetan baru.
Kesehatan   : Flu datang menghampiri mu.""" if (day < 19) else f"""
Hai, {nama}. Zodiakmu adalah Pisces.
{zodiak.Pisces}
Keuangan    : Banyak pengeluaran, tapi masih bisa diatasi kok. 
Pelajaran   : Tugas dapat kamu atasi dengan cepat.
Asmara      : Si dia mulai menjauh tuh.
Kesehatan   : Jangan terlalu memaksakan diri. """

    elif month == 'maret':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Pisces.
{zodiak.Pisces}
Keuangan    : Banyak pengeluaran, tapi masih bisa diatasi kok. 
Pelajaran   : Tugas dapat kamu atasi dengan cepat.
Asmara      : Si dia mulai menjauh tuh.
Kesehatan   : Jangan terlalu memaksakan diri. """ if (day < 21) else f"""
Hai, {nama}. Zodiakmu adalah Aries.
{zodiak.aries}
Keuangan    : Jangan terlalu boros teman.
Pelajaran   : Jangan kebanyakan santai.
Asmara      : Kasih perhatian lebih kepada si dia yuk.
Kesehatan   : Jangan sering keluar malam. """

    elif month == 'april':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Aries.
{zodiak.aries}
Keuangan    : Jangan terlalu boros teman.
Pelajaran   : Jangan kebanyakan santai.
Asmara      : Kasih perhatian lebih kepada si dia yuk.
Kesehatan   : Jangan sering keluar malam. """ if (day < 20) else f"""
Hai, {nama}. Zodiakmu adalah Taurus.
{zodiak.Taurus}
Keuangan    : Waahh, kamu dapat rezeki besar minggu ini.
Pelajaran   : Tugas jangan ditumpukin.
Asmara      : Ciee, makin lengket aja nich.
Kesehatan   : Tuhh, badan makin bugar aja. """

    elif month == 'mei':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Taurus.
{zodiak.Taurus}
Keuangan    : Waahh, kamu dapat rezeki besar minggu ini.
Pelajaran   : Tugas jangan ditumpukin.
Asmara      : Ciee, makin lengket aja nich.
Kesehatan   : Tuhh, badan makin bugar aja. """ if (day < 21) else f"""
Hai, {nama}. Zodiakmu adalah Gemini.
{zodiak.Gemini}
Keuangan    : Kamu kali ini terlalu royal.
Pelajaran   : Fokuskan pikiranmu kepada pelajaran.
Asmara      : Maaf ya, bulan ini kamu masih tetep jomblo.
Kesehatan   : Makin lebar aja nih bos. """

    elif month == 'juni':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Gemini.
{zodiak.Gemini}
Keuangan    : Kamu kali ini terlalu royal.
Pelajaran   : Fokuskan pikiranmu kepada pelajaran.
Asmara      : Maaf ya, bulan ini kamu masih tetep jomblo.
Kesehatan   : Makin lebar aja nih bos. """ if (day < 21) else f"""
Hai, {nama}. Zodiakmu adalah Cancer.
{zodiak.Cancer}
Keuangan    : Masih Stabil. 
Pelajaran   : Tetep seperti ini
Asmara      : Ayo cari pasangan mu.
Kesehatan   : Tambahi jam tidur. """

    elif month == 'juli':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Cancer.
{zodiak.Cancer}
Keuangan    : Masih Stabil. 
Pelajaran   : Tetep seperti ini
Asmara      : Ayo cari pasangan mu.
Kesehatan   : Tambahi jam tidur. """ if (day < 23) else f"""
Hai, {nama}. Zodiakmu adalah Leo.
{zodiak.Leo}
Keuangan    : Beli cemilannya dikurangi.
Pelajaran   : Perhatikan ketika dosen menjelaskan.
Asmara      : Si dia mulai menjauh tuh.
Kesehatan   : Tidak ada masalah. """

    elif month == 'agustus':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Leo.
{zodiak.Leo}
Keuangan    : Beli cemilannya dikurangi.
Pelajaran   : Perhatikan ketika dosen menjelaskan.
Asmara      : Si dia mulai menjauh tuh.
Kesehatan   : Tidak ada masalah. """ if (day < 23) else f"""
Hai, {nama}. Zodiakmu adalah Virgo.
{zodiak.Virgo}
Keuangan    : Rejeki mu  dateng tuh.
Pelajaran   : Kamu sangat menguasai materi ini.
Asmara      : Si dia lagi butuh perhatian dari kamu.
Kesehatan   : Sering sering olahraga. """

    elif month == 'september':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Virgo.
{zodiak.Virgo}
Keuangan    : Rejeki mu  dateng tuh.
Pelajaran   : Kamu sangat menguasai materi ini.
Asmara      : Si dia lagi butuh perhatian dari kamu.
Kesehatan   : Sering sering olahraga. """ if (day < 23) else f"""
Hai, {nama}. Zodiakmu adalah Libra.
{zodiak.Libra}
Keuangan    : Kamu terlalu boros teman.
Pelajaran   : Jangan tidur di kelas terus.
Asmara      : Kamu joblo sejati.
Kesehatan   : Sepertinya kamu bakal demam. """

    elif month == 'oktober':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Libra.
{zodiak.Libra}
Keuangan    : Kamu terlalu boros teman.
Pelajaran   : Jangan tidur di kelas terus.
Asmara      : Kamu joblo sejati.
Kesehatan   : Sepertinya kamu bakal demam. """ if (day < 23) else f"""
Hai, {nama}. Zodiakmu adalah Scorpio. 
{zodiak.scorpius}
Keuangan    : Masih stabil.
Pelajaran   : Tidak ada masalah.
Asmara      : Kamu bakal patah hati.
Kesehatan   : Sejauh ini masih baik."""

    elif month == 'november':
        zodiak_saya = f"""
Hai, {nama}. Zodiakmu adalah Scorpio. 
{zodiak.scorpius}
Keuangan    : Masih stabil.
Pelajaran   : Tidak ada masalah.
Asmara      : Kamu bakal patah hati.
Kesehatan   : Sejauh ini masih baik.""" if (day < 22) else f"""
Hai, {nama}. Zodiakmu adalah Sagitarius.
{zodiak.sagitarius[0]}
Keuangan    : Masih dapat dikontrol sejauh ini.
Pelajaran   : Tugas mulai numpuk tuh.
Asmara      : Kalo jomblo ya jomblo aja.
Kesehatan   : Makin gendut aja bos."""

    else:
        print('Maaf zodiak tidak dapat ditemukan')

    print(zodiak_saya)

def main_menu():
    print('=========== Menu ===========')
    print_menu()
    print('============================')
    
    option = input('Enter your choice: ')
    menu_func(option)

def menu_func(option):
    if option == '1':      
        nama = input('\nMasukkan nama : ')
        day = input('Masukkan tanggal Lahir : ')
        month = input('Masukkan bulan Lahir : ')
        month = month.lower()
        
        try:
            if int(day) > 31:
                print('Tanggal tidak Valid!')           
            elif not month in nama_bulan:
                print('Bulan tidak Valid!')
            elif (month == 'februari') and (int(day) > 29):
                print('Tanggal tidak Valid!')
            else:
                check_zodiak(nama, int(day), month)
                
        except:
            print("Please enter a valid data!")
            

        back_menu()
        option = input('Enter your choice: ')
        back_func(option)
        
    elif option == '2':
        print('Thanks for using the app!')
        exit()
    else:
        print('Please enter a number 1 or 2.\n')
    return main_menu()

print('    Welcome to My ZoChar    \n')
main_menu()
    
    
    
