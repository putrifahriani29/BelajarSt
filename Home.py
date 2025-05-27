import streamlit as st
import streamlit as st

# Judul halaman
st.title("Halo, Streamlit!")

# Teks biasa
st.write("Ini adalah aplikasi Streamlit pertama saya.")

# Markdown dengan format tebal, miring, dan list
st.markdown("""
### Selamat datang di aplikasi belajar Streamlit!

**Fitur-fitur yang ada:**
- Input teks
- Tombol interaktif
- Slider angka
- Checkbox
- Dropdown pilihan

_Coba gunakan fitur-fitur tersebut di bawah ini!_
""")

# Informasi tambahan dengan st.info
st.info("Pastikan kamu mengisi nama dan memilih opsi yang sesuai untuk hasil yang maksimal!")

# Input teks dari pengguna
nama = st.text_input("Masukkan nama kamu:")

# Tombol
if st.button("Sapa"):
    st.write(f"Halo, {nama}! Selamat belajar Streamlit.")

# Slider input angka
umur = st.slider("Berapa umur kamu?", 0, 100, 25)
st.write(f"Umur kamu adalah {umur} tahun.")

# Checkbox
if st.checkbox("Tampilkan pesan rahasia"):
    st.write("Ini pesan rahasia!")

# Pilihan dropdown
warna = st.selectbox("Pilih warna favorit kamu:", ["Merah", "Hijau", "Biru"])
st.write(f"Warna favorit kamu adalah {warna}.")
