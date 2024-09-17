# Toko Uap
Nama : Mirfak Naufal Pratama Putra

NPM: 2306244961

Kelas: PBP A

Link PWS: http://mirfak-naufal-tokouap.pbp.cs.ui.ac.id/

## Jawaban Pertanyaan Tugas 2

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

---

## Jawaban Pertanyaan Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian platform karena untuk memastikan data tersedia, dapat diakses tepat waktu, dan dapat dikirimkan dengan cara yang efisien. Data delivery juga diperlukan untuk meningkatkan skalabilitas. Dengan data delivery, platform dapat berfungsi dengan optimal.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik dan lebih populer dibandingkan XML karena JSON memiliki struktur yang lebih sederhana dan ringkas, ukuran data yang lebih kecil, serta lebih cepat untuk diparse oleh bahasa pemrograman, terutama JavaScript. 

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memvalidasi input dari user. Kita membutuhkan method tersebut untuk mencegah data yang tidak valid, memudahkan menangani error, dan menyederhanakan proses validasi.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token diperlukan dalam form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat mengeksploitasi sesi pengguna untuk mengirimkan permintaan berbahaya yang tampaknya sah. Tanpa csrf_token, data aplikasi rentan dimanipulasi oleh penyerang, karena tidak ada cara untuk memverifikasi bahwa permintaan berasal dari sumber yang sah. Token ini membantu memvalidasi permintaan dengan memastikan bahwa hanya permintaan yang menyertakan token yang valid yang diterima.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1. 

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

#### XML
![Screenshot 2024-09-17 222139](https://github.com/user-attachments/assets/c0cd0941-1a74-40fd-bef0-d0410b665e88)

#### XML by id
![Screenshot 2024-09-17 222216](https://github.com/user-attachments/assets/b1a79260-d0c0-47d6-9ba3-23603888a74d)

#### JSON
![Screenshot 2024-09-17 222235](https://github.com/user-attachments/assets/639d8f32-353c-42d8-bac8-6e533868248b)

#### JSON by id
![Screenshot 2024-09-17 222250](https://github.com/user-attachments/assets/73ea618e-1a78-4b3a-a52d-8125a6e26984)
