import streamlit as st
import streamlit.components.v1 as components

class GSATExtensions:
    
    @staticmethod
    def exam_alert(concept_key):
        """針對學測常考點與易錯陷阱提供警示"""
        traps = {
            "spatial_geometry": "🚨 **大考陷阱**：空間中「兩不平行直線」不一定相交！別忘了還有『歪斜線』的存在。",
            "conditional_prob_bayes": "🚨 **大考陷阱**：貝氏定理的分母是『所有導致結果的路徑總和』，畫樹狀圖最保險！",
            "log_modeling": "🚨 **計算小撇步**：學測對數題常給 log 2 ≈ 0.3010，計算時要注意題目要求取到小數第幾位。",
            "data_analysis": "🚨 **概念釐清**：相關係數 r 受『線性變換』影響嗎？記住：標準化後不變！",
            "trig_laws": "🚨 **解題關鍵**：看到『外接圓半徑 R』，90% 優先考慮正弦定理。",
            "poly_division": "🚨 **注意**：使用餘式定理 f(a) 時，除式必須是一次式 (x-a)。"
        }
        
        if concept_key in traps:
            st.info(traps[concept_key])

    @staticmethod
    def render_local_graph(concept_key, concepts_db):
        """繪製當前觀念與其上方基礎觀念的相依圖"""
        curr = concepts_db.get(concept_key)
        if not curr or not curr['parents']:
            return

        # 建立 Mermaid 語法
        # graph BT 表示 Bottom to Top (由下往上追溯)
        mermaid_code = "graph BT\n"
        style_code = ""
        
        # 加入當前節點
        mermaid_code += f"  {concept_key}[{curr['title']}]\n"
        style_code += f"  style {concept_key} fill:{curr['color']},stroke:#fff,stroke-width:2px,color:#fff\n"
        
        # 加入父節點
        for p_key in curr['parents']:
            p_data = concepts_db.get(p_key)
            if p_data:
                mermaid_code += f"  {concept_key} --> {p_key}[{p_data['title']}]\n"
                style_code += f"  style {p_key} fill:{p_data['color']}44,stroke:{p_data['color']},stroke-width:1px\n"

        # 渲染組件
        components.html(f"""
            <div class="mermaid" style="display:flex; justify-content:center;">
                {mermaid_code}
                {style_code}
            </div>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{ startOnLoad: true, theme: 'neutral', securityLevel: 'loose' }});
            </script>
        """, height=180)

    @staticmethod
    def ai_tutor_challenge(concept):
        """提供素養導向的深度思考題"""
        st.markdown("---")
        st.markdown(f"🤖 **AI 導師的深度挑戰：**")
        
        challenges = {
            "vector_inner_product": f"如果兩向量的內積為 0，在幾何上代表垂直；但在物理功的定義中，這代表什麼意思？",
            "exp_log_basic": f"為什麼對數的底數不能是 1？如果底數是 1，圖形會變成什麼樣子？",
            "classic_prob": f"『中獎率 1/100 的彩券買 100 張，必中一張』這個說法錯在哪？如何用觀念反駁？",
            "real_numbers": f"為什麼 √2 不能表示成分數？試著回想國中老師提過的『無理數』定義。"
        }
        
        challenge_text = challenges.get(st.session_state.current, f"如果你要考考同學關於『{concept['title']}』的定義，你會出哪一題？")
        st.write(f"*{challenge_text}*")

    @staticmethod
    def export_study_notes(history, current_key, concepts_db):
        """將溯源路徑匯出為 Markdown 學習筆記"""
        full_path = history + [current_key]
        
        note_content = f"# 學測數學觀念溯源筆記\n\n"
        note_content += f"**探索日期**: 2024年 學測衝刺期\n\n---\n\n"
        
        for i, key in enumerate(full_path):
            c = concepts_db[key]
            note_content += f"### 【階段 {i+1}】 {c['title']}\n"
            note_content += f"- **核心定義**: {c['summary']}\n"
            if c.get('formula'):
                note_content += f"- **關鍵公式**: `{c['formula']}`\n"
            note_content += f"- **重點筆記**: {c['detail'].strip()}\n\n"
            
        note_content += "\n---\n*本筆記由學測數學溯源探索器自動生成，祝金榜題名！*"

        st.download_button(
            label="📥 下載本次複習筆記 (Markdown)",
            data=note_content,
            file_name=f"GSAT_Math_{concepts_db[current_key]['title']}.md",
            mime="text/markdown",
            use_container_width=True
        )

    @staticmethod
    def learning_breadcrumb(history, current_key, concepts_db):
        """美化版麵包屑導航"""
        import styles
        steps = []
        for h_key in history:
            steps.append(styles.breadcrumb_step(concepts_db[h_key]['title']))
        steps.append(styles.breadcrumb_step(f"🎯 {concepts_db[current_key]['title']}"))
        
        st.markdown(f'<div class="breadcrumb-box">{" ➔ ".join(steps)}</div>', unsafe_allow_html=True)
