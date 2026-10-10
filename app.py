import os

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Analisis Preferensi Konsumen Skincare", layout="wide")

st.title("Analisis Preferensi Konsumen Produk Skincare")
st.caption("UTS ANALISIS MULTIVARIAT - Correspondence Analysis | Asthagina Delia Putri | 20244920001")

def tampil_gambar(path, caption):
    if os.path.exists(path):
        st.image(path, caption=caption)
    else:
        st.warning(f"File gambar '{path}' belum ada. Upload hasil ekspor grafik dari R ke folder img/.")


# =====================================================================
# 1. DATA AWAL
# =====================================================================
st.header("1. Gambaran Data")

st.markdown("""
Data yang digunakan merupakan data survei terhadap 300 responden untuk mengetahui hubungan antara preferensi tipe produk skincare dengan karakteristik konsumen. Tipe produk yang dianalisis meliputi moisturizer, sunscreen, serum, dan cleanser, sedangkan karakteristik konsumen dikelompokkan berdasarkan usia dan jenis kelamin. Analisis dilakukan menggunakan metode Correspondence Analysis (CA) untuk mengidentifikasi pola hubungan antara kategori produk dan karakteristik konsumen, sehingga dapat diketahui tipe produk yang cenderung berkaitan dengan kelompok konsumen tertentu.""")

st.subheader("Tabel 1: Tipe Produk vs Kelompok Usia")
data_usia = pd.DataFrame(
    [[40, 30, 20], [25, 35, 30], [30, 15, 10], [20, 25, 25]],
    index=["Moisturizer", "Sunscreen", "Serum", "Cleanser"],
    columns=["Muda (18-25)", "Dewasa (26-40)", "Tua (>40)"],
)
st.dataframe(data_usia)

st.subheader("Tabel 2: Tipe Produk vs Jenis Kelamin")
data_gender = pd.DataFrame(
    [[45, 45], [50, 40], [25, 30], [30, 40]],
    index=["Moisturizer", "Sunscreen", "Serum", "Cleanser"],
    columns=["Pria", "Wanita"],
)
st.dataframe(data_gender)

# =====================================================================
# 2. CODE R DAN OUTPUT R: PRODUK vs USIA
# =====================================================================
st.header("2. Correspondence Analysis: Tipe Produk vs Kelompok Usia")

kode_usia = r'''platform <- matrix(
  c(
    40, 30, 20,
    25, 35, 30,
    30, 15, 10,
    20, 25, 25
  ),
  nrow = 4,
  byrow = TRUE
)

rownames(platform) <- c(
  "Moisturizer", "Sunscreen",
  "Serum", "Cleanser"
)

colnames(platform) <- c(
  "Muda (18-25)", "Dewasa (26-40)", "Tua (>40)"
)

platform
rowSums(platform)
colSums(platform)
sum(platform)

prop.table(platform, margin = 1)
prop.table(platform, margin = 2)

chi_result <- chisq.test(platform)
chi_result
chi_result$expected

library(ca)
ca_result <- ca(platform)
ca_result
summary(ca_result)

plot(ca_result)
title("Correspondence Analysis - Preferensi Konsumen")
'''

