# FastAPI 프로젝트

이 프로젝트는 FastAPI를 사용한 웹 API 프로젝트입니다.

## 설치 방법

1. 가상환경 생성 및 활성화:

anaconda3를 사용하였다.

````bash
conda create -n "가상환경 이름" python=version

condata activate "가상환경 이름"


2. 의존성 설치:

```bash
pip install -r requirements.txt
````

## 실행 방법

```bash
uvicorn app.main:app --reload
```

## 프로젝트 구조

```
.
├── app/
│   ├── api/          # API 라우터
│   ├── core/         # 핵심 설정
│   └── models/       # 데이터 모델
├── requirements.txt  # 의존성 목록
└── README.md        # 프로젝트 설명
```
