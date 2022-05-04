class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas_tanah = 0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_luas_tanah(self):
        return self.luas_tanah

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian : "+ self.jenis + ".\n" + "Luas tanah : " + str(self.luas_tanah) + "m^2.\n" + "Jumlah kamar : " + str(self.jml_kamar) + " kamar.\n" + "Ditempati oleh : " + str(self.jml_penghuni) + " orang.\n\n"