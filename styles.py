import streamlit as st

def apply_styles(theme="清新學術 (Light)"):
    """
    套用學測數學專屬視覺樣式。
    主題選項: "清新學術 (Light)", "專注深色 (Dark)"
    """
    
    # 主題色彩定義
    if theme == "專注深色 (Dark)":
        bg_color = "#121212"
        card_bg = "#1E1E1E"
        text_color = "#E0E0E0"
        sub_text = "#A0A0A0"
        accent_color = "#64B5F6"
        border_color = "#333333"
        formula_bg = "#263238"
    else:
        bg_color = "#F8F9FA"
        card_bg = "#FFFFFF"
        text_color = "#2C3E50"
        sub_text = "#7F8C8D"
        accent_color = "#4A90E2"
        border_color = "#E0E0E0"
        formula_bg = "#F1F4F9"

    # 注入 Google Fonts 與全域 CSS
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&family=Fira+Code&display=swap');

        /* 基礎版面 */
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            font-family: 'Noto Sans TC', sans-serif;
        }}

        /* 隱藏預設元件 */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        /* 學測筆記風卡片 */
        .study-card {{
            background-color: {card_bg};
            border: 1px solid {border_color};
            border-left: 6px solid {accent_color};
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            transition: transform 0.2s ease;
        }}
        .study-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        }}

        /* 標題樣式 */
        .main-title {{
            color: {text_color};
            font-weight: 700;
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }}
        .sub-title {{
            color: {sub_text};
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }}

        /* 麵包屑路徑 (Breadcrumbs) */
        .breadcrumb-box {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 24px;
            font-size: 0.9rem;
            color: {sub_text};
            flex-wrap: wrap;
        }}
        .breadcrumb-step {{
            background: {accent_color}15;
            color: {accent_color};
            padding: 2px 10px;
            border-radius: 4px;
            font-weight: 500;
        }}

        /* 公式區塊 */
        .formula-container {{
            background-color: {formula_bg};
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
            border: 1px dashed {accent_color}66;
            text-align: center;
        }}

        /* 側邊欄樣式 */
        [data-testid="stSidebar"] {{
            background-color: {card_bg};
            border-right: 1px solid {border_color};
        }}
        .sidebar-header {{
            font-size: 1.2rem;
            font-weight: 700;
            color: {accent_color};
            margin-bottom: 1rem;
        }}

        /* 按鈕美化 */
        .stButton button {{
            border-radius: 8px;
            border: 1px solid {border_color};
            transition: all 0.2s;
            font-weight: 500;
        }}
        .stButton button:hover {{
            border-color: {accent_color};
            color: {accent_color};
            background-color: {accent_color}05;
        }}

        /* 進度條樣式 */
        .stProgress > div > div > div > div {{
            background-color: {accent_color};
        }}

        /* 警告/撇步區塊 */
        .stAlert {{
            border-radius: 10px;
            border: none;
            background-color: {accent_color}10;
        }}
        </style>
    """, unsafe_allow_html=True)

def render_header(title, subtitle):
    """渲染頁面頂部"""
    st.markdown(f"""
        <div style="text-align: center; padding: 20px 0;">
            <div class="main-title">{title}</div>
            <div class="sub-title">{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)

def card_wrapper(content_html):
    """將內容包裝在學習卡片中"""
    return f'<div class="study-card">{content_html}</div>'

def breadcrumb_step(text):
    """單個麵包屑步驟 HTML"""
    return f'<span class="breadcrumb-step">{text}</span>'
