import pulp as lp

# Parameter
biaya_penanganan = {
    "Produk 1" : 5,
    "Produk 2" : 6,
    "Produk 3" : 7,
    "Produk 4" : 8
}
jenis_prod = biaya_penanganan.keys()

biaya_jarak_delivery = {
    "Konsumen 1" : [10,100],
    "Konsumen 2" : [12,200],
    "Konsumen 3" : [15,300],
    "Konsumen 4" : [20,350]
}

konsumen = biaya_jarak_delivery.keys()

# kiri fc, kanan cost pemusnahan
cost_buang = {
    "Pembuangan 1" : [30000,10],
    "Pembuangan 2" : [32000,11],
    "Pembuangan 3" : [33000,12],
    "Pembuangan 4" : [34000,13]
}

pembuangan = cost_buang.keys()

# Inisiasi masalah
problem = lp.LpProblem(name="SCO", sense=lp.LpMinimize)
# Variable Decision
produk_from_manufaktur = lp.LpVariable.dicts("produk_from_manuf",jenis_prod,lowBound=0,upBound=None,cat=lp.LpInteger)
produk_to_konsumen = lp.LpVariable.dicts("produk_to_konsum",konsumen,lowBound=0,upBound=None,cat=lp.LpInteger)
pendirian_buang = lp.LpVariable.dicts("pendirian_buang",pembuangan,lowBound=0,upBound=1,cat=lp.LpBinary)
jumlah_dimusnahkan = lp.LpVariable.dicts("jumlah_dimusnahkan",pembuangan,lowBound=0,upBound=None,cat=lp.LpInteger) 

# print(produk_from_manufaktur)

biaya_penanganan_produk=lp.lpSum(produk_from_manufaktur[item]*biaya_penanganan[item] for item in biaya_penanganan)
biaya_pengiriman_konsumen = lp.lpSum(biaya_jarak_delivery[item][0]*produk_to_konsumen[item]*biaya_jarak_delivery[item][1] for item in biaya_jarak_delivery)

biaya_pendirian_buang = lp.lpSum(cost_buang[item][0]*pendirian_buang[item] for item in cost_buang)
biaya_proses_pemusnahan = lp.lpSum(cost_buang[item][1]*jumlah_dimusnahkan[item] for item in cost_buang)


Biaya_Pemanufaktur=0
Biaya_Distribusi = biaya_penanganan_produk + biaya_pengiriman_konsumen
Biaya_Pengumpulan = 0
Biaya_Pembuangan = biaya_pendirian_buang + biaya_proses_pemusnahan 

problem += lp.lpSum(Biaya_Pemanufaktur + Biaya_Distribusi + Biaya_Pengumpulan + Biaya_Pembuangan)

print(problem)