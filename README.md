# Toko Uap
Nama : Mirfak Naufal Pratama Putra

NPM: 2306244961

Kelas: PBP A

Link PWS: http://mirfak-naufal-tokouap.pbp.cs.ui.ac.id/
<details>
<summary>Jawaban Pertanyaan Tugas 2</summary>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial):

1. Membuat direktori toko-uap, mengaktifkan virtual environment, lalu start project menggunakan django dengan nama project toko_uap.
2. Membuat aplikasi dengan nama main, membuat direktori baru, lalu membuat berkas main.html untuk tampilan web.
3. Mengubah berkas models.py, mengisi file views.py, melakukan routing pada aplikasi main dan mengonfigurasi routing pada direktori proyek.
4. Melakukan add, commit, dan push kepada github dan PWS.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://drive.google.com/file/d/1j8FsfsbHzdqzthDkdS4eSv9-jqq99bC4/view?usp=sharing

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi yang berfungsi untuk melacak perubahan kode sumber dalam pengembangan perangkat lunak. Git membantu menjaga kualitas kode, meningkatkan efisiensi kolaborasi, dan mempermudah manajemen proyek.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering digunakan untuk pemula karena mudah untuk digunakan, arsitektur yang terstruktur, sakalbilitas dan fleksibilitas, keamanan yang kuat, dll.

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena mereka menyederhanakan interaksi antara aplikasi Python dan basis data relasional dengan cara yang terstruktur dan terstandarisasi. ORM Pada Django juga membantu mengurangi kebutuhan untuk menulis SQL secara langsung.
</details>

<details>
<summary>Jawaban Pertanyaan Tugas 3</summary>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian platform karena untuk memastikan data tersedia, dapat diakses tepat waktu, dan dapat dikirimkan dengan cara yang efisien. Data delivery juga diperlukan untuk meningkatkan skalabilitas. Dengan data delivery, platform dapat berfungsi dengan optimal.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik dan lebih populer dibandingkan XML karena JSON memiliki struktur yang lebih sederhana dan ringkas, ukuran data yang lebih kecil, serta lebih cepat untuk diparse oleh bahasa pemrograman, terutama JavaScript. 

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memvalidasi input dari user. Kita membutuhkan method tersebut untuk mencegah data yang tidak valid, memudahkan menangani error, dan menyederhanakan proses validasi.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token diperlukan dalam form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat mengeksploitasi sesi pengguna untuk mengirimkan permintaan berbahaya yang tampaknya sah. Tanpa csrf_token, data aplikasi rentan dimanipulasi oleh penyerang, karena tidak ada cara untuk memverifikasi bahwa permintaan berasal dari sumber yang sah. Token ini membantu memvalidasi permintaan dengan memastikan bahwa hanya permintaan yang menyertakan token yang valid yang diterima.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1. Membuat direktori baru pada root folder, menambahkan file base.html, mengonfigurasi file settings.py, dan mengubah file main.html.
2. Mengubah primary key dari integer menjadi uuid dengan cara mengimport uuid ke models.py.
3. Menambahkan file forms.py pada direktori main, import fungsi redirect pada file views.py, dan membuat fungsi baru pada views.py.
4. Mengimport fungsi baru dari views.py ke urls.py, menambahkan path untuk mengakses fungsi yang diimport, lalu membuat berkas baru dengan nama file fungsi yang diimport sebelumnya.
5. Mengimport fungsi HttpResponse dan serializers pada file views.py, lalu menambahkan fungsi baru untuk mengembalikan data dalam bentuk XML.
6. Melakukan import fungsi yang baru ditambahkan pada step 5 ke urls.py, lalu menambahkan path untuk mengakses fungsi tersebut.
7. Ulangi step 5 dan 6 untuk XML by id, JSON, dan JSON by id.

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

#### XML
![Screenshot 2024-09-17 222139](https://github.com/user-attachments/assets/c0cd0941-1a74-40fd-bef0-d0410b665e88)

#### XML by id
![Screenshot 2024-09-17 222216](https://github.com/user-attachments/assets/b1a79260-d0c0-47d6-9ba3-23603888a74d)

#### JSON
![Screenshot 2024-09-17 222235](https://github.com/user-attachments/assets/639d8f32-353c-42d8-bac8-6e533868248b)

#### JSON by id
![Screenshot 2024-09-17 222250](https://github.com/user-attachments/assets/73ea618e-1a78-4b3a-a52d-8125a6e26984)
</details>

<details>
<summary>Jawaban Pertanyaan Tugas 4</summary>
  
### Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect() dan redirect() di Django sama-sama digunakan untuk melakukan redirect ke URL yang berbeda, namun memiliki perbedaan dalam fleksibilitasnya. HttpResponseRedirect() hanya menerima URL dalam bentuk string dan mengembalikan respons HTTP 302. Sementara itu, redirect() lebih fleksibel, karena dapat menerima URL string, nama view yang akan di-resolve menjadi URL.

### Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model Product dengan User di Django, digunakan relasi ForeignKey pada model Product, yang mengaitkan setiap produk dengan user. Model Product akan memiliki field user yang merujuk ke model User melalui ForeignKey, dengan opsi on_delete=models.CASCADE agar produk yang dimiliki pengguna terhapus jika pengguna tersebut dihapus.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses memverifikasi identitas pengguna, sementara authorization adalah menentukan hak akses pengguna setelah terautentikasi. Saat login, Django melakukan authentication, dan jika berhasil, sistem menentukan authorization user.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login melalui cookies, dengan menyimpan sesi unik yang dikirim bersama setiap permintaan untuk mengenali pengguna. Cookies juga digunakan untuk menyimpan preferensi, melacak aktivitas, dan lain-lain.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1. Menyalankan virtual environtment, meng-import UserCreationForm dan messages. Menambahkan fungsi register pada views.py dan membuat file register.html pada direktori main/templates. Lalu melakukan routing pada urls.py
2. Kembali ke views.py lalu meng-import authenticate dan login. Lalu menambahkan fungsi login pada views.py dan membuat login.html untuk tampilan login. Lalu melakukan routing pada urls.py
3. Kembali ke views.py lalu meng-import logout. Lalu menambahkan fungsi logout pada views.py dan membuat logout.html untuk tampilan logout. Lalu melakukan routing pada urls.py
4. Kembali ke views.py lalu meng-import login_required untuk merestriksi akses halaman main.
5. Kembali lagi ke views.py dan meng-import HttpResponseRedirect, reverse, dan datetime. Mengupdate fungsi login_user untuk menambahkan last login, lalu mengupdate fungsi show_main untuk menambahkan informasi cookie last_login. Mengubah fungsi logout untuk menghapus cookies ketika logout. Lalu menambahkan tampilan kapan terakhir login pada main.html.
6. Membuka models.py dan meng-import User. Lalu menambahkan block code ```user = models.ForeignKey(User, on_delete=models.CASCADE)``` untuk mengaitkan Product dengan User.

</details>

<details>
<summary> Jawaban Pertanyaan Tugas 5</summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
1. 
  
</details>
