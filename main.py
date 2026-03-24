from union_sqli import run_union
from auth_sqli import run_auth_bypass

def main():
    print("=== SQL Injection 자동화 도구 ===")
    print("1. UNION SQLi (DB 정보 추출)")
    print("2. Login Bypass")

    choice = input("선택: ").strip()
    url = input("URL 입력 (예: https://target-lab-url.com/filter): ").strip()

    if not url.startswith("http"):
        print("❌ URL 형식이 이상함")
        return

    if choice == "1":
        run_union(url)
    elif choice == "2":
        run_auth_bypass(url)
    else:
        print("잘못된 선택")


if __name__ == "__main__":
    main()