import streamlit as st
import streamlit.components.v1 as components
import langchain_helper
import random

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Culinary Compass",
    page_icon="🍽️",
    layout="wide",
)

# ─────────────────────────────────────────────
# 🌿 ROYAL GREEN + CREAM + GLOSSY BLACK THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@300;400;600;700&display=swap');

/* Background */
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #f7f3e9, #efe7d6);
    color: #1a1a1a;
    font-family: 'Inter', sans-serif;
}

/* Hide default UI */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #0f2f24, #123b2d);
    border-right: 2px solid #1e5a44;
}

/* Button (Royal Green + Gold accent) */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #1e5a44, #2e7d5b, #3aa17e) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    padding: 0.75rem !important;
    font-weight: 700 !important;
    border: none !important;
    width: 100% !important;
    letter-spacing: 0.05em;
    transition: 0.25s ease;
}

div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(30, 90, 68, 0.35);
}

/* HERO */
.hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
    background: radial-gradient(circle at top, #e8f5e9, #f7f3e9);
    border-bottom: 1px solid #d8d2c4;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin: 0;
    color: #1b4332;
}

.hero p {
    color: #3b3b3b;
    margin-top: 0.5rem;
}

/* Badge */
.badge {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 20px;
    background: rgba(30, 90, 68, 0.08);
    border: 1px solid #2e7d5b;
    color: #1e5a44;
    font-size: 11px;
    margin-bottom: 12px;
}

/* SECTION TITLE */
.section-title {
    font-size: 18px;
    font-weight: 700;
    margin: 25px 0 10px;
    color: #1a1a1a;
}

/* MENU CARD */
.menu-card {
    background: linear-gradient(145deg, #ffffff, #f6f1e7);
    border: 1px solid #ddd3c2;
    border-radius: 16px;
    padding: 14px 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    transition: all 0.25s ease;
}

.menu-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(30, 90, 68, 0.15);
    border-color: #2e7d5b;
}

/* TEXT */
.menu-title {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    font-weight: 600;
    color: #0f172a; /* glossy black */
}

.menu-desc {
    font-size: 12px;
    color: #444;
    margin-top: 5px;
    line-height: 1.4;
}

.menu-price {
    margin-top: 8px;
    font-weight: 700;
    color: #1e5a44;
}

/* DIVIDER */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #2e7d5b, #1e5a44, transparent);
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SAMPLE MENU DATA
# ─────────────────────────────────────────────
INDIAN_MENU = {
    "🥗 Starters": [
        ("Samosa", "🥟", "Crispy pastry filled with spiced potato", "$8"),
        ("Paneer Tikka", "🧀", "Chargrilled cottage cheese cubes", "$13"),
    ],
    "🍛 Mains": [
        ("Butter Chicken", "🍗", "Creamy tomato-based chicken curry", "$18"),
        ("Dal Makhani", "🫘", "Slow-cooked black lentils in butter sauce", "$14"),
    ],
    "🍚 Rice": [
        ("Chicken Biryani", "🍗", "Fragrant basmati rice with spices", "$20"),
    ],
}

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.title("🌿 Culinary Compass")
    cuisine = st.selectbox("Choose Cuisine", ["Indian", "Italian", "Mexican"])
    generate = st.button("✨ Generate Restaurant")

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
components.html("""
<div class="hero">
  <div class="badge">ROYAL GREEN AI STUDIO</div>
  <h1>Culinary Compass</h1>
  <p>Elegant restaurant generator with luxury taste</p>
</div>
""", height=180)

# ─────────────────────────────────────────────
# MAIN LOGIC
# ─────────────────────────────────────────────
if generate:

    with st.spinner("Crafting your royal restaurant..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    restaurant_name = response["restaurant_name"]
    items = [i.strip() for i in response["menu_items"].split(",") if i.strip()]
    random.seed(restaurant_name)

    # ── HEADER CARD
    st.markdown(f"""
    <div class="menu-card" style="text-align:center; margin-bottom:20px;">
        <div class="badge">{cuisine.upper()} KITCHEN</div>
        <h2 style="font-family:Playfair Display; font-size:30px; color:#0f172a;">
            {restaurant_name}
        </h2>
        <div class="divider"></div>
        <p style="color:#444;">
            A royal green dining experience crafted by AI
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── MENU SECTION
    st.markdown("## 🍽️ Menu")

    menu_data = INDIAN_MENU if cuisine == "Indian" else {
        "🌿 Chef Specials": [
            (item, "🍴", "Signature gourmet preparation", f"${random.randint(12, 35)}")
            for item in items
        ]
    }

    for section, dishes in menu_data.items():
        st.markdown(f"<div class='section-title'>{section}</div>", unsafe_allow_html=True)

        cols = st.columns(2)

        for i, (name, icon, desc, price) in enumerate(dishes):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="menu-card">
                    <div class="menu-title">{icon} {name}</div>
                    <div class="menu-desc">{desc}</div>
                    <div class="menu-price">{price}</div>
                </div>
                """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center; padding:4rem; color:#333;">
        🍽️ Select cuisine and generate a royal green restaurant experience
    </div>
    """, unsafe_allow_html=True)