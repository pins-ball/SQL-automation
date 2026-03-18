from boolean_sqli import run_boolean
from union_sqli import run_union

url = input("URL 입력: ")
mode = input("모드 선택 (boolean / union): ")

if mode == "boolean":
    run_boolean(url)

elif mode == "union":
    run_union(url)

else:
    print("잘못된 모드입니다")