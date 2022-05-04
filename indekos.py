from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, ls_tanah):
        super().__init__("Indekos", luas_tanah = ls_tanah)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian : Indekos.\n" +  "Luas tanah : " + str(self.luas_tanah) + "m^2.\n" + "Nama penghuni : " + str(self.nama_penghuni) + ".\n\n"