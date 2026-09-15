import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Mini Garden Chatbot",
    page_icon="🌱",
    layout="centered"
)


# ==========================================
# JUDUL APLIKASI
# ==========================================

st.title("🌱 Mini Garden Chatbot")
st.subheader("🤖 Chatbot Data Tanaman")

st.write(
    "Halo! Saya Mini Garden Bot 🌿. "
    "Saya dapat membantu memberikan informasi "
    "tentang berbagai jenis tanaman."
)

st.divider()


# ==========================================
# DATABASE TANAMAN
# ==========================================

data_tanaman = {

    "lidah buaya": {
        "nama": "Lidah Buaya",
        "nama_ilmiah": "Aloe Vera",
        "jenis": "Sukulen",
        "cahaya": "Butuh cahaya terang",
        "air": "2–3×/minggu, jangan terlalu basah",
        "manfaat": "Perawatan kulit, obat tradisional",
        "perawatan": "Media porous, cukup cahaya, jangan terlalu sering disiram"
    },

    "pepaya": {
        "nama": "pepaya",
        "nama_ilmiah":"carica papaya",
        "jenis": "Tanaman buah",
        "cahaya": "cahaya matahari langsung dan cukup banyak",
        "air": "1×/hari saat tanah kering",
        "manfaat": "Buah, sumber vitamin",
        "perawatan": "Banyak cahaya, tanah subur, beri pupuk"
    },

    "pisang": {
        "nama": "pisang",
        "nama_ilmiah":"musa sp",
        "jenis": "Tanaman buah",
        "cahaya": "cahaya matahari langsung dan cukup banyak",
        "air": "1×/hari",
        "manfaat": "Buah, sumber energi",
        "perawatan": "Tanah lembap, cukup sinar matahari, beri pupuk"
    },

    "pandan": {
        "nama": "pandan",
        "nama_ilmiah":"Pandanus amaryllifolius",
        "jenis": "Tanaman rempah",
        "cahaya": "terang, tetapi tidak harus terkena matahari langsung sepanjang hari. Pandan dapat tumbuh baik di tempat terang dengan sedikit teduh.",
        "air": "1×/hari secukupnya",
        "manfaat": "Pewangi makanan/minuman",
        "perawatan": "Tanah lembap, cahaya cukup, pot memiliki drainase"
    },

    "cabai": {
        "nama": "cabai",
        "nama_ilmiah":"Capsicum annuum",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Bumbu dan sumber vitamin",
        "perawatan": "Sinar matahari cukup, siram teratur, beri pupuk"
    },

    "tomat": {
        "nama": "tomat",
        "nama_ilmiah":"Solanum lycopersicum",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Bahan makanan, vitamin",
        "perawatan": "Cahaya cukup, pasang penyangga, beri pupuk"
    },

    "kemangi": {
        "nama": "kemangi",
        "nama_ilmiah":"Ocimum basilicum",
        "jenis": "Tanaman herbal",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Lalapan dan bumbu",
        "perawatan": "Cukup sinar, pangkas pucuk, tanah tidak tergenang"
    },

    "seledri": {
        "nama": "seledri",
        "nama_ilmiah":"Apium graveolens",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya terang, tetapi lebih baik tidak terkena matahari langsung terlalu lama.",
        "air": "1×/hari",
        "manfaat": "Bumbu dan pelengkap makanan",
        "perawatan": "Tanah lembap, cahaya pagi, beri pupuk organik"
    },

    "bawang daun": {
        "nama": "bawang daun",
        "nama_ilmiah":"Allium fistulosum",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Bumbu masakan",
        "perawatan": "Tanah gembur, cukup cahaya, pot tidak tergenang"
    },

    "kangkung": {
        "nama": "kangkung",
        "nama_ilmiah":"Ipomoea aquatica",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Sayuran dan sumber serat",
        "perawatan": "Tanah lembap, cukup sinar matahari"
    },

    "sawi": {
        "nama": "sawi",
        "nama_ilmiah":"Brassica juncea",
        "jenis": "Tanaman sayuran",
        "cahaya":"cahaya matahari yang cukup dan tidak terlalu panas",
        "air": "1×/hari",
        "manfaat": "Sayuran, vitamin dan mineral",
        "perawatan": "Tanah subur, siram rutin, hindari genangan"
    },

    "jeruk": {
        "nama": "jeruk",
        "nama_ilmiah":"Citrus sp.",
        "jenis": "Tanaman buah",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari saat kering",
        "manfaat": "Buah dan sumber vitamin C",
        "perawatan": "Sinar matahari cukup, pupuk berkala"
    },

    "singkong": {
        "nama": "singkong",
        "nama_ilmiah":"Manihot esculenta",
        "jenis": "Tanaman pangan",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "2–3×/minggu",
        "manfaat": "Sumber karbohidrat",
        "perawatan": "Tanah gembur, cukup cahaya, jangan tergenang"
    },

    "talas": {
        "nama": "talas",
        "nama_ilmiah":"Colocasia Esculenta",
        "jenis": "Tanaman pangan/hias",
        "cahaya":"cahaya terang, tetapi bisa tumbuh di tempat teduh sebagian",
        "air": "1×/hari secukupnya",
        "manfaat": "Pangan dan tanaman hias",
        "perawatan": "Tanah lembap, teduh sebagian, beri pupuk"
    },

    "palem": {
        "nama": "palem",
        "nama_ilmiah":"Arecaceae sp.",
        "jenis": "Tanaman hias",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "2–4×/minggu",
        "manfaat": "Mempercantik dan menghijaukan lingkungan",
        "perawatan": "Cahaya cukup, pangkas daun kering, siram secukupnya"
    },

    "ubi jalar": {
        "nama": "ubi jalar",
        "nama_ilmiah":"Ipomoea batatas",
        "jenis": "Tanaman pangan",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari saat kering",
        "manfaat": "Sumber karbohidrat dan serat",
        "perawatan": "Tanah gembur, cukup cahaya, siram secukupnya"
    },

    "selada": {
        "nama": "selada",
        "nama_ilmiah":"Lactuca sativa",
        "jenis": "Sayuran",
        "cahaya":"cahaya terang, tetapi tidak terlalu terik atau tempat dengan teduh sebagian",
        "air": "1×/hari",
        "manfaat": "Lalapan, sumber serat dan vitamin",
        "perawatan": "Tanah lembap, tidak tergenang, cahaya cukup"
    },

    "terong": {
        "nama": "terong",
        "nama_ilmiah":"Solanum melongena",
        "jenis": "Sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Sumber serat dan vitamin",
        "perawatan": "Tanah subur, cukup cahaya, beri pupuk"
    },

    "bayam": {
        "nama": "bayam",
        "nama_ilmiah":"Amaranthus tricolor",
        "jenis": "Sayuran",
        "cahaya":"cahaya matahari langsung yang cukup",
        "air": "1×/hari",
        "manfaat": "Mengandung zat besi dan vitamin",
        "perawatan": "Tanah subur, lembap, dan cukup cahaya"
   
    }
}


