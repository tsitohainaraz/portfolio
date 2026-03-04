import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tsitohaina R. | Data Engineer & IoT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600;700&display=swap');

    /* ── Root Variables ── */
    :root {
        --bg-deep:   #020810;
        --bg-card:   #0a1628;
        --bg-panel:  #0d1e38;
        --cyan:      #00e5ff;
        --green:     #39ff14;
        --orange:    #ff6b35;
        --purple:    #b44dff;
        --text:      #e8f4f8;
        --muted:     #7a9ab0;
        --border:    rgba(0,229,255,0.18);
        --glow-cyan: 0 0 20px rgba(0,229,255,0.55), 0 0 60px rgba(0,229,255,0.22);
        --glow-green:0 0 20px rgba(57,255,20,0.55);
    }

    /* ── Global Reset ── */
    html, body, [class*="css"] {
        font-family: 'Exo 2', sans-serif !important;
        background-color: var(--bg-deep) !important;
        color: var(--text) !important;
    }
    .block-container { padding: 0 2rem 2rem 2rem !important; max-width: 1200px; }
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Animated grid background ── */
    .stApp {
        background-color: var(--bg-deep) !important;
        background-image:
            linear-gradient(rgba(0,229,255,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,229,255,0.04) 1px, transparent 1px);
        background-size: 50px 50px;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020810 0%, #071628 100%) !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] * { color: var(--text) !important; }
    .sidebar-logo {
        font-family: 'Orbitron', monospace;
        font-size: 1.1rem;
        font-weight: 900;
        color: var(--cyan) !important;
        text-shadow: var(--glow-cyan);
        letter-spacing: 2px;
        padding: 1rem 0 0.5rem 0;
    }
    .sidebar-sub {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.65rem;
        color: var(--muted) !important;
        letter-spacing: 1px;
        margin-bottom: 1.5rem;
    }
    .nav-item {
        display: block;
        padding: 0.6rem 1rem;
        margin: 0.2rem 0;
        border-radius: 6px;
        border: 1px solid transparent;
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.85rem;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.25s ease;
        text-decoration: none;
        color: var(--muted);
    }
    .nav-item:hover, .nav-active {
        border-color: var(--cyan);
        color: var(--cyan) !important;
        background: rgba(0,229,255,0.07);
        box-shadow: inset 3px 0 0 var(--cyan);
    }
    .sidebar-status {
        font-family:'Share Tech Mono',monospace;
        font-size:0.7rem;
        padding:0.5rem 0.8rem;
        border-radius:4px;
        margin-top:1rem;
        display:flex;
        align-items:center;
        gap:8px;
    }
    .dot-green {
        width:8px;height:8px;
        background:var(--green);
        border-radius:50%;
        box-shadow:var(--glow-green);
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0%,100%{opacity:1;transform:scale(1)}
        50%{opacity:0.5;transform:scale(1.3)}
    }

    /* ── Cards & Panels ── */
    .card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .card::before {
        content:'';
        position:absolute;
        top:0;left:0;right:0;
        height:2px;
        background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    }
    .card:hover {
        border-color: rgba(0,229,255,0.4);
        box-shadow: 0 4px 30px rgba(0,229,255,0.12);
        transform: translateY(-2px);
    }

    /* ── Section Titles ── */
    .section-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--cyan);
        text-shadow: var(--glow-cyan);
        letter-spacing: 3px;
        margin: 2rem 0 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .section-title::after {
        content:'';
        flex:1;
        height:1px;
        background: linear-gradient(90deg, var(--cyan), transparent);
        margin-left:12px;
    }
    .section-line {
        width: 60px; height: 3px;
        background: linear-gradient(90deg, var(--cyan), var(--green));
        border-radius: 2px;
        margin-bottom: 2rem;
    }

    /* ── Skill Bars ── */
    .skill-bar-wrap { margin-bottom: 0.8rem; }
    .skill-label {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.8rem;
        display: flex;
        justify-content: space-between;
        margin-bottom: 4px;
        color: var(--text);
    }
    .skill-bar-bg {
        background: rgba(255,255,255,0.06);
        border-radius: 3px;
        height: 8px;
        overflow: hidden;
    }
    .skill-bar-fill {
        height: 100%;
        border-radius: 3px;
        background: linear-gradient(90deg, var(--cyan), var(--green));
        box-shadow: 0 0 8px rgba(0,229,255,0.5);
        animation: fillBar 1.5s ease forwards;
    }
    @keyframes fillBar { from{width:0%} }

    /* ── Timeline ── */
    .timeline-item {
        border-left: 2px solid var(--cyan);
        padding: 0 0 1.5rem 1.5rem;
        margin-left: 0.5rem;
        position: relative;
    }
    .timeline-item::before {
        content:'';
        position:absolute;
        left:-6px;top:4px;
        width:10px;height:10px;
        background:var(--cyan);
        border-radius:50%;
        box-shadow:var(--glow-cyan);
    }
    .tl-date {
        font-family:'Share Tech Mono',monospace;
        font-size:0.72rem;
        color:var(--cyan);
        letter-spacing:1px;
        margin-bottom:4px;
    }
    .tl-title {
        font-family:'Orbitron',monospace;
        font-size:0.95rem;
        font-weight:700;
        color:var(--text);
        margin-bottom:2px;
    }
    .tl-company {
        font-size:0.8rem;
        color:var(--muted);
        margin-bottom:8px;
    }
    .tl-desc {
        font-size:0.82rem;
        color: #b0c8d8;
        line-height:1.6;
    }

    /* ── Tags / Badges ── */
    .tag {
        display:inline-block;
        padding:3px 10px;
        border-radius:20px;
        font-family:'Share Tech Mono',monospace;
        font-size:0.7rem;
        margin:3px 3px 3px 0;
        border:1px solid;
    }
    .tag-cyan  { border-color:var(--cyan);  color:var(--cyan);  background:rgba(0,229,255,0.08); }
    .tag-green { border-color:var(--green); color:var(--green); background:rgba(57,255,20,0.07); }
    .tag-orange{ border-color:var(--orange);color:var(--orange);background:rgba(255,107,53,0.08);}
    .tag-purple{ border-color:var(--purple);color:var(--purple);background:rgba(180,77,255,0.08);}

    /* ── Hero ── */
    .hero-wrap {
        padding: 3rem 0 2rem 0;
        position: relative;
    }
    .hero-greeting {
        font-family:'Share Tech Mono',monospace;
        color:var(--green);
        font-size:0.95rem;
        letter-spacing:3px;
        margin-bottom:0.5rem;
    }
    .hero-name {
        font-family:'Orbitron',monospace;
        font-size:3.2rem;
        font-weight:900;
        line-height:1.1;
        background: linear-gradient(135deg, #ffffff 30%, var(--cyan) 70%);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        background-clip:text;
        margin-bottom:0.5rem;
    }
    .hero-title {
        font-family:'Share Tech Mono',monospace;
        font-size:1rem;
        color:var(--cyan);
        letter-spacing:2px;
        margin-bottom:1.5rem;
        text-shadow:var(--glow-cyan);
    }
    .hero-desc {
        font-size:1rem;
        color:#b0c8d8;
        line-height:1.7;
        max-width:600px;
        margin-bottom:2rem;
    }

    /* ── Metric Cards ── */
    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s;
    }
    .metric-card:hover { box-shadow: var(--glow-cyan); border-color: var(--cyan); }
    .metric-val {
        font-family:'Orbitron',monospace;
        font-size:2rem;
        font-weight:900;
        color:var(--cyan);
        text-shadow:var(--glow-cyan);
    }
    .metric-label {
        font-family:'Share Tech Mono',monospace;
        font-size:0.65rem;
        color:var(--muted);
        letter-spacing:1px;
        margin-top:4px;
    }

    /* ── Project Cards ── */
    .project-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem;
        height: 100%;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .project-card::after {
        content:'';
        position:absolute;
        bottom:0;left:0;right:0;
        height:3px;
        background: linear-gradient(90deg, var(--green), var(--cyan));
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    .project-card:hover { border-color:rgba(57,255,20,0.4); transform:translateY(-4px); }
    .project-card:hover::after { transform:scaleX(1); }
    .project-icon {
        font-size:2rem;
        margin-bottom:0.8rem;
    }
    .project-title {
        font-family:'Orbitron',monospace;
        font-size:0.9rem;
        font-weight:700;
        color:var(--text);
        margin-bottom:0.6rem;
    }
    .project-desc {
        font-size:0.8rem;
        color:var(--muted);
        line-height:1.6;
        margin-bottom:1rem;
    }

    /* ── Contact ── */
    .contact-item {
        display:flex;
        align-items:center;
        gap:12px;
        padding:0.8rem 1rem;
        background:var(--bg-card);
        border:1px solid var(--border);
        border-radius:8px;
        margin-bottom:0.8rem;
        transition: all 0.25s;
        text-decoration:none;
    }
    .contact-item:hover { border-color:var(--cyan); box-shadow:var(--glow-cyan); }
    .contact-icon { font-size:1.3rem; }
    .contact-text { font-family:'Share Tech Mono',monospace; font-size:0.82rem; color:var(--text); }

    /* ── Profile photo placeholder ── */
    .profile-frame {
        width:180px;height:180px;
        border-radius:50%;
        border:3px solid var(--cyan);
        box-shadow: var(--glow-cyan);
        overflow:hidden;
        margin:0 auto 1rem auto;
        display:flex;align-items:center;justify-content:center;
        background:var(--bg-panel);
        font-size:4rem;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width:6px; }
    ::-webkit-scrollbar-track { background:var(--bg-deep); }
    ::-webkit-scrollbar-thumb { background:var(--cyan); border-radius:3px; }

    /* ── Streamlit widget overrides ── */
    .stSelectbox label, .stTextInput label { color: var(--cyan) !important; font-family:'Share Tech Mono',monospace !important; }
    div[data-baseweb="select"] { background:var(--bg-card) !important; border-color:var(--border) !important; }
    .stButton > button {
        background: transparent !important;
        border: 1px solid var(--cyan) !important;
        color: var(--cyan) !important;
        font-family:'Orbitron',monospace !important;
        letter-spacing:2px !important;
        font-size:0.8rem !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 6px !important;
        transition: all 0.25s !important;
    }
    .stButton > button:hover {
        background: rgba(0,229,255,0.12) !important;
        box-shadow: var(--glow-cyan) !important;
    }

    /* ── Education Card ── */
    .edu-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        border-left: 3px solid var(--purple);
        transition: all 0.3s;
    }
    .edu-card:hover { border-color: var(--purple); box-shadow: 0 0 20px rgba(180,77,255,0.15); }
    .edu-degree {
        font-family:'Orbitron',monospace;
        font-size:0.85rem;
        font-weight:700;
        color:var(--text);
        margin-bottom:3px;
    }
    .edu-school { font-size:0.78rem; color:var(--muted); margin-bottom:4px; }
    .edu-year {
        font-family:'Share Tech Mono',monospace;
        font-size:0.7rem;
        color:var(--purple);
    }

    /* ── Terminal block ── */
    .terminal {
        background:#000;
        border:1px solid rgba(57,255,20,0.3);
        border-radius:8px;
        padding:1.2rem;
        font-family:'Share Tech Mono',monospace;
        font-size:0.78rem;
        color:var(--green);
        line-height:1.8;
    }
    .terminal .prompt { color:var(--cyan); }
    .terminal .output { color:#b0c8d8; }

    /* ── Horizontal rule ── */
    hr { border-color: var(--border) !important; }

    /* ── Animated typing cursor ── */
    .cursor {
        display:inline-block;
        width:3px;height:1.1em;
        background:var(--cyan);
        vertical-align:text-bottom;
        animation:blink 1s infinite;
    }
    @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

    /* Photo placeholder instruction box */
    .photo-placeholder {
        width:180px;height:180px;
        border-radius:50%;
        border:3px dashed var(--cyan);
        display:flex;align-items:center;justify-content:center;
        margin:0 auto 1rem auto;
        background:rgba(0,229,255,0.04);
        font-size:3rem;
        text-align:center;
    }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('<div class="sidebar-logo">TSI.RAZ</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">DATA · IOT · ENERGY SYSTEMS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-status">
        <div class="dot-green"></div>
        <span style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:#39ff14;">
            AVAILABLE FOR HIRE
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "",
        ["🏠  HOME", "👤  ABOUT", "💼  EXPERIENCE", "🚀  PROJECTS", "🎓  EDUCATION", "📬  CONTACT"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.65rem;color:#4a6a80;padding:0.5rem 0;">
        <div style="margin-bottom:6px;">⚡ Python · SQL · R · C++</div>
        <div style="margin-bottom:6px;">📡 IoT · AWS · ETL</div>
        <div style="margin-bottom:6px;">☀️ PVsyst · HOMER Pro</div>
        <div>🤖 ML · Deep Learning</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.65rem;color:#4a6a80;text-align:center;">
        © 2025 Tsitohaina Razafindrajoa<br>
        <span style="color:#00e5ff;">Built with Streamlit</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════════════════════
if "HOME" in page:

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-greeting">&gt; HELLO_WORLD.execute() ▶</div>
        <div class="hero-name">TSITOHAINA<br>RAZAFINDRAJOA</div>
        <div class="hero-title">⚡ DATA ENGINEER &nbsp;|&nbsp; IoT ARCHITECT &nbsp;|&nbsp; DATA SCIENTIST &nbsp;|&nbsp; ENERGY ANALYST</div>
        <div class="hero-desc">
            Designing end-to-end data pipelines and intelligent IoT architectures that turn raw signals 
            into decision-ready intelligence. From edge sensors to cloud dashboards — 
            I engineer the full data journey.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats Row ──
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-val">5+</div>
            <div class="metric-label">YEARS EXPERIENCE</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-val">10+</div>
            <div class="metric-label">PROJECTS DELIVERED</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-val">3</div>
            <div class="metric-label">MASTER DEGREES</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-val">PhD</div>
            <div class="metric-label">DATA SCIENCE — IN PROGRESS</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Services ──
    st.markdown('<div class="section-title">⚡ CORE SERVICES</div>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">🔧</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#00e5ff;margin-bottom:0.6rem;">DATA ENGINEERING</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                End-to-end ETL pipelines, data ingestion automation, REST APIs, 
                deduplication logic, and structured storage integration.
            </div>
            <br>
            <span class="tag tag-cyan">Python ETL</span>
            <span class="tag tag-cyan">REST API</span>
            <span class="tag tag-cyan">SQL</span>
            <span class="tag tag-cyan">Streamlit</span>
        </div>""", unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">📡</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#39ff14;margin-bottom:0.6rem;">IoT & EMBEDDED SYSTEMS</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                Embedded C++ firmware, cloud integration (AWS S3, QuickSight, Boto3), 
                IoT data collection and real-time energy analytics.
            </div>
            <br>
            <span class="tag tag-green">C++</span>
            <span class="tag tag-green">AWS IoT</span>
            <span class="tag tag-green">Boto3</span>
            <span class="tag tag-green">MQTT</span>
        </div>""", unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">☀️</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#ff6b35;margin-bottom:0.6rem;">ENERGY & PHOTOVOLTAIC</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                Solar system design & simulation, energy analysis with PVsyst, 
                HOMER Pro, AutoCAD Electrical, and automated sizing tools.
            </div>
            <br>
            <span class="tag tag-orange">PVsyst</span>
            <span class="tag tag-orange">HOMER Pro</span>
            <span class="tag tag-orange">AutoCAD</span>
        </div>""", unsafe_allow_html=True)

    s4, s5, s6 = st.columns(3)
    with s4:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">📊</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#b44dff;margin-bottom:0.6rem;">DATA ANALYTICS & BI</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                Interactive dashboards with Power BI, Qlik Sense. 
                Data cleaning, exploration, and business intelligence storytelling.
            </div>
            <br>
            <span class="tag tag-purple">Power BI</span>
            <span class="tag tag-purple">Qlik Sense</span>
            <span class="tag tag-purple">Excel</span>
        </div>""", unsafe_allow_html=True)
    with s5:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">🤖</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#00e5ff;margin-bottom:0.6rem;">AI & DATA SCIENCE</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                Machine learning models, predictive analytics, AI-powered 
                automation (OpenAI Vision API), and PhD-level research in Data Science.
            </div>
            <br>
            <span class="tag tag-cyan">ML/AI</span>
            <span class="tag tag-cyan">OpenAI API</span>
            <span class="tag tag-cyan">Scikit-learn</span>
        </div>""", unsafe_allow_html=True)
    with s6:
        st.markdown("""
        <div class="card">
            <div style="font-size:2rem;margin-bottom:0.8rem;">🖥️</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;color:#39ff14;margin-bottom:0.6rem;">SOFTWARE DEVELOPMENT</div>
            <div style="font-size:0.82rem;color:#7a9ab0;line-height:1.6;">
                Desktop apps (Tkinter), web apps (Django, Streamlit), 
                automated document processing systems, and OCR pipelines.
            </div>
            <br>
            <span class="tag tag-green">Django</span>
            <span class="tag tag-green">Streamlit</span>
            <span class="tag tag-green">Tkinter</span>
        </div>""", unsafe_allow_html=True)

    # ── Terminal ──
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal">
        <span class="prompt">tsitohaina@data-lab:~$</span> cat profile.txt<br>
        <span class="output">
        ╔══════════════════════════════════════════════════════════╗<br>
        ║  NAME    : Tsitohaina Razafindrajoa                      ║<br>
        ║  ROLE    : Data Engineer | IoT Architect | PhD Candidate ║<br>
        ║  BASE    : Antananarivo, Madagascar 🇲🇬                   ║<br>
        ║  STATUS  : OPEN TO REMOTE WORK &amp; UPWORK CONTRACTS        ║<br>
        ║  STACK   : Python · SQL · C++ · AWS · Power BI           ║<br>
        ╚══════════════════════════════════════════════════════════╝<br>
        </span>
        <span class="prompt">tsitohaina@data-lab:~$</span> <span class="cursor"></span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ══════════════════════════════════════════════════════════════════════════════
elif "ABOUT" in page:
    st.markdown('<div class="section-title">👤 ABOUT ME</div>', unsafe_allow_html=True)

    col_photo, col_bio = st.columns([1, 2.5])

    with col_photo:
        # Try loading profile image, fall back to emoji
        try:
            st.image("profile.jpg", width=200, use_column_width=False)
            st.markdown("""
            <style>
            img { border-radius:50% !important; border:3px solid #00e5ff !important;
                  box-shadow: 0 0 20px rgba(0,229,255,0.55) !important; }
            </style>""", unsafe_allow_html=True)
        except:
            st.markdown("""
            <div class="photo-placeholder">🧑‍💻</div>
            <div style="font-family:'Share Tech Mono',monospace;font-size:0.65rem;
                        color:#4a6a80;text-align:center;">
                → Add <b style="color:#00e5ff;">profile.jpg</b><br>to project root
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:var(--bg-card);border:1px solid var(--border);
                    border-radius:8px;padding:1rem;font-family:'Share Tech Mono',monospace;
                    font-size:0.72rem;">
            <div style="color:#00e5ff;margin-bottom:8px;letter-spacing:1px;">// LANGUAGES</div>
            <div style="margin:4px 0;">🇲🇬 Malagasy — Native</div>
            <div style="margin:4px 0;">🇫🇷 French — Professional</div>
            <div style="margin:4px 0;">🇬🇧 English — Intermediate</div>
        </div>
        """, unsafe_allow_html=True)

    with col_bio:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:1rem;font-weight:700;
                        color:#00e5ff;margin-bottom:1rem;">PROFILE</div>
            <p style="font-size:0.9rem;color:#b0c8d8;line-height:1.8;">
                I'm a <strong style="color:#00e5ff;">Data Engineer</strong> with deep expertise in 
                <strong style="color:#39ff14;">IoT systems</strong>, <strong style="color:#ff6b35;">energy analytics</strong>, 
                and <strong style="color:#b44dff;">machine learning</strong>. Based in Antananarivo, Madagascar, 
                I design and deploy complete data architectures — from embedded sensors all the way to 
                interactive cloud dashboards.
            </p>
            <p style="font-size:0.9rem;color:#b0c8d8;line-height:1.8;">
                Currently pursuing a <strong style="color:#00e5ff;">PhD in Data Science</strong> at the 
                University of Antananarivo while simultaneously delivering freelance projects. 
                My work spans ETL automation, photovoltaic system simulation, 
                AI-powered document processing, and IoT firmware development.
            </p>
            <p style="font-size:0.9rem;color:#b0c8d8;line-height:1.8;">
                I'm actively seeking <strong style="color:#39ff14;">remote contracts on Upwork</strong> — 
                particularly in data engineering, IoT integration, dashboard development, 
                and renewable energy analytics.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🛠️ TECHNICAL SKILLS</div>', unsafe_allow_html=True)

    skill_col1, skill_col2 = st.columns(2)

    skills_left = [
        ("Python", 95),
        ("SQL", 88),
        ("C++ / Embedded", 85),
        ("R", 78),
        ("JavaScript / HTML / CSS", 70),
    ]
    skills_right = [
        ("Power BI / Qlik Sense", 90),
        ("Machine Learning (sklearn)", 82),
        ("AWS (S3, Boto3, QuickSight)", 80),
        ("Pandas / NumPy / Matplotlib", 92),
        ("Django / Streamlit / Tkinter", 88),
    ]

    with skill_col1:
        st.markdown("""
        <div class="card">
        <div style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#00e5ff;margin-bottom:1rem;letter-spacing:2px;">
            // LANGUAGES & FRAMEWORKS
        </div>
        """, unsafe_allow_html=True)
        for skill, pct in skills_left:
            st.markdown(f"""
            <div class="skill-bar-wrap">
                <div class="skill-label"><span>{skill}</span><span style="color:#00e5ff">{pct}%</span></div>
                <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{pct}%"></div></div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with skill_col2:
        st.markdown("""
        <div class="card">
        <div style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#39ff14;margin-bottom:1rem;letter-spacing:2px;">
            // TOOLS & PLATFORMS
        </div>
        """, unsafe_allow_html=True)
        for skill, pct in skills_right:
            st.markdown(f"""
            <div class="skill-bar-wrap">
                <div class="skill-label"><span>{skill}</span><span style="color:#39ff14">{pct}%</span></div>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width:{pct}%;background:linear-gradient(90deg,#39ff14,#00e5ff);"></div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Domain expertise ──
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#ff6b35;margin-bottom:1rem;letter-spacing:2px;">// DOMAIN EXPERTISE</div>
        <div>
        <span class="tag tag-cyan">Data Pipeline Design</span>
        <span class="tag tag-cyan">ETL Automation</span>
        <span class="tag tag-cyan">REST API Integration</span>
        <span class="tag tag-cyan">OpenAI Vision API</span>
        <span class="tag tag-green">IoT Architecture</span>
        <span class="tag tag-green">Embedded Firmware</span>
        <span class="tag tag-green">AWS Cloud Integration</span>
        <span class="tag tag-green">MQTT / TCP-IP</span>
        <span class="tag tag-orange">PVsyst Simulation</span>
        <span class="tag tag-orange">HOMER Pro</span>
        <span class="tag tag-orange">AutoCAD Electrical</span>
        <span class="tag tag-orange">Solar Sizing</span>
        <span class="tag tag-purple">Machine Learning</span>
        <span class="tag tag-purple">Predictive Modeling</span>
        <span class="tag tag-purple">Statistical Analysis</span>
        <span class="tag tag-purple">Big Data (Talend)</span>
        <span class="tag tag-cyan">Power BI</span>
        <span class="tag tag-cyan">Qlik Sense</span>
        <span class="tag tag-cyan">Google Sheets Automation</span>
        <span class="tag tag-cyan">Dashboard Design</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
elif "EXPERIENCE" in page:
    st.markdown('<div class="section-title">💼 WORK EXPERIENCE</div>', unsafe_allow_html=True)

    experiences = [
        {
            "date": "NOV 2025 — DEC 2026",
            "title": "Data Engineer (Freelance)",
            "company": "Chanfoui & Fils · Ankadimbahoaka",
            "desc": """
            • Designed and built a fully automated document ingestion pipeline using OpenAI Vision API, 
              normalizing extracted data and integrating it into a database via REST API + Python ETL.<br>
            • Built a real-time delivery tracking dashboard in Google Sheets (undelivered products, 
              total MGA value, top undelivered items, monthly filters).<br>
            • Tech stack: Python · Streamlit · REST API · OpenAI Vision · ETL
            """,
            "tags": [("Python ETL","cyan"),("OpenAI API","cyan"),("Streamlit","cyan"),("REST API","cyan"),("Google Sheets","green")],
        },
        {
            "date": "JUN 2024 — OCT 2025",
            "title": "Photovoltaic Systems Engineer",
            "company": "Madagascar Lano · Ivato",
            "desc": """
            • Designed technical solar solutions using advanced energy simulation tools.<br>
            • Performed energy audits and system sizing for photovoltaic installations.<br>
            • Tools: PVsyst · AutoCAD Electrical · HOMER Pro · SketchUp
            """,
            "tags": [("PVsyst","orange"),("HOMER Pro","orange"),("AutoCAD","orange"),("Solar Design","orange")],
        },
        {
            "date": "MAR 2024 — MAY 2024",
            "title": "IT Consultant (Freelance)",
            "company": "Madagascar Lano · Ivato",
            "desc": """
            • Developed a desktop application for automatic sizing of generator sets and solar systems 
              based on client data analysis, energy calculations, product recommendations, and quote generation.<br>
            • Tech stack: Python · Tkinter
            """,
            "tags": [("Python","cyan"),("Tkinter","cyan"),("Energy Calc","orange"),("Desktop App","green")],
        },
        {
            "date": "JUL 2021 — FEB 2024",
            "title": "Embedded Systems & IoT Engineer",
            "company": "Jirogasy Sarlu · Androhibe",
            "desc": """
            • Developed embedded C++ firmware for connected devices: OTA updates, IoT data collection.<br>
            • Integrated cloud solutions: AWS S3, Boto3, QuickSight for energy monitoring dashboards.<br>
            • Built Python ETL pipelines for IoT energy data analysis on AWS.
            """,
            "tags": [("C++","green"),("AWS S3","green"),("Boto3","green"),("QuickSight","green"),("IoT","green")],
        },
        {
            "date": "MAR 2021 — JUN 2021",
            "title": "Embedded Systems & IoT Engineer (Intern)",
            "company": "Jirogasy Sarlu · Androhibe",
            "desc": """
            • Cloud integration (AWS S3, Boto3, QuickSight).<br>
            • C++ development for embedded devices (firmware updates, IoT data collection).
            """,
            "tags": [("C++","green"),("AWS","green"),("IoT Firmware","green")],
        },
        {
            "date": "AUG 2020 — FEB 2021",
            "title": "Polyvalent Technician",
            "company": "Ankaratra Residence · Antsirabe",
            "desc": """
            • Handled client-side technical issues: IT failures, telephony, electrical, and network problems.<br>
            • Network protocols: TCP/IP · WLAN · OSI
            """,
            "tags": [("TCP/IP","purple"),("WLAN","purple"),("Network","purple")],
        },
        {
            "date": "FEB 2019 — MAR 2019",
            "title": "IT Intern",
            "company": "Finance Department · Antaninarenina",
            "desc": "Network configuration: TCP/IP · WLAN · OSI",
            "tags": [("TCP/IP","purple"),("Network Config","purple")],
        },
        {
            "date": "DEC 2017",
            "title": "Network Technician",
            "company": "Hay Business Service · Amboditsiry",
            "desc": "Network setup and cabling: switches, TCP/IP.",
            "tags": [("Networking","purple"),("Cabling","purple")],
        },
    ]

    st.markdown('<div style="padding-left:0.5rem;margin-top:1rem;">', unsafe_allow_html=True)
    for exp in experiences:
        tags_html = "".join(f'<span class="tag tag-{t[1]}">{t[0]}</span>' for t in exp["tags"])
        st.markdown(f"""
        <div class="timeline-item">
            <div class="tl-date">{exp['date']}</div>
            <div class="tl-title">{exp['title']}</div>
            <div class="tl-company">📍 {exp['company']}</div>
            <div class="tl-desc">{exp['desc']}</div>
            <div style="margin-top:8px;">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif "PROJECTS" in page:
    st.markdown('<div class="section-title">🚀 PROJECTS</div>', unsafe_allow_html=True)

    projects = [
        {
            "icon": "📄",
            "title": "OCR INVOICE PIPELINE",
            "subtitle": "Chanfoui & Fils — 2025",
            "desc": "Automated document ingestion system using OpenAI Vision API. Extracts invoice data, normalizes it, checks for duplicates, and pushes to database via REST API + Python ETL.",
            "tags": [("OpenAI Vision","cyan"),("Python ETL","cyan"),("REST API","cyan"),("Streamlit","cyan")],
            "link": "https://github.com/tsitohainaraz/CHANFUI_AND_FILS_SCANER",
            "badge": "LIVE ✓"
        },
        {
            "icon": "🌾",
            "title": "RICE YIELD AI PREDICTOR",
            "subtitle": "Data Science — CIRAD Dataverse",
            "desc": "Machine learning model predicting rice crop yield from meteorological, satellite, and climate data. Uses CIRAD rice datasets and advanced feature engineering.",
            "tags": [("ML/AI","purple"),("Python","purple"),("Climate Data","green"),("Prediction","purple")],
            "link": None,
            "badge": "RESEARCH"
        },
        {
            "icon": "☀️",
            "title": "AUTO SOLAR & GENSET SIZER",
            "subtitle": "IT Consultant — Madagascar Lano",
            "desc": "Desktop application that automatically sizes solar panels and generator sets based on client data analysis, energy load calculation, product recommendations, and automated quote generation.",
            "tags": [("Python","cyan"),("Tkinter","cyan"),("Energy Calc","orange"),("Desktop App","green")],
            "link": None,
            "badge": "DEPLOYED"
        },
        {
            "icon": "📊",
            "title": "WEB TRAFFIC ANALYTICS",
            "subtitle": "Personal Project",
            "desc": "Data visualization dashboard for web traffic analysis using JSON data in Qlik Sense. Tracks visitors, registration abandonment rates, and user behavior patterns.",
            "tags": [("Qlik Sense","purple"),("Python","cyan"),("SQL","cyan"),("JSON","green")],
            "link": None,
            "badge": "COMPLETED"
        },
        {
            "icon": "📈",
            "title": "INTERACTIVE SALES DASHBOARD",
            "subtitle": "Academic Project — Power BI",
            "desc": "Interactive Power BI dashboard built from Excel data. Features dynamic filters by country, segment, and product. Visualizes profit, annual revenue, and geographic distribution.",
            "tags": [("Power BI","purple"),("Power Query","purple"),("Excel","green"),("DAX","purple")],
            "link": None,
            "badge": "COMPLETED"
        },
        {
            "icon": "🌱",
            "title": "SMART AGRICULTURAL GREENHOUSE",
            "subtitle": "Master's Thesis Project",
            "desc": "Design and implementation of an intelligent greenhouse with electronic circuits, temperature sensor integration, and embedded C++ control system.",
            "tags": [("C++","green"),("Electronics","orange"),("Sensors","green"),("IoT","green")],
            "link": None,
            "badge": "ACADEMIC"
        },
        {
            "icon": "🤖",
            "title": "COLOR-SORTING ROBOT",
            "subtitle": "Licence Project — PLC Programming",
            "desc": "Industrial programmable logic controller-based robot that sorts parts by color. Programmed in LADDER language with Automgen simulation.",
            "tags": [("PLC","orange"),("LADDER","orange"),("Automgen","orange"),("Automation","orange")],
            "link": None,
            "badge": "ACADEMIC"
        },
        {
            "icon": "📦",
            "title": "DELIVERY TRACKING DASHBOARD",
            "subtitle": "Chanfoui & Fils — Google Sheets",
            "desc": "Dashboard showing total undelivered products, MGA value of undelivered stock, total ordered, top undelivered items over 12 months with monthly drill-down filters.",
            "tags": [("Google Sheets","green"),("ETL","cyan"),("Dashboard","purple"),("KPI","cyan")],
            "link": None,
            "badge": "LIVE ✓"
        },
    ]

    col1, col2 = st.columns(2)
    for i, p in enumerate(projects):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            tags_html = "".join(f'<span class="tag tag-{t[1]}">{t[0]}</span>' for t in p["tags"])
            badge_color = "#39ff14" if "LIVE" in p["badge"] else ("#00e5ff" if "DEPLOYED" in p["badge"] else "#b44dff")
            link_html = f'<br><a href="{p["link"]}" target="_blank" style="color:#00e5ff;font-family:Share Tech Mono,monospace;font-size:0.75rem;">🔗 VIEW ON GITHUB →</a>' if p["link"] else ""
            st.markdown(f"""
            <div class="project-card" style="margin-bottom:1rem;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div class="project-icon">{p['icon']}</div>
                    <span style="font-family:'Share Tech Mono',monospace;font-size:0.65rem;
                                 color:{badge_color};border:1px solid {badge_color};
                                 padding:2px 8px;border-radius:12px;">{p['badge']}</span>
                </div>
                <div class="project-title">{p['title']}</div>
                <div style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;
                             color:#7a9ab0;margin-bottom:0.6rem;">{p['subtitle']}</div>
                <div class="project-desc">{p['desc']}</div>
                <div>{tags_html}</div>
                {link_html}
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
elif "EDUCATION" in page:
    st.markdown('<div class="section-title">🎓 EDUCATION</div>', unsafe_allow_html=True)

    education = [
        {
            "degree": "PhD in Data Science",
            "school": "University of Antananarivo (EDSTI)",
            "year": "2022 — Present (final stage)",
            "icon": "🔬",
            "color": "#00e5ff"
        },
        {
            "degree": "Master in Mechatronics (ISA)",
            "school": "École Supérieure Polytechnique d'Antananarivo",
            "year": "2021",
            "icon": "⚙️",
            "color": "#39ff14"
        },
        {
            "degree": "Master in Automation & Computer Engineering",
            "school": "University of Vakinankaratra",
            "year": "2017 — 2019",
            "icon": "🤖",
            "color": "#b44dff"
        },
        {
            "degree": "Licence in Automation & Computer Engineering",
            "school": "University of Vakinankaratra",
            "year": "2015 — 2017",
            "icon": "🖥️",
            "color": "#ff6b35"
        },
        {
            "degree": "BAC — Industrial Electrotechnics",
            "school": "LTP Antsirabe",
            "year": "2011 — 2014",
            "icon": "⚡",
            "color": "#00e5ff"
        },
    ]

    for edu in education:
        st.markdown(f"""
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;
                    padding:1.3rem 1.5rem;margin-bottom:1rem;
                    border-left:4px solid {edu['color']};transition:all 0.3s;">
            <div style="display:flex;align-items:center;gap:12px;">
                <div style="font-size:1.8rem;">{edu['icon']}</div>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;
                                color:{edu['color']};margin-bottom:4px;">{edu['degree']}</div>
                    <div style="font-size:0.82rem;color:#7a9ab0;margin-bottom:4px;">{edu['school']}</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.72rem;
                                color:{edu['color']};opacity:0.8;">📅 {edu['year']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🏆 CERTIFICATIONS & EXPERTISE</div>', unsafe_allow_html=True)

    cert_col1, cert_col2 = st.columns(2)
    with cert_col1:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#00e5ff;margin-bottom:1rem;">
                // RESEARCH FOCUS
            </div>
            <div style="font-size:0.83rem;color:#b0c8d8;line-height:1.8;">
                🔬 PhD Research: Data Science applications in IoT<br>
                🌾 AI-based agricultural yield prediction (CIRAD)<br>
                📡 Real-time IoT data pipeline architectures<br>
                ☀️ Energy data analytics for renewable systems
            </div>
        </div>
        """, unsafe_allow_html=True)
    with cert_col2:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#39ff14;margin-bottom:1rem;">
                // PROFESSIONAL DOMAINS
            </div>
            <div style="font-size:0.83rem;color:#b0c8d8;line-height:1.8;">
                ⚙️ Industrial Automation & PLC Programming<br>
                🌐 Network Engineering (TCP/IP, WLAN, OSI)<br>
                🏭 Mechatronics & Electronic Systems<br>
                📊 Business Intelligence & Reporting
            </div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif "CONTACT" in page:
    st.markdown('<div class="section-title">📬 GET IN TOUCH</div>', unsafe_allow_html=True)

    col_contact, col_form = st.columns([1, 1.4])

    with col_contact:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:0.85rem;font-weight:700;
                        color:#00e5ff;margin-bottom:1.2rem;letter-spacing:2px;">
                // CONTACT INFO
            </div>
        </div>
        """, unsafe_allow_html=True)

        contacts = [
            ("📧", "rztsitohaina@gmail.com", "mailto:rztsitohaina@gmail.com"),
            ("📞", "038-81-030-83 / 033-52-031-18", None),
            ("🐙", "github.com/tsitohainaraz", "https://github.com/tsitohainaraz"),
            ("💼", "LinkedIn Profile", "https://www.linkedin.com/in/tsitohaina-razafindrajoa-375b51203/"),
            ("📍", "Antananarivo, Madagascar", None),
        ]
        for icon, text, link in contacts:
            if link:
                st.markdown(f"""
                <a href="{link}" target="_blank" class="contact-item" style="text-decoration:none;">
                    <span class="contact-icon">{icon}</span>
                    <span class="contact-text">{text}</span>
                </a>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="contact-item">
                    <span class="contact-icon">{icon}</span>
                    <span class="contact-text">{text}</span>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:var(--bg-card);border:1px solid rgba(57,255,20,0.3);
                    border-radius:8px;padding:1rem;">
            <div style="font-family:'Orbitron',monospace;font-size:0.75rem;color:#39ff14;margin-bottom:8px;">
                🌍 AVAILABILITY
            </div>
            <div style="font-size:0.8rem;color:#b0c8d8;line-height:1.7;">
                ✅ Remote work — Worldwide<br>
                ✅ Upwork contracts<br>
                ✅ Short & long term projects<br>
                ✅ Part-time / Freelance<br>
                🕐 GMT+3 (East Africa Time)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_form:
        st.markdown("""
        <div class="card">
            <div style="font-family:'Orbitron',monospace;font-size:0.85rem;font-weight:700;
                        color:#b44dff;margin-bottom:1.5rem;letter-spacing:2px;">
                // SEND A MESSAGE
            </div>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Your Name", placeholder="John Doe", key="contact_name")
        email = st.text_input("Your Email", placeholder="john@example.com", key="contact_email")
        subject = st.selectbox("Subject", [
            "Data Engineering Project",
            "IoT System Development",
            "Dashboard / BI Development",
            "Photovoltaic / Energy Analysis",
            "AI / Machine Learning",
            "Other"
        ], key="contact_subject")
        message = st.text_area("Message", placeholder="Describe your project...", height=150, key="contact_msg")

        if st.button("⚡  SEND MESSAGE"):
            if name and email and message:
                st.markdown("""
                <div style="background:rgba(57,255,20,0.08);border:1px solid #39ff14;
                            border-radius:8px;padding:1rem;text-align:center;margin-top:0.5rem;">
                    <div style="font-family:'Orbitron',monospace;color:#39ff14;font-size:0.85rem;">
                        ✓ MESSAGE TRANSMITTED
                    </div>
                    <div style="font-size:0.78rem;color:#7a9ab0;margin-top:4px;">
                        I'll respond within 24 hours
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Please fill in all fields.")

    # References
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🤝 REFERENCES</div>', unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)
    refs = [
        ("MR PTHOU MAHEMBITSY", "Manager — Chanfoui", "032-45-690-01", "elviniopathou@gmail.com", "#00e5ff"),
        ("MME ASNAH", "HR — Madagascar Lano", "034-36-305-86", "Service.rh@lano-madagascar.com", "#39ff14"),
        ("MME NOELA", "Production Manager — Jirogasy", "034-68-325-40", "nrazavaharisoa@jirogasy.com", "#b44dff"),
    ]
    for col, (name, role, phone, mail, color) in zip([r1, r2, r3], refs):
        with col:
            st.markdown(f"""
            <div style="background:var(--bg-card);border:1px solid {color}33;border-radius:10px;
                        padding:1.2rem;border-top:3px solid {color};">
                <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
                            color:{color};margin-bottom:4px;">{name}</div>
                <div style="font-size:0.75rem;color:#7a9ab0;margin-bottom:8px;">{role}</div>
                <div style="font-family:'Share Tech Mono',monospace;font-size:0.72rem;color:#b0c8d8;">
                    📞 {phone}<br>✉️ {mail}
                </div>
            </div>
            """, unsafe_allow_html=True)
