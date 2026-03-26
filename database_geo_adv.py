# database_geo_adv.py

CONCEPTS = {
    # ════════ LEVEL 3: 分科大考魔王 (空間分析與全球系統) ════════
    "geo_gis_modeling": {
        "level": 3, "title": "GIS 空間分析與建模", "emoji": "💻", "color": "#27AE60",
        "summary": "向量與網格的運算：疊圖、環域與路徑分析",
        "detail": "分科測驗核心：不只是辨識 GIS 功能，而是分析運算邏輯。例如：如何利用『環域分析』結合『疊圖分析』找出符合特定條件的連鎖店選址？區分向量數據（精確邊界）與網格數據（連續變化）的適用性。",
        "parents": ["geo_spatial_data", "geo_map_projection"],
        "formula": r"\text{Raster Output} = \sum (\text{Layer}_i \times \text{Weight}_i)"
    },
    "geo_global_climate": {
        "level": 3, "title": "全球氣候變遷與環流系統", "emoji": "🌪️", "color": "#2980B9",
        "summary": "行星風系、洋流與極端氣候（聖嬰現象）",
        "detail": "分科氣候重點：分析沃克環流（Walker Circulation）的強弱如何導致聖嬰與反聖嬰現象。理解行星風系隨季節偏移對各緯度氣候區（如地中海型、熱帶莽原）的動態影響。",
        "parents": ["geo_atmospheric_circ", "geo_energy_balance"],
        "formula": r"\text{Heat Surplus} \to \text{Circulation} \to \text{Heat Deficit}"
    },
    "geo_industrial_chain": {
        "level": 3, "title": "全球在地化與產業空間分工", "emoji": "🏭", "color": "#E67E22",
        "summary": "新國際分工、後福特主義與全球價值鏈",
        "detail": "分科產業重點：探討科技產業如何透過『全球在地化』調整產品以適應市場。分析研發（核心）、零件供應（半邊陲）與組裝（邊陲）的空間位移與區域發展不均問題。",
        "parents": ["geo_industrial_location", "geo_globalization_logic"],
        "formula": "Value Chain = R&D + Branding > Manufacturing"
    },

    # ════════ LEVEL 2: 分科核心工具 (理論模型) ════════
    "geo_atmospheric_circ": {
        "level": 2, "title": "大氣環流三胞環模型", "emoji": "☁️", "color": "#3498DB",
        "summary": "哈德里環流、費瑞爾環流與極地環流",
        "detail": "理解科氏力如何將熱力環流切割為三胞環。掌握副熱帶高壓帶與西風帶、信風帶的成因與空間分布。",
        "parents": ["geo_coriolis_force", "geo_energy_balance"],
        "formula": r"f = 2\Omega \sin \phi \quad \text{(Coriolis)}"
    },
    "geo_industrial_location": {
        "level": 2, "title": "工業區位理論", "emoji": "📍", "color": "#D35400",
        "summary": "韋伯區位論：運輸、勞工與集結指向",
        "detail": "分析原料指數 (Material Index) 對工廠區位的影響。理解現代產業如何從『成本導向』轉向『市場與資訊導向』。",
        "parents": ["geo_economic_rationality"],
        "formula": r"\text{Total Cost} = \text{Transp.} + \text{Labor} - \text{Agglomeration}"
    },
    "geo_map_projection": {
        "level": 2, "title": "地圖投影與幾何變形", "emoji": "🗺️", "color": "#16A085",
        "summary": "麥卡托、正距、等積投影的取捨",
        "detail": "探討圓柱、圓錐、平面投影在角度、面積、距離上的形變。理解 GIS 中座標轉換的核心邏輯。",
        "parents": ["geo_spatial_logic"],
        "formula": r"R \times \cos \phi \cdot \Delta \lambda"
    },

    # ════════ LEVEL 1: 學測基礎銜接 (基本規律) ════════
    "geo_spatial_data": {
        "level": 1, "title": "空間資料結構", "emoji": "💾", "color": "#BDC3C7",
        "summary": "向量格式 (Vector) 與網格格式 (Raster)",
        "detail": "向量以點、線、面紀錄幾何資訊；網格以像素像素紀錄屬性值。這是 GIS 運算的物理基礎。",
        "parents": ["geo_spatial_logic"],
        "formula": "Attribute + Geometry = Spatial Data"
    },
    "geo_energy_balance": {
        "level": 1, "title": "能量平衡與輻射收支", "emoji": "☀️", "color": "#BDC3C7",
        "summary": "太陽短波輻射與地面長波輻射",
        "detail": "理解溫室效應與地球熱平衡。高低緯度間的輻射盈虧是驅動大氣與海洋環流的根本動力。",
        "parents": ["geo_system_logic"],
        "formula": r"\text{Net Radiation} = I_{in} - I_{out}"
    },

    # ════════ LEVEL 0: 終極基石 (地理學公理) ════════
    "geo_spatial_logic": {
        "level": 0, "title": "空間位置與距離", "emoji": "📍", "color": "#7F8C8D",
        "summary": "絕對位置、相對位置與時空壓縮",
        "detail": "地理學的第一定律：萬物皆相關，但近處之物比遠處之物相關性更高 (Tobler's First Law)。",
        "parents": [],
        "formula": r"w_{ij} = f(1/d_{ij})"
    },
    "geo_system_logic": {
        "level": 0, "title": "人地系統與循環", "emoji": "♻️", "color": "#7F8C8D",
        "summary": "物質循環與能量流動",
        "detail": "地理學研究的核心：人類活動與自然環境之間的交互作用系統（Human-Environment Interaction）。",
        "parents": [],
        "formula": r"\text{Environment} \leftrightarrow \text{Human}"
    }
}
