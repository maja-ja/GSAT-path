# database_math_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (進階分析與運算) ════════
    "ma_calculus_fundamental": {
        "level": 3, "title": "微積分基本定理與應用", "emoji": "📉", "color": "#E74C3C",
        "summary": "微分與積分的橋樑：求曲線下圍成面積",
        "detail": "分科測驗核心：理解微分與積分互為逆運算。掌握定積分的計算步驟。應用於求旋轉體體積（數甲）、函數曲線下的面積，以及變率問題的求值。",
        "parents": ["ma_derivative_logic", "ma_limit_continuity"],
        "formula": r"\int_a^b f(x) dx = F(b) - F(a), \text{ where } F'(x) = f(x)"
    },
    "ma_complex_demoivre": {
        "level": 3, "title": "複數極式與棣美弗定理", "emoji": "🌀", "color": "#E67E22",
        "summary": "複數平面的旋轉與伸縮運算",
        "detail": "分科數學重點：將複數表示為 $r(\cos \theta + i \sin \theta)$。掌握棣美弗定理來計算複數的高次方。理解複數乘法在幾何上代表的『旋轉』與『伸縮』意義，以及 n 次方根在單位圓上的分佈。",
        "parents": ["ma_trig_functions", "ma_real_numbers"],
        "formula": r"[r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i \sin n\theta)"
    },
    "ma_random_variable": {
        "level": 3, "title": "離散隨機變數與期望值", "emoji": "🎲", "color": "#D35400",
        "summary": "機率分佈、變異數與標準差",
        "detail": "分科統計重點：建立機率質量函數 (PMF)。計算期望值 $E(X)$、變異數 $Var(X)$。掌握二項分佈及其性質。理解大數法則與信心水準在統計推論中的意義。",
        "parents": ["ma_classic_prob", "ma_sigma_logic"],
        "formula": r"E(X) = \sum p_i x_i, \quad Var(X) = E(X^2) - [E(X)]^2"
    },

    # ════════ LEVEL 2: 分科核心工具 (函數與變換) ════════
    "ma_derivative_logic": {
        "level": 2, "title": "導數與導函數", "emoji": "📈", "color": "#F39C12",
        "summary": "瞬時變化率與切線斜率",
        "detail": "理解導數的定義。掌握多項式函數、連鎖律的微分法則。利用一階導函數判斷增減性，二階導函數判斷凹向性與反曲點，進而描繪函數圖形。",
        "parents": ["ma_limit_continuity", "ma_poly_functions"],
        "formula": r"f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}"
    },
    "ma_matrix_transform": {
        "level": 2, "title": "矩陣與線性變換", "emoji": "🧱", "color": "#F39C12",
        "summary": "二階矩陣、旋轉、鏡射與伸縮",
        "detail": "掌握矩陣乘法。理解線性變換矩陣對平面向量的作用。特別注意旋轉矩陣、鏡射矩陣的構造，以及矩陣的反矩陣與行列式 (det) 的意義。",
        "parents": ["ma_plane_vector", "ma_real_numbers"],
        "formula": r"\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \begin{bmatrix}"
    },
    "ma_trig_functions": {
        "level": 2, "title": "三角函數的性質與圖形", "emoji": "🌊", "color": "#F39C12",
        "summary": "正弦波、週期、振幅與相位",
        "detail": "掌握 $y = A \sin(\omega x + \phi)$ 的圖形特徵。理解和差角公式、倍角公式。這是處理複數平面與微積分中三角換元的基礎。",
        "parents": ["ma_trig_laws", "ma_real_numbers"],
        "formula": r"\sin(A+B) = \sin A \cos B + \cos A \sin B"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (單元工具) ════════
    "ma_limit_continuity": {
        "level": 1, "title": "極限與連續性", "emoji": "🧮", "color": "#BDC3C7",
        "summary": "數列與函數趨近某值的行為",
        "detail": "理解極限的基本運算法則。掌握無窮等比數列的收斂條件。定義函數在某點連續的三要件：極限存在、函數值存在、兩者相等。",
        "parents": ["ma_real_numbers", "ma_poly_functions"],
        "formula": r"\lim_{x \to a} f(x) = L"
    },
    "ma_plane_vector": {
        "level": 1, "title": "平面向量與內積", "emoji": "➡️", "color": "#BDC3C7",
        "summary": "有向線段的代數與幾何意義",
        "detail": "向量的加減法與係數積。內積定義 $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}| \cos \theta$。這是一切線性變換與空間幾何的地基。",
        "parents": ["ma_real_numbers"],
        "formula": r"\vec{u} \cdot \vec{v} = x_1x_2 + y_1y_2"
    },

    # ════════ LEVEL 0: 終極基石 (數學公理) ════════
    "ma_real_numbers": {
        "level": 0, "title": "實數系與邏輯", "emoji": "♾️", "color": "#7F8C8D",
        "summary": "數學運算的最終邊界",
        "detail": "數學的最底層：有理數、無理數的完備性。包含絕對值、不等式基本性質、以及邏輯上的充分必要條件。",
        "parents": [],
        "formula": r"a, b \in \mathbb{R}"
    },
    "ma_poly_functions": {
        "level": 0, "title": "多項式基礎", "emoji": "🔢", "color": "#7F8C8D",
        "summary": "代數運算的起點",
        "detail": "函數的概念、多項式除法、餘式定理。這是進入微積分與進階代數的門票。",
        "parents": ["ma_real_numbers"],
        "formula": r"f(x) = a_n x^n + \dots + a_0"
    }
}