# ==========================================
# FUNGSI CHATBOT
# ==========================================

def chatbot(pertanyaan):

    pertanyaan = pertanyaan.lower()

    # Mencari tanaman berdasarkan kata kunci
    for kata_kunci, tanaman in data_tanaman.items():

        if kata_kunci in pertanyaan:

            # Pertanyaan tentang penyiraman
            if (
                "air" in pertanyaan
                or "siram" in pertanyaan
                or "penyiraman" in pertanyaan
            ):
                return (
                    f"💧 Untuk tanaman **{tanaman['nama']}**, "
                    f"penyiraman yang disarankan adalah "
                    f"**{tanaman['air']}**."
                )

            # Pertanyaan tentang cahaya
            elif (
                "cahaya" in pertanyaan
                or "matahari" in pertanyaan
                or "terang" in pertanyaan
            ):
                return (
                    f"☀️ Tanaman **{tanaman['nama']}** membutuhkan "
                    f"**{tanaman['cahaya']}**."
                )

            # Pertanyaan tentang manfaat
            elif (
                "manfaat" in pertanyaan
                or "fungsi" in pertanyaan
                or "guna" in pertanyaan
            ):
                return (
                    f"❤️ Manfaat dari **{tanaman['nama']}** adalah "
                    f"{tanaman['manfaat']}."
                )

            # Pertanyaan tentang perawatan
            elif (
                "rawat" in pertanyaan
                or "perawatan" in pertanyaan
                or "cara" in pertanyaan
            ):
                return (
                    f"🌱 Cara merawat **{tanaman['nama']}**:"
                    f"\n\n{tanaman['perawatan']}"
                    f"\n\n💧 Penyiraman: {tanaman['air']}"
                    f"\n\n☀️ Cahaya: {tanaman['cahaya']}"
                )

            # Jika hanya menyebut nama tanaman
            else:
                return (
                    f"🌿 **{tanaman['nama']}**\n\n"
                    f"🔬 Nama ilmiah: {tanaman['nama_ilmiah']}\n\n"
                    f"Jenis: {tanaman['jenis']}\n\n"
                    f"☀️ Cahaya: {tanaman['cahaya']}\n\n"
                    f"💧 Penyiraman: {tanaman['air']}\n\n"
                    f"❤️ Manfaat: {tanaman['manfaat']}\n\n"
                    f"🌱 Perawatan: {tanaman['perawatan']}"
                )


    # Pertanyaan umum
    if "tanaman" in pertanyaan:

        return (
            f"🌿 Saat ini saya memiliki data "
            f"**{len(data_tanaman)} jenis tanaman**.\n\n"
            "Kamu dapat menanyakan nama tanaman, "
            "cara perawatan, kebutuhan cahaya, "
            "penyiraman, atau manfaatnya."
        )


    if (
        "indoor" in pertanyaan
        or "dalam rumah" in pertanyaan
    ):

        return (
            "🏠 Beberapa tanaman yang cocok "
            "untuk di dalam rumah adalah:\n\n"
            "🌿 Monstera\n"
            "🪴 Lidah Mertua\n"
            "🌱 Peace Lily\n"
            "🍃 Sirih Gading\n"
            "🌿 Aglaonema\n"
            "🍃 Calathea"
        )


    if (
        "pemula" in pertanyaan
        or "mudah" in pertanyaan
    ):

        return (
            "🌱 Tanaman yang relatif mudah "
            "dirawat untuk pemula antara lain:\n\n"
            "🪴 Lidah Mertua\n"
            "🌵 Kaktus\n"
            "🍃 Sirih Gading\n"
            "🌱 Lidah Buaya"
        )


    if (
        "halo" in pertanyaan
        or "hai" in pertanyaan
        or "hello" in pertanyaan
    ):

        return (
            "Halo! 👋🌱\n\n"
            "Saya Mini Garden Bot. "
            "Silakan tanyakan sesuatu tentang tanaman."
        )


    # Jika chatbot tidak menemukan jawaban
    return (
        "🤔 Maaf, saya belum memahami pertanyaan tersebut.\n\n"
        "Coba tanyakan seperti:\n\n"
        "🌿 Cara merawat monstera?\n\n"
        "💧 Berapa kali menyiram kaktus?\n\n"
        "☀️ Cahaya yang dibutuhkan lidah mertua?\n\n"
        "❤️ Apa manfaat lidah buaya?"
    )


