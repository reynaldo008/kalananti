# import streamlit as st

# # --- Fungsi untuk menampilkan setiap halaman ---
# def show_homepage():
#     """Menampilkan halaman utama (homepage) aplikasi."""
#     st.title("Selamat Datang di Kopi Kala Nanti")
#     st.header("Filosofi Kami")
#     st.write(
#         """
#         Di Kopi Kala Nanti, kami percaya bahwa setiap tegukan kopi adalah
#         sebuah perenungan akan masa lalu dan inspirasi untuk masa depan.
#         Kami menyajikan kopi terbaik dari biji pilihan, diolah dengan
#         hati-hati untuk menghasilkan cita rasa yang tak terlupakan.
#         """
#     )
#     st.image("https://placehold.co/1200x600/1E2A36/A6B3A9?text=Ruang+Kopi+yang+Hangat", use_column_width=True)
#     st.markdown("---")
#     st.header("Pilihan Favorit")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.image("https://placehold.co/400x400/1E2A36/A6B3A9?text=Kopi+Susu+Gula+Aren")
#         st.subheader("Kopi Susu Gula Aren")
#         st.write("Perpaduan sempurna antara espresso, susu, dan manisnya gula aren.")
#     with col2:
#         st.image("https://placehold.co/400x400/1E2A36/A6B3A9?text=Cappuccino")
#         st.subheader("Cappuccino")
#         st.write("Espresso klasik dengan busa susu lembut di atasnya.")
#     with col3:
#         st.image("https://placehold.co/400x400/1E2A36/A6B3A9?text=Cokelat+Panas")
#         st.subheader("Cokelat Panas")
#         st.write("Minuman non-kopi yang kaya rasa dan menghangatkan.")

# def show_about_page():
#     """Menampilkan halaman About dengan sub-halaman."""
#     st.title("Tentang Kami")
#     sub_page = st.selectbox(
#         "Pilih:",
#         ["Our Story", "Sustainability", "Team"]
#     )
#     st.markdown("---")
#     if sub_page == "Our Story":
#         st.header("Our Story")
#         st.write("""
#             Kopi Kala Nanti berawal dari sebuah mimpi kecil untuk menciptakan ruang
#             di mana setiap orang bisa menikmati kopi berkualitas. Berdiri sejak 2020,
#             kami terus berinovasi sambil tetap menjaga esensi dari secangkir kopi yang otentik.
#         """)
#     elif sub_page == "Sustainability":
#         st.header("Sustainability")
#         st.write("""
#             Kami berkomitmen untuk praktik berkelanjutan. Kami bekerja sama dengan
#             petani lokal untuk memastikan biji kopi kami ditanam dengan etis dan
#             ramah lingkungan. Kami juga menggunakan kemasan daur ulang.
#         """)
#     elif sub_page == "Team":
#         st.header("Team")
#         st.write("""
#             Di balik setiap cangkir kopi kami ada tim yang bersemangat dan berdedikasi.
#             Mereka adalah barista yang ahli, roaster yang teliti, dan individu yang
#             percaya pada kekuatan kopi untuk menyatukan orang.
#         """)

# def show_menu_page():
#     """Menampilkan halaman Menu dengan sub-halaman."""
#     st.title("Menu")
#     menu_category = st.selectbox(
#         "Pilih Kategori Menu:",
#         ["Kopi Susu", "Espresso Based", "Non-Kopi", "Signature", "Seasonal & Limited"]
#     )
#     st.markdown("---")
#     st.header(menu_category)
#     if menu_category == "Kopi Susu":
#         st.write("Pilihan kopi susu andalan kami yang creamy dan nikmat.")
#         st.image("https://placehold.co/600x400/1E2A36/A6B3A9?text=Kopi+Susu+Gula+Aren")
#         st.write("**Kopi Susu Gula Aren:** Perpaduan otentik espresso dan gula aren.")
#         st.image("https://placehold.co/600x400/1E2A36/A6B3A9?text=Kopi+Susu+Karamel")
#         st.write("**Kopi Susu Karamel:** Manisnya karamel dengan sentuhan kopi.")
#     elif menu_category == "Espresso Based":
#         st.write("Menu klasik berbasis espresso untuk para penikmat sejati.")
#         st.image("https://placehold.co/600x400/1E2A36/A6B3A9?text=Latte")
#         st.write("**Latte:** Espresso dengan steamed milk.")
#     # Tambahkan lebih banyak konten untuk setiap kategori
#     elif menu_category == "Non-Kopi":
#         st.write("Pilihan lezat bagi yang tidak mengkonsumsi kopi.")
#     elif menu_category == "Signature":
#         st.write("Kreasi spesial dari barista kami.")
#     elif menu_category == "Seasonal & Limited":
#         st.write("Menu terbatas yang hanya tersedia di musim tertentu.")

