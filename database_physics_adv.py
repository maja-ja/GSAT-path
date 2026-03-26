# database_physics_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (近代物理與電磁場系統) ════════
    "phy_quantum_basics": {
        "level": 3, "title": "量子現象與原子結構", "emoji": "⚛️", "color": "#6200EA",
        "summary": "光電效應、物質波與波耳原子模型",
        "detail": "分科測驗重點：掌握愛因斯坦光電方程式 $E_k = hf - W$。理解德布羅意物質波長 $\lambda = h/p$。分析波耳氫原子模型的能階躍遷、角動量量子化與光譜頻率計算。",
        "parents": ["phy_wave_particle", "phy_electrostatics_adv"],
        "formula": r"hf = \Phi + \frac{1}{2}mv_{max}^2"
    },
    "phy_em_induction_adv": {
        "level": 3, "title": "電磁感應與馬克士威方程", "emoji": "🧲", "color": "#311B92",
        "summary": "法拉第定律、冷次定律與渦電流",
        "detail": "分科物理核心：計算變化的磁場產生的感應電動勢 $\mathcal{E}$。理解導線在磁場中運動切割磁力線產生的動生電動勢 $BLv$。深入分析電磁感應如何體現能量守恆（冷次定律）。",
        "parents": ["phy_magnetism_adv", "phy_energy_conservation"],
        "formula": r"\mathcal{E} = -N \frac{\Delta \Phi_B}{\Delta t}"
    },
    "phy_thermo_kinetic": {
        "level": 3, "title": "熱力學與氣體動力論", "emoji": "🔥", "color": "#B71C1C",
        "summary": "理想氣體、分子平均動能與熱力學第一定律",
        "detail": "分科物理重點：從微觀角度推導壓力 $P = \frac{1}{3} \rho v^2$。理解溫度與分子平均平移動能的關係 $\overline{E_k} = \frac{3}{2}kT$。掌握熱力學第一定律 $\Delta U = Q - W$ 在等壓、等溫、絕熱過程的應用。",
        "parents": ["phy_mechanics_logic", "phy_energy_conservation"],
        "formula": r"PV = nRT, \quad \Delta U = Q - W"
    },

    # ════════ LEVEL 2: 分科核心工具 (進階力學與場論) ════════
    "phy_circular_gravity": {
        "level": 2, "title": "圓周運動與萬有引力", "emoji": "🪐", "color": "#1976D2",
        "summary": "向心力、克普勒定律與衛星能量",
        "detail": "分析變速率圓周運動與切線加速度。掌握克普勒三大定律。計算衛星在軌道的動能、位能與總能量（束縛能）。理解逃逸速度的由來。",
        "parents": ["phy_mechanics_logic", "phy_field_concept"],
        "formula": r"a_c = \frac{v^2}{r} = \omega^2 r, \quad F = G\frac{Mm}{r^2}"
    },
    "phy_electrostatics_adv": {
        "level": 2, "title": "進階靜電學", "emoji": "⚡", "color": "#0288D1",
        "summary": "電場、電位與電位能",
        "detail": "理解點電荷、平行板與均勻帶電球殼的電場分布。計算電荷移動時的電位能變化 $\Delta U = q\Delta V$。理解等位面的幾何性質與電場線的關係。",
        "parents": ["phy_field_concept", "phy_energy_conservation"],
        "formula": r"V = \frac{kQ}{r}, \quad E = -\frac{\Delta V}{\Delta d}"
    },
    "phy_magnetism_adv": {
        "level": 2, "title": "電流磁效應與磁力", "emoji": "🌀", "color": "#0097A7",
        "summary": "必歐-沙伐定律、安培定律與勞倫茲力",
        "detail": "計算長直導線、圓形線圈與螺線管產生的磁場。分析帶電粒子在均勻磁場中的圓周運動軌跡。掌握磁力 $F = qvB\sin\theta$ 的方向判斷（右手定則）。",
        "parents": ["phy_field_concept", "phy_mechanics_logic"],
        "formula": r"F = q(\vec{E} + \vec{v} \times \vec{B})"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (牛頓體系) ════════
    "phy_mechanics_logic": {
        "level": 1, "title": "牛頓運動定律與衝量", "emoji": "🍎", "color": "#78909C",
        "summary": "力、質量與加速度的關係",
        "detail": "物體運動的基礎：$F=ma$。分析受力圖（Free Body Diagram）。理解衝量 $\vec{J} = \Delta \vec{p}$ 如何改變動量。這是所有經典物理問題的分析起點。",
        "parents": ["phy_space_time"],
        "formula": r"\vec{F} = \frac{d\vec{p}}{dt}"
    },
    "phy_wave_particle": {
        "level": 1, "title": "波動與光學基礎", "emoji": "🌊", "color": "#78909C",
        "summary": "干涉、繞射與折射",
        "detail": "理解波動的疊加原理。掌握雙狹縫干涉與單狹縫繞射的條紋分佈規律。理解光的反射與折射（司乃耳定律）。",
        "parents": ["phy_field_concept"],
        "formula": r"v = f\lambda, \quad n_1\sin\theta_1 = n_2\sin\theta_2"
    },

    # ════════ LEVEL 0: 終極基石 (物理公理與守恆律) ════════
    "phy_energy_conservation": {
        "level": 0, "title": "能量與動量守恆", "emoji": "♾️", "color": "#455A64",
        "summary": "物理學的第一性原理",
        "detail": "物理世界最底層的法則：守恆律。無論系統如何演化，孤立系統的能量與動量總量保持不變。這與時空的對稱性（諾特定理）密切相關。",
        "parents": [],
        "formula": r"E_1 = E_2, \quad \vec{p}_1 = \vec{p}_2"
    },
    "phy_field_concept": {
        "level": 0, "title": "場與交互作用", "emoji": "🌐", "color": "#455A64",
        "summary": "力在空間中的傳遞媒介",
        "detail": "物理學的核心假設：超距力是透過「場」（電場、磁場、重力場）來傳遞的。場的性質決定了物質間的交互作用。結構決定了宇宙的層次。",
        "parents": [],
        "formula": r"\vec{F} = q\vec{E}, \quad \vec{F} = m\vec{g}"
    },
    "phy_space_time": {
        "level": 0, "title": "時空與座標系", "emoji": "🕙", "color": "#455A64",
        "summary": "物理事件發生的舞台",
        "detail": "物理觀測的基礎：長度、時間與質量的定義。在慣性座標系中，物理定律具有相同的形式。這是所有運動學與動力學的先驗條件。",
        "parents": [],
        "formula": r"\Delta x, \Delta t"
    }
}
