# database.py

# ─────────────────────────────────────────────────────────────────────────────
# 學測數學 108 課綱知識圖譜
# ─────────────────────────────────────────────────────────────────────────────

CONCEPTS = {
    # ════════ LEVEL 0: 數學地基 (國中銜接與高一基礎) ════════
    "real_numbers": {
        "level": 0, "title": "實數與數線", "emoji": "📏", "color": "#FFD700",
        "summary": "數的分類、絕對值與分點公式",
        "detail": "學測第一冊的核心。包含無理數的估計（如 √2, √3）、算幾不等式、以及絕對值方程式的幾何意義。",
        "parents": [],
        "formula": r"\frac{a+b}{2} \ge \sqrt{ab} \quad (a, b \ge 0)"
    },
    "logic_sets": {
        "level": 0, "title": "邏輯與集合", "emoji": "💡", "color": "#FFD700",
        "summary": "集合運算與充分必要條件",
        "detail": "理解『且』(and)、『或』(or)、『若 P 則 Q』。這是所有數學題目敘述的邏輯基礎。",
        "parents": [],
        "formula": r"A \cap B, \ A \cup B, \ P \implies Q"
    },
    "pythagorean": {
        "level": 0, "title": "畢氏定理與直角三角形", "emoji": "📐", "color": "#FFD700",
        "summary": "邊角關係的起點",
        "detail": "國中幾何的精髓，延伸至高中的三角函數與向量長度公式。",
        "parents": [],
        "formula": r"a^2 + b^2 = c^2"
    },

    # ════════ LEVEL 1: 高一核心單元 (單一觀念) ════════
    "quadratic_func": {
        "level": 1, "title": "二次函數", "emoji": "📉", "color": "#C8A0FF",
        "summary": "拋物線的平移與極值",
        "detail": "配方法、頂點座標、對稱軸。學測常考拋物線與直線的交點個數（判別式）。",
        "parents": ["real_numbers"],
        "formula": r"y = a(x-h)^2 + k"
    },
    "poly_division": {
        "level": 1, "title": "多項式除法原理", "emoji": "➗", "color": "#C8A0FF",
        "summary": "餘式定理與因式定理",
        "detail": "學測必考單元。理解 f(a) 即為 f(x) 除以 (x-a) 的餘式。常用於處理高次多項式的求值。",
        "parents": ["real_numbers"],
        "formula": r"f(x) = (x-a)q(x) + f(a)"
    },
    "exp_log_basic": {
        "level": 1, "title": "指對數基本運算", "emoji": "🪵", "color": "#C8A0FF",
        "summary": "換底公式與指對數性質",
        "detail": "處理極大或極小數字的工具。換底公式是學測計算對數題目的標準動作。",
        "parents": ["real_numbers"],
        "formula": r"\log_a b = \frac{\log_c b}{\log_c a}"
    },

    # ════════ LEVEL 2: 高二核心工具 (解題工具) ════════
    "trig_laws": {
        "level": 2, "title": "正餘弦定理", "emoji": "🏹", "color": "#50C8FF",
        "summary": "解三角形的邊角關係",
        "detail": "只要看到題目給兩邊一夾角，或三邊長求角度，必想餘弦定理；看到外接圓半徑或對邊對角關係，必想正弦定理。",
        "parents": ["pythagorean", "quadratic_func"],
        "formula": r"a^2 = b^2 + c^2 - 2bc \cos A"
    },
    "vector_inner_product": {
        "level": 2, "title": "平面向量內積", "emoji": "➡️", "color": "#50C8FF",
        "summary": "長度、夾角與投影",
        "detail": "內積是向量運算的靈魂。定義為長度乘長度乘 cosθ。常用於求兩直線夾角或垂直判定。",
        "parents": ["pythagorean", "real_numbers"],
        "formula": r"\vec{u} \cdot \vec{v} = |\vec{u}||\vec{v}| \cos \theta"
    },
    "classic_prob": {
        "level": 2, "title": "古典機率與排列組合", "emoji": "🎲", "color": "#50C8FF",
        "summary": "樣本空間與事件機率",
        "detail": "計算『所有可能情形』分之『目標情形』。需熟練 C(n,k) 與 P(n,k) 的選取邏輯。",
        "parents": ["logic_sets"],
        "formula": r"P(A) = \frac{n(A)}{n(S)}"
    },

    # ════════ LEVEL 3: 學測大考魔王 (複合考點) ════════
    "spatial_geometry": {
        "level": 3, "title": "空間中的平面與直線", "emoji": "📦", "color": "#7AFFCC",
        "summary": "空間向量的綜合應用",
        "detail": "學測最難的幾何題。需同時運用向量外積找法向量、兩面角公式、以及點到平面的距離公式。",
        "parents": ["vector_inner_product", "trig_laws"],
        "formula": r"E: ax + by + cz = d"
    },
    "conditional_prob_bayes": {
        "level": 3, "title": "條件機率與貝氏定理", "emoji": "🧠", "color": "#7AFFCC",
        "summary": "分層機率與資訊更新",
        "detail": "經典題型：抽血檢驗準確率、三門問題。關鍵在於縮小樣本空間至已知事件發生後的情況。",
        "parents": ["classic_prob", "logic_sets"],
        "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)}"
    },
    "log_modeling": {
        "level": 3, "title": "指對數應用模型", "emoji": "🌋", "color": "#7AFFCC",
        "summary": "複利、半衰期與地震強度",
        "detail": "學測最愛考的素養題。將現實生活中的增長（如人口、地震能量、分貝）轉化為對數函數進行運算。",
        "parents": ["exp_log_basic", "quadratic_func"],
        "formula": r"M = \frac{2}{3} \log \frac{E}{E_0}"
    },
    "data_analysis": {
        "level": 3, "title": "數據分析與常態分佈", "emoji": "📊", "color": "#7AFFCC",
        "summary": "相關係數與信賴區間",
        "detail": "理解迴歸直線的斜率意義、標準化 (Z-score) 的性質。以及 68-95-99.7 法則在信賴區間的應用。",
        "parents": ["real_numbers", "classic_prob"],
        "formula": r"y - \mu_y = r \frac{\sigma_y}{\sigma_x} (x - \mu_x)"
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# 輔助工具函式
# ─────────────────────────────────────────────────────────────────────────────

def get_concept(key):
    """取得單一觀念資料"""
    return CONCEPTS.get(key)

def get_entry_points():
    """獲取 Level 3 (學測魔王考點) 作為首頁起始點"""
    return [k for k, v in CONCEPTS.items() if v['level'] == 3]

def search_concepts(query):
    """搜尋關鍵字"""
    if not query:
        return []
    query = query.lower()
    results = []
    for k, v in CONCEPTS.items():
        if query in v['title'].lower() or query in v['summary'].lower():
            results.append(k)
    return results

def get_path_to_axiom(key):
    """
    計算某個概念到 Level 0 的最短路徑長度 (用於進度條)
    """
    concept = CONCEPTS.get(key)
    if not concept or not concept['parents']:
        return 0
    return 1 + max(get_path_to_axiom(p) for p in concept['parents'])
