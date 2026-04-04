from os import read

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Monte Carlo Simulation, Markov Chain, and Hidden Markov Model")
st.header("Flowchart")
st.image("flowchart_uts.jpg")

st.header("Data")
data = pd.read_csv("Kasus Penyakit Menurut Provinsi dan Jenis Penyakit, 2024.csv")
st.write(data)
st.caption("Sumber: https://www.bps.go.id/id/statistics-table/3/YTA1Q1ptRmhUMEpXWTBsQmQyZzBjVzgwUzB4aVp6MDkjMyMwMDAw/kasus-penyakit-menurut-provinsi-dan-jenis-penyakit.html?year=2024 (Badan Pusat Statistik (BPS))")
st.markdown("Dataset yang digunakan berisi data kasus berbagai jenis penyakit di indonesia pada tahun 2024 berdasarkan provinsi. Data ini termasuk data epidemiologi yang dapat digunakan untuk melihat persebaran dan tignkat kejadian penyakit di tiap wilayah." \
"" \
"Dataset ini terdiri dari 46 baris dan 7 kolom variabel. setiap aris merepresentasikan satu provinsi, sedangkan kolom berisi indikator penyakit." \
"" \
"Variabel dalam dataset ini meliputi: Provinsi, angka penemuan TBC, angka keberhasilan pengobatan TBCm jumlah kasus HIV/AIDS, penemuan kasus kusta per 100.000 penduduk, angka kesakitan malaria per 1000 penduduk, dan angka kesakitan DBD per 100.000 penduduk."

"Secara umum, dataset ini merupakan data cross-sectional karena menggambarkan kondisi pada satu waktu, yaitu tahun 2024")

st.subheader("Data Exploration")

st.markdown("""```python
st.write("### Dataset")
st.dataframe(data)

st.write("### Informasi Dataset")
st.write(data.dtypes)

st.write("### Statistik Deskriptif")
st.write(data.describe())

st.write("### Missing Values")
st.write(data.isnull().sum())

st.write("### Distribusi Data")

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    fig, ax = plt.subplots()
    ax.hist(data[col].dropna())
    ax.set_title(f"Distribusi {col}")
    st.pyplot(fig)

st.write("### Deteksi Outliers")

for col in numeric_cols:
    fig, ax = plt.subplots()
    ax.boxplot(data[col].dropna())
    ax.set_title(f"Boxplot {col}")
    st.pyplot(fig)
```
""")

st.write("### Dataset")
st.dataframe(data)

st.write("### Informasi Dataset")
st.write(data.dtypes)

st.write("### Statistik Deskriptif")
st.write(data.describe())

st.write("### Missing Values")
st.write(data.isnull().sum())

st.write("### Distribusi Data")

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    fig, ax = plt.subplots()
    ax.hist(data[col].dropna())
    ax.set_title(f"Distribusi {col}")
    st.pyplot(fig)

st.write("### Deteksi Outliers")

for col in numeric_cols:
    fig, ax = plt.subplots()
    ax.boxplot(data[col].dropna())
    ax.set_title(f"Boxplot {col}")
    st.pyplot(fig)

st.subheader("Feature Engineering")
st.markdown("""
```python
# Pilih fitur numerik
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Normalisasi (Min-Max Scaling)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
            
st.write("### Hasil Normalisasi")
st.dataframe(data_scaled.head())""")

from sklearn.preprocessing import MinMaxScaler

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
scaler = MinMaxScaler()
data_scaled = data.copy()
data_scaled[numeric_cols] = scaler.fit_transform(data[numeric_cols])

st.write("### Hasil Normalisasi")
st.dataframe(data_scaled.head())

st.write("### Penjelasan")
st.write("""
Pada tahap feature engineering, fitur yang digunakan adalah seluruh variabel numerik seperti indikator TBC, HIV/AIDS, kusta, malaria, dan DBD. Selanjutnya dilakukan transformasi data menggunakan normalisasi Min-Max Scaling agar semua variabel berada pada skala yang sama, yaitu antara 0 hingga 1. Proses ini bertujuan untuk menghindari dominasi variabel dengan skala besar serta meningkatkan performa analisis pada tahap selanjutnya.
""")

st.subheader("Monte Carlo Simulation")

st.markdown("""
```python
import numpy as np

# mengambil satu variabel (DBD)
df = data["Jumlah Kasus Penyakit - Angka Kesakitan DBD per 100.000 Penduduk"].dropna()

# Parameter distribusi (mean & std)
mean = df.mean()
std = df.std()

# Simulasi Monte Carlo
simulasi = np.random.normal(mean, std, 1000)
st.write(simulasi[:10])
            
st.write("### Statistik Hasil Simulasi")
st.write({
    "Mean": np.mean(simulasi),
    "Std Dev": np.std(simulasi),
    "Min": np.min(simulasi),
    "Max": np.max(simulasi)
})
st.write("### Visualisasi Hasil Simulasi")

fig, ax = plt.subplots()
ax.hist(simulasi)
ax.set_title("Distribusi Simulasi Monte Carlo (DBD)")
st.pyplot(fig)""")

