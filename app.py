import streamlit as st
import importlib
import styles
from extensions import GSATExtensions as ext

st.set_page_config(page_title="分科測驗溯源系統", layout="centered")

# --- 自動載入對應分科資料庫的對照表 ---
SUBJECT_MAP = {
    "📐 數學甲/乙 (分科)": "database_math_adv",
    "⚛️ 物理 (分科)": "database_physics_adv",
    "🧪 化學 (分科)": "database_chem_adv",
    "🧬 生物 (分科)": "database_bio_adv",
    "📜 歷史 (分科)": "database_history_adv",
    "🌍 地理 (分科)": "database_geo_adv",
    "⚖️ 公民 (分科)": "database_civics_adv"
}

with st.sidebar:
    st.title("🎓 分科全方位導航")
    subject_label = st.selectbox("選擇分科考科", list(SUBJECT_MAP.keys()))
    module_name = SUBJECT_MAP[subject_label]
    
    # 動態掛載學科模組
    try:
        db_module = importlib.import_module(module_name)
        CONCEPTS = db_module.CONCEPTS
    except ImportError:
        st.error(f"找不到檔案 {module_name}.py，請確認檔案是否存在。")
        st.stop()

    # 如果更換學科，清空路徑
    if "active_subject" not in st.session_state or st.session_state.active_subject != subject_label:
        st.session_state.current = None
        st.session_state.history = []
        st.session_state.active_subject = subject_label

    styles.apply_styles()
    st.divider()
    st.caption("🔍 快速搜尋分科考點")
    search_q = st.text_input("", placeholder="輸入考點關鍵字...")
    if search_q:
        res = [k for k, v in CONCEPTS.items() if search_q in v['title']]
        for r in res:
            if st.button(CONCEPTS[r]['title'], key=f"s_{r}"):
                st.session_state.current = r
                st.rerun()

# --- 主渲染區邏輯 ---
if st.session_state.current is None:
    styles.render_header(f"{subject_label}", "挑戰分科測驗：深入核心觀念的源頭")
    
    # 顯示 Level 3 考點 (最難的起點)
    entries = [k for k, v in CONCEPTS.items() if v['level'] == 3]
    for e in entries:
        c = CONCEPTS[e]
        st.markdown(styles.card_wrapper(f"<h3>{c['emoji']} {c['title']}</h3><p>{c['summary']}</p>"), unsafe_allow_html=True)
        if st.button(f"深入分析 {c['title']}", key=f"btn_{e}", use_container_width=True):
            st.session_state.current = e
            st.rerun()
else:
    # 這裡放詳細頁邏輯（同前述版本）
    key = st.session_state.current
    c = CONCEPTS[key]
    ext.render_concept_page(key, c, CONCEPTS)