# def show_order_delivery_page():
#     """Menampilkan halaman Order / Delivery dengan sub-halaman."""
#     st.title("Pesan & Pengiriman")
#     sub_page = st.selectbox(
#         "Pilih:",
#         ["Online Delivery", "Pre-Order Coffee Box / Beans", "Membership / Subscription"]
#     )
#     st.markdown("---")
#     if sub_page == "Online Delivery":
#         st.header("Online Delivery")
#         st.write("""
#             Pesan kopi favorit Anda melalui aplikasi pengiriman makanan online.
#             Temukan kami di GoFood, GrabFood, dan ShopeeFood.
#         """)
#         st.image("https://placehold.co/600x200/1E2A36/A6B3A9?text=Aplikasi+Delivery")
#     elif sub_page == "Pre-Order Coffee Box / Beans":
#         st.header("Pre-Order Coffee Box & Biji Kopi")
#         st.write("""
#             Pesan biji kopi atau kotak kopi untuk kebutuhan Anda di rumah atau kantor.
#             Silakan hubungi kami untuk informasi lebih lanjut.
#         """)
#     elif sub_page == "Membership / Subscription":
#         st.header("Membership & Langganan")
#         st.write("""
#             Dapatkan keuntungan eksklusif dengan menjadi anggota kami atau
#             berlangganan paket kopi bulanan.
#         """)

# def show_blog_page():
#     """Menampilkan halaman Blog dengan sub-halaman."""
#     st.title("Blog")
#     sub_page = st.selectbox(
#         "Pilih:",
#         ["Tips & Edukasi Kopi", "Coffee Culture", "Behind the Bar", "Bisnis & Ghost Kitchen"]
#     )
#     st.markdown("---")
#     if sub_page == "Tips & Edukasi Kopi":
#         st.header("Tips & Edukasi Kopi")
#         st.write("**Cara Menyeduh Kopi V60 yang Sempurna:** Ikuti panduan langkah demi langkah kami.")
#     elif sub_page == "Coffee Culture":
#         st.header("Coffee Culture")
#         st.write("**Sejarah Kopi:** Dari biji hingga menjadi minuman favorit dunia.")
#     elif sub_page == "Behind the Bar":
#         st.header("Behind the Bar")
#         st.write("**Meet Our Barista:** Kisah di balik para ahli kopi kami.")
#     elif sub_page == "Bisnis & Ghost Kitchen":
#         st.header("Bisnis & Ghost Kitchen")
#         st.write("**Membangun Kopi Kala Nanti:** Strategi kami dalam bisnis kopi.")

# def show_location_contact_page():
#     """Menampilkan halaman Lokasi & Kontak dengan sub-halaman."""
#     st.title("Lokasi & Kontak")
#     sub_page = st.selectbox(
#         "Pilih:",
#         ["Map & Address", "WhatsApp CTA", "Social Media", "Jam Operasional"]
#     )
#     st.markdown("---")
#     if sub_page == "Map & Address":
#         st.header("Peta & Alamat")
#         st.write("Temukan lokasi kami di sini:")
#         st.image("https://placehold.co/600x400/1E2A36/A6B3A9?text=Google+Maps")
#         st.write("Jalan Kopi No. 123, Jakarta Selatan")
#     elif sub_page == "WhatsApp CTA":
#         st.header("WhatsApp")
#         st.write("Pesan melalui WhatsApp dengan mengklik tombol di bawah:")
#         st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/628123456789)")
#     elif sub_page == "Social Media":
#         st.header("Media Sosial")
#         st.write("Ikuti kami di media sosial untuk update terbaru!")
#         st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/kopikalananti)")
#     elif sub_page == "Jam Operasional":
#         st.header("Jam Operasional")
#         st.write("Senin - Jumat: 09.00 - 21.00")
#         st.write("Sabtu - Minggu: 10.00 - 22.00")

# def show_shop_page():
#     """Menampilkan halaman Shop dengan sub-halaman."""
#     st.title("Shop")
#     sub_page = st.selectbox(
#         "Pilih:",
#         ["Beans", "Merchandise", "Brewing Tools"]
#     )
#     st.markdown("---")
#     if sub_page == "Beans":
#         st.header("Biji Kopi")
#         st.write("Pilihan biji kopi single origin dan house blend terbaik.")
#     elif sub_page == "Merchandise":
#         st.header("Merchandise")
#         st.write("T-shirt, tumbler, dan merchandise eksklusif lainnya.")
#     elif sub_page == "Brewing Tools":
#         st.header("Peralatan Seduh")
#         st.write("Alat-alat seduh manual untuk pengalaman kopi di rumah.")

# # --- Bagian utama aplikasi ---
# # Konfigurasi halaman
# st.set_page_config(
#     page_title="Kopi Kala Nanti",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Kustomisasi CSS
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
# html, body, [class*="css"] {
#     font-family: 'Poppins', sans-serif;
# }
# .main {
#     background-color: #F8F8F8;
#     color: #333;
# }
# .sidebar .sidebar-content {
#     background-color: #ECECEC;
#     color: #333;
# }
# .stRadio > label {
#     font-weight: bold;
# }
# .stSelectbox > label {
#     font-weight: bold;
# }
# h1, h2, h3 {
#     color: #4A2E1F;
# }
# </style>
# """, unsafe_allow_html=True)

