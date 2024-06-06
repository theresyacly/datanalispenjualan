import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV
df = pd.read_csv('theresyacpenjualan.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(df.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(df.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(df.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(df.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(df.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(df.dtypes)

# Visualisasi

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(df.index, df['Jumlah'], color='blue', alpha=0.5)
plt.title('Scatter Plot Penjualan')
plt.xlabel('Index')
plt.ylabel('Jumlah')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(df['Jumlah'].dropna(), bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Jumlah Penjualan')
plt.xlabel('Jumlah')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(df['Jumlah'].dropna())
plt.title('Box Plot of Jumlah Penjualan')
plt.ylabel('Jumlah')

# Membuat data untuk barplot jenis kelamin
gender_data = df['Jenis Kelamin'].value_counts()

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(gender_data.index, gender_data.values, color=['blue', 'pink'])
plt.title('Barplot Jenis Kelamin Penjualan')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
