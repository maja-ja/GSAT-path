import streamlit as st
import streamlit.components.v1 as components
import styles

class GSATExtensions:
    """
    分科測驗專用進階功能擴充模組
    包含：觀念圖譜、解題撇步、AI 挑戰、筆記匯出
    """

    @staticmethod
    def render_local_graph(concept_key, concepts_db):
        """
        利用 Mermaid.js 渲染當前觀念及其「家長觀念」的局部圖譜。
        這能幫助學生視覺化理解：為什麼這個分科魔王題解不出來（因為基礎不穩）。
        """
        curr = concepts_db.get(concept_key)
        if not curr or not curr.get('parents'):
            return

        # 構建 Mermaid 語法 (由下往上追溯)
        mermaid_code = "graph BT\n"
        
        # 當前節點樣式
        mermaid_code += f"  {concept_key}[{curr['title']}]\n"
        mermaid_code += f"  style {concept_key} fill:#2563EB,stroke:#fff,stroke-width:2px,color:#fff\n"
        
        # 遍歷父節點
        for p_key in curr['parents']:
            p_data = concepts_db.get(p_key)
            if p_data:
                mermaid_code += f"  {concept_key} --> {p_key}[{p_data['title']}]\n"
                mermaid_code += f"  style {p_key} fill:#F1F5F9,stroke:#2563EB,stroke-width:1px,color:#1E293B\n"

        # 透過 HTML 元件注入 Mermaid
        components.html(f"""
            <div class="mermaid" style="display:flex; justify-content:center; background: transparent;">
                {mermaid_code}
            </div>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{ 
                    startOnLoad: true, 
                    theme: 'neutral',
                    securityLevel: 'loose',
                    fontFamily: 'Noto Sans TC'
                }});
            </script>
        """, height=200)

    @staticmethod
    def exam_tips(concept_key, subject_name):
        """
        針對分科測驗高難度單元提供「考點直擊」與「常見陷阱」。
        """
        # 分科測驗專屬撇步庫
        tips_db = {
            # 數學甲/乙
            "ma_calculus_fundamental": "💡 **分科關鍵**：注意積分常數 $C$ 的處理，以及分段函數在銜接點是否連續。",
            "ma_complex_demoivre": "💡 **解題技巧**：看到複數的高次方，第一反應永遠是轉換成『極式』。",
            # 物理
            "phy_quantum_basics": "💡 **陷阱**：光電效應中，增加光強是增加『光子數量』，而非『單個光子的能量』。",
            "phy_em_induction_adv": "💡 **必考**：冷次定律本質上是能量守恆。感應電流的方向永遠在『反抗』磁通量的變化。",
            # 化學
            "chem_equilibrium_adv": "💡 **注意**：只有『溫度』會改變平衡常數 $K$。濃度與壓力的改變僅影響平衡移動方向。",
            "chem_organic_functional": "💡 **記憶法**：分科常考醇、醛、酸的氧化層級，注意反應條件是否需要強氧化劑。",
            # 公民
            "civ_constitutional_court": "💡 **法律更新**：注意《憲法訴訟法》實施後，大法官可審查『裁判憲法』，這是分科新重點。",
            "civ_market_failure": "💡 **經濟要點**：外部性問題要分清『社會成本』與『私部門成本』的差距。"
        }

        if concept_key in tips_db:
            st.warning(tips_db[concept_key])

    @staticmethod
    def ai_tutor_challenge(concept):
        """
        提供「素養導向」的深層提問，模擬分科測驗可能的探究與實作題型。
        """
        st.markdown("---")
        st.markdown("🤖 **AI 導師的深度思辨挑戰：**")
        
        # 範例挑戰問題 (可根據 concept_key 擴充)
        challenges = {
            "ma_derivative_logic": "如果你在路邊看到一條曲線，你如何僅透過觀察『凹向性』來預測這條曲線的二階導數正負？",
            "phy_thermo_kinetic": "為什麼在絕熱壓縮過程中，即便沒有加熱，氣體的溫度也會升高？試從分子撞擊的角度解釋。",
            "chem_molecular_structure": "為什麼水分子的鍵角約為 104.5 度，而非正四面體的 109.5 度？孤對電子的斥力扮演什麼角色？",
            "civ_electoral_systems": "如果你是一個小政黨的領袖，你會支持『並立制』還是『聯立制』？為什麼？"
        }
        
        challenge_text = challenges.get(st.session_state.current, f"思考一下：『{concept['title']}』的觀念如果套用到現實生活中的爭議問題，你會如何利用這個工具來分析？")
        st.write(f"*{challenge_text}*")

    @staticmethod
    def export_study_notes(history, current_key, concepts_db, subject_name):
        """
        自動化生成當前溯源路徑的 Markdown 複習筆記，方便學生下載。
        """
        full_path = history + [current_key]
        
        md_text = f"# 分科測驗深度複習筆記：{subject_name}\n\n"
        md_text += f"> 本筆記由【分科溯源探索器】自動生成。追蹤觀念地基，打通解題脈絡。\n\n---\n\n"
        
        for i, key in enumerate(full_path):
            c = concepts_db.get(key)
            if c:
                level_str = ["地基公理", "基礎銜接", "核心工具", "分科大魔王"][c['level']]
                md_text += f"## 第 {i+1} 階段：{c['emoji']} {c['title']} ({level_str})\n"
                md_text += f"- **摘要**: {c['summary']}\n"
                if c.get('formula'):
                    md_text += f"- **核心定義/公式**: `${c['formula']}$`\n"
                md_text += f"- **詳細解析**: {c['detail'].strip()}\n\n"
        
        md_text += "---\n**祝 考場發揮順利，金榜題名！**"

        st.download_button(
            label=f"📥 下載 {concepts_db[current_key]['title']} 複習筆記 (MD)",
            data=md_text,
            file_name=f"Advanced_Notes_{current_key}.md",
            mime="text/markdown",
            use_container_width=True
        )

    @staticmethod
    def learning_breadcrumb(history, current_key, concepts_db):
        """
        呼叫 Styles 模組渲染美化版的麵包屑導航。
        """
        history_titles = [concepts_db[h]['title'] for h in history]
        current_title = concepts_db[current_key]['title']
        st.markdown(styles.breadcrumb_html(history_titles, current_title), unsafe_allow_html=True)
