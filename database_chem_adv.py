# database_chem_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (進階定量與有機合成) ════════
    "chem_equilibrium_adv": {
        "level": 3, "title": "化學平衡與平衡常數", "emoji": "⚖️", "color": "#E74C3C",
        "summary": "平衡常數 K、勒沙特列原理與解離平衡",
        "detail": "分科測驗重點：掌握平衡常數 Kc 與 Kp 的轉換。理解勒沙特列原理中「壓力」、「濃度」與「溫度」對平衡移動的影響。計算弱酸弱鹼的多段解離、同離子效應與緩衝溶液的 pH 值變化。",
        "parents": ["chem_reaction_rates", "chem_stoichiometry_adv"],
        "formula": r"K = \frac{[C]^c [D]^d}{[A]^a [B]^b}"
    },
    "chem_organic_functional": {
        "level": 3, "title": "有機化合物與官能基反應", "emoji": "🧪", "color": "#D35400",
        "summary": "烴、醇、醚、醛、酮、酸、酯、胺、醯胺",
        "detail": "分科化學痛點：掌握有機物的命名與同分異構物。分析各官能基的特性反應（如：醇的氧化、酯化反應、銀鏡反應）。理解費雪酯化、皂化反應與聚合物（如蛋白質、尼龍）的合成路徑。",
        "parents": ["chem_molecular_structure", "chem_atomic_bonding"],
        "formula": r"R-COOH + R'-OH \to R-COOR' + H_2O"
    },
    "chem_electrochem_adv": {
        "level": 3, "title": "電化學與電解", "emoji": "🔋", "color": "#C0392B",
        "summary": "標準電極電位、法拉第電解定律與能斯特方程式",
        "detail": "分科電化學重點：區分伏打電池（自發）與電解池（非自發）。計算電解時析出的物質質量。分析電池的標準電位（E°）並判斷反應方向。",
        "parents": ["chem_redox_basic", "chem_stoichiometry_adv"],
        "formula": r"W = \frac{It}{F} \cdot \frac{M}{n} \quad \text{(Faraday's Law)}"
    },

    # ════════ LEVEL 2: 分科核心工具 (理論模型) ════════
    "chem_molecular_structure": {
        "level": 2, "title": "分子形狀與混成軌域", "emoji": "🪁", "color": "#F39C12",
        "summary": "VSEPR 理論、sp/sp2/sp3 混成軌域",
        "detail": "理解價殼層電子對斥力理論 (VSEPR)。判斷分子的幾何形狀（如：四面體、平面三角形、折線型）。分析中心原子的混成方式與 $\sigma$ 鍵、$\pi$ 鍵的數量。",
        "parents": ["chem_atomic_bonding", "chem_electron_config_adv"],
        "formula": r"AX_nE_m \text{ (VSEPR Type)}"
    },
    "chem_reaction_rates": {
        "level": 2, "title": "反應速率定律", "emoji": "⏱️", "color": "#F39C12",
        "summary": "速率常數 k、反應級數與碰撞理論",
        "detail": "分析濃度、溫度、催化劑對反應速率的影響。掌握阿瑞尼氏方程式與活化能 (Ea) 的概念。理解有效碰撞與反應位能圖的解析。",
        "parents": ["chem_stoichiometry_adv", "chem_energy_logic"],
        "formula": r"R = k[A]^m[B]^n"
    },
    "chem_stoichiometry_adv": {
        "level": 2, "title": "進階化學計量", "emoji": "🧮", "color": "#F39C12",
        "summary": "莫耳濃度、限量試劑與氣體定律 (PV=nRT)",
        "detail": "處理溶液稀釋、滴定計算以及理想氣體與分壓定律。這是所有定量化學反應的基礎計算工具。",
        "parents": ["chem_mole_concept"],
        "formula": r"PV = nRT"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (基本規律) ════════
    "chem_atomic_bonding": {
        "level": 1, "title": "化學鍵結觀念", "emoji": "🔗", "color": "#BDC3C7",
        "summary": "離子鍵、共價鍵與金屬鍵",
        "detail": "理解原子如何透過電子轉移或共用達成穩定。分析鍵能與分子間作用力（如氫鍵、凡得瓦力）對熔沸點的影響。",
        "parents": ["chem_electron_config_adv"],
        "formula": r"\text{Electronegativity Difference} \Delta EN"
    },
    "chem_redox_basic": {
        "level": 1, "title": "氧化還原基本原理", "emoji": "🔄", "color": "#BDC3C7",
        "summary": "氧化數的定義與得失電子",
        "detail": "判斷元素的氧化數。氧化是失去電子（氧化數上升），還原是得到電子（氧化數下降）。這是電池與防蝕技術的核心。",
        "parents": ["chem_electron_config_adv"],
        "formula": r"\text{Oxidation: loss of } e^-"
    },

    # ════════ LEVEL 0: 終極基石 (化學公理) ════════
    "chem_electron_config_adv": {
        "level": 0, "title": "原子構造與電子組態", "emoji": "⚛️", "color": "#7F8C8D",
        "summary": "量子數、軌域與週期律",
        "detail": "化學學科的最底層：s, p, d, f 軌域。遵循遞建原理、包立不相容原理與洪德定則。原子的電子排列決定了所有的化學性質。",
        "parents": [],
        "formula": r"1s^2 2s^2 2p^6 \dots"
    },
    "chem_energy_logic": {
        "level": 0, "title": "能量與質量守恆", "emoji": "🌡️", "color": "#7F8C8D",
        "summary": "反應熱、赫斯定律與熱力學第一定律",
        "detail": "所有化學變化的基礎公理：質量不滅與能量守恆。能量總是以熱或功的形式交換。理解狀態函數的概念。",
        "parents": [],
        "formula": r"\Delta H = H_{products} - H_{reactants}"
    },
    "chem_mole_concept": {
        "level": 0, "title": "莫耳與粒子數", "emoji": "🧱", "color": "#7F8C8D",
        "summary": "亞佛加厥數與物質的量",
        "detail": "連結微觀粒子與宏觀質量的橋樑。1 mole = $6.02 \times 10^{23}$ 個粒子。這是化學計量的起點。",
        "parents": [],
        "formula": r"n = \frac{W}{M}"
    }
}
