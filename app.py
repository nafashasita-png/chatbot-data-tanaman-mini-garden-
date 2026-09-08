```python
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

    "monstera": {
        "nama": "Monstera",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya terang tidak langsung",
        "air": "2–3 kali seminggu",
        "manfaat": "Mempercantik ruangan",
        "perawatan": "Letakkan di tempat terang dan hindari sinar matahari langsung."
    },

    "lidah mertua": {
        "nama": "Lidah Mertua",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya sedang",
        "air": "1 kali seminggu",
        "manfaat": "Membantu meningkatkan kualitas udara",
        "perawatan": "Jangan terlalu sering menyiram karena tanaman tahan terhadap kondisi kering."
    },

    "kaktus": {
        "nama": "Kaktus",
        "jenis": "Tanaman Sukulen",
        "cahaya": "Cahaya matahari langsung",
        "air": "1–2 kali seminggu",
        "manfaat": "Mudah dirawat",
        "perawatan": "Gunakan tanah dengan drainase baik dan jangan terlalu banyak air."
    },

    "lidah buaya": {
        "nama": "Lidah Buaya",
        "jenis": "Tanaman Sukulen",
        "cahaya": "Cahaya terang",
        "air": "1–2 kali seminggu",
        "manfaat": "Gel lidah buaya dapat dimanfaatkan untuk perawatan kulit",
        "perawatan": "Gunakan media tanam yang tidak mudah menahan air."
    },

    "sirih gading": {
        "nama": "Sirih Gading",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya terang tidak langsung",
        "air": "2–3 kali seminggu",
        "manfaat": "Mempercantik ruangan",
        "perawatan": "Dapat ditanam di tanah maupun air dan membutuhkan cahaya yang cukup."
    },

    "peace lily": {
        "nama": "Peace Lily",
        "jenis": "Tanaman Indoor",
        "cahaya": "Cahaya rendah hingga sedang",
        "air": "2 kali seminggu",
        "manfaat": "Cocok digunakan sebagai tanaman hias indoor",
        "perawatan": "Jaga kelembapan tanah dan hindari sinar matahari langsung."
    },

    "bambu rejeki": {
        "nama": "Bambu Rejeki",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya tidak langsung",
        "air": "2–3 kali seminggu",
        "manfaat": "Mempercantik ruangan",
        "perawatan": "Dapat ditanam menggunakan media air dan hindari cahaya matahari langsung."
    },

    "aglaonema": {
        "nama": "Aglaonema",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya rendah hingga sedang",
        "air": "2 kali seminggu",
        "manfaat": "Mempercantik ruangan",
        "perawatan": "Gunakan media tanam yang lembap tetapi tidak tergenang."
    },

    "calathea": {
        "nama": "Calathea",
        "jenis": "Tanaman Hias",
        "cahaya": "Cahaya tidak langsung",
        "air": "2–3 kali seminggu",
        "manfaat": "Memiliki corak daun yang menarik",
        "perawatan": "Menyukai kelembapan tinggi dan tidak cocok terkena matahari langsung."
    },

    "lavender": {
        "nama": "Lavender",
        "jenis": "Tanaman Aromatik",
        "cahaya": "Cahaya matahari langsung",
        "air": "2 kali seminggu",
        "manfaat": "Memiliki aroma khas",
        "perawatan": "Letakkan di tempat yang mendapat banyak cahaya matahari dan memiliki drainase baik."
    },

    "kemangi": {
        "nama": "Kemangi",
        "jenis": "Tanaman Herbal",
        "cahaya": "Cahaya matahari",
        "air": "Setiap hari secukupnya",
        "manfaat": "Dapat digunakan sebagai tanaman herbal",
        "perawatan": "Berikan cahaya yang cukup dan jaga tanah tetap lembap."
    },

    "paku boston": {
        "nama": "Paku Boston",
        "jenis": "Tanaman Indoor",
        "cahaya": "Cahaya tidak langsung",
        "air": "3 kali seminggu",
        "manfaat": "Mempercantik ruangan",
        "perawatan": "Jaga kelembapan media tanam dan hindari kondisi terlalu kering."
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

        st.warning("Silakan masukkan pertanyaan terlebih dahulu.")


st.divider()

st.caption(
    "🌱 Mini Garden Chatbot | Projek Informatika Kelas XII"
)
```
