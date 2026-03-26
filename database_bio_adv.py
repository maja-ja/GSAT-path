# database_bio_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (現代生技與複雜生理) ════════
    "bio_biotech_adv": {
        "level": 3, "title": "現代生物技術：基因工程", "emoji": "🧬", "color": "#27AE60",
        "summary": "PCR、DNA 測序與 CRISPR 基因編輯",
        "detail": "分科測驗重點：掌握聚合酶連鎖反應 (PCR) 的步驟（變性、黏合、延伸）。理解限制酶與連接酶如何構建重組 DNA。探討如何利用質體作為載體進行轉殖，並進行篩選（如抗生素抗性篩選）。",
        "parents": ["bio_central_dogma", "bio_dna_structure"],
        "formula": r"2^n \text{ (PCR 擴增倍數)}"
    },
    "bio_nervous_signal": {
        "level": 3, "title": "神經衝動與動作電位", "emoji": "🧠", "color": "#16A085",
        "summary": "去極化、再極化與突觸傳遞",
        "detail": "分科生理重點：分析 Na+ 與 K+ 離子通道的開閉順序如何產生動作電位。掌握全有全無律 (All-or-none law)。理解神經傳遞物在突觸間隙的釋放與受體結合過程，以及 EPSP 與 IPSP 的整合。",
        "parents": ["bio_cell_membrane_transport", "bio_homeostasis"],
        "formula": r"E = \frac{RT}{zF} \ln \frac{[ion]_{out}}{[ion]_{in}} \text{ (Nernst eq.)}"
    },
    "bio_plant_hormones": {
        "level": 3, "title": "植物激素與發育調節", "emoji": "🌱", "color": "#2ECC71",
        "summary": "生長素、吉貝素、離層酸與開花素",
        "detail": "分科植物學痛點：區分不同激素對生長的促進或抑制作用。分析植物對光的反應（光週期現象）與開花素 (Florigen) 的運輸。理解種子萌發中吉貝素與離層酸的拮抗作用。",
        "parents": ["bio_cell_signaling", "bio_metabolism_basics"],
        "formula": r"\text{Pr} \leftrightarrow \text{Pfr} \text{ (光敏素轉化)}"
    },

    # ════════ LEVEL 2: 分科核心工具 (核心機制) ════════
    "bio_central_dogma": {
        "level": 2, "title": "分子生物學中心教條", "emoji": "🧵", "color": "#1ABC9C",
        "summary": "DNA 複製、轉錄與轉譯",
        "detail": "理解遺傳訊息如何從 DNA 傳遞至 RNA，最後合成蛋白質。掌握密碼子 (Codon) 與反密碼子的配對，以及內含子 (Intron) 的修飾剪接。",
        "parents": ["bio_dna_structure", "bio_proteins"],
        "formula": r"\text{DNA} \to \text{RNA} \to \text{Protein}"
    },
    "bio_energy_coupling": {
        "level": 2, "title": "能量耦合：光合與呼吸作用", "emoji": "🔋", "color": "#27AE60",
        "summary": "電子傳遞鏈與 ATP 合成",
        "detail": "分析葉綠體與線粒體中如何透過質子梯度 (H+) 驅動 ATP 合成酶。掌握卡爾文循環與克雷伯氏循環的碳流向。",
        "parents": ["bio_redox_logic", "bio_cell_organelles"],
        "formula": r"C_6H_{12}O_6 + 6O_2 \to 6CO_2 + 6H_2O + \text{ATP}"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (生命活動基礎) ════════
    "bio_cell_membrane_transport": {
        "level": 1, "title": "細胞膜與運輸", "emoji": "⚓", "color": "#95A5A6",
        "summary": "擴散、促進擴散與主動運輸",
        "detail": "理解流體鑲嵌模型。區分耗能（主動）與不耗能（被動）的物質跨膜方式。",
        "parents": ["bio_homeostasis"],
        "formula": r"\Delta C \to \text{Diffusion}"
    },
    "bio_dna_structure": {
        "level": 1, "title": "核酸分子結構", "emoji": "🥨", "color": "#95A5A6",
        "summary": "雙螺旋、鹼基配對與去氧核糖",
        "detail": "理解查加夫法則 (A=T, G=C)。DNA 的反向平行結構 (5' to 3') 是複製與轉錄的物理基礎。",
        "parents": ["bio_biomolecules"],
        "formula": r"A+G = T+C"
    },

    # ════════ LEVEL 0: 終極基石 (生命科學公理) ════════
    "bio_homeostasis": {
        "level": 0, "title": "恆定性公理", "emoji": "⚖️", "color": "#7F8C8D",
        "summary": "維持內環境溫定的動態平衡",
        "detail": "所有生理活動的核心目的：透過負回饋控制，維持溫度、pH值、血糖與水分的穩定。",
        "parents": [],
        "formula": r"\text{Input} \to \text{Sensor} \to \text{Effector} \to \text{Response}"
    },
    "bio_biomolecules": {
        "level": 0, "title": "生物分子本質", "emoji": "🧱", "color": "#7F8C8D",
        "summary": "碳骨架與官能基的組合",
        "detail": "生命是由碳、氫、氧、氮、磷、硫組成的有序系統。結構決定功能。",
        "parents": [],
        "formula": r"C_x(H_2O)_y, \text{R-CH(NH}_2\text{)COOH}"
    }
}
