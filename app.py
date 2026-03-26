import streamlit as st
import importlib
import styles
from extensions import GSATExtensions as ext

# ─────────────────────────────────────────────────────────────────────────────
# 1. 頁面初始化設定 (Page Configuration)
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="分科測驗觀念溯源系統",
    page_icon="🎓",
    layout="centered", # 適合長時間閱讀與公式檢視
    initial_sidebar_state="expanded"
)

# 定義分科考科與資料庫檔案的對照 (檔案需並列於同目錄下)
SUBJECT_MAP = {
    "📐 數學甲/乙 (分科)": "database_math_adv",
    "⚛️ 物理 (分科)": "database_physics_adv",
    "🧪 化學 (分科)": "database_chem_adv",
    "🧬 生物 (分科)": "database_bio_adv",
    "📜 歷史 (分科)": "database_history_adv",
    "🌍 地理 (分科)": "database_geo_adv",
    "⚖️ 公民 (分科)": "database_civics_adv"
}

# ─────────────────────────────────────────────────────────────────────────────
# 2. 側邊欄邏輯 (Subject Selector & Navigation)
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("<div class='sidebar-label'>Advanced Subjects Test</div>", unsafe_allow_html=True)
    st.title("分科全科導航")
    
    # 學科切換選擇器
    subject_label = st.selectbox("請選擇分科複習科目", list(SUBJECT_MAP.keys()))
    module_name = SUBJECT_MAP[subject_label]
    
    # 動態掛載對應的學科資料庫
    try:
        db_module = importlib.import_module(module_name)
        CONCEPTS = db_module.CONCEPTS
    except ImportError:
        st.error(f"❌ 找不到資料庫檔案: {module_name}.py")
        st.stop()

    # 初始化與重置邏輯：如果換科目，則清空目前的追蹤路徑
    if "active_subject" not in st.session_state or st.session_state.active_subject != subject_label:
        st.session_state.current = None
        st.session_state.history = []
        st.session_state.active_subject = subject_label

    # 套用主視覺樣式 (可選擇 Light/Dark)
    theme_choice = st.radio("視覺模式", ["清新學術 (Light)", "極致專注 (Dark)"], horizontal=True)
    styles.apply_styles(theme=theme_choice)

    st.divider()

    # 考點快速搜尋 (僅限當前科目)
    st.markdown("<div class='sidebar-label'>快速檢索考點</div>", unsafe_allow_html=True)
    search_query = st.text_input("", placeholder="輸入考點、定律、公式...")
    if search_query:
        search_results = [k for k, v in CONCEPTS.items() if search_query.lower() in v['title'].lower() or search_query.lower() in v['summary'].lower()]
        if search_results:
            for res_key in search_results:
                if st.button(f"🔍 {CONCEPTS[res_key]['title']}", key=f"search_{res_key}", use_container_width=True):
                    if st.session_state.current:
                        st.session_state.history.append(st.session_state.current)
                    st.session_state.current = res_key
                    st.rerun()

    st.divider()
    
    # 重置按鈕
    if st.button("🏠 回到首頁 / 重置路徑", use_container_width=True):
        st.session_state.current = None
        st.session_state.history = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# 3. 主畫面渲染邏輯
# ─────────────────────────────────────────────────────────────────────────────

# --- A. 首頁視圖 (未選取考點時) ---
if st.session_state.current is None:
    styles.render_header(f"{subject_label}", "深度複習：從分科魔王考點追溯至學科基石")
    
    st.markdown("### 🎯 選擇你要分析的挑戰單元")
    st.info("分科測驗常出現跨章節考題，建議從 Level 3 的複合觀念開始拆解。")
    
    # 抓取 Level 3 (分科大考魔王) 作為入口
    entry_keys = [k for k, v in CONCEPTS.items() if v['level'] == 3]
    
    for key in entry_keys:
        concept = CONCEPTS[key]
        card_html = f"""
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h4 style="margin:0; color:#2563EB;">{concept['emoji']} {concept['title']}</h4>
                <p style="margin:0; font-size:0.9rem; opacity:0.8;">{concept['summary']}</p>
            </div>
            <div style="font-weight:bold; color:#2563EB;">LV 3</div>
        </div>
        """
        st.markdown(styles.card_wrapper(card_html), unsafe_allow_html=True)
        if st.button(f"深入探究 {concept['title']}", key=f"entry_{key}", use_container_width=True):
            st.session_state.current = key
            st.rerun()

# --- B. 詳情視圖 (進入觀念溯源時) ---
else:
    curr_key = st.session_state.current
    concept = CONCEPTS[curr_key]
    
    # 1. 麵包屑導航 (由 Extensions 提供)
    ext.learning_breadcrumb(st.session_state.history, curr_key, CONCEPTS)
    
    # 2. 標題與層級進度
    st.markdown(f"<h1 style='margin-bottom:0;'>{concept['emoji']} {concept['title']}</h1>", unsafe_allow_html=True)
    level_names = ["地基公理", "基礎銜接", "核心工具", "分科大考魔王"]
    st.caption(f"觀念層級：{level_names[concept['level']]} (Level {concept['level']})")
    st.progress((concept['level'] + 1) * 25)

    # 3. 內容佈局：左側文字與公式，右側視覺化圖表
    col_content, col_viz = st.columns([1.6, 1])

    with col_content:
        st.markdown(f"**【核心解析】**\n\n{concept['detail']}")
        
        if concept.get('formula'):
            st.markdown(f'<div class="formula-container">', unsafe_allow_html=True)
            st.latex(concept['formula'])
            st.markdown('</div>', unsafe_allow_html=True)
        
        # 顯示分科解題撇步
        ext.exam_