output_usia = r'''##             Muda (18-25) Dewasa (26-40) Tua (>40)
## Moisturizer           40             30        20
## Sunscreen             25             35        30
## Serum                 30             15        10
## Cleanser              20             25        25

> rowSums(platform)
## Moisturizer   Sunscreen       Serum    Cleanser 
##          90          90          55          70

> colSums(platform)
##   Muda (18-25) Dewasa (26-40)      Tua (>40) 
##            115            105             85

> sum(platform)
## [1] 305

> prop.table(platform, margin = 1)
##             Muda (18-25) Dewasa (26-40) Tua (>40)
## Moisturizer    0.4444444      0.3333333 0.2222222
## Sunscreen      0.2777778      0.3888889 0.3333333
## Serum          0.5454545      0.2727273 0.1818182
## Cleanser       0.2857143      0.3571429 0.3571429

> prop.table(platform, margin = 2)
##             Muda (18-25) Dewasa (26-40) Tua (>40)
## Moisturizer    0.3478261      0.2857143 0.2352941
## Sunscreen      0.2173913      0.3333333 0.3529412
## Serum          0.2608696      0.1428571 0.1176471
## Cleanser       0.1739130      0.2380952 0.2941176

> chi_result
## 
##  Pearson's Chi-squared test
## 
## data:  platform
## X-squared = 15.917, df = 6, p-value = 0.01421

> chi_result$expected
##             Muda (18-25) Dewasa (26-40) Tua (>40)
## Moisturizer     33.93443       30.98361  25.08197
## Sunscreen       33.93443       30.98361  25.08197
## Serum           20.73770       18.93443  15.32787
## Cleanser        26.39344       24.09836  19.50820

> ca_result
## 
##  Principal inertias (eigenvalues):
##            1        2      
## Value      0.051038 0.00115
## Percentage 97.8%    2.2%   
## 
## 
##  Rows:
##         Moisturizer Sunscreen     Serum Cleanser
## Mass       0.295082  0.295082  0.180328 0.229508
## ChiDist    0.154384  0.206486  0.351785 0.211406
## Inertia    0.007033  0.012581  0.022316 0.010257
## Dim. 1    -0.669688  0.907177 -1.550532 0.912932
## Dim. 2    -0.906464 -0.742427  0.955767 1.369042
## 
## 
##  Columns:
##         Muda (18-25) Dewasa (26-40) Tua (>40)
## Mass        0.377049       0.344262  0.278689
## ChiDist     0.281643       0.115600  0.251862
## Inertia     0.029909       0.004600  0.017679
## Dim. 1     -1.245771       0.473245  1.100858
## Dim. 2      0.316590      -1.296457  1.173178

> summary(ca_result)
## 
## Principal inertias (eigenvalues):
## 
##  dim    value      %   cum%   scree plot               
##  1      0.051038  97.8  97.8  ************************ 
##  2      0.001150   2.2 100.0  *                        
##         -------- -----                                 
##  Total: 0.052188 100.0                                 
## 
## 
## Rows:
##     name   mass  qlt  inr    k=1 cor ctr    k=2 cor ctr  
## 1 | Mstr |  295 1000  135 | -151 960 132 |  -31  40 242 |
## 2 | Snsc |  295 1000  241 |  205 985 243 |  -25  15 163 |
## 3 | Serm |  180 1000  428 | -350 992 434 |   32   8 165 |
## 4 | Clns |  230 1000  197 |  206 952 191 |   46  48 430 |
## 
## Columns:
##     name   mass  qlt  inr    k=1 cor ctr    k=2 cor ctr  
## 1 | M182 |  377 1000  573 | -281 999 585 |   11   1  38 |
## 2 | D264 |  344 1000   88 |  107 855  77 |  -44 145 579 |
## 3 | Tu40 |  279 1000  339 |  249 975 338 |   40  25 384 |
'''

st.subheader("Code R")
st.code(kode_usia, language="r")

st.subheader("Output R")
st.code(output_usia, language="text")

st.subheader("Grafik")
tampil_gambar("tabel 1.png", caption="Correspondence Analysis - Preferensi Konsumen")

st.subheader("Hubungan antara tipe produk dan kelompok usia")
st.markdown("""
**Uji independensi.** χ² = 15,917; df = 6; p-value = 0,01421 (< 0,05), sehingga H₀ ditolak.
Terdapat hubungan yang **signifikan** antara tipe produk dan kelompok usia.

**Hasil CA.** Total inersia 0,0522. Dimensi 1 menjelaskan 97,8% inersia, sedangkan Dimensi 2 hanya 2,2%,
sehingga interpretasi cukup memakai Dimensi 1 yang berfungsi sebagai **sumbu usia**
(kiri = usia muda, kanan = usia lebih tua). Kualitas representasi (qlt) semua titik = 1000.
Kontributor terbesar Dimensi 1 adalah kelompok Muda (58,5%) dan Serum (43,4%).

| Titik | Koordinat Dim 1 | Posisi |
|---|---|---|
| Serum | -0,350 | Paling kiri |
| Muda (18-25) | -0,281 | Kiri |
| Moisturizer | -0,151 | Kiri-tengah |
| Dewasa (26-40) | +0,107 | Dekat pusat |
| Sunscreen | +0,205 | Kanan |
| Cleanser | +0,206 | Kanan |
| Tua (>40) | +0,249 | Paling kanan |

**Pola hubungan:**
- Serum dan Moisturizer berasosiasi dengan kelompok **Muda** (Serum: 54,5% pembelinya kelompok Muda; frekuensi
  observasi 30 vs harapan 20,7).
- Sunscreen dan Cleanser berasosiasi dengan kelompok **Tua dan Dewasa** (Sunscreen-Tua 30 vs harapan 25,1;
  Cleanser-Tua 25 vs harapan 19,5).
- Kelompok **Dewasa** dekat dengan pusat, artinya preferensinya mendekati rata-rata populasi.
- Sunscreen kurang diminati kelompok Muda, dan Serum kurang diminati kelompok Tua.
""")

# =====================================================================
# 3. CODE R DAN OUTPUT R: PRODUK vs GENDER
# =====================================================================
st.header("3. Correspondence Analysis: Tipe Produk vs Jenis Kelamin")

