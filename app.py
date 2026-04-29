import streamlit as st

st.set_page_config(
    page_title="AskYourCSV — Talk to your spreadsheets",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


st.html("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');

  /* Streamlit native chrome removal */
  [data-testid="stHeader"] {display: none !important;}
  [data-testid="stFooter"] {display: none !important;}
  #MainMenu {display: none !important;}

  /* App shell — force dark bg everywhere so no white gaps show */
  .stApp {background: var(--bg) !important;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  .stMarkdown {width: 100% !important;}
  div.element-container {padding: 0 !important; margin: 0 !important;}
  div[data-testid="stHtml"] {padding: 0 !important; margin: 0 !important;}

  :root{
    --bg: oklch(0.17 0.008 250);
    --bg-2: oklch(0.21 0.01 250);
    --panel: oklch(0.23 0.012 250);
    --panel-2: oklch(0.26 0.014 250);
    --line: oklch(0.32 0.014 250);
    --line-2: oklch(0.40 0.016 250);
    --ink: oklch(0.96 0.005 250);
    --ink-2: oklch(0.78 0.01 250);
    --ink-3: oklch(0.58 0.012 250);
    --accent: oklch(0.86 0.18 135);
    --accent-ink: oklch(0.22 0.05 135);
    --cyan: oklch(0.82 0.10 210);
    --amber: oklch(0.85 0.14 80);
    --rose: oklch(0.78 0.15 20);
    --mono: 'JetBrains Mono', ui-monospace, monospace;
    --sans: 'Inter', system-ui, sans-serif;
    --serif: 'Instrument Serif', Georgia, serif;
  }

  *{box-sizing:border-box}

  .landing-wrap {
    font-family: var(--sans);
    background: var(--bg);
    color: var(--ink);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
    width: 100%;
    background-image:
      radial-gradient(1200px 600px at 90% -10%, oklch(0.27 0.04 145 / 0.18), transparent 60%),
      radial-gradient(900px 500px at -10% 20%, oklch(0.28 0.03 210 / 0.14), transparent 60%),
      linear-gradient(var(--bg), var(--bg));
  }
  .landing-wrap a {text-decoration: none; color: inherit;}

  .mono{font-family:var(--mono)}
  .serif{font-family:var(--serif);font-style:italic;font-weight:400}
  .wrap{max-width:1280px;margin:0 auto;padding:0 28px}
  .hr{height:1px;background:var(--line);border:0}

  /* nav */
  .nav{
    position:sticky;top:0;z-index:40;
    backdrop-filter: blur(10px);
    background: oklch(0.17 0.008 250 / 0.78);
    border-bottom:1px solid var(--line);
  }
  .nav-inner{display:flex;align-items:center;justify-content:space-between;height:60px}
  .brand{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-weight:600;letter-spacing:-0.01em}
  .brand-mark{
    width:22px;height:22px;border-radius:5px;
    background: linear-gradient(135deg, var(--accent), oklch(0.78 0.14 150));
    box-shadow: 0 0 0 1px var(--line-2), inset 0 1px 0 oklch(1 0 0 / 0.3);
    display:grid;place-items:center;color:var(--accent-ink);font-size:11px;
  }
  .nav-links{display:flex;gap:22px;align-items:center;font-family:var(--mono);font-size:13px;color:var(--ink-2)}
  .nav-links a{color:inherit;text-decoration:none}
  .nav-links a:hover{color:var(--ink)}
  .btn{
    font-family:var(--mono);font-size:13px;font-weight:500;
    display:inline-flex;align-items:center;gap:8px;
    padding:8px 14px;border-radius:8px;border:1px solid var(--line-2);
    background:var(--panel);color:var(--ink);cursor:pointer;text-decoration:none;
    transition: transform .1s ease, background .15s ease, border-color .15s;
  }
  .btn:hover{background:var(--panel-2);border-color:oklch(0.5 0.02 250)}
  .btn-primary, .nav-links a.btn-primary{
    background:var(--accent);color:#000 !important;border-color:transparent;
    box-shadow: 0 0 0 1px oklch(from var(--accent) l c h / 0.4), 0 8px 24px -10px oklch(from var(--accent) l c h / 0.6);
    font-weight:600;
  }
  .btn-primary:hover, .nav-links a.btn-primary:hover{background:oklch(from var(--accent) calc(l + 0.04) c h);border-color:transparent;color:#000 !important}

  /* hero */
  .hero{padding:56px 0 18px;position:relative;text-align:center}
  .eyebrow{
    display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:12px;color:var(--ink-2);
    padding:6px 10px;border:1px solid var(--line);border-radius:999px;background:oklch(0.20 0.01 250 / 0.6);
  }
  .eyebrow .dot{width:6px;height:6px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px oklch(0.86 0.18 135 / 0.2)}
  h1.display{
    font-size: clamp(44px, 5.8vw, 76px);
    line-height:0.98;letter-spacing:-0.035em;font-weight:600;margin:20px auto 0;max-width:14ch;
  }
  h1.display em{font-family:var(--serif);font-weight:400;font-style:italic;color:var(--accent);}
  .lede{color:var(--ink-2);font-size:17px;line-height:1.5;max-width:520px;margin:16px auto 22px}
  .hero-ctas{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
  .hero-meta{margin-top:20px;font-family:var(--mono);font-size:12px;color:var(--ink-3)}
  .hero-meta b{color:var(--ink-2);font-weight:500}

  /* demo */
  .demo-stage{padding:14px 0 40px;position:relative}
  .demo-frame{
    max-width:1180px;margin:0 auto;
    border:1px solid var(--line);border-radius:16px;
    background: linear-gradient(180deg, var(--panel), var(--panel-2));
    box-shadow: 0 60px 120px -50px oklch(0 0 0 / 0.7), 0 2px 0 oklch(1 0 0 / 0.03) inset;
    overflow:hidden;
  }
  .demo-top{
    display:flex;align-items:center;justify-content:space-between;gap:12px;
    padding:12px 18px;border-bottom:1px solid var(--line);font-family:var(--mono);font-size:12px;color:var(--ink-3);
    background:oklch(0.21 0.01 250 / 0.5);
  }
  .demo-top .tlite{display:flex;gap:6px}
  .demo-top .tlite i{width:11px;height:11px;border-radius:50%;display:block}
  .demo-top .tlite i:nth-child(1){background:oklch(0.7 0.16 25)}
  .demo-top .tlite i:nth-child(2){background:oklch(0.85 0.15 85)}
  .demo-top .tlite i:nth-child(3){background:oklch(0.82 0.15 140)}
  .demo-body{padding:20px 22px 16px;display:grid;grid-template-rows:auto 1fr;gap:14px;min-height:280px}
  .demo-q{
    display:flex;align-items:flex-start;gap:10px;
    font-size:18px;line-height:1.35;letter-spacing:-0.01em;
  }
  .demo-q .caret{color:var(--accent);font-family:var(--mono);font-weight:700;margin-top:2px}
  .demo-q .txt{color:var(--ink)}
  .demo-answer{
    border:1px solid var(--line);border-radius:12px;background:var(--bg-2);
    overflow:hidden;display:flex;flex-direction:column;
  }
  .demo-answer .ans-hdr{
    display:flex;align-items:center;justify-content:space-between;gap:10px;
    padding:10px 14px;border-bottom:1px solid var(--line);
    font-family:var(--mono);font-size:11.5px;color:var(--ink-3);
  }
  .demo-answer .ans-hdr .l{display:flex;align-items:center;gap:8px}
  .demo-answer .ans-hdr .l .dotg{width:6px;height:6px;border-radius:50%;background:var(--accent)}
  .demo-answer .ans-body{padding:12px 16px;color:var(--ink-2);font-size:13.5px;line-height:1.5;display:flex;flex-direction:column;gap:10px}
  .demo-answer .ans-body b{color:var(--ink)}
  .demo-answer .ans-body code{background:oklch(0.25 0.01 250);color:var(--accent);padding:1px 6px;border-radius:4px;font-size:12.5px}
  .demo-answer .code-block{
    font-family:var(--mono);font-size:12.5px;color:var(--accent);
    background:oklch(0.19 0.01 250);border:1px solid var(--line);border-radius:8px;padding:10px 12px;
  }
  .demo-bottom{
    padding:10px 18px;border-top:1px solid var(--line);
    display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:12px;color:var(--ink-3);
    background:oklch(0.21 0.01 250 / 0.5);
  }
  .demo-bottom .tag{color:var(--ink-2)}

  /* section */
  section{padding:90px 0;position:relative}
  .sec-eyebrow{font-family:var(--mono);font-size:12px;color:var(--ink-3);letter-spacing:0.06em;text-transform:uppercase}
  h2.sec{font-size:clamp(32px,4vw,52px);font-weight:600;letter-spacing:-0.03em;line-height:1.02;margin:10px 0 0;max-width:920px}
  h2.sec em{font-family:var(--serif);font-weight:400;color:var(--accent)}
  .sec-lede{color:var(--ink-2);font-size:17px;max-width:640px;margin-top:14px;line-height:1.55}

  /* features */
  .features{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:52px}
  @media(max-width:880px){.features{grid-template-columns:1fr}}
  .feat{
    border:1px solid var(--line);border-radius:14px;padding:22px;
    background: linear-gradient(180deg, var(--panel), oklch(0.20 0.01 250));
    position:relative;overflow:hidden;min-height:280px;display:flex;flex-direction:column;
  }
  .feat .tag{font-family:var(--mono);font-size:11px;color:var(--ink-3)}
  .feat h3{font-size:22px;font-weight:600;margin:10px 0 6px;letter-spacing:-0.01em}
  .feat p{color:var(--ink-2);font-size:14.5px;line-height:1.55;margin:0}
  .feat .viz{margin-top:auto;padding-top:16px}

  /* steps */
  .steps{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:52px;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--panel)}
  @media(max-width:880px){.steps{grid-template-columns:1fr}}
  .step{padding:30px 28px;position:relative;border-right:1px solid var(--line)}
  .step:last-child{border-right:0}
  @media(max-width:880px){.step{border-right:0;border-bottom:1px solid var(--line)}.step:last-child{border-bottom:0}}
  .step .n{font-family:var(--mono);font-size:12px;color:var(--ink-3);display:flex;align-items:center;gap:8px}
  .step .n b{color:var(--accent)}
  .step h4{font-size:20px;font-weight:600;margin:14px 0 8px;letter-spacing:-0.01em}
  .step p{color:var(--ink-2);font-size:14px;line-height:1.55;margin:0 0 16px}
  .step .ill{height:120px;border-radius:10px;border:1px dashed var(--line-2);background:oklch(0.19 0.01 250);display:grid;place-items:center;font-family:var(--mono);font-size:12px;color:var(--ink-3);overflow:hidden;position:relative}

  .chip{
    font-family:var(--mono);font-size:11px;padding:4px 8px;border-radius:6px;border:1px solid var(--line);
    background:oklch(0.22 0.01 250);color:var(--ink-2)
  }
  .chip.ok{color:var(--accent);border-color:oklch(0.86 0.18 135 / 0.4);background:oklch(0.86 0.18 135 / 0.08)}

  /* cta */
  .cta{
    margin:60px 0 40px;border:1px solid var(--line);border-radius:20px;padding:56px 40px;
    background:
      radial-gradient(600px 200px at 80% 20%, oklch(0.86 0.18 135 / 0.18), transparent),
      linear-gradient(180deg, var(--panel), var(--panel-2));
    display:grid;grid-template-columns: 1.2fr auto;gap:24px;align-items:center;
  }
  @media(max-width:880px){.cta{grid-template-columns:1fr}}
  .cta h3{font-size:clamp(28px,3.2vw,42px);margin:0;letter-spacing:-0.02em;font-weight:600;line-height:1.05}
  .cta p{color:var(--ink-2);margin:12px 0 0}

  footer.landing-footer{padding:40px 0 60px;border-top:1px solid var(--line);color:var(--ink-3);font-family:var(--mono);font-size:12px}
  footer.landing-footer .f{display:flex;justify-content:space-between;flex-wrap:wrap;gap:14px}
  footer.landing-footer a{color:var(--ink-2);text-decoration:none;margin-right:16px;transition:color .15s}
  footer.landing-footer a:hover{color:var(--ink)}

  /* grid backdrop */
  .grid-bg{
    position:absolute;inset:0;pointer-events:none;opacity:0.35;
    background-image:
      linear-gradient(var(--line) 1px, transparent 1px),
      linear-gradient(90deg, var(--line) 1px, transparent 1px);
    background-size: 56px 56px;
    mask-image: radial-gradient(ellipse at 50% 0%, black 20%, transparent 70%);
    -webkit-mask-image: radial-gradient(ellipse at 50% 0%, black 20%, transparent 70%);
  }

  /* chart gallery */
  .gallery{
    margin-top:40px;
    display:grid;grid-template-columns:repeat(6,1fr);gap:10px;
  }
  @media(max-width:1080px){.gallery{grid-template-columns:repeat(4,1fr)}}
  @media(max-width:680px){.gallery{grid-template-columns:repeat(2,1fr)}}
  .gcard{
    position:relative;
    background:var(--panel);border:1px solid var(--line);border-radius:10px;
    padding:8px;display:flex;flex-direction:column;gap:6px;
    transition:border-color .15s, transform .15s;
  }
  .gcard:hover{border-color:var(--line-2);transform:translateY(-1px)}
  .gcard .viz{height:110px;width:100%}
  .gcard .lbl{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);display:flex;justify-content:space-between;align-items:center;padding:0 2px 2px}
  .gcard .lbl b{color:var(--ink-2);font-weight:500}

  .small{font-size:12px;color:var(--ink-3);font-family:var(--mono)}
  .fade-in{animation:fadein .6s ease both}
  @keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

  /* file icon helper */
  .file-ico{
    width:44px;height:54px;border-radius:6px;background:oklch(0.24 0.01 250);
    border:1px solid var(--line-2);display:grid;place-items:center;font-family:var(--mono);font-size:10px;color:var(--ink-2);
    position:relative;
  }
  .file-ico::before{
    content:"";position:absolute;top:-1px;right:-1px;width:12px;height:12px;
    background: linear-gradient(225deg, var(--bg-2) 50%, transparent 50%);
    border-left:1px solid var(--line-2);border-bottom:1px solid var(--line-2);border-radius:0 5px 0 4px;
  }
</style>
""")

st.html("""
<div class="landing-wrap">

<!-- NAV -->
<div class="nav">
  <div class="wrap nav-inner">
    <div class="brand">
      <div class="brand-mark">▤</div>
      askyourcsv<span style="color:var(--accent)">.</span>
    </div>
    <div class="nav-links">
      <a href="#demo">Demo</a>
      <a href="#features">Features</a>
      <a href="#how">How it works</a>
      <a href="#charts">Charts</a>
      <a href="http://localhost:8502" class="btn btn-primary" target="_self">Playground →</a>
    </div>
  </div>
</div>

<!-- HERO -->
<section class="hero">
  <div class="grid-bg"></div>
  <div class="wrap">
    <div class="eyebrow"><span class="dot"></span> AI assistant for your data</div>
    <h1 class="display">Talk to your <em>spreadsheets</em>.</h1>
    <p class="lede">Drop a CSV or Excel. Ask questions. Get interactive charts.</p>
    <div class="hero-ctas">
      <a href="http://localhost:8502" class="btn btn-primary" target="_self">Open Playground →</a>
      <a href="https://t.me/askyourcsv_bot" class="btn" target="_blank">Telegram Bot</a>
    </div>
    <div class="hero-meta"><b>No signup</b> · Your own API key · 100% private</div>
  </div>
</section>

<!-- DEMO -->
<section id="demo" class="demo-stage">
  <div class="wrap">
    <div class="demo-frame">
      <div class="demo-top">
        <div class="tlite"><i></i><i></i><i></i></div>
        <span class="mono">askyourcsv · demo</span>
        <span class="mono" style="color:var(--ink-3)">live</span>
      </div>
      <div class="demo-body">
        <div class="demo-q">
          <span class="caret">›</span>
          <span class="txt">What were my top-selling products in 2026?</span>
        </div>
        <div class="demo-answer">
          <div class="ans-hdr">
            <div class="l"><span class="dotg"></span><span>askyourcsv</span></div>
            <div class="l" style="color:var(--ink-3)"><span>✓ in 0.6s</span></div>
          </div>
          <div class="ans-body">
            <b>Alpha Kit</b> leads with <b>$4.12M</b> in revenue (38.2% of total), followed by <b>Gamma</b> at $3.01M (27.9%) and <b>Beta Pro</b> at $2.46M (22.8%).
            <div class="code-block">
              <div style="color:var(--ink-3);font-size:11px;margin-bottom:6px">→ generated query</div>
              df.groupby('product')['revenue'].sum().sort_values(ascending=False)
            </div>
          </div>
        </div>
      </div>
      <div class="demo-bottom">
        <span class="tag">01 / 04</span>
        <span style="flex:1"></span>
        <span class="mono">demo static</span>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section id="features">
  <div class="wrap">
    <div class="sec-eyebrow">// 02 · features</div>
    <h2 class="sec">A spreadsheet that <em>answers back.</em></h2>

    <div class="features">
      <div class="feat">
        <span class="tag">// upload</span>
        <h3>CSV, XLSX, Parquet</h3>
        <p>Drag-and-drop files up to 2M rows. We auto-detect delimiters, encodings, date formats and sheet tabs. Join multiple files on shared keys.</p>
        <div class="viz">
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <span class="chip ok">.csv</span><span class="chip">.xlsx</span><span class="chip">.parquet</span>
          </div>
        </div>
      </div>
      <div class="feat">
        <span class="tag">// chat</span>
        <h3>Ask in plain English</h3>
        <p>"Top 10 customers by margin in Q3", "why did revenue drop in April?" — multi-turn reasoning with citations back to the rows that matter.</p>
        <div class="viz" style="font-family:var(--mono);font-size:12px;color:var(--ink-2);background:oklch(0.19 0.01 250);border:1px solid var(--line);border-radius:8px;padding:10px 12px">
          <div style="color:var(--ink-3)">&gt; forecast next quarter</div>
          <div style="color:var(--accent)">⟶ $2.41M ± 0.18M</div>
        </div>
      </div>
      <div class="feat">
        <span class="tag">// charts</span>
        <h3>Interactive charts</h3>
        <p>Every chart is live. Zoom, pan, toggle series, export PNG/SVG, or embed the figure in Notion or Slack.</p>
        <div class="viz">
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <span class="chip">bar</span><span class="chip">line</span><span class="chip ok">scatter</span><span class="chip">heatmap</span>
          </div>
        </div>
      </div>
    </div>

    <div class="features" style="margin-top:18px">
      <div class="feat">
        <span class="tag">// pin</span>
        <h3>Dashboards on tap</h3>
        <p>Pin any answer to a dashboard. Re-runs on fresh data each morning — Slack digest optional.</p>
        <div class="viz">
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <span class="chip ok">auto-refresh</span><span class="chip">export PNG</span>
          </div>
        </div>
      </div>
      <div class="feat">
        <span class="tag">// explain</span>
        <h3>Every answer shows its work</h3>
        <p>Pandas, SQL, or Polars — pick a runtime. The code is right there, so your team can audit, edit, or export.</p>
        <div class="viz" style="font-family:var(--mono);font-size:11.5px;color:var(--ink-2);background:oklch(0.19 0.01 250);border:1px solid var(--line);border-radius:8px;padding:10px 12px;white-space:pre;overflow:hidden">
df.groupby(['region','month'])
  .agg(rev=('revenue','sum'))
  .reset_index()</div>
      </div>
      <div class="feat">
        <span class="tag">// secure</span>
        <h3>Your data stays yours</h3>
        <p>EU + US regions. On-prem deployment available. We never train on your files.</p>
        <div class="viz" style="display:flex;gap:6px;flex-wrap:wrap">
          <span class="chip ok">encrypted at rest</span><span class="chip">delete anytime</span><span class="chip">no training</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CHART GALLERY -->
<section id="charts" style="padding-top:40px">
  <div class="wrap">
    <div class="sec-eyebrow">// charts</div>
    <h2 class="sec">Every chart type, <em>generated from a sentence.</em></h2>
    <p class="sec-lede">Ask for a distribution, a forecast, a correlation, a funnel — we pick the right chart type and render a live figure you can zoom, hover and export.</p>
    <div class="gallery">

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:flex-end;justify-content:center;gap:3px;padding:6px">
          <div style="width:10%;height:35%;background:var(--accent);border-radius:2px"></div>
          <div style="width:10%;height:65%;background:var(--accent);border-radius:2px"></div>
          <div style="width:10%;height:50%;background:var(--accent);border-radius:2px"></div>
          <div style="width:10%;height:80%;background:var(--accent);border-radius:2px"></div>
          <div style="width:10%;height:60%;background:var(--accent);border-radius:2px"></div>
          <div style="width:10%;height:45%;background:var(--accent);border-radius:2px"></div>
        </div>
        <div class="lbl"><b>bar</b><span>01</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;flex-direction:column;justify-content:center;gap:4px;padding:6px 10px">
          <div style="width:75%;height:10%;background:var(--cyan);border-radius:2px"></div>
          <div style="width:55%;height:10%;background:var(--cyan);border-radius:2px"></div>
          <div style="width:85%;height:10%;background:var(--cyan);border-radius:2px"></div>
          <div style="width:45%;height:10%;background:var(--cyan);border-radius:2px"></div>
          <div style="width:65%;height:10%;background:var(--cyan);border-radius:2px"></div>
        </div>
        <div class="lbl"><b>bar.h</b><span>02</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:flex-end;justify-content:center;gap:3px;padding:6px">
          <div style="width:12%;height:55%;display:flex;flex-direction:column;gap:1px">
            <div style="flex:2;background:var(--accent);border-radius:1px 1px 0 0"></div>
            <div style="flex:1;background:var(--cyan)"></div>
            <div style="flex:1;background:var(--amber);border-radius:0 0 1px 1px"></div>
          </div>
          <div style="width:12%;height:70%;display:flex;flex-direction:column;gap:1px">
            <div style="flex:3;background:var(--accent);border-radius:1px 1px 0 0"></div>
            <div style="flex:1;background:var(--cyan)"></div>
            <div style="flex:1;background:var(--amber);border-radius:0 0 1px 1px"></div>
          </div>
          <div style="width:12%;height:45%;display:flex;flex-direction:column;gap:1px">
            <div style="flex:1;background:var(--accent);border-radius:1px 1px 0 0"></div>
            <div style="flex:1;background:var(--cyan)"></div>
            <div style="flex:2;background:var(--amber);border-radius:0 0 1px 1px"></div>
          </div>
          <div style="width:12%;height:60%;display:flex;flex-direction:column;gap:1px">
            <div style="flex:2;background:var(--accent);border-radius:1px 1px 0 0"></div>
            <div style="flex:2;background:var(--cyan)"></div>
            <div style="flex:1;background:var(--amber);border-radius:0 0 1px 1px"></div>
          </div>
        </div>
        <div class="lbl"><b>stacked</b><span>03</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60" preserveAspectRatio="none">
            <polyline points="0,45 15,35 30,40 45,25 60,30 75,15 90,20 100,10" fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="lbl"><b>line</b><span>04</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60" preserveAspectRatio="none">
            <path d="M0,50 L15,35 L30,40 L45,20 L60,28 L75,15 L90,18 L100,8 L100,60 L0,60 Z" fill="oklch(0.82 0.10 210 / 0.25)" stroke="var(--cyan)" stroke-width="2"/>
          </svg>
        </div>
        <div class="lbl"><b>area</b><span>05</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60" preserveAspectRatio="none">
            <polyline points="0,40 20,30 40,35 60,20 80,25 100,15" fill="none" stroke="var(--accent)" stroke-width="2"/>
            <polyline points="0,50 20,45 40,40 60,35 80,30 100,25" fill="none" stroke="var(--cyan)" stroke-width="2"/>
          </svg>
        </div>
        <div class="lbl"><b>multi-line</b><span>06</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <circle cx="15" cy="40" r="2.5" fill="var(--accent)"/>
            <circle cx="35" cy="25" r="2.5" fill="var(--accent)"/>
            <circle cx="55" cy="35" r="2.5" fill="var(--accent)"/>
            <circle cx="25" cy="15" r="2.5" fill="var(--accent)"/>
            <circle cx="75" cy="30" r="2.5" fill="var(--accent)"/>
            <circle cx="85" cy="12" r="2.5" fill="var(--accent)"/>
            <circle cx="45" cy="45" r="2.5" fill="var(--accent)"/>
            <circle cx="65" cy="20" r="2.5" fill="var(--accent)"/>
          </svg>
        </div>
        <div class="lbl"><b>scatter</b><span>07</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <circle cx="20" cy="30" r="4" fill="var(--accent)" opacity="0.7"/>
            <circle cx="50" cy="20" r="7" fill="var(--cyan)" opacity="0.7"/>
            <circle cx="35" cy="45" r="5" fill="var(--amber)" opacity="0.7"/>
            <circle cx="70" cy="35" r="6" fill="var(--accent)" opacity="0.7"/>
            <circle cx="80" cy="15" r="3" fill="var(--cyan)" opacity="0.7"/>
            <circle cx="15" cy="50" r="5" fill="var(--amber)" opacity="0.7"/>
          </svg>
        </div>
        <div class="lbl"><b>bubble</b><span>08</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:center;justify-content:center">
          <div style="width:60px;height:60px;border-radius:50%;background:conic-gradient(var(--accent) 0% 40%,var(--cyan) 40% 68%,var(--amber) 68% 86%,var(--rose) 86% 100%)"></div>
        </div>
        <div class="lbl"><b>pie</b><span>09</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:center;justify-content:center">
          <div style="width:60px;height:60px;border-radius:50%;background:conic-gradient(var(--accent) 0% 55%,var(--cyan) 55% 80%,var(--amber) 80% 92%,var(--rose) 92% 100%);position:relative">
            <div style="position:absolute;inset:16px;border-radius:50%;background:var(--panel)"></div>
          </div>
        </div>
        <div class="lbl"><b>donut</b><span>10</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:grid;grid-template-columns:repeat(7,1fr);grid-template-rows:repeat(5,1fr);gap:2px;padding:4px">
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
        </div>
        <div class="lbl"><b>heatmap</b><span>11</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <line x1="22" y1="10" x2="22" y2="55" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="14" y="22" width="16" height="20" fill="var(--panel-2)" stroke="var(--accent)" stroke-width="1.5" rx="1"/>
            <line x1="10" y1="30" x2="34" y2="30" stroke="var(--accent)" stroke-width="1.5"/>
            <line x1="58" y1="8" x2="58" y2="52" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="50" y="18" width="16" height="24" fill="var(--panel-2)" stroke="var(--cyan)" stroke-width="1.5" rx="1"/>
            <line x1="46" y1="28" x2="70" y2="28" stroke="var(--cyan)" stroke-width="1.5"/>
          </svg>
        </div>
        <div class="lbl"><b>box</b><span>12</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:flex-end;justify-content:center;gap:1px;padding:6px">
          <div style="width:5%;height:15%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:25%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:40%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:60%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:85%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:70%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:50%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:30%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:20%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:35%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:55%;background:var(--accent);border-radius:1px"></div>
          <div style="width:5%;height:45%;background:var(--accent);border-radius:1px"></div>
        </div>
        <div class="lbl"><b>histogram</b><span>13</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <line x1="20" y1="10" x2="20" y2="55" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="16" y="18" width="8" height="22" fill="var(--accent)" rx="1"/>
            <line x1="40" y1="8" x2="40" y2="52" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="36" y="28" width="8" height="18" fill="var(--rose)" rx="1"/>
            <line x1="60" y1="12" x2="60" y2="50" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="56" y="15" width="8" height="28" fill="var(--accent)" rx="1"/>
            <line x1="80" y1="15" x2="80" y2="55" stroke="var(--ink-3)" stroke-width="1"/>
            <rect x="76" y="30" width="8" height="15" fill="var(--rose)" rx="1"/>
          </svg>
        </div>
        <div class="lbl"><b>candlestick</b><span>14</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <polygon points="5,5 95,5 80,22 20,22" fill="var(--accent)"/>
            <polygon points="20,24 80,24 68,40 32,40" fill="var(--cyan)"/>
            <polygon points="32,42 68,42 56,58 44,58" fill="var(--amber)"/>
          </svg>
        </div>
        <div class="lbl"><b>funnel</b><span>15</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:1.2fr 1fr;gap:2px;padding:4px">
          <div style="background:var(--accent);border-radius:2px"></div>
          <div style="background:var(--cyan);border-radius:2px"></div>
          <div style="background:var(--amber);border-radius:2px"></div>
          <div style="background:var(--rose);border-radius:2px"></div>
        </div>
        <div class="lbl"><b>treemap</b><span>16</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <polygon points="50,5 78,20 70,48 30,48 22,20" fill="rgba(158,240,138,0.3)" stroke="var(--accent)" stroke-width="1.5"/>
            <circle cx="50" cy="5" r="2" fill="var(--accent)"/>
            <circle cx="78" cy="20" r="2" fill="var(--accent)"/>
            <circle cx="70" cy="48" r="2" fill="var(--accent)"/>
            <circle cx="30" cy="48" r="2" fill="var(--accent)"/>
            <circle cx="22" cy="20" r="2" fill="var(--accent)"/>
          </svg>
        </div>
        <div class="lbl"><b>radar</b><span>17</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60">
            <path d="M10,50 A40,40 0 0,1 90,50" fill="none" stroke="var(--panel-2)" stroke-width="8" stroke-linecap="round"/>
            <path d="M10,50 A40,40 0 0,1 70,18" fill="none" stroke="var(--accent)" stroke-width="8" stroke-linecap="round"/>
            <text x="50" y="48" text-anchor="middle" fill="var(--ink)" font-family="var(--mono)" font-size="14" font-weight="600">72</text>
          </svg>
        </div>
        <div class="lbl"><b>gauge</b><span>18</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60" preserveAspectRatio="none">
            <path d="M0,55 L20,45 L40,48 L60,35 L80,38 L100,28 L100,60 L0,60 Z" fill="rgba(158,240,138,0.7)"/>
            <path d="M0,50 L20,42 L40,44 L60,32 L80,34 L100,26 L100,60 L0,60 Z" fill="rgba(126,206,224,0.75)"/>
            <path d="M0,48 L20,40 L40,42 L60,30 L80,32 L100,24 L100,60 L0,60 Z" fill="rgba(244,192,106,0.75)"/>
          </svg>
        </div>
        <div class="lbl"><b>stacked area</b><span>19</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 60" preserveAspectRatio="none">
            <polyline points="0,45 15,40 30,35 45,30 60,28 75,25" fill="none" stroke="var(--cyan)" stroke-width="2" stroke-dasharray="3,2"/>
            <polyline points="75,25 90,20 100,15" fill="none" stroke="var(--accent)" stroke-width="2"/>
            <circle cx="75" cy="25" r="2.5" fill="var(--accent)"/>
            <circle cx="90" cy="20" r="2.5" fill="var(--accent)"/>
            <circle cx="100" cy="15" r="2.5" fill="var(--accent)"/>
          </svg>
        </div>
        <div class="lbl"><b>forecast</b><span>20</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:grid;grid-template-columns:repeat(8,1fr);grid-template-rows:repeat(6,1fr);gap:2px;padding:4px">
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--accent);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--cyan);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--amber);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
          <div style="background:var(--panel-2);border-radius:1px"></div>
        </div>
        <div class="lbl"><b>cohort</b><span>21</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="padding:6px">
          <svg width="100%" height="100%" viewBox="0 0 100 30" preserveAspectRatio="none">
            <polyline points="0,25 10,20 20,22 30,15 40,18 50,10 60,12 70,8 80,10 90,5 100,8" fill="none" stroke="var(--accent)" stroke-width="2"/>
          </svg>
        </div>
        <div class="lbl"><b>spark</b><span>22</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:center;justify-content:center">
          <div style="width:48px;height:48px;border-radius:50%;background:conic-gradient(var(--accent) 0% 60%,var(--cyan) 60% 85%,var(--amber) 85% 100%);position:relative">
            <div style="position:absolute;inset:14px;border-radius:50%;background:var(--panel)"></div>
          </div>
        </div>
        <div class="lbl"><b>donut.mini</b><span>23</span></div>
      </div>

      <div class="gcard">
        <div class="viz" style="display:flex;align-items:flex-end;justify-content:center;gap:4px;padding:6px">
          <div style="width:12%;height:50%;background:var(--accent);border-radius:2px"></div>
          <div style="width:12%;height:20%;background:var(--rose);border-radius:2px;margin-bottom:30%"></div>
          <div style="width:12%;height:65%;background:var(--accent);border-radius:2px"></div>
          <div style="width:12%;height:45%;background:var(--accent);border-radius:2px"></div>
          <div style="width:12%;height:80%;background:var(--cyan);border-radius:2px"></div>
        </div>
        <div class="lbl"><b>waterfall</b><span>24</span></div>
      </div>

    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how">
  <div class="wrap">
    <div class="sec-eyebrow">// 03 · how it works</div>
    <h2 class="sec">Three steps. <em>No setup.</em></h2>
    <div class="steps">
      <div class="step">
        <div class="n"><b>01</b> / upload</div>
        <h4>Drop your file</h4>
        <p>CSV, XLSX, TSV or Parquet. We parse, profile and index columns in under a second.</p>
        <div class="ill">
          <div style="display:flex;align-items:center;gap:10px">
            <div class="file-ico" style="background:oklch(0.24 0.01 250)">XLSX</div>
            <span class="mono small">→ profiling · types · dates</span>
          </div>
        </div>
      </div>
      <div class="step">
        <div class="n"><b>02</b> / ask</div>
        <h4>Chat with your data</h4>
        <p>Type questions like you'd Slack a colleague. Follow-ups remember context — no prompt engineering required.</p>
        <div class="ill">
          <div class="mono small" style="text-align:left;padding:0 14px">
            <div style="color:var(--ink-2)">&gt; which region grew fastest?</div>
            <div style="color:var(--accent)">⟶ EMEA (+119% YoY)</div>
          </div>
        </div>
      </div>
      <div class="step">
        <div class="n"><b>03</b> / explore</div>
        <h4>Get live charts</h4>
        <p>Every answer renders as an interactive figure. Zoom, export, or pin to a dashboard.</p>
        <div class="ill">
          <div style="display:flex;gap:6px;align-items:center">
            <span class="chip ok">zoom</span><span class="chip">export</span><span class="chip ok">pin</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section style="padding:0">
  <div class="wrap">
    <div class="cta">
      <div>
        <div class="sec-eyebrow">// start</div>
        <h3>Your next question is one upload away.</h3>
        <p>Free tier includes 3 files, unlimited questions. No credit card.</p>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a href="http://localhost:8502" class="btn btn-primary" target="_self">Open Playground →</a>
        <a href="https://t.me/askyourcsv_bot" class="btn" target="_blank">Telegram Bot</a>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="landing-footer">
  <div class="wrap f">
    <div>
      <div class="brand" style="margin-bottom:10px">
        <div class="brand-mark">▤</div>
        askyourcsv<span style="color:var(--accent)">.</span>
      </div>
      <div>© 2026 askyourcsv · built for people who think in spreadsheets</div>
    </div>
    <div>
      <a href="#features">Features</a>
      <a href="#how">How it works</a>
      <a href="#charts">Charts</a>
      <a href="http://localhost:8502" target="_self">Playground</a>
      <a href="https://t.me/askyourcsv_bot" target="_blank">Telegram</a>
    </div>
  </div>
</footer>

</div>
""")
