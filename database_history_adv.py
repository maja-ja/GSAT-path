# database_history_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (時代轉型與全球議題) ════════
    "his_modernity_global": {
        "level": 3, "title": "現代性的擴張與全球化", "emoji": "🌐", "color": "#E74C3C",
        "summary": "冷戰解體、去殖民化與全球一體化的挑戰",
        "detail": "分科測驗重點：探討二戰後解殖運動（Decolonization）如何重塑世界版圖。分析冷戰對峙下的意識型態競爭，以及 1990 年代後全球化如何衝擊民族國家的主權，並引發在地文化的認同危機。",
        "parents": ["his_cold_war_logic", "his_nationalism_adv"],
        "formula": r"\text{Modernity} = \text{Rationality} + \text{Capitalism} + \text{Nation-State}"
    },
    "his_east_west_collision": {
        "level": 3, "title": "東西方文明的衝突與交會", "emoji": "⛵", "color": "#D35400",
        "summary": "從絲路到條約體系：貿易、宗教與戰爭",
        "detail": "分科跨區域重點：比較傳統朝貢體系（Tributary System）與近代條約體系（Treaty System）的邏輯衝突。分析大航海時代後，全球貿易網如何將歐、亞、美洲連結，並探討西力東漸下東亞社會的制度轉型與陣痛。",
        "parents": ["his_maritime_trade", "his_imperialism_logic"],
        "formula": r"\text{Tributary System} \leftrightarrow \text{Sovereign Equality}"
    },
    "his_ideological_rev": {
        "level": 3, "title": "近代思想革命與社會劇變", "emoji": "📜", "color": "#C0392B",
        "summary": "啟蒙運動、馬克思主義與極權主義的興起",
        "detail": "分科思想重點：分析科學革命如何引發啟蒙運動對王權的質疑。探討工業革命後的社會不均如何孕育社會主義，並進一步連結到 20 世紀極權主義（Totalitarianism）對民主憲政的挑戰。",
        "parents": ["his_enlightenment", "his_industrial_logic"],
        "formula": r"\text{Liberty} + \text{Equality} \to \text{Democracy / Revolution}"
    },

    # ════════ LEVEL 2: 分科核心工具 (制度與框架) ════════
    "his_cold_war_logic": {
        "level": 2, "title": "冷戰兩極對抗架構", "emoji": "❄️", "color": "#9B59B6",
        "summary": "圍堵政策、代理人戰爭與核威懾",
        "detail": "理解美蘇對峙下的國際體制（如：北大西洋公約、華沙公約）。分析兩極體系如何影響第三世界國家的發展路徑。",
        "parents": ["his_ww_impact"],
        "formula": r"\text{USA (Liberalism)} \text{ vs } \text{USSR (Communism)}"
    },
    "his_nationalism_adv": {
        "level": 2, "title": "民族主義的演變", "emoji": "🚩", "color": "#9B59B6",
        "summary": "從想像的共同體到建國運動",
        "detail": "探討民族主義如何從 19 世紀的建國動力（如德、義統一），轉變為 20 世紀引發兩次世界大戰的激進力量。理解「國族」作為政治動員單位的建構過程。",
        "parents": ["his_nation_state_origin"],
        "formula": r"\text{Shared Identity} + \text{Political Sovereignty} = \text{Nation}"
    },
    "his_tributary_system": {
        "level": 2, "title": "傳統東亞朝貢秩序", "emoji": "🏯", "color": "#F39C12",
        "summary": "華夷之辨與冊封體制",
        "detail": "理解以中國為中心的宗藩關係。分析這種非平等、階層式的外交邏輯如何維繫了東亞數百年的區域穩定。",
        "parents": ["his_confucian_order"],
        "formula": r"\text{Center (Suzerain)} \leftrightarrow \text{Periphery (Vassal)}"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (重大轉折) ════════
    "his_enlightenment": {
        "level": 1, "title": "啟蒙運動與理性主義", "emoji": "💡", "color": "#BDC3C7",
        "summary": "天賦人權、社會契約與分權制衡",
        "detail": "洛克、孟德斯鳩、盧梭等人的思想，奠定了現代民主政治的憲法基礎。它是所有近代革命的火種。",
        "parents": ["his_scientific_rev"],
        "formula": r"\text{Reason} > \text{Tradition}"
    },
    "his_industrial_logic": {
        "level": 1, "title": "工業革命的動力", "emoji": "⚙️", "color": "#BDC3C7",
        "summary": "技術創新與資本累積",
        "detail": "從蒸汽機到自動化生產，工業革命不僅改變了生產方式，更重組了人類的城鄉比例與社會階級結構。",
        "parents": ["his_capitalism_origin"],
        "formula": r"\text{Machinery} + \text{Efficiency} = \text{Mass Production}"
    },

    # ════════ LEVEL 0: 終極基石 (歷史學公理) ════════
    "his_causality": {
        "level": 0, "title": "歷史因果邏輯", "emoji": "⏳", "color": "#7F8C8D",
        "summary": "變遷、延續與斷裂",
        "detail": "歷史學的第一核心：沒有一件事情是孤立發生的。所有的變遷都有其長程、中程與短程原因（Annales School 史學觀）。",
        "parents": [],
        "formula": r"\text{Context} \times \text{Event} = \text{Change}"
    },
    "his_evidence": {
        "level": 0, "title": "史料與歷史解釋", "emoji": "🔍", "color": "#7F8C8D",
        "summary": "證據、立場與多重敘事",
        "detail": "歷史學的公理：歷史不是過去發生的「事」，而是透過史料建構出來的「解釋」。需區分一手與二手史料，並察覺作者的立場偏見。",
        "parents": [],
        "formula": r"\text{Sources} + \text{Interpretation} = \text{History}"
    }
}