kode_gender = r'''# Matriks asli (Produk di baris, Gender di kolom)
tabel2 <- matrix(c(45, 45,
                   50, 40,
                   25, 30,
                   30, 40),
                 nrow = 4, byrow = TRUE,
                 dimnames = list(Produk = c("Moisturizer", "Sunscreen", "Serum", "Cleanser"),
                                 Gender = c("Pria", "Wanita")))

tabel2      # 4 baris x 2 kolom
dim(tabel2)

chi2 <- chisq.test(tabel2)
chi2
chi2$expected

# ---------- CA manual dengan SVD ----------
N  <- tabel2
P  <- N / sum(N)
r  <- rowSums(P)                      # massa baris
cc <- colSums(P)                      # massa kolom

S   <- diag(1/sqrt(r)) %*% (P - r %o% cc) %*% diag(1/sqrt(cc))
sv  <- svd(S)

k   <- 1                              # hanya 1 dimensi yang bermakna
eig <- sv$d[k]^2
tot_inersia <- sum(sv$d^2)

# Koordinat utama (principal coordinates)
row_coord <- (1/sqrt(r))  * sv$u[, k] * sv$d[k]
col_coord <- (1/sqrt(cc)) * sv$v[, k] * sv$d[k]
names(row_coord) <- rownames(N)
names(col_coord) <- colnames(N)

# Inersia, kontribusi, dan kualitas
row_inertia <- r  * rowSums(sweep(sweep(P / r,  2, cc, "-")^2, 2, cc, "/"))
col_inertia <- cc * rowSums(sweep(sweep(t(P) / cc, 2, r, "-")^2, 2, r, "/"))

# ---------- (d) Ringkasan ----------
ringkasan <- data.frame(
  Dimensi        = 1,
  Singular_Value = round(sv$d[k], 4),
  Eigenvalue     = round(eig, 5),
  Persen_Inersia = round(eig / tot_inersia * 100, 2)
)
ringkasan
cat("Total inersia:", round(tot_inersia, 5), "\n")
cat("Chi-square / n:", round(unname(chi2$statistic) / sum(N), 5),
    "(harus sama dengan total inersia)\n\n")

hasil_baris <- data.frame(
  Massa     = round(r, 4),
  Inersia   = round(row_inertia, 5),
  Koord_Dim1 = round(row_coord, 4),
  Kontribusi = round(r * row_coord^2 / eig * 100, 2),
  Cos2       = round(row_coord^2 * r / row_inertia, 4)
)
hasil_kolom <- data.frame(
  Massa     = round(cc, 4),
  Inersia   = round(col_inertia, 5),
  Koord_Dim1 = round(col_coord, 4),
  Kontribusi = round(cc * col_coord^2 / eig * 100, 2),
  Cos2       = round(col_coord^2 * cc / col_inertia, 4)
)
cat("--- Baris (Produk) ---\n"); hasil_baris
cat("\n--- Kolom (Gender) ---\n"); hasil_kolom

# ---------- (e) Plot 1 dimensi ----------
library(ggplot2)
library(ggrepel)

df_plot <- rbind(
  data.frame(label = names(row_coord), x = unname(row_coord), y =  0.05, tipe = "Produk"),
  data.frame(label = names(col_coord), x = unname(col_coord), y = -0.05, tipe = "Gender")
)

ggplot(df_plot, aes(x, y, color = tipe, shape = tipe)) +
  geom_hline(yintercept = 0) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey50") +
  geom_point(size = 4) +
  geom_text_repel(aes(label = label), size = 4, show.legend = FALSE) +
  scale_y_continuous(limits = c(-0.3, 0.3)) +
  labs(title = "Correspondence Analysis: Tipe Produk vs Jenis Kelamin",
       x = "Dimensi 1 (100% inersia)", y = NULL, color = NULL, shape = NULL) +
  theme_minimal() +
  theme(axis.text.y = element_blank(), panel.grid.major.y = element_blank())
'''

output_gender = r'''> tabel2
##              Gender
## Produk        Pria Wanita
##   Moisturizer   45     45
##   Sunscreen     50     40
##   Serum         25     30
##   Cleanser      30     40

> dim(tabel2)
## [1] 4 2

> chi2
## 
##  Pearson's Chi-squared test
## 
## data:  tabel2
## X-squared = 2.913, df = 3, p-value = 0.4052

> chi2$expected
##              Gender
## Produk            Pria   Wanita
##   Moisturizer 44.26230 45.73770
##   Sunscreen   44.26230 45.73770
##   Serum       27.04918 27.95082
##   Cleanser    34.42623 35.57377

> ringkasan
##   Dimensi Singular_Value Eigenvalue Persen_Inersia
## 1       1         0.0977    0.00955            100

> cat("Total inersia:", ...)
## Total inersia: 0.00955
## Chi-square / n: 0.00955 (harus sama dengan total inersia)

> hasil_baris
## --- Baris (Produk) ---
##              Massa Inersia Koord_Dim1 Kontribusi Cos2
## Moisturizer 0.2951 0.00008    -0.0164       0.83    1
## Sunscreen   0.2951 0.00480    -0.1275      50.24    1
## Serum       0.1803 0.00100     0.0745      10.49    1
## Cleanser    0.2295 0.00367     0.1265      38.44    1

> hasil_kolom
## --- Kolom (Gender) ---
##         Massa Inersia Koord_Dim1 Kontribusi Cos2
## Pria   0.4918 0.00485    -0.0993      50.82    1
## Wanita 0.5082 0.00470     0.0961      49.18    1
'''

