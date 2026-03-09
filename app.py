import streamlit as st
import yt_dlp

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Video Downloader Pro - Pilih Resolusi", page_icon="🎬", layout="centered")

# --- IKLAN ADSTERRA ATAS ---
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
st.write("Tempel link YouTube, pilih resolusi, dan download gratis!")

url = st.text_input("Tempel Link YouTube di sini:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    try:
        with st.spinner('Sedang mengambil daftar resolusi...'):
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title')
                thumbnail = info.get('thumbnail')
                
                st.image(thumbnail, use_container_width=True)
                st.subheader(f"✅ {title}")
                
                # --- PROSES FILTER RESOLUSI ---
                formats = info.get('formats', [])
                valid_formats = []
                seen_resolutions = set()

                # Cari format MP4 yang punya video + audio
                for f in formats:
                    if f.get('vcodec') != 'none' and f.get('acodec') != 'none' and f.get('ext') == 'mp4':
                        res = f.get('height')
                        if res and res not in seen_resolutions:
                            valid_formats.append(f)
                            seen_resolutions.add(res)
                
                # Urutkan dari resolusi tertinggi ke terendah
                valid_formats = sorted(valid_formats, key=lambda x: x['height'], reverse=True)

                if valid_formats:
                    # Buat daftar pilihan untuk dropdown
                    options = {f"{f['height']}p (MP4)": f['url'] for f in valid_formats}
                    
                    selected_res = st.selectbox("Pilih Resolusi Video:", list(options.keys()))
                    download_url = options[selected_res]

                    st.markdown(
                        f'''
                        <div style="text-align: center;">
                            <a href="{download_url}" target="_blank" style="text-decoration: none;">
                                <div style="background-color: #2ecc71; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 22px; margin-top: 20px; cursor: pointer;">
                                    🚀 DOWNLOAD {selected_res}
                                </div>
                            </a>
                            <p style="color: #ffcc00; font-size: 14px; margin-top: 15px; font-weight: bold;">
                                TIPS: Jika video terbuka di tab baru, klik TITIK TIGA (⋮) di pojok video lalu pilih "Download".
                            </p>
                        </div>
                        ''', 
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("Maaf, tidak ditemukan format MP4 standar untuk video ini. Coba link video lain.")

    except Exception as e:
        st.error("Terjadi kesalahan atau video tidak ditemukan. Pastikan link YouTube benar.")

# --- ARTIKEL SEO ---
st.write("---")
st.subheader("Cara Download Video YouTube ke Galeri")
st.write("""
Layanan ini memungkinkan Anda memilih berbagai resolusi mulai dari **360p, 480p, hingga 720p (HD)**. 
Cukup salin URL video dari aplikasi YouTube, tempelkan di kotak di atas, pilih kualitas yang diinginkan, 
dan klik tombol download. Sangat mudah, tanpa login, dan gratis selamanya!
""")

# --- IKLAN ADSTERRA BAWAH ---
st.components.v1.html(
    """
    <div style="text-align:center;">
        <script type="text/javascript" src="https://pl28877010.effectivegatecpm.com/45/b9/cf/45b9cfd5714d13c257a8ba8f497c1705.js"></script>
    </div>
    """,
    height=150,
)
