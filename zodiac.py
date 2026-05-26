"""星座 + MBTI 搭子兼容性数据"""

# ===== 12 星座基本信息 =====
ZODIAC_SIGNS = {
    "aries":       {"name": "白羊座", "emoji": "♈", "date": "3.21-4.19", "element": "火",
                    "traits": "热情勇敢、行动力超强，是天生的开拓者和竞争者"},
    "taurus":      {"name": "金牛座", "emoji": "♉", "date": "4.20-5.20", "element": "土",
                    "traits": "稳重踏实、热爱美好事物，对生活品质有执念"},
    "gemini":      {"name": "双子座", "emoji": "♊", "date": "5.21-6.21", "element": "风",
                    "traits": "聪明好奇、多变灵活，是社交圈的开心果和信息枢纽"},
    "cancer":      {"name": "巨蟹座", "emoji": "♋", "date": "6.22-7.22", "element": "水",
                    "traits": "温柔细腻、重视家庭，是最会照顾人的暖心担当"},
    "leo":         {"name": "狮子座", "emoji": "♌", "date": "7.23-8.22", "element": "火",
                    "traits": "自信大方、天生舞台感，走到哪里都是焦点"},
    "virgo":       {"name": "处女座", "emoji": "♍", "date": "8.23-9.22", "element": "土",
                    "traits": "细致严谨、追求完美，默默把事情做到极致"},
    "libra":       {"name": "天秤座", "emoji": "♎", "date": "9.23-10.23", "element": "风",
                    "traits": "优雅公正、社交达人，天生自带和平使者光环"},
    "scorpio":     {"name": "天蝎座", "emoji": "♏", "date": "10.24-11.22", "element": "水",
                    "traits": "深沉敏锐、极度专注，要么不做要么做到骨子里"},
    "sagittarius": {"name": "射手座", "emoji": "♐", "date": "11.23-12.21", "element": "火",
                    "traits": "乐观自由、热爱探索，人生就是一场大冒险"},
    "capricorn":   {"name": "摩羯座", "emoji": "♑", "date": "12.22-1.19", "element": "土",
                    "traits": "坚韧务实、目标至上，低调爬向人生巅峰"},
    "aquarius":    {"name": "水瓶座", "emoji": "♒", "date": "1.20-2.18", "element": "风",
                    "traits": "独立特行、脑洞清奇，永远活在未来世界的革新者"},
    "pisces":      {"name": "双鱼座", "emoji": "♓", "date": "2.19-3.20", "element": "水",
                    "traits": "浪漫梦幻、共情力爆表，是行走的情绪雷达和艺术家"},
}

# ===== 星座最佳配对（每个星座 3 个最契合星座）=====
ZODIAC_COMPATIBLE = {
    "aries":       ["leo", "sagittarius", "gemini"],
    "taurus":      ["virgo", "capricorn", "cancer"],
    "gemini":      ["libra", "aquarius", "aries"],
    "cancer":      ["scorpio", "pisces", "taurus"],
    "leo":         ["aries", "sagittarius", "libra"],
    "virgo":       ["taurus", "capricorn", "scorpio"],
    "libra":       ["gemini", "aquarius", "leo"],
    "scorpio":     ["cancer", "pisces", "virgo"],
    "sagittarius": ["aries", "leo", "aquarius"],
    "capricorn":   ["taurus", "virgo", "pisces"],
    "aquarius":    ["gemini", "libra", "sagittarius"],
    "pisces":      ["cancer", "scorpio", "capricorn"],
}

# ===== 星座 → 对应的 MBTI 类型 =====
ZODIAC_MBTI = {
    "aries":       ["ESTP", "ENTJ"],
    "taurus":      ["ISFP", "ESTJ"],
    "gemini":      ["ENTP", "ENFP"],
    "cancer":      ["ISFJ", "INFJ"],
    "leo":         ["ENFJ", "ESFP"],
    "virgo":       ["ISTJ", "ISFJ"],
    "libra":       ["ESFJ", "ENFJ"],
    "scorpio":     ["INFJ", "INTJ"],
    "sagittarius": ["ENFP", "ENTP"],
    "capricorn":   ["INTJ", "ENTJ"],
    "pisces":      ["INFP", "ISFP"],
}