st.subheader("Code R")
st.code(kode_gender, language="r")

st.subheader("Output R")
st.code(output_gender, language="text")

st.subheader("Grafik")
tampil_gambar("tabel 2.png", caption="Correspondence Analysis: Tipe Produk vs Jenis Kelamin")

st.subheader("Hubungan antara tipe produk dan jenis kelamin")
st.markdown("""
**Uji independensi.** χ² = 2,913; df = 3; p-value = 0,4052 (> 0,05), sehingga H₀ gagal ditolak.
**Tidak ada hubungan yang signifikan** antara tipe produk dan jenis kelamin. Total inersia sangat kecil (0,00955)
dan frekuensi observasi sangat dekat dengan frekuensi harapan.

**Hasil CA.** Hanya ada satu dimensi (min(4,2) - 1 = 1) yang menjelaskan 100% inersia.

| Titik | Koordinat | Kontribusi |
|---|---|---|
| Sunscreen | -0,1275 | 50,24% |
| Moisturizer | -0,0164 | 0,83% |
| Pria | -0,0993 | 50,82% |
| Serum | +0,0745 | 10,49% |
| Cleanser | +0,1265 | 38,44% |
| Wanita | +0,0961 | 49,18% |

Secara deskriptif, Sunscreen sedikit condong ke Pria, Cleanser dan Serum sedikit condong ke Wanita, sedangkan
Moisturizer netral (50:50). Namun perbedaan ini kecil dan tidak signifikan, sehingga jenis kelamin bukan faktor
pembeda preferensi produk yang berarti.
""")

# =====================================================================
# 4. JAWABAN PERTANYAAN
# =====================================================================

st.subheader("Pola preferensi produk berdasarkan kelompok usia")
st.markdown("""
- **Muda (18-25):** condong ke Serum dan Moisturizer; kurang tertarik pada Sunscreen.
- **Dewasa (26-40):** relatif seimbang, dengan kecenderungan ringan ke Sunscreen dan Cleanser.
- **Tua (>40):** condong ke Sunscreen dan Cleanser; kurang tertarik pada Serum.
- Semakin tua usia, preferensi bergeser dari produk perawatan (Serum, Moisturizer) ke produk perlindungan
  dan pembersih (Sunscreen, Cleanser).
""")

st.subheader("Pola preferensi produk berdasarkan jenis kelamin")
st.markdown("""
- Pria cenderung sedikit lebih banyak memilih **Sunscreen** (55,6% pembelinya Pria).
- Wanita cenderung sedikit lebih banyak memilih **Cleanser** (57,1% Wanita) dan **Serum** (54,5% Wanita).
- **Moisturizer** diminati merata (50:50).
- Karena uji chi-square tidak signifikan (p = 0,405), pola ini lemah dan tidak dapat dijadikan dasar pembeda
  yang kuat.
""")

st.subheader("Rekomendasi strategi pemasaran untuk perusahaan skincare")
st.markdown("""
1. **Segmentasi utama berdasarkan usia, bukan gender**, karena usia terbukti signifikan sedangkan gender tidak.
2. **Kelompok Muda:** fokus pada Serum dan Moisturizer melalui media sosial, influencer, konten edukasi, serta
   paket bundling dengan harga terjangkau. Perkuat edukasi Sunscreen, misalnya lewat moisturizer ber-SPF.
3. **Kelompok Dewasa:** tawarkan portofolio lengkap dan seimbang dengan pesan perawatan menyeluruh
   (starter kit rutinitas lengkap).
4. **Kelompok Tua (>40):** unggulkan Sunscreen dan Cleanser dengan klaim perlindungan dan kelembutan; kembangkan
   serum anti-aging dengan edukasi manfaat yang jelas untuk meningkatkan penetrasi Serum.
5. **Kampanye gender-netral** dengan kemasan dan komunikasi inklusif. Pendekatan khusus gender hanya sebagai
   pelengkap.
6. **Moisturizer sebagai produk andalan lintas segmen** karena netral terhadap gender dan relatif diminati semua
   usia, cocok sebagai produk entry-level.
""")

st.caption(
    "Catatan: CA bersifat eksploratif dan deskriptif. Tanda koordinat bersifat arbitrer; yang bermakna adalah "
    "posisi relatif antar titik."
)
