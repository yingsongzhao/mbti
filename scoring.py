"""计分逻辑：根据答案计算 MBTI 类型（权重计分）"""

from questions import QUESTIONS


def score_answers(answers: dict) -> dict:
    """
    根据答案计算各维度得分和最终 MBTI 类型。

    参数:
        answers: {qid: "A"/"B"/"C"/"D"}，qid 为题目 ID (1-24)

    返回:
        {
            "mbti_type": "ENFJ",
            "e_score": 6, "i_score": 3,
            "n_score": 8, "s_score": 4,
            ...
        }
    """
    scores = {"E": 0, "I": 0, "N": 0, "S": 0, "F": 0, "T": 0, "J": 0, "P": 0}

    question_map = {q["id"]: q for q in QUESTIONS}

    for qid_str, choice in answers.items():
        qid = int(qid_str)
        q = question_map.get(qid)
        if not q:
            continue
        mapping = q["mapping"].get(choice)
        if mapping:
            dim_key, weight = mapping   # 从元组解包
            scores[dim_key] += weight

    # 确定每个维度：高分胜出，平局按第一个字母排列
    ei = "E" if scores["E"] >= scores["I"] else "I"
    ns = "N" if scores["N"] >= scores["S"] else "S"
    ft = "F" if scores["F"] >= scores["T"] else "T"
    jp = "J" if scores["J"] >= scores["P"] else "P"

    mbti_type = ei + ns + ft + jp

    return {
        "mbti_type": mbti_type,
        "e_score": scores["E"],
        "i_score": scores["I"],
        "n_score": scores["N"],
        "s_score": scores["S"],
        "f_score": scores["F"],
        "t_score": scores["T"],
        "j_score": scores["J"],
        "p_score": scores["P"],
    }
