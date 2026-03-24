from union_sqli import run_union

def main():
    print("=== SQL Injection 자동화 도구 ===")

    url = input("URL 입력 (예: https://target-lab-url.com/filter): ").strip()

    if not url.startswith("http"):
        print("❌ URL 형식이 이상함")
        return

    run_union(url)

if __name__ == "__main__":
    main()