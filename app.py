import streamlit as st
import yt_dlp

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Video Downloader Pro", page_icon="🎬", layout="centered")

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
st.write("Jika pilihan 720p tidak muncul, berarti YouTube memproteksi format tersebut untuk link langsung.")

url = st.text_input("Tempel Link YouTube di sini:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    try:
        with st.spinner('Mencari kualitas video yang tersedia...'):
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                # Menggunakan User Agent terbaru agar dianggap browser asli
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                st.image(info.get('thumbnail'), use_container_width=True)
                st.subheader(f"✅ {info.get('title')}")
                
                formats = info.get('formats', [])
                valid_formats = []
                seen_resolutions = set()

                # LOGIKA BARU: Cari SEMUA format yang punya video + audio (termasuk non-MP4 jika perlu)
                for f in formats:
                    # Syarat: Harus ada video, harus ada audio, dan harus ada URL downloadnya
                    if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                        res = f.get('height')
                        ext = f.get('ext')
                        
                        # Kita ambil resolusi yang unik
                        if res and res >= 144:
                            # Label unik agar user tahu formatnya (misal: 720p mp4)
                            label = f"{res}p ({ext})"
                            if label not in seen_resolutions:
                                valid_formats.append({
                                    'label': label,
                                    'url': f.get('url'),
                                    'height': res
                                })
                                seen_resolutions.add(label)
                
                # Urutkan dari yang paling jernih (tinggi)
                valid_formats = sorted(valid_formats, key=lambda x: x['height'], reverse=True)

                if valid_formats:
                    options = {f['label']: f['url'] for f in valid_formats}
                    selected_label = st.selectbox("Pilih Kualitas Tersedia:", list(options.keys()))
                    download_url = options[selected_label]

                    st.markdown(
                        f'''
                        <div style="text-align: center;">
                            <a href="{download_url}" target="_blank" style="text-decoration: none;">
                                <div style="background-color: #2ecc71; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 22px; margin-top: 20px;">
                                    🚀 DOWNLOAD {selected_label}
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
                    st.warning("Video ini hanya tersedia dalam kualitas rendah atau link diproteksi oleh YouTube.")

    except Exception as e:
        st.error("Terjadi gangguan koneksi ke YouTube. Silakan coba lagi nanti.")

st.write("---")
st.caption("Catatan: Beberapa video mungkin tidak menampilkan pilihan HD karena kebijakan hak cipta YouTube.")

# --- IKLAN ADSTERRA BAWAH ---
st.components.v1.html(
    """
    <div style="text-align:center;">
        <script type="text/javascript" src="https://pl28877010.effectivegatecpm.com/45/b9/cf/45b9cfd5714d13c257a8ba8f497c1705.js"></script>
    </div>
    """,
    height=150,
)
