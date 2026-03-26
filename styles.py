import streamlit as st

def apply_styles(theme="清新學術 (Light)"):
    """
    針對分科測驗深度學習設計的視覺樣式。
    支援：Light (白紙感) / Dark (代碼專注感)
    """
    
    # 1. 主題配色定義 (採用專業學術色調)
    if theme == "極致專注 (Dark)":
        bg_color = "#0F172A"       # 深藍黑 (Slate 900)
        card_bg = "#1E293B"        # 深板岩色 (Slate 800)
        text_color = "#F1F5F9"     # 亮灰 (Slate 100)
        sub_text = "#94A3B8"       # 藍灰 (Slate 400)
        accent_color = "#38BDF8"   # 水藍色 (Sky 400)
        border_color = "#334155"   # Slate 700
        formula_bg = "#020617"     # 極深色背景
    else:
        bg_color = "#F8FAFC"       # 暖白 (Slate 50)
        card_bg = "#FFFFFF"        # 純白
        text_color = "#1E293B"     # 深藍黑 (Slate 800)
        sub_text = "#64748B"       # 灰藍 (Slate 500)
        accent_color = "#2563EB"   # 專業藍 (Blue 600)
        border_color = "#E2E8F0"   # Slate 200
        formula_bg = "#F1F5F9"     # 淺藍灰 (Slate 100)

    # 2. 注入 Google Fonts 與全域 CSS
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Noto+Sans+TC:wght@400;500;700&family=Fira+Code&display=swap');

        /* 全域樣式設定 */
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
        }}

        /* 隱藏 Streamlit 預設裝飾 */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}

        /* 分科專業卡片 (Study Card) */
        .study-card {{
            background-color: {card_bg};
            border: 1px solid {border_color};
            border-top: 6px solid {accent_color}; /* 頂部色條區分科目 */
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .study-card:hover {{
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }}

        /* 主副標題樣式 */
        .main-title {{
            font-size: 2.8rem;
            font-weight: 700;
            color: {text_color};
            letter-spacing: -0.05em;
            margin-bottom: 0.5rem;
            text-align: center;
        }}
        .sub-title {{
            font-size: 1.2rem;
            color: {sub_text};
            text-align: center;
            margin-bottom: 2.5rem;
        }}

        /* 麵包屑導航路徑 (Breadcrumbs) */
        .breadcrumb-container {{
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 2rem;
            font-size: 0.85rem;
        }}
        .breadcrumb-item {{
            padding: 0.3rem 0.8rem;
            background: {accent_color}15; /* 15% 透明度的主色 */
            color: {accent_color};
            border-radius: 6px;
            font-weight: 600;
            border: 1px solid {accent_color}30;
        }}
        .breadcrumb-arrow {{
            color: {sub_text};
            font-weight: bold;
        }}

        /* 公式區塊自定義 */
        .formula-container {{
            background-color: {formula_bg};
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-left: 4px solid {accent_color};
            font-family: 'Fira Code', monospace;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }}

        /* 側邊欄優化 */
        [data-testid="stSidebar"] {{
            background-color: {card_bg};
            border-right: 1px solid {border_color};
        }}
        .sidebar-label {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            color: {sub_text};
            margin-bottom: 0.5rem;
            letter-spacing: 0.05em;
        }}

        /* 按鈕美化 */
        .stButton button {{
            border-radius: 8px;
            border: 1px solid {border_color};
            background-color: {card_bg};
            color: {text_color};
            font-weight: 600;
            transition: all 0.2s;
            width: 100%;
        }}
        .stButton button:hover {{
            border-color: {accent_color};
            color: {accent_color};
            background-color: {accent_color}0A;
        }}
        
        /* 進度條顏色 */
        .stProgress > div > div > div > div {{
            background-color: {accent_color};
        }}

        /* 針對 LaTeX 字體大小微調 */
        .katex {{ font-size: 1.1em !important; }}
        </style>
    """, unsafe_allow_html=True)

def render_header(title, subtitle):
    """渲染分科專用頁首"""
    st.markdown(f'<div class="main-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">{subtitle}</div>', unsafe_allow_html=True)

def card_wrapper(content_html):
    """將內容包裝在專業學術卡片中"""
    return f'<div class="study-card">{content_html}</div>'

def breadcrumb_html(history_titles, current_title):
    """
    生成溯源路徑的 HTML 結構
    """
    html = '<div class="breadcrumb-container">'
    for title in history_titles:
        html += f'<span class="breadcrumb-item">{title}</span>'
        html += '<span class="breadcrumb-arrow">❯</span>'
    html += f'<span class="breadcrumb-item" style="background:#2563EB; color:white; border:none;">🎯 {current_title}</span>'
    html += '</div>'
    return html
