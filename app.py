import streamlit as st
import yt_dlp
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Free YT Downloader", page_icon="📥")

# Bagian Iklan (Placeholder)
st.markdown('<div style="text-align: center; color: gray;">IKLAN DISINI (Banner)</div>', unsafe_allow_html=True)

st.title("📥 YouTube Video Downloader")
st.write("Download video favoritmu gratis tanpa aplikasi!")

url = st.text_input("Paste Link YouTube di sini:")

if url:
    try:
        ydl_opts = {'quiet': True, 'noplaylist': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'video')
            thumbnail = info.get('thumbnail')
            
            st.image(thumbnail, width=300)
            st.subheader(title)

            # Filter format yang punya video dan audio (MP4)
            formats = [f for f in info.get('formats', []) if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
            
            option = st.selectbox("Pilih Kualitas:", formats, format_func=lambda x: f"{x.get('height')}p - {x.get('ext')}")

            if st.button("Generate Download Link"):
                # Di versi web gratisan, kita berikan link langsung ke server YouTube
                # agar server kita tidak berat/kena ban
                download_url = option.get('url')
                st.success("Siap! Klik kanan tombol di bawah dan pilih 'Save Link As' atau klik langsung.")
                st.markdown(f'<a href="{download_url}" target="_blank" style="padding: 10px; background-color: #2ecc71; color: white; text-decoration: none; border-radius: 5px;">Download Video Sekarang</a>', unsafe_allow_html=True)
                
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# Footer Iklan
st.markdown('---')
st.markdown('<div style="text-align: center; color: gray;">IKLAN DISINI (Native Ads)</div>', unsafe_allow_html=True)
