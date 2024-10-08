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
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, prioritas pengambilan ditentukan oleh spesifisitas. Urutan prioritasnya adalah inline styles, diikuti oleh ID selectors, class selectors, attribute selectors, dan pseudo-classes, kemudian element selectors dan pseudo-elements. Jika terdapat spesifisitas yang sama, aturan yang muncul terakhir di kode akan diterapkan.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting agar tampilan aplikasi web dapat menyesuaikan berbagai ukuran layar perangkat, sehingga pengguna mendapatkan pengalaman yang optimal. Contoh aplikasi yang sudah menerapkan responsive design adalah YouTube, sementara contoh yang belum adalah beberapa situs lama yang hanya didesain untuk desktop.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang di luar elemen, border adalah garis yang mengelilingi elemen, dan padding adalah ruang di dalam elemen, antara konten dan border. Ketiga hal ini dapat diimplementasikan di CSS dengan properti margin, border, dan padding serta nilainya, contoh: ```margin: 10px; border: 1px solid black; padding: 5px;```.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah sistem tata letak satu dimensi yang berguna untuk mengatur elemen secara fleksibel dalam satu baris atau kolom, sedangkan grid layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Flexbox digunakan untuk tata letak sederhana seperti navigasi, sementara grid lebih cocok untuk tata letak yang kompleks seperti dashboard.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
1. Menambahkan Tailwind ke dalam aplikasi Toko Uap.
2. Buka file views.py dan tambahkan ```edit_product```. Menambahkan file ```edit_product.html``` pada direktori main/templates. Lalu mengimport fungsi dan menambahkan path ke urls.py. Lalu menambahkan edit button ke main.html
3. Buka kembali file views.py dan tambahkan ```delete_product```. Lalu mengimport fungsi dan menambahkan path ke urls.py. Setelah itu menambahkan button di main.html
4. Buka direktori templates di root directory, lalu menambahkan ```navbar.html```. Kemudian menambahkan block code ```{% include 'navbar.html' %}``` ke file main.html, create_product_entry.html, dan edit_product.html.
5. Membuat direktori baru pada root directory yaitu direktori ```static/css```. Lalu tambahkan file ```global.css```. Setelah itu hubungkan ```global.css``` dan script Tailwind ke base.html. Lalu tambahkan custom styling ke ```global.css```.
6. Setelah itu, kita bisa memulai untuk styling page-page seperti login, register, home page, dll.
</details>
<details>
<summary>Jawaban Pertanyaan Tugas 6</summary>
  
### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript sangat bermanfaat dalam pengembangan aplikasi web karena memungkinkan pembuatan antarmuka pengguna yang dinamis dan interaktif secara langsung di browser. Dengan JavaScript, pengembang dapat memperbarui konten halaman tanpa perlu memuat ulang seluruh halaman, memberikan pengalaman yang lebih responsif bagi pengguna. Selain itu, JavaScript juga mendukung integrasi API, manipulasi DOM, dan validasi data di sisi klien, yang meningkatkan efisiensi dan keamanan.

### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi ```await``` saat menggunakan ```fetch()``` adalah untuk menghentikan eksekusi kode hingga permintaan jaringan selesai dan hasilnya dikembalikan, sehingga kita bisa menangani respons atau kesalahan secara sinkron. Tanpa ```await```, ```fetch()``` akan mengembalikan promise yang belum selesai, menyebabkan kode berikutnya berjalan sebelum hasil permintaan diterima. Ini dapat menyebabkan penggunaan data yang belum tersedia, misalnya ketika mencoba mengakses respons dari ```fetch()``` sebelum server merespons, yang dapat mengakibatkan bug.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Kita perlu menggunakan decorator ```csrf_exempt``` pada view yang digunakan untuk AJAX POST jika permintaan tersebut tidak menyertakan token CSRF (Cross-Site Request Forgery). Secara default, Django mengharuskan setiap permintaan POST dari klien yang terautentikasi untuk menyertakan token CSRF demi keamanan. Jika tidak, Django akan memblokir permintaan tersebut sebagai perlindungan terhadap serangan CSRF. Namun, dalam beberapa kasus seperti AJAX POST dari sumber tertentu, token CSRF mungkin tidak disertakan, sehingga decorator ini digunakan untuk menonaktifkan pemeriksaan CSRF pada view tertentu. Meski begitu, ini perlu digunakan dengan hati-hati agar tidak melemahkan keamanan aplikasi.

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna perlu dilakukan di backend karena validasi di frontend saja tidak cukup aman. Meskipun frontend bisa mencegah beberapa kesalahan input, penyerang dapat memanipulasi data sebelum dikirim ke server, melewati validasi frontend. Backend memastikan bahwa semua data yang masuk valid dan aman sebelum diproses atau disimpan di server, melindungi aplikasi dari serangan seperti injeksi SQL atau XSS. Validasi di backend juga menjaga konsistensi aturan untuk semua input, terlepas dari bagaimana data dikirim.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
1. Mengimport ```csrf_exempt``` dan ```require_POST``` pada views.py. Lalu menambahkan fungsi untuk menambahkan entry product menggunakan AJAX. Lalu melakukan routing untuk fungsi tersebut pada urls.py.
2. Pada views.py kita mengubah bagian data pada ```show_json``` dan ```show_xml```. Lalu pada main.html, kita menambahkan function untuk ```fetch``` data. Kita juga menambahkan function untuk me-refresh data.
3. Menambahkan modal pada main.html serta fungsi-fungsi yang diperlukan. Tambahkan juga button untuk membuat entry product menggunakan AJAX.
4. Menambahkan function pada main.html yaitu ```addProduct()```. Lalu tambahkan event listener untuk menjalankan function ```addProduct()```.
5. Pada views.py dan forms.py, import ```strip_tags```. Lalu gunakan fungsi ```strip_tags``` pada data ```nama```, ```review```, dan ```description```. Lalu tambahkan method pada forms.py untuk ketiga data tersebut.
</details>
