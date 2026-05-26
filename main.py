"""MBTI 候选人测试系统 — FastAPI 主服务"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, Response
from pydantic import BaseModel

from questions import QUESTIONS, get_type_description
from scoring import score_answers
from models import init_db, save_result, get_all_results, get_type_distribution, get_dimension_stats
from zodiac import get_buddy_recommendations, ZODIAC_SIGNS

# 管理员密码
ADMIN_PASSWORD = "admin123"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="MBTI 测试系统", lifespan=lifespan)


# ----- 禁用缓存（防止 Cloudflare / 浏览器缓存旧版页面）-----
@app.middleware("http")
async def add_no_cache_headers(request: Request, call_next):
    response: Response = await call_next(request)
    # 对所有 HTML 和 JSON 响应禁用缓存
    content_type = response.headers.get("content-type", "")
    if any(t in content_type for t in ("text/html", "application/json", "text/css", "application/javascript", "text/javascript")):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response

# ----- 静态文件 -----
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/test")


@app.get("/test")
async def test_page():
    return FileResponse("static/test.html")


@app.get("/admin")
async def admin_page():
    return FileResponse("static/admin.html")


# ----- API -----

class SubmitRequest(BaseModel):
    candidate: str = ""
    zodiac: str = ""     # 星座英文 key，如 "aries"
    answers: dict  # {"1": "A", "2": "B", ...}


@app.get("/api/questions")
async def get_questions():
    """返回所有题目"""
    result = []
    for q in QUESTIONS:
        item = {"id": q["id"], "text": q["text"]}
        for k, v in q["options"].items():
            item[f"option_{k.lower()}"] = v
        result.append(item)
    return result


@app.post("/api/submit")
async def submit(request: SubmitRequest):
    """提交答案，计算 MBTI 类型"""
    answers_dict = request.answers

    # 验证：必须答完 24 题
    if len(answers_dict) != len(QUESTIONS):
        raise HTTPException(status_code=400, detail=f"需要回答全部 {len(QUESTIONS)} 题，当前 {len(answers_dict)} 题")

    # 计分
    scores = score_answers(answers_dict)
    mbti_type = scores["mbti_type"]
    desc = get_type_description(mbti_type)

    # 保存结果
    name = request.candidate.strip() or "匿名"
    result_id = save_result(name, scores)

    return {
        "id": result_id,
        "candidate": name,
        "mbti_type": mbti_type,
        "description": desc["summary"],
        "strengths": desc["strengths"],
        "careers": desc["careers"],
        "celebrities": desc["celebrities"],
        "scores": scores,
        "buddies": get_buddy_recommendations(request.zodiac, mbti_type),
    }


@app.get("/api/zodiacs")
async def get_zodiacs():
    """返回 12 星座列表（供选择器使用）"""
    return [
        {"key": k, "name": v["name"], "emoji": v["emoji"], "date": v["date"]}
        for k, v in ZODIAC_SIGNS.items()
    ]


@app.get("/api/public-url")
async def public_url():
    """返回当前公网访问地址（供 QR 码使用）"""
    try:
        with open("public-url.txt", "r", encoding="utf-8") as f:
            url = f.read().strip()
        if url:
            return {"url": url}
    except FileNotFoundError:
        pass
    return {"url": ""}


@app.get("/api/stats/types")
async def stats_types(password: str = ""):
    """管理员：类型分布统计"""
    if password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="密码错误")
    return get_type_distribution()


@app.get("/api/stats/dimensions")
async def stats_dimensions(password: str = ""):
    """管理员：四维度统计"""
    if password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="密码错误")
    return get_dimension_stats()


@app.get("/api/stats/results")
async def stats_results(password: str = ""):
    """管理员：所有结果明细"""
    if password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="密码错误")
    return get_all_results()


if __name__ == "__main__":
    import uvicorn
    local_ip = os.environ.get("LOCAL_IP", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    print(f"\n  🔒 本地服务: http://{local_ip}:{port}")
    print(f"  📝 测试页面: http://{local_ip}:{port}/test")
    print(f"  📊 管理后台: http://{local_ip}:{port}/admin\n")
    uvicorn.run(app, host="0.0.0.0", port=port)
