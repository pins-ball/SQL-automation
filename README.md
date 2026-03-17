# SQL Injection Automation Tool

## 📌 개요

Web Security Academy 환경에서 SQL Injection 취약점을 분석하는 과정에서 반복적인 수동 테스트의 비효율을 느껴, Python 기반의 자동화 도구를 설계 및 구현하였다.

본 도구는 Boolean 기반 SQL Injection과 UNION 기반 SQL Injection을 구분하여 테스트할 수 있도록 설계되었다.

---

## ⚙️ 주요 기능

### 1. Boolean 기반 SQL Injection 탐지

* True / False 조건을 활용하여 응답 길이를 비교
* 데이터 증가 및 감소 여부를 통해 취약점 판단

### 2. UNION 기반 SQL Injection 분석

* UNION SELECT 구문을 활용하여 데이터베이스 정보 추출
* Oracle DB 환경에서 version 정보 탐지 가능

---

## 🧠 동작 방식

### Boolean SQL Injection

* 정상 요청 (Baseline) 기준 설정
* True 조건 (`OR 1=1`) → 데이터 증가 확인
* False 조건 (`AND 1=2`) → 데이터 감소 확인
* 결과 비교를 통해 취약 여부 판단

### UNION SQL Injection

* `UNION SELECT`를 이용하여 결과값 삽입
* 응답 HTML에서 특정 문자열(예: Oracle) 탐지
* 정규표현식을 이용한 버전 정보 추출

---

## 🛠 사용 기술

* Python 3.x
* requests 라이브러리
* 정규표현식 (re)

---

## 🚀 실행 방법

```bash
python main.py
```

실행 후:

* URL 입력
* 모드 선택 (boolean / union)

---

## 📂 프로젝트 구조

```
sqli_tool/
 ├── main.py
 ├── boolean_sqli.py
 ├── union_sqli.py
```

---

## 🎯 결과

* 반복적인 수동 테스트를 자동화하여 효율성 향상
* SQL Injection 취약점 탐지 및 데이터 추출 과정 이해
* 공격 흐름을 코드로 구현하여 실무적인 감각 확보

---

## 💡 느낀 점

단순히 문제를 해결하는 것에서 나아가, 공격 과정을 자동화하는 도구를 직접 구현하면서 웹 취약점 분석에 대한 이해도를 높일 수 있었다.

특히 Boolean 기반과 UNION 기반 SQL Injection의 차이를 코드로 구조화하면서 공격 기법을 더 명확하게 정리할 수 있었다.
