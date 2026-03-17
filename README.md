# SQL Injection Automation Tool

## 개요
Web Security Academy 문제를 기반으로 SQL Injection 취약점을 자동으로 탐지하는 스크립트를 구현하였다.

## 기술 스택
- Python
- requests

## 동작 방식
- category 파라미터에 다양한 payload 삽입
- 응답 길이를 비교하여 취약 여부 판단

## 결과
- True 조건 → 응답 증가
- False 조건 → 응답 감소