# ==========================================
# TAMPILAN DATA TANAMAN
# ==========================================

st.header("🌿 Data Tanaman")

nama_tanaman = st.selectbox(
    "Pilih tanaman untuk melihat datanya:",
    ["Pilih tanaman"] + [
        tanaman["nama"]
        for tanaman in data_tanaman.values()
    ]
)

if nama_tanaman != "Pilih tanaman":

    for tanaman in data_tanaman.values():

        if tanaman["nama"] == nama_tanaman:

            st.info(f"🌱 **{tanaman['nama']}**")

            st.write(f"**nama ilmiah:** {tanaman['nama ilmiah']}")
            st.write(f"**Jenis:** {tanaman['jenis']}")
            st.write(f"**☀️ Cahaya:** {tanaman['cahaya']}")
            st.write(f"**💧 Penyiraman:** {tanaman['air']}")
            st.write(f"**❤️ Manfaat:** {tanaman['manfaat']}")
            st.write(f"**🌱 Perawatan:** {tanaman['perawatan']}")

            break


st.divider()


# ==========================================
# CHATBOT
# ==========================================

st.header("🤖 Tanya Mini Garden Bot")

pertanyaan = st.text_input(
    "Masukkan pertanyaan:",
    placeholder="Contoh: Cara merawat monstera?"
)

if st.button("💬 Tanya Chatbot"):

    if pertanyaan:

        jawaban = chatbot(pertanyaan)

        st.success("🤖 Jawaban Chatbot:")
        st.write(jawaban)

    else:

        st.warning(".")


st.divider()

st.caption(
    "🌱 Mini Garden Chatbot | Projek Informatika Kelas XII"
)