# mengambil satu variabel (DBD)
df = data["Jumlah Kasus Penyakit - Angka Kesakitan DBD per 100.000 Penduduk"].dropna()

# Parameter distribusi (mean & std)
mean = df.mean()
std = df.std()

# Simulasi Monte Carlo
simulasi = np.random.normal(mean, std, 1000)
st.write(simulasi[:10])

st.write("### Statistik Hasil Simulasi")
st.write({
    "Mean": np.mean(simulasi),
    "Std Dev": np.std(simulasi),
    "Min": np.min(simulasi),
    "Max": np.max(simulasi)
})

st.write("### Visualisasi Hasil Simulasi")

fig, ax = plt.subplots()
ax.hist(simulasi)
ax.set_title("Distribusi Simulasi Monte Carlo (DBD)")
st.pyplot(fig)

st.write("### Penjelasan")
st.write("""
Hasil simulasi Monte Carlo pada data angka kesakitan Demam Berdarah Dengue (DBD) per 100.000 penduduk diasumsikan mengikuti distribusi normal (Gaussian) yang bersifat simetris dengan pusat pada nilai rata-rata. Parameter yang digunakan adalah mean (μ) sebesar 98,50 dan standar deviasi (σ) sebesar 66,48, yang menunjukkan bahwa rata-rata kasus berada di sekitar 98 dengan variasi data yang cukup tinggi. Rentang nilai dari -114,31 hingga 340,86 mengindikasikan adanya penyebaran yang luas, meskipun nilai negatif muncul sebagai konsekuensi matematis dari distribusi normal dan tidak relevan secara nyata.
""")

st.subheader("Markov Chain")

# Tampilkan code
st.markdown("""
```python
import numpy as np
import pandas as pd
def kategori(x):
    if x < 627:
        return "Rendah"
    elif x < 1255:
        return "Sedang"
    else:
        return "Tinggi"
data["State"] = data["Jumlah Kasus Penyakit - HIV/AIDS Kasus Baru"].apply(kategori)
states = data["State"].values
unique_states = ["Rendah", "Sedang", "Tinggi"]
matrix = pd.DataFrame(0, index=unique_states, columns=unique_states)
for i in range(len(states)-1):
    matrix.loc[states[i], states[i+1]] += 1
matrix = matrix.div(matrix.sum(axis=1).replace(0, 1), axis=0)
st.write("### Matriks Transisi Markov Chain")
st.dataframe(matrix)

st.write("### Visualisasi Matriks Transisi")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
cax = ax.matshow(matrix)
plt.title("Transition Matrix")
plt.colorbar(cax)

ax.set_xticks(range(len(unique_states)))
ax.set_yticks(range(len(unique_states)))
ax.set_xticklabels(unique_states)
ax.set_yticklabels(unique_states)

st.pyplot(fig)""")

import numpy as np
import pandas as pd

def kategori(x):
    if x < 65:
        return "Rendah"
    elif x < 98:
        return "Sedang"
    else:
        return "Tinggi"
data["State"] = data["Jumlah Kasus Penyakit - Angka Kesakitan DBD per 100.000 Penduduk"].apply(kategori)
states = data["State"].values
unique_states = ["Rendah", "Sedang", "Tinggi"]
matrix = pd.DataFrame(0, index=unique_states, columns=unique_states)
for i in range(len(states)-1):
    matrix.loc[states[i], states[i+1]] += 1
matrix = matrix.div(matrix.sum(axis=1).replace(0, 1), axis=0)
st.write("### Matriks Transisi Markov Chain")
st.dataframe(matrix)

st.write("### Visualisasi Matriks Transisi")

fig, ax = plt.subplots()
cax = ax.matshow(matrix)
plt.title("Transition Matrix")
plt.colorbar(cax)

ax.set_xticks(range(len(unique_states)))
ax.set_yticks(range(len(unique_states)))
ax.set_xticklabels(unique_states)
ax.set_yticklabels(unique_states)

st.pyplot(fig)

