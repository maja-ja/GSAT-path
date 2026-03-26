import streamlit as st
import database as db
import styles
from extensions import GSATExtensions as ext

# ─────────────────────────────────────────────────────────────────────────────
# 1. 頁面初始化 (Page Config & State)
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="學測數學觀念溯源",
    page_icon="🎓",
    layout="centered", # 集中視覺，適合閱讀學習筆記
    initial_sidebar_state="expanded"
)

# 初始化 Session State
if "history" not in st.session_state:
    st.session_state.history = []  # 存放溯源路徑
if "current" not in st.session_state:
    st.session_state.current = None  # 當前檢視的考點 key

# ─────────────────────────────────────────────────────────────────────────────
# 2. 側邊欄 (導航與工具箱)
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("<div class='sidebar-header'>📖 複習工具箱</div>", unsafe_allow_html=True)
    
    # 主題切換 (Light/Dark)
    theme_choice = st.select_slider(
        "切換閱讀模式",
        options=["清新學術 (Light)", "專注深色 (Dark)"]
    )
    styles.apply_styles(theme=theme_choice)

    # 考點快搜
    search_q = st.text_input("🔍 快速搜尋考點/公式", placeholder="例如：餘式定理...")
    if search_q:
        results = db.search_concepts(search_q)
        if results:
            for r_key in results:
                r_data = db.get_concept(r_key)
                if st.button(f"{r_data['emoji']} {r_data['title']}", key=f"search_{r_key}", use_container_width=True):
                    if st.session_state.current:
                        st.session_state.history.append(st.session_state.current)
                    st.session_state.current = r_key
                    st.rerun()
        else:
            st.caption("找不到相關考點，請換個關鍵字。")

    st.divider()

    # 複習進度導航
    st.markdown("#### 🛤️ 觀念溯源路徑")
    if not st.session_state.history:
        st.info("點擊首頁魔王題開始溯源")
    else:
        for i, h_key in enumerate(st.session_state.history):
            h_data = db.get_concept(h_key)
            if st.button(f"{i+1}. {h_data['title']}", key=f"hist_{i}", use_container_width=True):
                st.session_state.current = h_key
                st.session_state.history = st.session_state.history[:i]
                st.rerun()

    st.divider()

    # 匯出與重置
    if st.session_state.current:
        ext.export_study_notes(st.session_state.history, st.session_state.current, db.CONCEPTS)
    
    if st.button("🏠 回到主選單", use_container_width=True, type="primary"):
        st.session_state.current = None
        st.session_state.history = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# 3. 主畫面邏輯
# ─────────────────────────────────────────────────────────────────────────────

# --- A. 首頁：學測大考魔王考點 ---
if st.session_state.current is None:
    styles.render_header("🚀 學測數學溯源地圖", "108 課綱專用：從大考題目拆解回最基礎的定義")
    
    st.markdown("### 🎯 選擇你想攻克的考點")
    st.write("點擊下方學測常考題型，開始進行觀念拆解：")
    
    entry_keys = db.get_entry_points()
    for key in entry_keys:
        concept = db.get_concept(key)
        # 使用自定義卡片 HTML
        card_content = f"""
        <div style="display:flex; align-items:center; gap:15px;">
            <span style="font-size:2.5rem;">{concept['emoji']}</span>
            <div>
                <h4 style="margin:0; color:#4A90E2;">{concept['title']}</h4>
                <p style="margin:0; font-size:0.9rem; opacity:0.8;">{concept['summary']}</p>
            </div>
        </div>
        """
        st.markdown(styles.card_wrapper(card_content), unsafe_allow_html=True)
        if st.button(f"開始溯源 {concept['title']}", key=f"btn_{key}", use_container_width=True):
            st.session_state.current = key
            st.rerun()

# --- B. 詳情頁：觀念分析與追溯 ---
else:
    curr_key = st.session_state.current
    concept = db.get_concept(curr_key)
    
    # 1. 顯示麵包屑 (顯示你是怎麼來到這一層的)
    ext.learning_breadcrumb(st.session_state.history, curr_key, db.CONCEPTS)

    # 2. 標題與簡介
    st.markdown(f"## {concept['emoji']} {concept['title']}")
    
    # 3. 學習層級與進度條
    lvl_labels = ["國中銜接基石", "高一基礎單元", "高二核心工具", "學測大考魔王"]
    st.caption(f"觀念層級：{lvl_labels[concept['level']]}")
    st.progress((concept['level'] + 1) * 25)

    # 4. 左右佈局
    col_main, col_viz = st.columns([2, 1])

    with col_main:
        st.markdown(f"**核心筆記：**\n{concept['detail']}")
        
        # 顯示公式區
        if concept.get('formula'):
            st.markdown(f'<div class="formula-container">', unsafe_allow_html=True)
            st.latex(concept['formula'])
            st.markdown('</div>', unsafe_allow_html=True)
        
        # 顯示學測陷阱警報
        ext.exam_alert(curr_key)

    with col_viz:
        # 觀念相依地圖 (Mermaid)
        st.markdown("**觀念關聯圖**")
        ext.render_local_graph(curr_key, db.CONCEPTS)

    # 5. 核心互動：向下追溯基礎
    st.divider()
    parents = concept.get('parents', [])
    
    if parents:
        st.subheader("🔍 解不出來？可能是這些基礎不穩：")
        st.write("點擊下列基礎觀念進行深度補完：")
        
        cols = st.columns(len(parents))
        for i, p_key in enumerate(parents):
            p_data = db.get_concept(p_key)
            with cols[i]:
                # 基礎觀念小卡
                st.markdown(f"""
                <div style="background:rgba(74, 144, 226, 0.1); padding:10px; border-radius:8px; border:1px solid #4A90E2; min-height:100px;">
                    <b style="color:#4A90E2;">{p_data['emoji']} {p_data['title']}</b><br>
                    <small>{p_data['summary']}</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"追溯 {p_data['title']}", key=f"p_btn_{p_key}", use_container_width=True):
                    st.session_state.history.append(curr_key)
                    st.session_state.current = p_key
                    st.rerun()
    else:
        st.success("🏁 **你已抵達觀念基石！** 這已經是該單元最底層的定義了。掌握好這個定義，上面的魔王題就能迎刃而解。")
        st.balloons()

    # 6. AI 思考挑戰
    ext.ai_tutor_challenge(concept)

    # 7. 底部導航
    st.write("<br>", unsafe_allow_html=True)
    b_col1, b_col2 = st.columns([1, 4])
    with b_col1:
        if st.button("⬅️ 返回上一層", use_container_width=True):
            if st.session_state.history:
                st.session_state.current = st.session_state.history.pop()
                st.rerun()
            else:
                st.session_state.current = None
                st.rerun()
