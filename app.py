import streamlit as st
import yt_dlp

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Free Video Downloader", page_icon="🎬", layout="centered")

# --- IKLAN ADSTERRA ATAS ---
# Bagian ini akan menampilkan iklan Anda di bagian paling atas halaman
st.components.v1.html(
    """
    <div style="text-align:center;">
        <script type="text/javascript" src="https://pl28877010.effectivegatecpm.com/45/b9/cf/45b9cfd5714d13c257a8ba8f497c1705.js"></script>
    </div>
    """,
    height=150,
)

# --- TAMPILAN UTAMA ---
st.title("🎬 YouTube Video Downloader")
st.write("Download video YouTube favorit Anda dengan mudah dan gratis!")

# Input URL dari User
url = st.text_input("Tempel Link YouTube di sini:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    try:
        # Menampilkan loading spinner saat mengecek video
        with st.spinner('Sedang mencari video...'):
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'format': 'best', # Mengambil format terbaik yang sudah tergabung (Video+Audio)
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title')
                thumbnail = info.get('thumbnail')
                
                # Tampilkan Preview Video
                st.image(thumbnail, use_container_width=True)
                st.subheader(f"✅ {title}")
                
                # Ambil Link Download Langsung dari Server YouTube
                # Kita pilih format MP4 yang paling umum
                formats = [f for f in info.get('formats', []) if f.get('vcodec') != 'none' and f.get('acodec') != 'none' and f.get('ext') == 'mp4']
                
                if formats:
                    # Ambil yang kualitasnya paling oke
                    best_format = formats[-1]
                    download_url = best_format.get('url')
                    
                    st.success("Video siap didownload!")
                    
                    # Tombol Download Besar
                    st.markdown(
                        f'''
                        <a href="{download_url}" target="_blank" style="text-decoration: none;">
                            <div style="background-color: #2ecc71; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 20px; margin-top: 10px;">
                                📥 DOWNLOAD SEKARANG
                            </div>
                        </a>
                        <p style="text-align: center; font-size: 12px; color: gray; margin-top: 5px;">
                            (Setelah klik, video akan terbuka di tab baru. Klik kanan dan "Save Video As" atau klik titik tiga di pojok video)
                        </p>
                        ''', 
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("Maaf, format MP4 langsung tidak ditemukan untuk video ini.")

    except Exception as e:
        st.error("Waduh! Link tidak valid atau video tidak bisa diakses. Pastikan link benar ya!")

# --- JARAK ---
st.write("---")

# --- IKLAN ADSTERRA BAWAH ---
# Bagian ini untuk iklan tambahan di bawah agar pendapatan maksimal
st.components.v1.html(
    """
    <div style="text-align:center;">
        <script type="text/javascript" src="https://pl28877010.effectivegatecpm.com/45/b9/cf/45b9cfd5714d13c257a8ba8f497c1705.js"></script>
    </div>
    """,
    height=150,
)

st.caption("© 2026 Free Downloader Service. Semua hak cipta dilindungi.")
