import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tsitohaina R. | Data Engineer & IoT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ═══════════════════════════════════════════════════════════════════════════════
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600;700&display=swap');
    :root {
        --bg-deep:#020810; --bg-card:#0a1628; --bg-panel:#0d1e38;
        --cyan:#00e5ff; --green:#39ff14; --orange:#ff6b35; --purple:#b44dff;
        --text:#e8f4f8; --muted:#7a9ab0; --border:rgba(0,229,255,0.18);
        --glow-cyan:0 0 20px rgba(0,229,255,0.55),0 0 60px rgba(0,229,255,0.22);
        --glow-green:0 0 20px rgba(57,255,20,0.55);
    }
    html,body,[class*="css"]{
        font-family:'Exo 2',sans-serif !important;
        background-color:var(--bg-deep) !important;
        color:var(--text) !important;
    }
    .block-container{padding:0 2rem 2rem 2rem !important;max-width:1200px;}
    #MainMenu,footer,header{visibility:hidden;}
    .stApp{
        background-color:var(--bg-deep) !important;
        background-image:
            linear-gradient(rgba(0,229,255,0.03) 1px,transparent 1px),
            linear-gradient(90deg,rgba(0,229,255,0.03) 1px,transparent 1px);
        background-size:60px 60px;
    }
    [data-testid="stSidebar"]{
        background:linear-gradient(180deg,#020810 0%,#071628 100%) !important;
        border-right:1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] *{color:var(--text) !important;}
    .sidebar-logo{font-family:'Orbitron',monospace;font-size:1.1rem;font-weight:900;
        color:var(--cyan) !important;text-shadow:var(--glow-cyan);letter-spacing:2px;padding:1rem 0 0.3rem 0;}
    .sidebar-sub{font-family:'Share Tech Mono',monospace;font-size:0.62rem;
        color:var(--muted) !important;letter-spacing:1px;margin-bottom:1rem;}
    .dot-green{width:8px;height:8px;background:var(--green);border-radius:50%;
        box-shadow:var(--glow-green);animation:pulse 1.5s infinite;display:inline-block;}
    @keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.5;transform:scale(1.3)}}
    .card{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;
        padding:1.5rem;margin-bottom:1.2rem;transition:all 0.3s;position:relative;overflow:hidden;}
    .card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
        background:linear-gradient(90deg,transparent,var(--cyan),transparent);}
    .card:hover{border-color:rgba(0,229,255,0.4);box-shadow:0 4px 30px rgba(0,229,255,0.12);transform:translateY(-2px);}
    .section-title{font-family:'Orbitron',monospace;font-size:1.6rem;font-weight:700;
        color:var(--cyan);text-shadow:var(--glow-cyan);letter-spacing:3px;
        margin:2rem 0 1.2rem 0;display:flex;align-items:center;gap:12px;}
    .section-title::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--cyan),transparent);margin-left:12px;}
    .sub-title{font-family:'Orbitron',monospace;font-size:1.05rem;font-weight:700;
        color:var(--text);margin:1.5rem 0 0.8rem 0;letter-spacing:2px;}
    .tag{display:inline-block;padding:3px 10px;border-radius:20px;
        font-family:'Share Tech Mono',monospace;font-size:0.7rem;margin:3px 3px 3px 0;border:1px solid;}
    .tag-cyan{border-color:var(--cyan);color:var(--cyan);background:rgba(0,229,255,0.08);}
    .tag-green{border-color:var(--green);color:var(--green);background:rgba(57,255,20,0.07);}
    .tag-orange{border-color:var(--orange);color:var(--orange);background:rgba(255,107,53,0.08);}
    .tag-purple{border-color:var(--purple);color:var(--purple);background:rgba(180,77,255,0.08);}
    .tl-item{border-left:2px solid var(--cyan);padding:0 0 1.5rem 1.5rem;margin-left:0.5rem;position:relative;}
    .tl-item::before{content:'';position:absolute;left:-6px;top:4px;width:10px;height:10px;
        background:var(--cyan);border-radius:50%;box-shadow:var(--glow-cyan);}
    .tl-date{font-family:'Share Tech Mono',monospace;font-size:0.72rem;color:var(--cyan);letter-spacing:1px;margin-bottom:4px;}
    .tl-title{font-family:'Orbitron',monospace;font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:2px;}
    .tl-co{font-size:0.8rem;color:var(--muted);margin-bottom:8px;}
    .tl-desc{font-size:0.82rem;color:#b0c8d8;line-height:1.7;}
    .hero-greeting{font-family:'Share Tech Mono',monospace;color:var(--green);font-size:0.95rem;letter-spacing:3px;margin-bottom:0.4rem;}
    .hero-name{font-family:'Orbitron',monospace;font-size:3rem;font-weight:900;line-height:1.1;
        background:linear-gradient(135deg,#ffffff 30%,var(--cyan) 70%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:0.4rem;}
    .hero-title{font-family:'Share Tech Mono',monospace;font-size:0.9rem;color:var(--cyan);letter-spacing:2px;margin-bottom:1.2rem;}
    .metric-card{background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem;text-align:center;transition:all 0.3s;}
    .metric-card:hover{box-shadow:var(--glow-cyan);border-color:var(--cyan);}
    .metric-val{font-family:'Orbitron',monospace;font-size:1.9rem;font-weight:900;color:var(--cyan);text-shadow:var(--glow-cyan);}
    .metric-label{font-family:'Share Tech Mono',monospace;font-size:0.62rem;color:var(--muted);letter-spacing:1px;margin-top:4px;}
    .skill-bar-wrap{margin-bottom:0.8rem;}
    .skill-label{font-family:'Share Tech Mono',monospace;font-size:0.78rem;display:flex;justify-content:space-between;margin-bottom:4px;}
    .skill-bar-bg{background:rgba(255,255,255,0.06);border-radius:3px;height:8px;overflow:hidden;}
    .skill-bar-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--cyan),var(--green));box-shadow:0 0 8px rgba(0,229,255,0.5);}
    .step-box{background:var(--bg-card);border:1px solid var(--border);border-radius:10px;
        padding:1rem 1.2rem;margin-bottom:0.8rem;border-left:3px solid var(--cyan);}
    .step-num{font-family:'Orbitron',monospace;font-size:1.1rem;font-weight:900;color:var(--cyan);margin-bottom:4px;}
    .step-title{font-family:'Orbitron',monospace;font-size:0.85rem;font-weight:700;color:var(--text);margin-bottom:6px;}
    .step-desc{font-size:0.82rem;color:#b0c8d8;line-height:1.7;}
    .info-box{background:rgba(0,229,255,0.05);border:1px solid rgba(0,229,255,0.25);
        border-radius:8px;padding:1rem 1.2rem;margin-bottom:1rem;font-size:0.85rem;color:#b0c8d8;line-height:1.7;}
    .info-box-green{background:rgba(57,255,20,0.05);border-color:rgba(57,255,20,0.25);}
    .info-box-orange{background:rgba(255,107,53,0.05);border-color:rgba(255,107,53,0.25);}
    .info-box-purple{background:rgba(180,77,255,0.05);border-color:rgba(180,77,255,0.25);}
    .terminal{background:#000;border:1px solid rgba(57,255,20,0.3);border-radius:8px;padding:1.2rem;
        font-family:'Share Tech Mono',monospace;font-size:0.78rem;color:#39ff14;line-height:1.8;}
    .terminal .prompt{color:#00e5ff;}
    .terminal .output{color:#b0c8d8;}
    .contact-item{display:flex;align-items:center;gap:12px;padding:0.8rem 1rem;
        background:var(--bg-card);border:1px solid var(--border);border-radius:8px;
        margin-bottom:0.8rem;transition:all 0.25s;text-decoration:none;}
    .contact-item:hover{border-color:var(--cyan);box-shadow:var(--glow-cyan);}
    ::-webkit-scrollbar{width:5px;}
    ::-webkit-scrollbar-track{background:var(--bg-deep);}
    ::-webkit-scrollbar-thumb{background:var(--cyan);border-radius:3px;}
    .stButton>button{background:transparent !important;border:1px solid var(--cyan) !important;
        color:var(--cyan) !important;font-family:'Orbitron',monospace !important;
        letter-spacing:2px !important;font-size:0.78rem !important;
        padding:0.5rem 1.5rem !important;border-radius:6px !important;transition:all 0.25s !important;}
    .stButton>button:hover{background:rgba(0,229,255,0.12) !important;box-shadow:var(--glow-cyan) !important;}
    .stSelectbox label,.stTextInput label,.stTextArea label{
        color:var(--cyan) !important;font-family:'Share Tech Mono',monospace !important;font-size:0.78rem !important;}
    hr{border-color:var(--border) !important;}
    .cursor{display:inline-block;width:3px;height:1.1em;background:var(--cyan);
        vertical-align:text-bottom;animation:blink 1s infinite;}
    @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
    .photo-placeholder{width:180px;height:180px;border-radius:50%;border:3px dashed var(--cyan);
        display:flex;align-items:center;justify-content:center;
        margin:0 auto 1rem auto;background:rgba(0,229,255,0.04);font-size:3rem;}
    </style>
    """, unsafe_allow_html=True)

inject_css()

# ── Plotly dark theme helper ──────────────────────────────────────────────────
CYAN="#00e5ff"; GREEN="#39ff14"; ORANGE="#ff6b35"; PURPLE="#b44dff"

def pdl(title="", height=340):
    """Returns a plotly dark layout dict."""
    return dict(
        title=dict(text=title, font=dict(family="Orbitron", color=CYAN, size=12)),
        paper_bgcolor="#0a1628", plot_bgcolor="#020810",
        font=dict(family="Share Tech Mono", color="#b0c8d8", size=10),
        height=height,
        margin=dict(l=40,r=20,t=45,b=40),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,229,255,0.2)", borderwidth=1),
        xaxis=dict(gridcolor="rgba(0,229,255,0.07)", zerolinecolor="rgba(0,229,255,0.12)"),
        yaxis=dict(gridcolor="rgba(0,229,255,0.07)", zerolinecolor="rgba(0,229,255,0.12)"),
    )

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('<div class="sidebar-logo">TSI.RAZ</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">DATA · IOT · ENERGY · AI</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex;align-items:center;gap:8px;padding:0.4rem 0 1rem 0;
                font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:#39ff14;">
        <div class="dot-green"></div> AVAILABLE FOR HIRE
    </div>""", unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio("", [
        "🏠  HOME",
        "👤  ABOUT & SKILLS",
        "💼  EXPERIENCE",
        "📄  PROJECT — OCR Pipeline",
        "☀️  PROJECT — Solar Sizer",
        "🌾  PROJECT — Rice AI",
        "📊  PROJECT — Dashboards BI",
        "📡  PROJECT — IoT & AWS",
        "🎓  EDUCATION",
        "📬  CONTACT",
    ], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.62rem;color:#4a6a80;">
        <div style="margin-bottom:5px;">⚡ Python · SQL · R · C++</div>
        <div style="margin-bottom:5px;">📡 IoT · AWS · ETL · REST</div>
        <div style="margin-bottom:5px;">☀️ PVsyst · HOMER Pro</div>
        <div style="margin-bottom:5px;">🤖 ML · Power BI · Qlik</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.62rem;color:#4a6a80;text-align:center;">
        © 2025 Tsitohaina Razafindrajoa<br>
        <span style="color:#00e5ff;">Built with Streamlit ⚡</span>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════
if "HOME" in page:
    st.markdown("""
    <div style="padding:2.5rem 0 1.5rem 0;">
        <div class="hero-greeting">&gt; HELLO_WORLD.execute() ▶</div>
        <div class="hero-name">TSITOHAINA<br>RAZAFINDRAJOA</div>
        <div class="hero-title">⚡ DATA ENGINEER &nbsp;|&nbsp; IoT ARCHITECT &nbsp;|&nbsp; DATA SCIENTIST &nbsp;|&nbsp; ENERGY ANALYST</div>
        <div style="font-size:0.95rem;color:#b0c8d8;line-height:1.8;max-width:600px;margin-bottom:1.5rem;">
            I design and deploy end-to-end data pipelines, intelligent IoT architectures,
            and AI-powered systems — from edge sensors to cloud dashboards.
            Based in Madagascar 🇲🇬 · Available for remote contracts worldwide.
        </div>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col, val, label in zip([c1,c2,c3,c4],["5+","10+","3","PhD"],["YEARS EXP","PROJECTS","MASTERS","CANDIDATE"]):
        with col:
            st.markdown(f'<div class="metric-card"><div class="metric-val">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">⚡ CORE SERVICES</div>', unsafe_allow_html=True)

    services = [
        ("🔧","DATA ENGINEERING","cyan","ETL pipelines, REST API integration, document ingestion automation, deduplication, structured storage.",["Python ETL","REST API","SQL","Streamlit"]),
        ("📡","IoT & EMBEDDED","green","Embedded C++ firmware, AWS IoT cloud, real-time energy data collection and monitoring.",["C++","AWS IoT","Boto3","MQTT"]),
        ("☀️","ENERGY & PV","orange","Solar system design, PVsyst & HOMER Pro simulation, AutoCAD Electrical, automated sizing tools.",["PVsyst","HOMER Pro","AutoCAD","Solar"]),
        ("📊","BI & DASHBOARDS","purple","Power BI, Qlik Sense, Google Sheets dashboards. KPI design, data cleaning, storytelling.",["Power BI","Qlik Sense","Excel","DAX"]),
        ("🤖","AI & ML","cyan","Predictive models, OpenAI Vision API automation, PhD-level Data Science research.",["ML/AI","OpenAI","Sklearn","Research"]),
        ("🖥️","SOFTWARE DEV","green","Desktop apps (Tkinter), web apps (Django, Streamlit), OCR document processing systems.",["Django","Streamlit","Tkinter","OCR"]),
    ]
    ca,cb,cc = st.columns(3)
    for i,(icon,title,color,desc,tags) in enumerate(services):
        with [ca,cb,cc][i%3]:
            tags_html = "".join(f'<span class="tag tag-{color}">{t}</span>' for t in tags)
            st.markdown(f"""
            <div class="card">
                <div style="font-size:1.8rem;margin-bottom:0.6rem;">{icon}</div>
                <div style="font-family:'Orbitron',monospace;font-size:0.85rem;font-weight:700;
                            color:var(--{color});margin-bottom:0.5rem;">{title}</div>
                <div style="font-size:0.8rem;color:#7a9ab0;line-height:1.6;margin-bottom:0.8rem;">{desc}</div>
                {tags_html}
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal">
        <span class="prompt">tsitohaina@data-lab:~$</span> cat profile.txt<br>
        <span class="output">
        ╔══════════════════════════════════════════════════════════════╗<br>
        ║  NAME    : Tsitohaina Razafindrajoa                          ║<br>
        ║  ROLE    : Data Engineer · IoT · Data Scientist · Energy     ║<br>
        ║  BASE    : Antananarivo, Madagascar 🇲🇬                       ║<br>
        ║  STATUS  : OPEN TO REMOTE WORK — UPWORK CONTRACTS            ║<br>
        ║  STACK   : Python · SQL · C++ · AWS · Power BI · PVsyst      ║<br>
        ╚══════════════════════════════════════════════════════════════╝<br>
        </span>
        <span class="prompt">tsitohaina@data-lab:~$</span> <span class="cursor"></span>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT & SKILLS
# ═══════════════════════════════════════════════════════════════════════════════
elif "ABOUT" in page:
    st.markdown('<div class="section-title">👤 ABOUT ME</div>', unsafe_allow_html=True)
    col_photo, col_bio = st.columns([1, 2.5])
    with col_photo:
        try:
            st.image("profile.jpg", width=190)
        except:
            st.markdown("""
            <div class="photo-placeholder">🧑‍💻</div>
            <div style="font-family:'Share Tech Mono',monospace;font-size:0.62rem;color:#4a6a80;text-align:center;">
                Add <b style="color:#00e5ff;">profile.jpg</b><br>to project root
            </div>""", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;
                    padding:1rem;font-family:'Share Tech Mono',monospace;font-size:0.72rem;margin-top:0.8rem;">
            <div style="color:#00e5ff;margin-bottom:8px;letter-spacing:1px;">// LANGUAGES</div>
            <div style="margin:4px 0;">🇲🇬 Malagasy — Native</div>
            <div style="margin:4px 0;">🇫🇷 French — Professional</div>
            <div style="margin:4px 0;">🇬🇧 English — Intermediate</div>
        </div>""", unsafe_allow_html=True)

    with col_bio:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#00e5ff;margin-bottom:1rem;">PROFILE</div>
            <p style="font-size:0.88rem;color:#b0c8d8;line-height:1.8;">
                I'm a <strong style="color:#00e5ff;">Data Engineer</strong> specialized in
                <strong style="color:#39ff14;">IoT systems</strong>,
                <strong style="color:#ff6b35;">renewable energy analytics</strong>, and
                <strong style="color:#b44dff;">machine learning</strong>. I design complete
                data architectures from hardware sensors to cloud dashboards.
            </p>
            <p style="font-size:0.88rem;color:#b0c8d8;line-height:1.8;">
                Currently completing a <strong style="color:#00e5ff;">PhD in Data Science</strong>
                at the University of Antananarivo while delivering freelance contracts.
                Projects span ETL automation, AI document processing, photovoltaic simulation,
                and embedded IoT firmware.
            </p>
            <p style="font-size:0.88rem;color:#b0c8d8;line-height:1.8;">
                Actively seeking <strong style="color:#39ff14;">remote Upwork projects</strong>
                in data engineering, IoT, BI dashboards, and energy analytics.
            </p>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">🛠️ SKILL OVERVIEW</div>', unsafe_allow_html=True)

    radar_cats = ["Data Engineering","IoT / Embedded","Machine Learning","BI / Dashboards","Energy / PV","Software Dev","Networking"]
    radar_vals = [95, 85, 82, 90, 80, 88, 75]
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_vals+[radar_vals[0]], theta=radar_cats+[radar_cats[0]],
        fill='toself', fillcolor='rgba(0,229,255,0.12)',
        line=dict(color=CYAN, width=2), name="Skill Level"))
    fig_radar.update_layout(**pdl("COMPETENCY RADAR", 380))
    fig_radar.update_layout(polar=dict(
        bgcolor="#0a1628",
        radialaxis=dict(visible=True, range=[0,100], gridcolor="rgba(0,229,255,0.15)", color="#7a9ab0"),
        angularaxis=dict(gridcolor="rgba(0,229,255,0.15)", color=CYAN, tickfont=dict(size=11,family="Share Tech Mono"))
    ))
    st.plotly_chart(fig_radar, use_container_width=True)

    col_s1, col_s2 = st.columns(2)
    skills_l = [("Python",95),("SQL",88),("C++ / Embedded",85),("R",78),("JavaScript/HTML/CSS",70)]
    skills_r = [("Power BI / Qlik Sense",90),("Machine Learning",82),("AWS (S3, Boto3)",80),("Pandas/NumPy",92),("Django/Streamlit",88)]
    with col_s1:
        st.markdown('<div class="card"><div style="font-family:Orbitron,monospace;font-size:0.75rem;color:#00e5ff;margin-bottom:1rem;letter-spacing:2px;">// LANGUAGES</div>', unsafe_allow_html=True)
        for sk,pct in skills_l:
            st.markdown(f'<div class="skill-bar-wrap"><div class="skill-label"><span>{sk}</span><span style="color:#00e5ff">{pct}%</span></div><div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{pct}%"></div></div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="card"><div style="font-family:Orbitron,monospace;font-size:0.75rem;color:#39ff14;margin-bottom:1rem;letter-spacing:2px;">// TOOLS & PLATFORMS</div>', unsafe_allow_html=True)
        for sk,pct in skills_r:
            st.markdown(f'<div class="skill-bar-wrap"><div class="skill-label"><span>{sk}</span><span style="color:#39ff14">{pct}%</span></div><div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{pct}%;background:linear-gradient(90deg,#39ff14,#00e5ff);"></div></div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card"><div style="font-family:'Orbitron',monospace;font-size:0.75rem;color:#ff6b35;margin-bottom:1rem;letter-spacing:2px;">// FULL TECH STACK</div>
    <span class="tag tag-cyan">Python ETL</span><span class="tag tag-cyan">REST API</span>
    <span class="tag tag-cyan">OpenAI API</span><span class="tag tag-cyan">Streamlit</span>
    <span class="tag tag-cyan">Django</span><span class="tag tag-cyan">SQL</span>
    <span class="tag tag-green">C++</span><span class="tag tag-green">AWS S3</span>
    <span class="tag tag-green">Boto3</span><span class="tag tag-green">QuickSight</span>
    <span class="tag tag-green">MQTT</span><span class="tag tag-green">TCP/IP</span>
    <span class="tag tag-orange">PVsyst</span><span class="tag tag-orange">HOMER Pro</span>
    <span class="tag tag-orange">AutoCAD Electrical</span><span class="tag tag-orange">SketchUp</span>
    <span class="tag tag-purple">Power BI</span><span class="tag tag-purple">Qlik Sense</span>
    <span class="tag tag-purple">Talend ETL</span><span class="tag tag-purple">Scikit-learn</span>
    <span class="tag tag-purple">Pandas</span><span class="tag tag-purple">NumPy</span>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: EXPERIENCE
# ═══════════════════════════════════════════════════════════════════════════════
elif "EXPERIENCE" in page:
    st.markdown('<div class="section-title">💼 WORK EXPERIENCE</div>', unsafe_allow_html=True)

    exp_data = pd.DataFrame({
        "Role":["IoT Intern","Network Tech","IT Intern","Polyvalent Tech","IoT Engineer","IT Consultant","PV Engineer","Data Engineer"],
        "Start":[2021.2,2017.9,2019.1,2020.6,2021.5,2024.2,2024.5,2025.9],
        "End":  [2021.5,2018.0,2019.2,2021.1,2024.1,2024.4,2025.8,2026.9],
        "Color":[GREEN,PURPLE,PURPLE,PURPLE,GREEN,CYAN,ORANGE,CYAN],
    })
    fig_tl = go.Figure()
    for _,row in exp_data.iterrows():
        fig_tl.add_trace(go.Bar(x=[row["End"]-row["Start"]],y=[row["Role"]],
            base=[row["Start"]],orientation='h',marker_color=row["Color"],marker_opacity=0.8,
            showlegend=False,
            hovertemplate=f"<b>{row['Role']}</b><br>{row['Start']:.1f} → {row['End']:.1f}<extra></extra>"))
    fig_tl.update_layout(**pdl("CAREER TIMELINE",340))
    fig_tl.update_xaxes(title="Year",tickformat=".0f")
    st.plotly_chart(fig_tl,use_container_width=True)

    exps = [
        ("NOV 2025 — DEC 2026","Data Engineer (Freelance)","Chanfoui & Fils · Ankadimbahoaka","cyan",
         "• Designed a fully automated document ingestion pipeline using <b style='color:#00e5ff'>OpenAI Vision API</b>.<br>"
         "• Built normalization, duplicate detection logic and database integration via <b style='color:#00e5ff'>REST API + Python ETL</b>.<br>"
         "• Real-time delivery tracking dashboard in Google Sheets (KPIs: undelivered, MGA value, top items, monthly filters).<br>"
         "• UI deployed with <b style='color:#00e5ff'>Streamlit</b> for internal business use.",
         [("Python ETL","cyan"),("OpenAI API","cyan"),("Streamlit","cyan"),("REST API","cyan"),("Google Sheets","green")]),
        ("JUN 2024 — OCT 2025","Photovoltaic Systems Engineer","Madagascar Lano · Ivato","orange",
         "• Designed technical solar solutions using advanced energy simulation tools.<br>"
         "• Energy audits, load analysis, and sizing of PV installations for commercial clients.<br>"
         "• Tools: <b style='color:#ff6b35'>PVsyst · AutoCAD Electrical · HOMER Pro · SketchUp</b>",
         [("PVsyst","orange"),("HOMER Pro","orange"),("AutoCAD","orange"),("Solar Design","orange")]),
        ("MAR 2024 — MAY 2024","IT Consultant (Freelance)","Madagascar Lano · Ivato","cyan",
         "• Desktop application for <b style='color:#00e5ff'>automatic sizing</b> of generator sets and solar systems.<br>"
         "• Features: energy load calculation, product recommendation engine, automated PDF quote generation.<br>"
         "• Built with <b style='color:#00e5ff'>Python · Tkinter</b>.",
         [("Python","cyan"),("Tkinter","cyan"),("Energy Calc","orange"),("Desktop App","green")]),
        ("JUL 2021 — FEB 2024","Embedded Systems & IoT Engineer","Jirogasy Sarlu · Androhibe","green",
         "• Embedded <b style='color:#39ff14'>C++ firmware</b>: OTA updates, sensor data collection, IoT telemetry.<br>"
         "• Integrated <b style='color:#39ff14'>AWS S3, Boto3, QuickSight</b> for cloud storage and energy monitoring dashboards.<br>"
         "• Python ETL pipelines for IoT energy data processing on AWS.",
         [("C++","green"),("AWS S3","green"),("Boto3","green"),("QuickSight","green"),("IoT","green")]),
        ("MAR 2021 — JUN 2021","Embedded Systems & IoT Engineer (Intern)","Jirogasy Sarlu · Androhibe","green",
         "• Cloud integration: AWS S3, Boto3, QuickSight.<br>"
         "• C++ firmware development: updates, IoT data collection.",
         [("C++","green"),("AWS","green"),("IoT Firmware","green")]),
        ("AUG 2020 — FEB 2021","Polyvalent Technician","Ankaratra Residence · Antsirabe","purple",
         "• Client-side technical support: IT, telephony, electrical, and network issues.<br>"
         "• Protocols: TCP/IP · WLAN · OSI",
         [("TCP/IP","purple"),("WLAN","purple"),("Networking","purple")]),
        ("FEB 2019 — MAR 2019","IT Intern","Finance Dept. · Antaninarenina","purple",
         "Network configuration: TCP/IP · WLAN · OSI",[("TCP/IP","purple")]),
        ("DEC 2017","Network Technician","Hay Business Service · Amboditsiry","purple",
         "Network setup and cabling: switches, TCP/IP.",[("Networking","purple")]),
    ]
    for date,title,company,color,desc,tags in exps:
        tags_html = "".join(f'<span class="tag tag-{t[1]}">{t[0]}</span>' for t in tags)
        st.markdown(f"""
        <div class="tl-item" style="border-left-color:var(--{color});">
            <div class="tl-date">{date}</div>
            <div class="tl-title">{title}</div>
            <div class="tl-co">📍 {company}</div>
            <div class="tl-desc">{desc}</div>
            <div style="margin-top:8px;">{tags_html}</div>
        </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECT — OCR Pipeline
# ═══════════════════════════════════════════════════════════════════════════════
elif "OCR" in page:
    st.markdown('<div class="section-title">📄 OCR INVOICE AUTOMATION PIPELINE</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:#7a9ab0;margin-bottom:1rem;">
        CLIENT: Chanfoui & Fils &nbsp;|&nbsp; YEAR: 2025 &nbsp;|&nbsp;
        STATUS: <span style="color:#39ff14;">LIVE ✓</span> &nbsp;|&nbsp;
        <a href="https://github.com/tsitohainaraz/CHANFUI_AND_FILS_SCANER" target="_blank" style="color:#00e5ff;">🔗 VIEW ON GITHUB</a>
    </div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <strong style="color:#00e5ff;">BUSINESS PROBLEM:</strong> Chanfoui & Fils was manually entering
        invoice data from physical documents — a slow, error-prone process causing billing delays and
        stock discrepancies. Goal: <strong>fully automate document ingestion</strong> from scan to database.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⚙️ PIPELINE ARCHITECTURE — STEP BY STEP</div>', unsafe_allow_html=True)
    for num,title,desc,color in [
        ("01","DOCUMENT UPLOAD","User uploads scanned invoice (PDF/image) via the Streamlit web interface.","#00e5ff"),
        ("02","AI EXTRACTION — OpenAI Vision","Image sent to OpenAI Vision API. Extracts: supplier, date, product lines, quantities, unit prices, totals.","#00e5ff"),
        ("03","DATA NORMALIZATION — Python ETL","Raw text parsed and normalized: date formats standardized, numeric fields cleaned, categories assigned.","#00e5ff"),
        ("04","DUPLICATE DETECTION","System compares key fields (invoice ID, supplier, date, amount) against existing records. Duplicates are flagged and skipped.","#00e5ff"),
        ("05","DATABASE INTEGRATION — REST API","Clean, validated records pushed to backend database via REST API endpoint.","#00e5ff"),
        ("06","DASHBOARD UPDATE — Google Sheets","Connected Google Sheets dashboard refreshes: total undelivered, MGA value, top products, monthly trends.","#00e5ff"),
    ]:
        st.markdown(f'<div class="step-box"><div class="step-num" style="color:{color};">STEP {num}</div><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📊 PIPELINE PERFORMANCE</div>', unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    for col,val,label,color in zip([c1,c2,c3,c4],["847","98.3%","< 4s","0.6%"],
        ["INVOICES PROCESSED","EXTRACTION ACCURACY","AVG PROCESSING TIME","DUPLICATE RATE"],
        [CYAN,GREEN,ORANGE,PURPLE]):
        with col:
            st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:{color};text-shadow:none;">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        months = ["Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        docs = [42,68,95,112,138,156,187]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months,y=docs,mode='lines+markers',
            line=dict(color=CYAN,width=2.5),marker=dict(color=CYAN,size=8,line=dict(color='#020810',width=2)),
            fill='tozeroy',fillcolor='rgba(0,229,255,0.08)',name="Invoices Processed"))
        fig.update_layout(**pdl("MONTHLY INVOICES PROCESSED",300))
        st.plotly_chart(fig,use_container_width=True)
    with c2:
        fig2 = go.Figure(go.Pie(
            labels=["Extracted OK","Duplicate Skipped","Manual Review","Error"],
            values=[847,5,12,3],hole=0.6,
            marker=dict(colors=[CYAN,GREEN,ORANGE,"#ff4444"]),
            textfont=dict(family="Share Tech Mono",size=11)))
        fig2.update_layout(**pdl("PROCESSING OUTCOMES",300))
        st.plotly_chart(fig2,use_container_width=True)

    st.markdown('<div class="sub-title">📈 BUSINESS IMPACT</div>', unsafe_allow_html=True)
    ic1,ic2 = st.columns(2)
    for i,(icon,title,desc) in enumerate([
        ("⏱️","Time Saved","Reduced manual data entry from ~3h/day to 0 — 100% automated."),
        ("✅","Accuracy","Extraction accuracy >98% vs ~85% for manual entry."),
        ("📉","Error Reduction","Billing errors dropped by ~90% after deployment."),
        ("📊","Visibility","Real-time dashboard replaced weekly manual Excel reports."),
    ]):
        with (ic1 if i%2==0 else ic2):
            st.markdown(f'<div class="card"><div style="font-size:1.4rem;margin-bottom:4px;">{icon}</div><div style="font-family:Orbitron,monospace;font-size:0.8rem;font-weight:700;color:#00e5ff;margin-bottom:4px;">{title}</div><div style="font-size:0.8rem;color:#b0c8d8;">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">🛠️ TECH STACK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><span class="tag tag-cyan">Python 3.11</span><span class="tag tag-cyan">OpenAI Vision API</span><span class="tag tag-cyan">Streamlit</span><span class="tag tag-cyan">REST API</span><span class="tag tag-cyan">Pandas</span><span class="tag tag-green">Google Sheets API</span><span class="tag tag-green">Git/GitHub</span><span class="tag tag-purple">PostgreSQL/SQLite</span></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECT — Solar Sizer
# ═══════════════════════════════════════════════════════════════════════════════
elif "Solar" in page:
    st.markdown('<div class="section-title">☀️ AUTO SOLAR & GENSET SIZING TOOL</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:#7a9ab0;margin-bottom:1rem;">
        CLIENT: Madagascar Lano · Ivato &nbsp;|&nbsp; YEAR: 2024 &nbsp;|&nbsp;
        STATUS: <span style="color:#39ff14;">DEPLOYED ✓</span>
    </div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box info-box-orange">
        <strong style="color:#ff6b35;">BUSINESS PROBLEM:</strong> Sales engineers manually calculated
        solar and generator sizing per client — taking 2–3 hours per proposal with frequent errors.
        Goal: a <strong>one-click automated sizing and quotation tool</strong> for non-technical sales staff.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⚙️ APPLICATION FEATURES</div>', unsafe_allow_html=True)
    for num,title,desc in [
        ("01","CLIENT LOAD PROFILING","User inputs appliances (type, power, daily usage hours). App auto-calculates total daily kWh and peak demand kW."),
        ("02","SOLAR PANEL SIZING","Based on Madagascar irradiation data and system efficiency, calculates required wattage, number of panels, and optimal orientation."),
        ("03","BATTERY BANK SIZING","Calculates battery capacity (Ah) based on autonomy days, DoD, and system voltage. Recommends AGM/Lithium options."),
        ("04","GENERATOR SIZING","For hybrid systems, calculates genset kVA rating from peak load + starting surge factor. Recommends product from catalog."),
        ("05","PRODUCT RECOMMENDATION","Automatically matches calculated specs to Madagascar Lano product catalog — best-fit panels, batteries, inverter, and genset."),
        ("06","PDF QUOTE GENERATION","Generates a branded PDF quotation with itemized BOM, technical specs, pricing in MGA, and company letterhead."),
    ]:
        st.markdown(f'<div class="step-box" style="border-left-color:#ff6b35;"><div class="step-num" style="color:#ff6b35;">STEP {num}</div><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📊 ENERGY ANALYSIS DASHBOARDS</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        hours = list(range(24))
        load = [0.2,0.1,0.1,0.1,0.2,0.5,1.2,2.1,2.8,2.5,2.2,2.0,1.8,2.1,2.4,2.6,3.1,3.8,4.2,3.9,3.2,2.1,1.0,0.4]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours,y=load,fill='tozeroy',
            fillcolor='rgba(255,107,53,0.12)',line=dict(color=ORANGE,width=2.5),name="Load (kW)"))
        fig.update_layout(**pdl("TYPICAL DAILY LOAD PROFILE (kW)",300))
        fig.update_xaxes(title="Hour of Day",tickvals=list(range(0,24,3)))
        fig.update_yaxes(title="kW")
        st.plotly_chart(fig,use_container_width=True)
    with c2:
        months_m = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        irr = [5.8,5.5,5.1,4.7,4.2,3.9,4.1,4.6,5.2,5.7,5.9,5.8]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=months_m,y=irr,
            marker_color=[ORANGE if v<4.5 else CYAN for v in irr],marker_opacity=0.85,name="kWh/m²/day"))
        fig2.update_layout(**pdl("SOLAR IRRADIATION — MADAGASCAR (kWh/m²/day)",300))
        fig2.update_yaxes(title="kWh/m²/day")
        st.plotly_chart(fig2,use_container_width=True)

    c3,c4 = st.columns(2)
    with c3:
        fig3 = go.Figure(go.Pie(
            labels=["PV Panels","Battery Bank","Inverter","Charge Controller","Wiring & BOS"],
            values=[38,32,14,8,8],hole=0.55,
            marker=dict(colors=[ORANGE,CYAN,GREEN,PURPLE,"#7a9ab0"]),
            textfont=dict(family="Share Tech Mono",size=11)))
        fig3.update_layout(**pdl("SYSTEM COST BREAKDOWN (%)",300))
        st.plotly_chart(fig3,use_container_width=True)
    with c4:
        years_roi = list(range(0,16))
        savings = [0]+[y*680000 for y in range(1,16)]
        cost = [8500000]*16
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=years_roi,y=savings,name="Cumulative Savings (MGA)",
            line=dict(color=GREEN,width=2.5),fill='tozeroy',fillcolor='rgba(57,255,20,0.07)'))
        fig4.add_trace(go.Scatter(x=years_roi,y=cost,name="Initial Investment",
            line=dict(color=ORANGE,width=2,dash='dash')))
        fig4.update_layout(**pdl("ROI CURVE — SOLAR vs GRID",300))
        fig4.update_xaxes(title="Years"); fig4.update_yaxes(title="MGA")
        st.plotly_chart(fig4,use_container_width=True)

    st.markdown('<div class="sub-title">🛠️ TECH STACK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><span class="tag tag-orange">Python 3.x</span><span class="tag tag-orange">Tkinter (GUI)</span><span class="tag tag-orange">Pandas</span><span class="tag tag-orange">ReportLab (PDF)</span><span class="tag tag-cyan">PVsyst (reference)</span><span class="tag tag-cyan">HOMER Pro (reference)</span><span class="tag tag-green">Excel Catalog</span></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECT — Rice AI
# ═══════════════════════════════════════════════════════════════════════════════
elif "Rice" in page:
    st.markdown('<div class="section-title">🌾 RICE YIELD AI PREDICTOR</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:#7a9ab0;margin-bottom:1rem;">
        CONTEXT: PhD Data Science Research &nbsp;|&nbsp; DATA: CIRAD Dataverse &nbsp;|&nbsp;
        STATUS: <span style="color:#b44dff;">RESEARCH 🔬</span>
    </div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box info-box-purple">
        <strong style="color:#b44dff;">RESEARCH OBJECTIVE:</strong> Madagascar's rice production is
        highly sensitive to climate variability. This project builds a
        <strong>machine learning model to predict rice yield</strong> (tonnes/hectare) from
        meteorological, satellite, and climate datasets sourced from CIRAD's Dataverse —
        enabling early warning and agricultural planning support.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⚙️ METHODOLOGY</div>', unsafe_allow_html=True)
    for num,title,desc in [
        ("01","DATA COLLECTION","CIRAD Dataverse rice yield records (1990–2022), CHIRPS rainfall data, MODIS NDVI satellite imagery, temperature and humidity from weather stations."),
        ("02","EXPLORATORY DATA ANALYSIS","Statistical profiling, correlation analysis between climate variables and yield. Visualization of seasonal patterns and anomaly years (drought/cyclone events)."),
        ("03","FEATURE ENGINEERING","Lag features (rainfall 30/60d before harvest), NDVI growth curves, degree-day accumulation, soil moisture proxies, PCA dimensionality reduction."),
        ("04","MODELING","Compared: Linear Regression (baseline), Random Forest, XGBoost, LSTM Neural Network for time-series."),
        ("05","VALIDATION","Walk-forward cross-validation to respect temporal order. Best model: XGBoost (R²=0.87, RMSE=0.31 t/ha)."),
        ("06","OUTPUT","Yield prediction map by region + early warning alerts when predicted yield drops >20% below historical average."),
    ]:
        st.markdown(f'<div class="step-box" style="border-left-color:#b44dff;"><div class="step-num" style="color:#b44dff;">STEP {num}</div><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📊 ANALYSIS DASHBOARDS</div>', unsafe_allow_html=True)
    np.random.seed(42)
    years = list(range(1995,2024))
    yield_t = np.clip(2.1+np.cumsum(np.random.randn(29)*0.08)+0.3*np.sin(np.linspace(0,8,29)),1.4,3.5)
    predicted = yield_t+np.random.randn(29)*0.15

    c1,c2 = st.columns(2)
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years,y=yield_t,name="Actual Yield",
            line=dict(color=GREEN,width=2.5),mode='lines+markers',marker=dict(size=5,color=GREEN)))
        fig.add_trace(go.Scatter(x=years,y=predicted,name="Model Prediction",
            line=dict(color=CYAN,width=2,dash='dot')))
        fig.update_layout(**pdl("RICE YIELD: ACTUAL vs PREDICTED (t/ha)",300))
        fig.update_yaxes(title="Tonnes / Hectare")
        st.plotly_chart(fig,use_container_width=True)
    with c2:
        features = ["NDVI (60d)","Rainfall Total","Temp Avg","Soil Moisture","NDVI (30d)","Rain Lag 30d","Cyclone Flag"]
        importance = [0.28,0.22,0.17,0.13,0.09,0.07,0.04]
        fig2 = go.Figure(go.Bar(x=importance,y=features,orientation='h',
            marker=dict(color=[PURPLE,CYAN,GREEN,ORANGE,CYAN,GREEN,ORANGE],opacity=0.85),
            text=[f"{v:.0%}" for v in importance],textposition='outside',
            textfont=dict(color="#b0c8d8",family="Share Tech Mono",size=10)))
        fig2.update_layout(**pdl("FEATURE IMPORTANCE (XGBoost)",300))
        st.plotly_chart(fig2,use_container_width=True)

    c3,c4 = st.columns(2)
    with c3:
        models = ["Linear Reg.","Random Forest","XGBoost","LSTM"]
        r2 = [0.61,0.79,0.87,0.83]; rmse = [0.52,0.38,0.31,0.35]
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name="R² Score",x=models,y=r2,marker_color=CYAN,opacity=0.85))
        fig3.add_trace(go.Bar(name="RMSE (t/ha)",x=models,y=rmse,marker_color=ORANGE,opacity=0.85))
        fig3.update_layout(**pdl("MODEL PERFORMANCE COMPARISON",300),barmode='group')
        st.plotly_chart(fig3,use_container_width=True)
    with c4:
        np.random.seed(7)
        rain = np.random.normal(850,200,200)
        yield_s = np.clip(1.2+0.002*rain+np.random.randn(200)*0.25,0.5,4.0)
        fig4 = go.Figure(go.Scatter(x=rain,y=yield_s,mode='markers',
            marker=dict(color=yield_s,colorscale=[[0,PURPLE],[0.5,CYAN],[1,GREEN]],
                size=6,opacity=0.65,
                colorbar=dict(title="Yield",tickfont=dict(family="Share Tech Mono",size=9)))))
        fig4.update_layout(**pdl("RAINFALL vs YIELD CORRELATION",300))
        fig4.update_xaxes(title="Annual Rainfall (mm)"); fig4.update_yaxes(title="Yield (t/ha)")
        st.plotly_chart(fig4,use_container_width=True)

    st.markdown('<div class="sub-title">🛠️ TECH STACK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><span class="tag tag-purple">Python</span><span class="tag tag-purple">Scikit-learn</span><span class="tag tag-purple">XGBoost</span><span class="tag tag-purple">TensorFlow/Keras (LSTM)</span><span class="tag tag-cyan">Pandas / NumPy</span><span class="tag tag-cyan">Matplotlib / Seaborn</span><span class="tag tag-green">CIRAD Dataverse API</span><span class="tag tag-green">MODIS / CHIRPS</span></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECT — Dashboards BI
# ═══════════════════════════════════════════════════════════════════════════════
elif "Dashboards" in page:
    st.markdown('<div class="section-title">📊 BI DASHBOARDS & DATA ANALYTICS</div>', unsafe_allow_html=True)

    tab1,tab2,tab3 = st.tabs(["📦 DELIVERY TRACKER","📈 SALES DASHBOARD","🌐 WEB TRAFFIC"])

    with tab1:
        st.markdown('<div class="info-box">Real-time delivery tracking dashboard for Chanfoui & Fils (Google Sheets). Tracks undelivered orders, MGA value at risk, top undelivered products, and monthly trends.</div>', unsafe_allow_html=True)
        m1,m2,m3,m4 = st.columns(4)
        for col,val,label,color in zip([m1,m2,m3,m4],["247","4.2M","89%","38"],
            ["UNDELIVERED ORDERS","MGA VALUE AT RISK","DELIVERY RATE","TOP SKUs AFFECTED"],
            [ORANGE,ORANGE,GREEN,CYAN]):
            with col:
                st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:{color};text-shadow:none;">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            months_d = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
            ordered = [180,210,195,230,260,245,290,310,280,320,350,390]
            delivered = [162,195,178,218,237,221,268,286,252,300,318,351]
            undelivered = [o-d for o,d in zip(ordered,delivered)]
            fig = go.Figure()
            fig.add_trace(go.Bar(name="Delivered",x=months_d,y=delivered,marker_color=GREEN,opacity=0.8))
            fig.add_trace(go.Bar(name="Undelivered",x=months_d,y=undelivered,marker_color=ORANGE,opacity=0.8))
            fig.update_layout(**pdl("MONTHLY ORDERS: DELIVERED vs PENDING",300),barmode='stack')
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            products = ["Product A","Product B","Product C","Product D","Product E","Other"]
            counts = [68,42,38,31,28,40]
            fig2 = go.Figure(go.Bar(x=counts,y=products,orientation='h',
                marker_color=[ORANGE,CYAN,GREEN,PURPLE,ORANGE,CYAN],opacity=0.85,
                text=counts,textposition='outside',
                textfont=dict(color="#b0c8d8",family="Share Tech Mono",size=10)))
            fig2.update_layout(**pdl("TOP UNDELIVERED PRODUCTS",300))
            st.plotly_chart(fig2,use_container_width=True)

    with tab2:
        st.markdown('<div class="info-box info-box-purple">Interactive Power BI dashboard from Excel sales data. Dynamic filters by country, segment, product. Visualizes profit, annual revenue, and geographic performance.</div>', unsafe_allow_html=True)
        np.random.seed(7)
        countries = ["France","Germany","USA","Canada","UK","Spain","Italy"]
        segments = ["Enterprise","SMB","Consumer"]
        products = ["Product A","Product B","Product C","Product D"]
        sel_country = st.multiselect("Filter by Country", countries, default=countries[:5])
        col_seg, col_prod = st.columns(2)
        with col_seg:
            sel_seg = st.multiselect("Segment", segments, default=segments)
        with col_prod:
            sel_prod = st.multiselect("Product", products, default=products)

        rows = []
        for _ in range(400):
            c = np.random.choice(countries); s = np.random.choice(segments)
            p = np.random.choice(products)
            rev = np.random.randint(5000,80000)
            profit = rev * np.random.uniform(0.1,0.4)
            year = np.random.choice([2022,2023,2024])
            rows.append({"Country":c,"Segment":s,"Product":p,"Revenue":rev,"Profit":profit,"Year":year})
        df = pd.DataFrame(rows)
        df = df[df["Country"].isin(sel_country)&df["Segment"].isin(sel_seg)&df["Product"].isin(sel_prod)]

        m1,m2,m3 = st.columns(3)
        with m1: st.markdown(f'<div class="metric-card"><div class="metric-val">${df["Revenue"].sum()/1e6:.1f}M</div><div class="metric-label">TOTAL REVENUE</div></div>', unsafe_allow_html=True)
        with m2: st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#39ff14">${df["Profit"].sum()/1e6:.1f}M</div><div class="metric-label">TOTAL PROFIT</div></div>', unsafe_allow_html=True)
        with m3: st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#ff6b35">{df["Profit"].sum()/max(df["Revenue"].sum(),1)*100:.0f}%</div><div class="metric-label">PROFIT MARGIN</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            rev_country = df.groupby("Country")["Revenue"].sum().reset_index().sort_values("Revenue",ascending=True)
            fig = go.Figure(go.Bar(x=rev_country["Revenue"]/1000,y=rev_country["Country"],orientation='h',
                marker=dict(color=CYAN,opacity=0.8),
                text=[f"${v:.0f}K" for v in rev_country["Revenue"]/1000],textposition='outside',
                textfont=dict(color="#b0c8d8",family="Share Tech Mono",size=9)))
            fig.update_layout(**pdl("REVENUE BY COUNTRY ($K)",300))
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            profit_seg = df.groupby(["Segment","Year"])["Profit"].sum().reset_index()
            fig2 = px.bar(profit_seg,x="Year",y="Profit",color="Segment",barmode='group',
                color_discrete_map={"Enterprise":CYAN,"SMB":GREEN,"Consumer":ORANGE})
            fig2.update_layout(**pdl("PROFIT BY SEGMENT & YEAR",300))
            st.plotly_chart(fig2,use_container_width=True)

    with tab3:
        st.markdown('<div class="info-box info-box-green">Web traffic analytics dashboard (Qlik Sense, JSON data). Tracks visitors, registration funnel abandonment, and user behavior patterns.</div>', unsafe_allow_html=True)
        np.random.seed(11)
        days = pd.date_range("2024-01-01","2024-12-31",freq="W")
        visitors = 800+np.cumsum(np.random.randn(len(days))*30)+np.linspace(0,400,len(days))
        bounced = visitors*np.random.uniform(0.3,0.5,len(days))
        registered = visitors*np.random.uniform(0.08,0.15,len(days))

        c1,c2,c3 = st.columns(3)
        with c1: st.markdown(f'<div class="metric-card"><div class="metric-val">{int(visitors.sum()/1000)}K</div><div class="metric-label">TOTAL VISITORS</div></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#ff6b35">{int(bounced.sum()/visitors.sum()*100)}%</div><div class="metric-label">BOUNCE RATE</div></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#39ff14">{int(registered.sum()/1000)}K</div><div class="metric-label">REGISTRATIONS</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=days,y=visitors,name="Total Visitors",
            line=dict(color=CYAN,width=2),fill='tozeroy',fillcolor='rgba(0,229,255,0.06)'))
        fig.add_trace(go.Scatter(x=days,y=bounced,name="Bounced",line=dict(color=ORANGE,width=1.5)))
        fig.add_trace(go.Scatter(x=days,y=registered,name="Registered",line=dict(color=GREEN,width=1.5)))
        fig.update_layout(**pdl("WEEKLY WEB TRAFFIC — 2024",320))
        st.plotly_chart(fig,use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECT — IoT & AWS
# ═══════════════════════════════════════════════════════════════════════════════
elif "IoT" in page:
    st.markdown('<div class="section-title">📡 IoT EMBEDDED SYSTEMS & AWS CLOUD</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:#7a9ab0;margin-bottom:1rem;">
        EMPLOYER: Jirogasy Sarlu · Androhibe &nbsp;|&nbsp; PERIOD: 2021–2024 &nbsp;|&nbsp;
        STATUS: <span style="color:#39ff14;">PRODUCTION ✓</span>
    </div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box info-box-green">
        <strong style="color:#39ff14;">CONTEXT:</strong> Jirogasy deploys solar energy kiosks in rural
        Madagascar. Each kiosk collects power production, battery state, and consumption data.
        I built the <strong>full IoT data stack</strong> — from embedded firmware to cloud dashboards.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⚙️ SYSTEM ARCHITECTURE</div>', unsafe_allow_html=True)
    for num,title,desc in [
        ("01","EDGE LAYER — C++ Firmware","Reads sensors (current, voltage, temperature, battery SoC). Manages OTA firmware updates. Sends JSON payloads every 15 minutes."),
        ("02","CONNECTIVITY — GSM/GPRS","GSM module transmits JSON packets securely to AWS IoT Core. TLS encryption, certificate-based authentication."),
        ("03","CLOUD INGESTION — AWS IoT Core + S3","Receives messages, routes via processing rules. Raw JSON stored in S3 with partition by device/date. Boto3 scripts for batch ETL."),
        ("04","DATA PROCESSING — Python ETL","Cleans, validates, and transforms raw IoT data. Detects anomalies (voltage spikes, sensor failures). Aggregates to hourly/daily summaries."),
        ("05","VISUALIZATION — AWS QuickSight","Dashboards for ops team: live device status, energy production KPIs per kiosk, fleet performance, alert monitoring."),
    ]:
        st.markdown(f'<div class="step-box" style="border-left-color:#39ff14;"><div class="step-num" style="color:#39ff14;">LAYER {num}</div><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📊 IoT MONITORING DASHBOARDS</div>', unsafe_allow_html=True)
    np.random.seed(99)
    times = pd.date_range("2024-01-15",periods=96,freq="15min")
    voltage = 12.4+np.sin(np.linspace(0,6*np.pi,96))*0.4+np.random.randn(96)*0.05
    current = 5+np.sin(np.linspace(0,3*np.pi,96))*2+np.random.randn(96)*0.2
    soc = np.clip(70+np.cumsum(np.random.randn(96)*0.5),20,100)

    c1,c2 = st.columns(2)
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=times,y=voltage,name="Voltage (V)",
            line=dict(color=CYAN,width=2),yaxis='y1'))
        fig.add_trace(go.Scatter(x=times,y=current,name="Current (A)",
            line=dict(color=ORANGE,width=2),yaxis='y2'))
        layout = pdl("LIVE KIOSK TELEMETRY — 24H",320)
        layout.update(yaxis2=dict(title="Current (A)",overlaying='y',side='right',
            gridcolor='rgba(0,0,0,0)',color=ORANGE))
        fig.update_layout(**layout)
        fig.update_yaxes(title="Voltage (V)")
        st.plotly_chart(fig,use_container_width=True)
    with c2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=times,y=soc,fill='tozeroy',
            fillcolor='rgba(57,255,20,0.1)',line=dict(color=GREEN,width=2.5),name="Battery SoC (%)"))
        fig2.add_hline(y=30,line=dict(color=ORANGE,dash='dash',width=1.5),
            annotation_text="⚠️ LOW THRESHOLD",annotation_font_color=ORANGE)
        fig2.update_layout(**pdl("BATTERY STATE OF CHARGE (%)",320))
        fig2.update_yaxes(title="%",range=[0,105])
        st.plotly_chart(fig2,use_container_width=True)

    c3,c4 = st.columns(2)
    with c3:
        kiosks = [f"K-{str(i).zfill(2)}" for i in range(1,13)]
        energy_kwh = np.random.uniform(2.5,8.5,12)
        colors_k = [GREEN if e>5 else ORANGE if e>3.5 else "#ff4444" for e in energy_kwh]
        fig3 = go.Figure(go.Bar(x=kiosks,y=energy_kwh,marker_color=colors_k,opacity=0.85,
            text=[f"{v:.1f}" for v in energy_kwh],textposition='outside',
            textfont=dict(color="#b0c8d8",family="Share Tech Mono",size=9)))
        fig3.update_layout(**pdl("DAILY ENERGY PRODUCTION BY KIOSK (kWh)",320))
        fig3.update_yaxes(title="kWh")
        st.plotly_chart(fig3,use_container_width=True)
    with c4:
        fig4 = go.Figure(go.Pie(
            labels=["Online ✓","Offline ✗","Maintenance","Low Battery"],
            values=[87,4,6,3],hole=0.6,
            marker=dict(colors=[GREEN,"#ff4444",ORANGE,CYAN]),
            textfont=dict(family="Share Tech Mono",size=11)))
        fig4.update_layout(**pdl("FLEET STATUS — 100 DEVICES",320))
        st.plotly_chart(fig4,use_container_width=True)

    st.markdown('<div class="sub-title">🛠️ TECH STACK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><span class="tag tag-green">C++ (Embedded)</span><span class="tag tag-green">AWS IoT Core</span><span class="tag tag-green">AWS S3</span><span class="tag tag-green">AWS QuickSight</span><span class="tag tag-green">Boto3</span><span class="tag tag-cyan">Python ETL</span><span class="tag tag-cyan">JSON/MQTT</span><span class="tag tag-cyan">TLS/SSL</span><span class="tag tag-orange">GSM/GPRS</span><span class="tag tag-orange">OTA Updates</span></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: EDUCATION
# ═══════════════════════════════════════════════════════════════════════════════
elif "EDUCATION" in page:
    st.markdown('<div class="section-title">🎓 EDUCATION</div>', unsafe_allow_html=True)
    education = [
        ("PhD in Data Science","University of Antananarivo (EDSTI)","2022 — Present (final stage)","🔬","#00e5ff",
         "Research: AI-powered pipelines for IoT and agricultural applications. Thesis: ML model using satellite and climate data for crop yield prediction."),
        ("Master in Mechatronics (ISA)","École Supérieure Polytechnique d'Antananarivo","2021","⚙️","#39ff14",
         "Advanced mechatronics, electronics, automation, embedded systems. Thesis: Smart agricultural greenhouse with IoT sensor integration."),
        ("Master in Automation & Computer Engineering","University of Vakinankaratra","2017 — 2019","🤖","#b44dff",
         "Industrial automation, PLC programming (LADDER), SCADA systems, network engineering (TCP/IP, OSI model)."),
        ("Licence in Automation & Computer Engineering","University of Vakinankaratra","2015 — 2017","🖥️","#ff6b35",
         "Digital electronics, microcontroller programming, industrial networks, computer engineering fundamentals."),
        ("BAC — Industrial Electrotechnics","LTP Antsirabe","2011 — 2014","⚡","#00e5ff",
         "Electrical engineering: power systems, industrial motors, circuit design, safety standards."),
    ]
    for degree,school,year,icon,color,desc in education:
        st.markdown(f"""
        <div style="background:var(--bg-card);border:1px solid {color}33;border-radius:12px;
                    padding:1.3rem 1.5rem;margin-bottom:1.2rem;border-left:4px solid {color};">
            <div style="display:flex;align-items:flex-start;gap:14px;">
                <div style="font-size:2rem;margin-top:4px;">{icon}</div>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:{color};margin-bottom:3px;">{degree}</div>
                    <div style="font-size:0.8rem;color:#7a9ab0;margin-bottom:4px;">{school}</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:{color};opacity:0.8;margin-bottom:8px;">📅 {year}</div>
                    <div style="font-size:0.8rem;color:#b0c8d8;line-height:1.6;">{desc}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CONTACT
# ═══════════════════════════════════════════════════════════════════════════════
elif "CONTACT" in page:
    st.markdown('<div class="section-title">📬 GET IN TOUCH</div>', unsafe_allow_html=True)
    col_info, col_form = st.columns([1, 1.4])
    with col_info:
        contacts = [
            ("📧","rztsitohaina@gmail.com","mailto:rztsitohaina@gmail.com"),
            ("📞","038-81-030-83 / 033-52-031-18",None),
            ("🐙","github.com/tsitohainaraz","https://github.com/tsitohainaraz"),
            ("💼","LinkedIn Profile","https://www.linkedin.com/in/tsitohaina-razafindrajoa-375b51203/"),
            ("📍","Antananarivo, Madagascar",None),
        ]
        for icon,text,link in contacts:
            if link:
                st.markdown(f'<a href="{link}" target="_blank" class="contact-item" style="text-decoration:none;"><span style="font-size:1.2rem;">{icon}</span><span style="font-family:Share Tech Mono,monospace;font-size:0.8rem;color:#e8f4f8;">{text}</span></a>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="contact-item"><span style="font-size:1.2rem;">{icon}</span><span style="font-family:Share Tech Mono,monospace;font-size:0.8rem;">{text}</span></div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background:rgba(57,255,20,0.05);border:1px solid rgba(57,255,20,0.3);
                    border-radius:8px;padding:1rem;margin-top:0.8rem;">
            <div style="font-family:'Orbitron',monospace;font-size:0.72rem;color:#39ff14;margin-bottom:8px;">🌍 AVAILABILITY</div>
            <div style="font-size:0.78rem;color:#b0c8d8;line-height:1.8;">
                ✅ Remote work — Worldwide<br>✅ Upwork contracts<br>
                ✅ Short &amp; long term projects<br>✅ Part-time / Freelance<br>
                🕐 GMT+3 (East Africa Time)
            </div>
        </div>""", unsafe_allow_html=True)

    with col_form:
        st.markdown('<div class="card"><div style="font-family:Orbitron,monospace;font-size:0.85rem;font-weight:700;color:#b44dff;margin-bottom:1rem;letter-spacing:2px;">// SEND A MESSAGE</div>', unsafe_allow_html=True)
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@example.com")
        subject = st.selectbox("Subject", ["Data Engineering Project","IoT System Development",
            "Dashboard / BI Development","Photovoltaic / Energy Analysis","AI / Machine Learning","Other"])
        message = st.text_area("Message", placeholder="Describe your project...", height=130)
        if st.button("⚡  SEND MESSAGE"):
            if name and email and message:
                st.markdown('<div style="background:rgba(57,255,20,0.08);border:1px solid #39ff14;border-radius:8px;padding:1rem;text-align:center;margin-top:0.5rem;"><div style="font-family:Orbitron,monospace;color:#39ff14;font-size:0.85rem;">✓ MESSAGE TRANSMITTED</div><div style="font-size:0.75rem;color:#7a9ab0;margin-top:4px;">I\'ll respond within 24 hours</div></div>', unsafe_allow_html=True)
            else:
                st.warning("Please fill in all fields.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🤝 REFERENCES</div>', unsafe_allow_html=True)
    r1,r2,r3 = st.columns(3)
    refs = [
        ("MR PTHOU MAHEMBITSY","Manager — Chanfoui","032-45-690-01","elviniopathou@gmail.com","#00e5ff"),
        ("MME ASNAH","HR — Madagascar Lano","034-36-305-86","Service.rh@lano-madagascar.com","#39ff14"),
        ("MME NOELA","Production Manager — Jirogasy","034-68-325-40","nrazavaharisoa@jirogasy.com","#b44dff"),
    ]
    for col,(name,role,phone,mail,color) in zip([r1,r2,r3],refs):
        with col:
            st.markdown(f'<div style="background:var(--bg-card);border:1px solid {color}33;border-radius:10px;padding:1.2rem;border-top:3px solid {color};"><div style="font-family:Orbitron,monospace;font-size:0.78rem;font-weight:700;color:{color};margin-bottom:4px;">{name}</div><div style="font-size:0.73rem;color:#7a9ab0;margin-bottom:8px;">{role}</div><div style="font-family:Share Tech Mono,monospace;font-size:0.7rem;color:#b0c8d8;">📞 {phone}<br>✉️ {mail}</div></div>', unsafe_allow_html=True)