# ===== MBTI 最佳配对（每个类型 3 个最契合类型）=====
MBTI_COMPATIBLE = {
    "INTJ": ["ENFP", "ENTP", "INTP"],
    "INTP": ["ENFJ", "ENTJ", "INFP"],
    "ENTJ": ["INTP", "INFP", "INTJ"],
    "ENTP": ["INFJ", "INTJ", "ENFJ"],
    "INFJ": ["ENFP", "ENTP", "INTJ"],
    "INFP": ["ENFJ", "ENFP", "INFJ"],
    "ENFJ": ["INFP", "INTP", "ISFP"],
    "ENFP": ["INFJ", "INTJ", "ISFJ"],
    "ISTJ": ["ESFJ", "ESFP", "ISFJ"],
    "ISFJ": ["ESTP", "ESFP", "ISFJ"],
    "ESTJ": ["ISFP", "ISFJ", "ISTP"],
    "ESFJ": ["ISFP", "ISTP", "ENFP"],
    "ISTP": ["ESFJ", "ESTJ", "ISFJ"],
    "ISFP": ["ENFJ", "ESTJ", "ESFJ"],
    "ESTP": ["ISFJ", "ISTJ", "ESFJ"],
    "ESFP": ["ISFJ", "ISTJ", "ENFJ"],
}

# ===== MBTI 简短人格标签 =====
MBTI_LABELS = {
    "INTJ": "建筑师", "INTP": "逻辑学家", "ENTJ": "指挥官", "ENTP": "辩论家",
    "INFJ": "提倡者", "INFP": "调停者", "ENFJ": "主人公", "ENFP": "竞选者",
    "ISTJ": "物流师", "ISFJ": "守卫者", "ESTJ": "总经理", "ESFJ": "执政官",
    "ISTP": "鉴赏家", "ISFP": "探险家", "ESTP": "企业家", "ESFP": "表演者",
}


def get_buddy_recommendations(zodiac_sign: str, mbti_type: str) -> dict:
    """
    综合星座 + MBTI，计算搭子推荐。
    返回：星座搭子 TOP 3、MBTI 搭子 TOP 3、最佳综合搭子 TOP 5
    """
    z = zodiac_sign.lower()
    z_info = ZODIAC_SIGNS.get(z, {})
    z_compat = ZODIAC_COMPATIBLE.get(z, [])
    z_mbti = ZODIAC_MBTI.get(z, [])
    m_compat = MBTI_COMPATIBLE.get(mbti_type.upper(), [])

    # --- 星座搭子 ---
    zodiac_buddies = []
    for zc in z_compat:
        info = ZODIAC_SIGNS.get(zc, {})
        zodiac_buddies.append({
            "key": zc,
            "name": info.get("name", zc),
            "emoji": info.get("emoji", ""),
            "traits": info.get("traits", ""),
            "typical_mbti": ZODIAC_MBTI.get(zc, []),
        })

    # --- MBTI 搭子 ---
    mbti_buddies = []
    for mc in m_compat:
        mbti_buddies.append({
            "type": mc,
            "label": MBTI_LABELS.get(mc, mc),
            "typical_zodiac": [k for k, v in ZODIAC_MBTI.items() if mc in v],
        })

    # --- 综合搭子（星座兼容 + MBTI 兼容 双维度打分）---
    combined_scores = {}
    for sign_key, sign_info in ZODIAC_SIGNS.items():
        score = 0
        reasons = []

        # 星座兼容加分
        if sign_key in z_compat:
            score += 3
            reasons.append(f"星座高度契合")

        # 该星座的典型 MBTI 与用户 MBTI 兼容加分
        sign_mbtis = ZODIAC_MBTI.get(sign_key, [])
        for sm in sign_mbtis:
            if sm in m_compat:
                score += 2
                reasons.append(f"{sm} 是你的 MBTI 理想搭子")

        # 用户星座的典型 MBTI 与该星座典型 MBTI 兼容加分
        for zm in z_mbti:
            if zm in m_compat and zm in sign_mbtis:
                score += 1

        if score > 0:
            combined_scores[sign_key] = {
                "key": sign_key,
                "name": sign_info.get("name", sign_key),
                "emoji": sign_info.get("emoji", ""),
                "traits": sign_info.get("traits", ""),
                "typical_mbti": sign_mbtis,
                "score": score,
                "reasons": list(set(reasons)),
            }

    # 按分数排序取 TOP 5
    sorted_combined = sorted(combined_scores.values(), key=lambda x: x["score"], reverse=True)[:5]

    return {
        "zodiac_buddies": zodiac_buddies,
        "mbti_buddies": mbti_buddies,
        "combined_buddies": sorted_combined,
        "user_zodiac": {
            "key": z,
            "name": z_info.get("name", z),
            "emoji": z_info.get("emoji", ""),
            "traits": z_info.get("traits", ""),
            "element": z_info.get("element", ""),
        }
    }