st.write("### Penjelasan")
st.write("""
Model Markov Chain ini menunjukkan dinamika tingkat kasus DBD yang cukup realistis:

- Rendah cenderung stabil (0,4545), tapi masih bisa naik ke sedang/tinggi.
- Sedang paling fluktuatif, dengan kecenderungan terbesar naik ke tinggi (0,4167).
- Tinggi juga cukup stabil (0,4286), namun lebih sering turun ke sedang daripada langsung ke rendah.

Kesimpulannya, kenaikan kasus bisa terjadi cepat (terutama dari sedang ke tinggi), sedangkan penurunan cenderung bertahap (tinggi -> sedang -> rendah).
""")

st.subheader("Hidden Markov Model (HMM)")
st.markdown("""
```python
from hmmlearn import hmm
import numpy as np

# Gunakan satu variabel (DBD)
data = data["Jumlah Kasus Penyakit - Angka Kesakitan DBD per 100.000 Penduduk"].dropna().values
# Ubah ke format 2D
data = data.reshape(-1, 1)
# Bangun model HMM dengan 3 hidden states
model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
# Training model
model.fit(data)
# Prediksi hidden states (Viterbi)
hidden_states = model.predict(data)
st.write("### Hidden States yang Diprediksi")
st.write(hidden_states)""")

from hmmlearn import hmm
import numpy as np

data = data["Jumlah Kasus Penyakit - Angka Kesakitan DBD per 100.000 Penduduk"].dropna().values
data = data.reshape(-1, 1)
model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
model.fit(data)
hidden_states = model.predict(data)
st.write("### Hidden States yang Diprediksi")
st.write(hidden_states)

st.write("### Penjelasan")
st.write("""
Model membagi data menjadi 3 state tersembunyi, yang umumnya bisa ditafsirkan sebagai:
- State 0: tingkat kasus rendah
- State 1: tingkat kasus sedang
- State 2: tingkat kasus tinggi
Deret hidden_states menunjukkan urutan kondisi tiap provinsi/waktu, misalnya:
- Jika banyak nilai sama berurutan: kondisi relatif stabil
- Jika sering berubah: menunjukkan fluktuasi kasus DBD
Secara umum:
- State dengan nilai observasi kecil: risiko rendah
- State dengan nilai besar: risiko tinggi
- Perpindahan antar state: menggambarkan dinamika peningkatan/penurunan kasus
""")

st.subheader("Evaluation and Discussion")
st.write("""
### Perbandingan Model
Metode Monte Carlo mampu menggambarkan distribusi dan variasi data secara umum, tetapi tidak menangkap pola transisi atau ketergantungan antar waktu. Markov Chain lebih baik dalam menunjukkan probabilitas perpindahan antar kategori (rendah, sedang, tinggi), sehingga mampu merepresentasikan dinamika perubahan kondisi. Sementara itu, Hidden Markov Model (HMM) memberikan hasil yang lebih kompleks dengan mengidentifikasi state tersembunyi, sehingga mampu menangkap pola laten dan dinamika yang tidak terlihat langsung dari data.

### Diskusi
Kelebihan:
Metode Monte Carlo mampu menggambarkan distribusi dan ketidakpastian data secara sederhana. Markov Chain efektif dalam memodelkan perpindahan antar kategori sehingga dapat menunjukkan dinamika perubahan kondisi. HMM unggul dalam mengidentifikasi state tersembunyi dan menangkap pola laten yang tidak terlihat langsung dari data.

Keterbatasan:
Monte Carlo bergantung pada asumsi distribusi normal yang dapat menghasilkan nilai tidak realistis (misalnya negatif). Markov Chain memerlukan pengkategorian data awal yang bersifat subjektif dan dalam analisis ini menggunakan variabel berbeda. HMM cenderung lebih kompleks, sensitif terhadap parameter, dan interpretasi state-nya tidak selalu langsung jelas.

Interpretasi:
Hasil analisis menunjukkan bahwa data penyakit memiliki variasi tinggi dan dinamika yang fluktuatif. Monte Carlo menekankan pada penyebaran data, Markov Chain pada pola transisi antar kondisi, dan HMM pada struktur tersembunyi. Ketiganya saling melengkapi dalam memberikan gambaran menyeluruh, meskipun perbandingan tidak sepenuhnya langsung karena perbedaan variabel yang digunakan.

### Kesimpulan
Berdasarkan hasil analisis, data angka kesakitan DBD per 100.000 penduduk menunjukkan variasi yang tinggi serta dinamika yang kompleks. Metode Monte Carlo memberikan gambaran distribusi data dan tingkat penyebarannya, Markov Chain menunjukkan pola perpindahan antar kategori kasus, sedangkan Hidden Markov Model (HMM) mengungkap pola tersembunyi yang tidak terlihat secara langsung.

Secara keseluruhan, kombinasi metode ini memberikan pemahaman yang lebih komprehensif terhadap distribusi, dinamika perubahan, dan struktur laten kasus DBD.""")