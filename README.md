# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut, berdiri sejak tahun 2000, telah mencetak lulusan berkualitas dengan reputasi yang baik. Namun, tingginya angka siswa dropout menjadi tantangan serius yang berdampak pada reputasi dan efektivitas program akademik.Dropout disebabkan oleh berbagai faktor, seperti latar belakang akademik, kondisi sosial ekonomi, dan motivasi belajar. Untuk mengatasi masalah ini, analisis data diperlukan guna memahami pola dan faktor risiko dropout.

### Permasalahan Bisnis
1. Bagaimana distribusi status siswa (dropout, aktif, lulus) secara keseluruhan?
2. Apakah siswa dengan beasiswa (Scholarship_holder) memiliki tingkat dropout yang lebih rendah?
3. Apakah tingkat pengangguran (Unemployment_rate), inflasi (Inflation_rate), atau PDB (GDP) memiliki pola tertentu terhadap status dropout?

### Cakupan Proyek
Proyek ini bertujuan untuk mengembangkan dashboard interaktif yang memberikan wawasan mendalam terkait status siswa di Jaya Jaya Institut. Cakupan proyek meliputi:

1. Pengumpulan dan Pembersihan Data: Memastikan data yang digunakan akurat, lengkap, dan siap dianalisis.
2. Analisis Data Eksploratif: Mengidentifikasi pola, tren, dan hubungan antar variabel yang berkaitan dengan status siswa.
3. Pembuatan Dashboard Interaktif: Merancang visualisasi data yang mudah dipahami, seperti grafik distribusi, tren dropout, dan analisis faktor risiko.
4. Pemantauan dan Evaluasi: Mengukur efektivitas dashboard dalam mendukung pengambilan keputusan dan strategi pencegahan dropout.
5. Membuat Prototype : Mengembangkan solusi machine learning yang dapat digunakan untuk membantu intitusi mendeteksi status siswa.
6. Rekomendasi Strategis: Memberikan rekomendasi berbasis data untuk membantu institusi dalam mengurangi angka dropout dan meningkatkan retensi siswa.

### Persiapan

Sumber data: [https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success]

Setup environment:
```
pip install -r requirements.txt
```

## Business Dashboard
- 4,424 Total Student: Jumlah total siswa yang terdaftar di institusi.
- 10.64 Average of Curricular Units 1st Sem Grade: Rata-rata nilai mata kuliah di semester pertama.
- 10.23 Average of Curricular Units 2nd Sem Grade: Rata-rata nilai mata kuliah di semester kedua.
- Status :
  Menunjukkan proporsi siswa berdasarkan status:
  1. Graduate (49.9%) - Lulus (warna kuning)
  2. Dropout (32.1%) - Putus studi (warna merah muda)
  3. Enrolled (17.9%) - Masih aktif (warna hijau)
- Course:
  Distribusi siswa berdasarkan kategori kursus atau beban akademik:
  1. 8,750 - 10,000 (90.01%) - Mayoritas siswa berada di rentang ini (warna ungu).
  2. 0 - 1,250 (5.13%) dan 7,500 - 8,750 (4.86%) menunjukkan kelompok siswa dengan beban kursus yang lebih rendah (warna biru muda & cyan).
- Inflation_rate
  Pada tingkat inflasi 1.4%, terdapat angka dropout tertinggi (284 siswa), yang bisa menunjukkan adanya pengaruh tekanan ekonomi terhadap risiko putus studi.
  Sebaliknya, pada tingkat inflasi negatif seperti -0.8%, jumlah lulusan relatif tinggi (250 siswa), mungkin karena kondisi ekonomi lebih stabil.
- GDP
  Terdapat korelasi antara GDP negatif dengan tingginya angka dropout, mengindikasikan bahwa krisis ekonomi mungkin berdampak pada keberlanjutan studi siswa.
- Scholarship_holder
  Siswa penerima beasiswa cenderung memiliki proporsi kelulusan yang lebih tinggi dibandingkan siswa tanpa beasiswa.
  Sebaliknya, dropout lebih banyak terjadi pada siswa yang tidak memiliki beasiswa, menunjukkan beasiswa bisa menjadi faktor protektif terhadap risiko putus studi.

Link Dashboard = [http://localhost:3000/public/dashboard/1b461ec9-a7d5-4e9e-a3f0-48c57c222f63]

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
- Distribusi status siswa pada institut ini kurang baik dimana total kelulusan kurang dari 50%
- Beasiswa berperan sebagai proteksi ganda—tidak hanya mengurangi beban finansial, tetapi juga meningkatkan rasa percaya diri dan motivasi siswa.
- Resiliensi individu dan dukungan lingkungan sosial seperti keluarga dan komunitas institut memainkan peran penting dalam membantu siswa bertahan hingga lulus, bahkan di tengah tantangan ekonomi yang sulit.
- Dropout tidak hanya disebabkan oleh faktor ekonomi, tetapi juga tekanan akademik, distribusi kursus yang tidak merata, dan faktor pribadi seperti motivasi belajar.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang dapat dilakukan institut untuk mengurangi angka dropout :
- Perlu adanya intervensi strategis seperti peningkatan program beasiswa, bimbingan akademik, dan pemantauan kondisi ekonomi untuk mengurangi angka dropout.
- Membuat sesi konsultasi rutin dengan seluruh orang tua siswa terutama siswa dengan resiko dropout.
- 
