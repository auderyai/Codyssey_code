# 🐳 Codyssey_code

> Python 웹서버 · Docker 컨테이너 빌드 및 실행 실습 기록

---

## 📁 저장소 구조

Codyssey_code/
├── README.md

├── Dockerfile

├── src/

│   └── server.py

├── tests/

└── images/

    ├── 01_local_8080.png
    
    └── 02_docker_ps.png

---

## 🖥️ 실행 방법

### 1. 로컬 실행

python src/server.py

브라우저에서 [http://localhost:8080](images/01_local_8080.png) 접속

### 2. Docker 실행

docker build -t codyssey-web:latest .
docker run -d -p 8080:8080 codyssey-web:latest

---

## 📸 실행 화면

| 파일 | 설명 |
|------|------|
| [01_local_8080.png](images/01_local_8080.png) | 로컬 실행 화면 |
| [02_docker_ps.png](images/02_docker_ps.png) | Docker 실행 화면 |

---

## 🛠️ 개발 환경

| 항목 | 내용 |
|------|------|
| OS | Windows 11 |
| 언어 | Python 3.11 |
| 컨테이너 | Docker |
| 버전관리 | Git / GitHub |

---

## ✅ 1주차 완료 항목

- [x] [Python 웹서버 작성 (server.py)](src/server.py)
- [x] [Dockerfile 작성](Dockerfile)
- [x] [로컬 실행 확인 (localhost:8080)](images/01_local_8080.png)
- [x] [Docker 이미지 빌드](Dockerfile)
- [x] [Docker 컨테이너 실행 확인](images/02_docker_ps.png)
- [x] [실행 화면 캡처 및 업로드](images/)

---

## 🔗 관련 저장소

- [Codyssey (문서·로그)](https://github.com/auderyai/Codyssey)