# database_civics_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (複合實務與模型) ════════
    "civ_market_failure": {
        "level": 3, "title": "市場失靈與政府干預", "emoji": "📉", "color": "#E67E22",
        "summary": "當看不見的手失效時：外部性、公共財與資訊不對稱",
        "detail": "分科測驗核心：分析外部性（正/負）對社會福利的影響。探討為何市場無法達成效率分配，以及政府如何透過課稅（皮古稅）或補貼來矯正。",
        "parents": ["civ_market_equilibrium", "civ_social_welfare"],
        "formula": r"\text{Social Cost} = \text{Private Cost} + \text{External Cost}"
    },
    "civ_constitutional_court": {
        "level": 3, "title": "憲法法庭與人權保障", "emoji": "⚖️", "color": "#2980B9",
        "summary": "憲法訴訟法下的裁判憲法審查",
        "detail": "分科法律重點：大法官不再只是『釋憲』，而是可以針對『法院判決』進行審查。區分聲請要件、暫時處分與審理程序。",
        "parents": ["civ_rule_of_law", "civ_human_rights_adv"],
        "formula": "權力分立 + 權力制衡 = 法治國原則"
    },
    "civ_electoral_systems": {
        "level": 3, "title": "選舉制度與政黨體系", "emoji": "🗳️", "color": "#27AE60",
        "summary": "單一選區、比例代表與杜瓦傑法則",
        "detail": "政治學核心：選制如何影響政黨數量？分析『並立制』與『聯立制』的差異。計算分配席次時的門檻與剩餘餘數法。",
        "parents": ["civ_democratic_rep", "civ_political_parties"],
        "formula": "選制 → 政黨體系 (Duverger's Law)"
    },

    # ════════ LEVEL 2: 分科核心工具 (中階理論) ════════
    "civ_market_equilibrium": {
        "level": 2, "title": "市場均衡與變動", "emoji": "📊", "color": "#F39C12",
        "summary": "需求與供給的移動對價格的影響",
        "detail": "區分『需求量變動』（點的移動）與『需求變動』（線的移動）。分析政府價格上限與下限帶來的無謂損失。",
        "parents": ["civ_opportunity_cost"],
        "formula": r"Q_d = Q_s \implies \text{Equilibrium Price}"
    },
    "civ_social_welfare": {
        "level": 2, "title": "經濟效率與社會福利", "emoji": "💰", "color": "#F39C12",
        "summary": "消費者剩餘、生產者剩餘與總剩餘",
        "detail": "理解經濟效率的達成。探討市場干預（課稅、配額）如何導致無謂損失 (Deadweight Loss)。",
        "parents": ["civ_rational_choice"],
        "formula": r"CS + PS = \text{Social Welfare}"
    },
    "civ_rule_of_law": {
        "level": 2, "title": "法治國原則", "emoji": "📜", "color": "#3498DB",
        "summary": "法律保留、法律優位與正當法律程序",
        "detail": "形式法治國與實質法治國的區分。確保國家權力受到憲法與法律的嚴格約束，保障人民的基本權。",
        "parents": ["civ_legal_hierarchy"],
        "formula": "行政程序法 + 訴願法 + 行政訴訟法"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (基本功) ════════
    "civ_opportunity_cost": {
        "level": 1, "title": "機會成本與比較利益", "emoji": "🧠", "color": "#BDC3C7",
        "summary": "選擇的代價與專業化分工",
        "detail": "機會成本 = 外顯成本 + 隱含成本。比較利益原理是國際貿易的基礎。",
        "parents": ["civ_scarcity"],
        "formula": r"\text{OC} = \text{Explicit} + \text{Implicit}"
    },
    "civ_legal_hierarchy": {
        "level": 1, "title": "法律位階觀念", "emoji": "🏢", "color": "#BDC3C7",
        "summary": "憲法、法律與命令的層級",
        "detail": "根據凱爾森 (Kelsen) 的法位階理論，下位階律法不得牴觸上位階。",
        "parents": ["civ_human_dignity"],
        "formula": "憲法 > 法律 > 命令"
    },

    # ════════ LEVEL 0: 終極基石 (社會科學公理) ════════
    "civ_scarcity": {
        "level": 0, "title": "稀少性原理", "emoji": "🌫️", "color": "#7F8C8D",
        "summary": "慾望無限、資源有限",
        "detail": "經濟學的第一大公理。因為稀少，所以需要選擇，進而產生經濟學。",
        "parents": [],
        "formula": "慾望 > 資源"
    },
    "civ_human_dignity": {
        "level": 0, "title": "人性尊嚴與正義", "emoji": "♾️", "color": "#7F8C8D",
        "summary": "一切權利與憲法的最終根基",
        "detail": "法律與政治存在的終極目的：保障個人作為主體的人格尊嚴與自我實現。",
        "parents": [],
        "formula": "人為目的而非工具"
    }
}
