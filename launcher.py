"""MBTI 测试系统 — 一键启动脚本（FastAPI + Cloudflare Tunnel）"""
import subprocess
import threading
import time
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PYTHON = r"C:\Users\ZYB\AppData\Local\Programs\Python\Python312\python.exe"
CLOUDFLARED = os.path.expandvars(r"%USERPROFILE%\cloudflared.exe")

PUBLIC_URL = "https://mbti.clawopen.ink"


def start_fastapi():
    """在后台启动 FastAPI 服务"""
    print("[1/2] Starting FastAPI server...")
    proc = subprocess.Popen(
        [PYTHON, "main.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc


def start_cloudflared():
    """启动永久 Cloudflare Tunnel（清除代理，避免连接被拒）"""
    print("[2/2] Starting Cloudflare Tunnel...")
    env = os.environ.copy()
    for key in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"):
        env.pop(key, None)
    proc = subprocess.Popen(
        [CLOUDFLARED, "tunnel", "run", "mbti-tunnel"],
        stdout=sys.stdout,
        stderr=sys.stderr,
        env=env,
    )
    return proc


if __name__ == "__main__":
    # 写入固定公网地址
    with open("public-url.txt", "w", encoding="utf-8") as f:
        f.write(PUBLIC_URL)

    # 启动 FastAPI
    api_proc = start_fastapi()

    # 等待 FastAPI 就绪
    print("  Waiting for FastAPI...")
    for i in range(15):
        time.sleep(2)
        try:
            import urllib.request
            urllib.request.urlopen("http://localhost:8000/test", timeout=3)
            print("  FastAPI ready!")
            break
        except Exception:
            print(f"  ...{i+1}")

    # 启动 Cloudflare Tunnel
    cf_proc = start_cloudflared()

    print()
    print("=" * 50)
    print(f"  公网地址:  {PUBLIC_URL}/test")
    print(f"  管理后台:  {PUBLIC_URL}/admin")
    print(f"  本地访问:  http://localhost:8000")
    print("=" * 50)
    print()
    print("  管理后台密码: admin123")
    print("  关闭此窗口即停止所有服务")
    print()

    # 保持主线程运行
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nShutting down...")
        api_proc.terminate()
        cf_proc.terminate()
