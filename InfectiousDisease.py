# Impporting libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("PenyakitMenularDKI.csv")
print(data)
print(data.info())

data['tahun']=data['tahun'].astype('category')
data['wilayah']=data['wilayah'].astype('category')
data['nama_penyakit']=data['nama_penyakit'].astype('category')
print(data.info())

# Pada tahun berapa penyakit menular tertinggi?
# Plot ini dibuat menggunakan pandas plot dan digrup berdasaran tahun untuk mendapatkan total kasus tiap tahun.
pertahun = data.groupby('tahun').jumlah_penderita.sum()
print(pertahun)
pertahun.plot(kind='line',xlabel='Tahun',ylabel='Jumlah',title='Jumlah Penderita Penyakit Menular di DKI Jakarta \n  2015-2020')

# Penyakit menular apa yang terbanyak dari tahun 2015-2020
# Plot ini menggunakann pandas
penyakit = data.groupby('nama_penyakit').jumlah_penderita.sum().sort_values()
print(penyakit)
penyakit.plot(kind='barh',xlabel='Nama Penyakit',title='Jumlah Penderita Penyakit Menular di DKI Jakarta \n Menurut Jenis Penyakit')

# Menghitung Jumlah Penderita Penyakit Menular berdasarkan wilayahnnya.
wilayah = data.groupby('wilayah').jumlah_penderita.sum().sort_values()
print(wilayah)
wilayah.plot(kind='barh',xlabel='Kabupaten/Kota Administrasi', title='Jumlah Penderita Penyakit Menular di DKI Jakarta \n Menurut Kabupaten/Kota Administrasi')

# Membuat plot Penderita penyakit pertahun
sns.set_style('darkgrid')
g1 = sns.catplot(x='nama_penyakit',y='jumlah_penderita',col='tahun',data=data,kind='bar',ci=None,col_wrap=3,height=5,sharey=False,sharex=False)
g1.fig.subplots_adjust(top=0.9) 
g1.fig.suptitle('Jumlah Penderita Penyakit per tahun',fontsize=19)
plt.show()
plt.clf()
# Dapat dilihat bahwa tiap tahun, yang mendominasi penyakit menular di DKI Jakarta adalah TBC, disusul oleh Gastro Entritits lalu DBD.

# Membuat plot penderita penyakit tiap wilayah pertahun.
g3 = sns.catplot(x='wilayah',y='jumlah_penderita',col='tahun',data=data,kind='bar',ci=None,col_wrap=3,height=5,sharey=False)
g3.set_xticklabels(rotation=30)
g3.fig.subplots_adjust(top=0.9) 
g3.fig.suptitle('Jumlah Penderita Tiap Wilayah Per Tahun',fontsize=19)
# Dapat dilihat bahwa tiap tahun, wilayah administrasi yang memiliki jumlah penderita penyakit menular terbanyak adalah Jakarta Timur, disusul oleh Jakarta Barat dan Jakarta Selatan.

# Penderita penyakit per wilayah administrasi
sns.set_style('darkgrid')
g2 = sns.catplot(x='nama_penyakit',y='jumlah_penderita',col='wilayah',data=data,kind='bar',ci=None,col_wrap=3,height=5,sharey=False,sharex=False)
g2.set_xlabels(fontsize=15)
g2.fig.subplots_adjust(top=0.9) 
g2.fig.suptitle('Jumlah Penderita Penyakit per Wilayah Administrasi',fontsize=19)

# Plot trend penyakit tiap tahun
tren = pd.pivot_table(data, index='tahun', columns='nama_penyakit', values='jumlah_penderita')
print(tren)
tren.plot(kind='line',xlabel='Tahun', title='Jumlah Penderita Penyakit Menular di DKI Jakarta').legend(loc='upper left')
