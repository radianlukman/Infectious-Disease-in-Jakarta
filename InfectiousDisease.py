# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset as pandas dataframe "data".
data = pd.read_csv("PenyakitMenularDKI.csv")
print(data)
print(data.info())

# Change year, region, and disease column type into category 
data['tahun']=data['tahun'].astype('category')
data['wilayah']=data['wilayah'].astype('category')
data['nama_penyakit']=data['nama_penyakit'].astype('category')
print(data.info())

pertahun = data.groupby('tahun').jumlah_penderita.sum()
print(pertahun)
pertahun.plot(kind='line',xlabel='Tahun',ylabel='Jumlah',title='Jumlah Penderita Penyakit Menular di DKI Jakarta \n  2015-2020')

def PlotGrup(grup,judul):
    data_a = data.groupby(grup).jumlah_penderita.sum().sort_values()
    print(data_a)
    data_a.plot(kind="barh",title=judul)
    
PlotGrup(grup='nama_penyakit',judul='Jumlah Penderita Penyakit Menular di DKI Jakarta Berdasarkan Jenis Penyakit')
PlotGrup(grup='wilayah',judul="Jumlah Penderita Penyakit Menular di DKI Jakarta Berdasarkan Wilayah")

def PlotGrid(baris, kolom, judul):
    sns.set_style('darkgrid')
    g1=sns.catplot(x=baris,y='jumlah_penderita', col=kolom, data=data, kind='bar',ci=None,col_wrap=3,height=5,sharey=False)
    g1.fig.subplots_adjust(top=0.9)
    g1.fig.suptitle(judul,fontsize=19)
    g1.set_xticklabels(rotation=30)
    plt.show()
    plt.clf()

# Membuat plot Penderita penyakit pertahun
PlotGrid(baris='nama_penyakit',kolom='tahun',judul="Jumlah Penderita Penyakit per Tahun")

# Membuat plot penderita penyakit tiap wilayah pertahun.
PlotGrid(baris='wilayah',kolom='tahun',judul='Jumlah Penderita Tiap Wilayah per Tahun')

# Membuat plot jenis penyakit per wilayah.
PlotGrid(baris='nama_penyakit',kolom='wilayah',judul='Jumlah Penderita Penyakit Tiap Wilayah')

# Plot trend penyakit tiap tahun
tren = pd.pivot_table(data, index='tahun', columns='nama_penyakit', values='jumlah_penderita')
print(tren)
tren.plot(kind='line',xlabel='Tahun', title='Jumlah Penderita Penyakit Menular di DKI Jakarta').legend(loc='upper left')