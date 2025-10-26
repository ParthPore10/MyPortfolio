import base64
import textwrap
from pathlib import Path

import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Parth Pore | Portfolio", layout="wide", page_icon="💻")

# -------------------- LOAD IMAGE --------------------
img_path = Path("assets/IMG_6438.jpg")
if img_path.exists():
    with open(img_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()
    img_tag = (
        f'<img src="data:image/jpeg;base64,{img_base64}" class="profile-pic" alt="Parth Pore">'
    )
else:
    img_tag = '<div class="missing-photo">⚠️ Photo not found (assets/IMG_9043.jpg)</div>'

# -------------------- CUSTOM CSS --------------------
st.markdown(
    textwrap.dedent(
        """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
            color: #11132a;
            scroll-behavior: smooth;
        }

        #MainMenu, footer {
            visibility: hidden;
        }

        .stApp {
            background: linear-gradient(180deg, #f6f8fb 0%, #eef4ff 60%, #fef9ff 100%);
        }

        .block-container {
            padding: 0 !important;
        }

        /* ---- NAVBAR ---- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 22px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(18px);
            background: rgba(255, 255, 255, 0.85);
            border-bottom: 1px solid rgba(31, 32, 58, 0.08);
            z-index: 999;
        }

        .brand {
            font-weight: 600;
            font-size: 20px;
            letter-spacing: 0.04em;
        }

        .nav-links {
            display: flex;
            gap: 28px;
        }

        .nav-link {
            text-decoration: none;
            color: #11132a;
            font-weight: 500;
            transition: color 0.2s ease;
        }

        .nav-link:hover {
            color: #006fdd;
        }

        /* ---- HERO SECTION ---- */
        .hero {
            padding: 180px 8% 140px;
            display: flex;
            gap: 48px;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            position: relative;
        }

        .hero::after {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 20% 20%, rgba(0, 148, 255, 0.12), transparent 50%),
                        radial-gradient(circle at 80% 30%, rgba(255, 105, 180, 0.12), transparent 55%);
            z-index: 0;
        }

        .hero-card, .hero-info {
            position: relative;
            z-index: 1;
        }

        .hero-card {
            width: 340px;
            text-align: center;
            background: linear-gradient(145deg, rgba(255,255,255,0.96), rgba(235,240,255,0.75));
            padding: 42px 28px;
            border-radius: 36px;
            box-shadow: 0 38px 66px rgba(18, 19, 42, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.55);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 22px;
        }

        .photo-wrap {
            width: 100%;
            max-width: 260px;
            padding: 18px;
            border-radius: 30px;
            background: linear-gradient(160deg, rgba(255,255,255,0.9), rgba(224,232,255,0.65));
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.55), 0 28px 48px rgba(17, 19, 42, 0.2);
        }

        .profile-pic {
            width: 100%;
            aspect-ratio: 3 / 4;
            border-radius: 26px;
            object-fit: cover;
            object-position: center;
            border: 2px solid rgba(0, 112, 221, 0.35);
            box-shadow: 0 18px 35px rgba(17, 19, 42, 0.22);
            display: block;
        }

        .hero-caption {
            font-size: 20px;
            font-weight: 600;
            color: #11132a;
            letter-spacing: 0.04em;
        }

        .hero-role {
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.28em;
            color: #3a3f68;
        }

        .hero-socials {
            display: flex;
            gap: 16px;
            justify-content: center;
            margin-top: 8px;
        }

        .hero-socials a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 1px solid rgba(17, 25, 58, 0.16);
            background: rgba(255,255,255,0.85);
            color: #1a1d3d;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            text-decoration: none;
        }

        .hero-socials a:hover {
            transform: translateY(-3px);
            box-shadow: 0 14px 26px rgba(17, 25, 58, 0.16);
        }

        .hero-socials svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }

        .hero-info h1 {
            font-size: 52px;
            margin-bottom: 18px;
            background: linear-gradient(90deg, #1f203a, #0070dd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-info p {
            max-width: 520px;
            font-size: 19px;
            color: #24274b;
            margin-bottom: 28px;
        }

        .cta-row {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 14px 32px;
            border-radius: 999px;
            border: none;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.25s ease;
        }

        .btn-primary {
            background: linear-gradient(120deg, #0b1f68, #155ad5);
            color: #ffffff;
            box-shadow: 0 18px 30px rgba(11, 31, 104, 0.35);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.18);
        }

        .btn-primary:hover {
            box-shadow: 0 22px 36px rgba(11, 31, 104, 0.42);
            transform: translateY(-2px);
        }

        .btn-outline {
            background: rgba(255,255,255,0.6);
            border: 1px solid rgba(11, 31, 104, 0.38);
            color: #0b1f68;
        }

        .btn-outline:hover {
            background: rgba(0, 112, 221, 0.08);
        }

        .btn-icon {
            width: 52px;
            height: 52px;
            padding: 0;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .btn-icon svg {
            width: 22px;
            height: 22px;
            fill: currentColor;
        }

        /* ---- SECTION STYLES ---- */
        section {
            padding: 120px 8%;
            position: relative;
        }

        .section-title {
            font-size: 18px;
            text-transform: uppercase;
            letter-spacing: 0.32em;
            color: #31345a;
            margin-bottom: 18px;
        }

        .section-heading {
            font-size: 36px;
            font-weight: 600;
            margin-bottom: 30px;
            color: #11132a;
        }

        .blurb {
            max-width: 720px;
            color: #1f2244;
            line-height: 1.85;
        }

        /* ---- FOCUS CARDS ---- */
        .focus-section {
            position: relative;
            overflow: hidden;
        }

        .focus-section::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.7), rgba(218,228,255,0.35));
            z-index: 0;
        }

        .focus-inner {
            position: relative;
            z-index: 1;
        }

        .focus-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 28px;
            margin-top: 48px;
        }

        .focus-card {
            padding: 32px 28px;
            border-radius: 26px;
            background: rgba(255,255,255,0.92);
            box-shadow: 0 22px 44px rgba(24, 26, 56, 0.12);
            border: 1px solid rgba(24, 26, 56, 0.04);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .focus-card h4 {
            font-size: 20px;
            margin: 0;
            color: #11132a;
        }

        .focus-card p {
            color: #1f2244;
            margin: 0;
            line-height: 1.7;
        }

        /* ---- PROJECTS ---- */
        .projects-section {
            background: linear-gradient(135deg, #e7ecff 0%, #f9f5ff 100%);
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
        }

        .skills-section {
            background: rgba(255,255,255,0.82);
            border-top: 1px solid rgba(17, 19, 42, 0.04);
            border-bottom: 1px solid rgba(17, 19, 42, 0.04);
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 28px;
        }

        .skill-group {
            background: rgba(246, 248, 252, 0.9);
            border-radius: 26px;
            padding: 28px 30px;
            border: 1px solid rgba(24, 26, 56, 0.05);
            box-shadow: 0 18px 36px rgba(24, 26, 56, 0.08);
        }

        .skill-group h4 {
            margin-bottom: 16px;
            font-size: 18px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #30345b;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .skill-tag {
            padding: 8px 16px;
            border-radius: 999px;
            background: rgba(17, 25, 58, 0.1);
            color: #11193a;
            font-size: 13px;
            font-weight: 500;
            letter-spacing: 0.03em;
        }

        .project-card {
            padding: 32px;
            border-radius: 30px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 24px 44px rgba(31, 32, 58, 0.12);
            border: 1px solid rgba(0, 112, 221, 0.08);
            display: flex;
            flex-direction: column;
            gap: 18px;
        }

        .project-card span {
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.08em;
            color: #0b1f68;
            text-transform: uppercase;
        }

        .project-card h3 {
            font-size: 24px;
            margin: 0;
            color: #11132a;
        }

        .project-card p {
            color: #202349;
            line-height: 1.7;
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .tag {
            padding: 8px 16px;
            border-radius: 999px;
            background: rgba(0, 112, 221, 0.12);
            color: #0b4c8c;
            font-weight: 500;
            font-size: 13px;
        }

        /* ---- EXPERIENCE TIMELINE ---- */
        .timeline {
            border-left: 2px solid rgba(0, 112, 221, 0.18);
            margin-top: 40px;
            padding-left: 28px;
        }

        .timeline-item {
            position: relative;
            padding-bottom: 40px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -39px;
            top: 4px;
            width: 14px;
            height: 14px;
            background: #0070dd;
            border-radius: 50%;
            box-shadow: 0 0 0 6px rgba(0, 112, 221, 0.15);
        }

        .timeline-item h4 {
            margin-bottom: 6px;
            font-size: 20px;
        }

        .timeline-item .role {
            font-weight: 600;
            color: #11132a;
        }

        .timeline-item .time {
            text-transform: uppercase;
            letter-spacing: 0.2em;
            font-size: 12px;
            color: #343760;
            margin-bottom: 12px;
            display: inline-block;
        }

        .timeline-item p {
            color: #202349;
        }

        .timeline-list {
            margin: 16px 0 0;
            padding-left: 22px;
            color: #202349;
            line-height: 1.75;
        }

        .timeline-list li {
            margin-bottom: 10px;
        }

        /* ---- CONTACT ---- */
        .contact-section {
            text-align: center;
            padding-bottom: 140px;
        }

        .contact-card {
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 18px;
            background: rgba(255,255,255,0.9);
            padding: 48px 70px;
            border-radius: 36px;
            box-shadow: 0 28px 52px rgba(31, 32, 58, 0.15);
        }

        .contact-card p {
            max-width: 520px;
            color: #1f2244;
            line-height: 1.8;
        }

        .missing-photo {
            padding: 18px;
            border-radius: 16px;
            background: rgba(255, 174, 0, 0.12);
            color: #c15e00;
            font-weight: 500;
        }

        @media (max-width: 768px) {
            .hero {
                padding-top: 160px;
            }
            .hero-info h1 {
                font-size: 40px;
            }
            .navbar {
                padding: 18px 6%;
            }
            section {
                padding: 90px 6%;
            }
        }
    </style>
    """
    ),
    unsafe_allow_html=True,
)

# -------------------- NAVIGATION --------------------
st.markdown(
    textwrap.dedent(
        """
    <div class="navbar">
        <div class="brand">Parth Pore</div>
        <div class="nav-links">
            <a class="nav-link" href="#about">About</a>
            <a class="nav-link" href="#skills">Skills</a>
            <a class="nav-link" href="#projects">Projects</a>
            <a class="nav-link" href="#experience">Experience</a>
            <a class="nav-link" href="#contact">Contact</a>
        </div>
    </div>
    """
    ),
    unsafe_allow_html=True,
)

# -------------------- HERO SECTION --------------------
st.markdown(
    textwrap.dedent(
        f"""
    <section class="hero" id="about">
        <div class="hero-card">
            <div class="photo-wrap">
                {img_tag}
            </div>
            <div class="hero-role">Ml-Engineer · Data Scientist · Graduate Researcher</div>
        </div>
        <div class="hero-info">
            <h1>Parth Pore.</h1>
            <p>
                Graduate student in Computer Engineering at UT Dallas and researcher at the EACAS Lab,
                working on search algorithm optimization and Hyperdimensional Computing (HDC) for adaptive perception systems.
                Former Data Scientist at Hitachi, where I led the transition toward value-based pricing through ML-driven forecasting,
                margin optimization, and NLP text extraction. Experienced in Python, SQL, C++, and Power BI, with a focus on bridging classical computing
                and machine learning for scalable, real-world solutions.
            </p>
            <div class="cta-row">
                <a class="btn btn-primary" href="#projects">See featured work</a>
                <a class="btn btn-outline" href="mailto:parthpore2002@gmail.com">Connect via email</a>
                <a class="btn btn-outline btn-icon" href="https://github.com/ParthPore10" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
                    <svg viewBox="0 0 24 24" role="img">
                        <path d="M12 .5C5.649.5.5 5.65.5 12.007c0 5.097 3.292 9.41 7.865 10.938.575.107.786-.25.786-.557 0-.275-.01-1.002-.015-1.967-3.2.695-3.877-1.543-3.877-1.543-.523-1.327-1.277-1.68-1.277-1.68-1.043-.713.079-.699.079-.699 1.153.081 1.76 1.18 1.76 1.18 1.026 1.757 2.692 1.25 3.348.955.104-.743.402-1.25.73-1.537-2.554-.291-5.238-1.278-5.238-5.686 0-1.256.448-2.283 1.182-3.087-.119-.29-.512-1.462.112-3.047 0 0 .964-.309 3.16 1.18a10.94 10.94 0 0 1 2.879-.388c.976.004 1.96.133 2.879.388 2.194-1.489 3.156-1.18 3.156-1.18.626 1.585.233 2.757.114 3.047.737.804 1.18 1.831 1.18 3.087 0 4.418-2.688 5.392-5.252 5.676.413.357.781 1.058.781 2.133 0 1.54-.014 2.78-.014 3.157 0 .309.208.67.792.556C20.21 21.413 23.5 17.1 23.5 12.007 23.5 5.65 18.351.5 12 .5Z"/>
                    </svg>
                </a>
                <a class="btn btn-outline btn-icon" href="https://www.linkedin.com/in/parth-pore-ab17a4197/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                    <svg viewBox="0 0 24 24" role="img">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.447-2.136 2.941v5.665H9.351V9h3.414v1.561h.049c.476-.9 1.637-1.85 3.368-1.85 3.602 0 4.268 2.368 4.268 5.455v6.286ZM5.337 7.433a2.062 2.062 0 1 1 0-4.123 2.062 2.062 0 0 1 0 4.123ZM7.115 20.452H3.56V9h3.555v11.452Z"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>
    """
    ),
    unsafe_allow_html=True,
)

# -------------------- SKILLS SECTION --------------------
st.markdown(
    textwrap.dedent(
        """
    <section class="skills-section" id="skills">
        <div class="section-title">Core Strengths</div>
        <div class="section-heading">Tools and practices I reach for first.</div>
        <div class="skills-grid">
            <div class="skill-group">
                <h4>Programming & Tooling</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">C++</span>
                    <span class="skill-tag">TensorFlow</span>
                    <span class="skill-tag">PyTorch</span>
                    <span class="skill-tag">SQL</span>
                    <span class ="skill-tag">Scikit-learn</span>
                </div>
            </div>
            <div class="skill-group">
                <h4>Machine Learning</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Regression</span>
                    <span class="skill-tag">Classification</span>
                    <span class="skill-tag">NLP</span>
                    <span class="skill-tag">Unsupervised Learning</span>
                    <span class="skill-tag">Time-Series forecasting</span>
                </div>
            </div>
            <div class="skill-group">
                <h4>Visualization & Libraries</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Pandas</span>
                    <span class="skill-tag">NumPy</span>
                    <span class="skill-tag">Power-bi</span>
                    <span class="skill-tag">Streamlit</span>
                    <span class="skill-tag">Matplotlib</span>
                    <span class="skill-tag">Plotly</span>
                    <span class="skill-tag">Github</span>
                    <span class="skill-tag"> Edge Impulse</span>
                </div>
            </div>
            <div class="skill-group">
                <h4>Embedded & AI Research</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Dynamic Neural Fields</span>
                    <span class="skill-tag">Hyperdimensional Computing</span>
                    <span class="skill-tag">Tiny ML</span>
                    <span class="skill-tag">Tiny MPC</span>
                </div>
            </div>
        </div>
    </section>
    """
    ),
    unsafe_allow_html=True,
)


# -------------------- PROJECTS SECTION --------------------
st.markdown(
    textwrap.dedent(
        """
    <section class="projects-section" id="projects">
        <div class="section-title">Featured Work</div>
        <div class="section-heading">Selected collaborations & prototypes</div>
        <div class="projects-grid">
            <div class="project-card">
                <span>Research</span>
                <h3>Dynamic Neural Fields for Closed-Loop Attention</h3>
                <p>
                    Working on optimizing the Dynamic Neural Field (DNF) framework for real-time multi-object tracking by 
                    automating parameter tuning and optimizing the search algorithm for improved stability and convergence.
                    Integrating Hyperdimensional Computing (HDC) for energy-efficient, noise-robust on-device learning 
                </p>
                <div class="tag-row">
                    <div class="tag">DNF</div>
                    <div class="tag">C++</div>
                    <div class="tag">DSA</div>
                </div>
            </div>
            <div class="project-card">
                <span>Industry</span>
                <h3>Driving Pricing Intelligence at Hitachi Energy</h3>
                <p>
                    Led the transition from cost-plus to value-based pricing by developing machine learning models that forecasted product demand and 
                    optimized margins across U.S. and European portfolios.Designed data-driven pricing frameworks that quantified customer value sensitivity,
                    enabling smarter bid decisions and improved profitability.Automated analytics pipelines and dashboards using Python, SQL, and Power BI, 
                    reducing manual effort and improving pricing governance efficiency.
                </p>
                <div class="tag-row">
                    <div class="tag">Python</div>
                    <div class="tag">Regression</div>
                    <div class="tag">CLTV</div>
                    <div class="tag">Statistics</div>
                </div>
            </div>
            <div class="project-card">
                <span>Industry</span>
                <h3>Automated Text Mining for Business Analytics</h3>
                <p>
                    Developed NLP models to summarize and extract insights from unstructured pricing reports, sales notes, and bid documents. 
                    Automated information retrieval pipelines that improved decision turnaround time and reduced manual report analysis by over 60%.
                </p>
                <div class="tag-row">
                    <div class="tag">NLP</div>
                    <div class="tag">Python</div>
                </div>
            </div>
        </div>
    </section>
    """
    ),
    unsafe_allow_html=True,
)

# -------------------- EXPERIENCE SECTION --------------------
st.markdown(
    textwrap.dedent(
        """
    <section id="experience">
        <div class="section-title">Experience</div>
        <div class="section-heading">A journey across research & Industry</div>
        <div class="timeline">
            <div class="timeline-item">
                <div class="time">Sep 2025 - Present</div>
                <h4 class="role">Graduate Researcher · UT Dallas EACAS Lab</h4>
                <ul class = "timeline-list">
                    <li>Optimizing search algorithms for automatic parameter tuning to achieve optimal DNF 
                    solutions for adaptive perception and control workloads.</li>
                </ul>
            </div>
            <div class="timeline-item">
                <div class="time">Aug 2023 — Aug 2025</div>
                <h4 class="role">Data Scientist · Hitachi</h4>
                <ul class="timeline-list">
                    <li>Developed an ML-driven pricing optimization framework that integrates regression and clustering models for value-based decisions across multi-regional portfolios.</li>
                    <li>Engineered an unsupervised service classification model covering ~28k products, cutting manual effort by more than 700 hours annually.</li>
                    <li>Created real-time dashboards tracking conversion metrics and operational KPIs, improving cross-functional decision velocity.</li>
                    <li>Built NLP automation to classify and analyze product descriptions, reducing manual categorization by roughly 350 hours each year.</li>
                    <li>Implemented time-series and regression models inside a recommendation engine, monitoring drift and feature importance to keep production robust.</li>
                </ul>
            </div>
            <div class="timeline-item">
                <div class="time">Feb 2023 — Aug 2023</div>
                <h4 class="role">Data science intern · Hitachi</h4>
                <ul class = "timeline-list">
                    <li> Built data-processing watchdog automation, reducing manual workload by 75 %.</li>
                    <li>Supported model evaluation and KPI analytics for early versions of pricing and demand-forecast systems.</li>
                    <li>Collaborated with commercial and R&D teams to align analytics outcomes with product roadmap priorities.</li>
                </ul>
            </div>
            <div class="timeline-item">
                <div class="time">Sep 2022 — Nov 2022</div>
                <h4 class="role">Data science intern · Schnider Electric</h4>
                <ul class = "timeline-list">
                    <li>Developed automated calibration data-collection pipelines for manufacturing analytics; improved workflow
                        efficiency by 90 %.</li>
                    <li>Collaborated on the production line, specifically with automatic calibration of RCCBs.</li>
                    <li>Streamlined data collection and post-processing, managing large datasets for optimized workflow.</li>
                </ul>
            </div>
        </div>
    </section>
    """
    ),
    unsafe_allow_html=True,
)

# -------------------- CONTACT SECTION --------------------
st.markdown(
    textwrap.dedent(
        """
    <section class="contact-section" id="contact">
        <div class="contact-card">
            <div class="section-title">Let’s Collaborate</div>
            <div class="section-heading">Tell me about your next idea.</div>
            <p>
                Exploring opportunities in classical computing and ML, focusing on algorithm design, optimization, and scalable AI systems.
            </p>
            <a class="btn btn-primary" href="mailto:parthpore2002@gmail.com">parthpore2002@gmail.com</a>
        </div>
    </section>
    """
    ),
    unsafe_allow_html=True,
)