# # Navigasi di sidebar
# st.sidebar.image("https://placehold.co/300x150/1E2A36/A6B3A9?text=Kopi+Kala+Nanti+Logo")
# st.sidebar.title("Navigasi")
# page = st.sidebar.radio(
#     "Pilih Halaman:",
#     ["Homepage", "About", "Menu", "Order / Delivery", "Blog", "Location / Contact", "Shop"]
# )
# st.sidebar.markdown("---")
# st.sidebar.info("Web ini dibuat dengan Streamlit.")

# # Menampilkan halaman yang dipilih
# if page == "Homepage":
#     show_homepage()
# elif page == "About":
#     show_about_page()
# elif page == "Menu":
#     show_menu_page()
# elif page == "Order / Delivery":
#     show_order_delivery_page()
# elif page == "Blog":
#     show_blog_page()
# elif page == "Location / Contact":
#     show_location_contact_page()
# elif page == "Shop":
#     show_shop_page()

import streamlit as st

# --- Fungsi untuk menampilkan setiap halaman ---
def show_homepage():
    st.markdown("<h1 class='main-title'>Selamat Datang di <span>Kopi Kala Nanti</span></h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subtitle'>Filosofi Kami</h2>", unsafe_allow_html=True)
    st.write(
        """
        Di Kopi Kala Nanti, kami percaya setiap tegukan kopi adalah perenungan masa lalu
        dan inspirasi untuk masa depan. Kami menyajikan kopi terbaik dari biji pilihan,
        diolah dengan hati-hati untuk menghasilkan cita rasa tak terlupakan.
        """
    )
    st.image("https://placehold.co/1200x600/8B5E3C/EFE7DC?text=Ruang+Kopi+Hangat", use_column_width=True)
    st.markdown("---")

    st.markdown("<h2 class='subtitle'>Pilihan Favorit</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(card("Kopi Susu Gula Aren", "Perpaduan espresso, susu, dan gula aren.", "https://placehold.co/400x400/8B5E3C/EFE7DC?text=Kopi+Susu"))
    with col2:
        st.markdown(card("Cappuccino", "Espresso klasik dengan busa susu lembut.", "https://placehold.co/400x400/8B5E3C/EFE7DC?text=Cappuccino"))
    with col3:
        st.markdown(card("Cokelat Panas", "Minuman non-kopi yang kaya rasa.", "https://placehold.co/400x400/8B5E3C/EFE7DC?text=Cokelat+Panas"))

# --- Fungsi Card untuk styling produk/menu ---
def card(title, desc, img_url):
    return f"""
    <div class="card">
        <img src="{img_url}" class="card-img"/>
        <div class="card-body">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
    </div>
    """

# --- Bagian utama aplikasi ---
st.set_page_config(
    page_title="Kopi Kala Nanti",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Playfair+Display:wght@600&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #FDFBF7;
    color: #3E2C23;
}

/* Judul utama */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    color: #3E2C23;
    text-align: center;
    margin-bottom: 0.5em;
}
.main-title span {
    color: #8B5E3C;
}

/* Subtitle */
.subtitle {
    font-size: 1.6rem;
    font-weight: 600;
    color: #5C3D2E;
    margin: 1em 0;
}

/* Card */
.card {
    background: #FFFDF9;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(139, 94, 60, 0.15);
    overflow: hidden;
    text-align: center;
    transition: transform 0.2s ease;
    padding-bottom: 1em;
}
.card:hover {
    transform: translateY(-5px);
}
.card-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}
.card-body {
    padding: 1em;
}
.card-body h3 {
    margin: 0.5em 0;
    font-size: 1.2rem;
    color: #3E2C23;
}
.card-body p {
    font-size: 0.9rem;
    color: #5C3D2E;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EFE7DC;
    padding: 1em;
}
section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    color: #3E2C23;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://placehold.co/250x120/8B5E3C/EFE7DC?text=Kopi+Kala+Nanti")
st.sidebar.title("Navigasi")
page = st.sidebar.radio(
    "Pilih Halaman:",
    ["Homepage", "About", "Menu", "Order / Delivery", "Blog", "Location / Contact", "Shop"]
)

st.sidebar.markdown("---")
st.sidebar.info("☕ Web ini dibuat dengan Streamlit")

# Routing halaman
if page == "Homepage":
    show_homepage()
elif page == "About":
    st.markdown("<h1 class='main-title'>Tentang Kami</h1>", unsafe_allow_html=True)
elif page == "Menu":
    st.markdown("<h1 class='main-title'>Menu</h1>", unsafe_allow_html=True)
elif page == "Order / Delivery":
    st.markdown("<h1 class='main-title'>Pesan & Pengiriman</h1>", unsafe_allow_html=True)
elif page == "Blog":
    st.markdown("<h1 class='main-title'>Blog</h1>", unsafe_allow_html=True)
elif page == "Location / Contact":
    st.markdown("<h1 class='main-title'>Lokasi & Kontak</h1>", unsafe_allow_html=True)
elif page == "Shop":
    st.markdown("<h1 class='main-title'>Shop</h1>", unsafe_allow_html=True)
