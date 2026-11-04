# 🐳 Codyssey_code

> Python 웹서버 · Docker 컨테이너 빌드 및 실행 · 커스텀 이미지 실습 기록

📎 문서·로그 저장소: [Codyssey](https://github.com/auderyai/Codyssey)

---

## 📁 저장소 구조

```
Codyssey_code/

├── README.md

├── Dockerfile 
                        ← 커스텀 nginx 이미지용
├── .gitignore

├── site/

│   └── index.html
                     ← nginx 서빙 HTML
├── src/

│   └── server.py
                      ← Python 웹서버
├── tests/

├── images/

│   ├── 01_local_8080.png
             ← 로컬 실행 화면
│   └── 02_docker_ps.png
               ← Docker 실행 화면
└── reports/

    └── docker-custom-image/

        ├── README.md 
                         ← 커스텀 이미지 실습 보고서
        └── screenshots/

            ├── build.png
                          ← 이미지 빌드 화면
            └── run.png 
                           ← 컨테이너 실행 화면
```

---

## 🖥️ 실행 방법

### 1. 로컬 실행 (Python 웹서버)

```bash
python src/server.py
```

브라우저에서 `http://localhost:8080` 접속

### 2. Docker 실행 (Python 웹서버)

```bash
docker build -t codyssey-web:latest .
docker run -d -p 8080:8080 codyssey-web:latest
```

### 3. 커스텀 nginx 이미지 실행

```bash
docker build -t my-custom-nginx .
docker run -d -p 8081:80 my-custom-nginx
```

브라우저에서 `http://localhost:8081` 접속

---

## 📸 실행 화면

| 파일 | 설명 |
|------|------|
| [01_local_8080.png](images/01_local_8080.png) | 로컬 Python 웹서버 실행 화면 |
| [02_docker_ps.png](images/02_docker_ps.png) | Docker 컨테이너 실행 확인 |
| [build.png](reports/docker-custom-image/screenshots/build.png) | 커스텀 이미지 빌드 화면 |
| [run.png](reports/docker-custom-image/screenshots/run.png) | 커스텀 컨테이너 실행 화면 |

---

## 🛠️ 개발 환경

| 항목 | 내용 |
|------|------|
| OS | Windows 11 + WSL2 (Ubuntu 22.04.5 LTS) |
| Shell | bash |
| 언어 | Python 3.11 |
| 컨테이너 | Docker 29.9.2 |
| 버전관리 | Git 2.34.1 / GitHub |

---

## ✅ 완료 항목

- [x] [Python 웹서버 작성 (server.py)](src/server.py)
- [x] [Dockerfile 작성](Dockerfile)
- [x] [로컬 실행 확인 (localhost:8080)](images/01_local_8080.png)
- [x] [Docker 이미지 빌드](Dockerfile)
- [x] [Docker 컨테이너 실행 확인](images/02_docker_ps.png)
- [x] [실행 화면 캡처 및 업로드](images/)
- [x] [커스텀 nginx Dockerfile 작성](Dockerfile)
- [x] [site/index.html 작성](site/index.html)
- [x] [커스텀 이미지 빌드 (my-custom-nginx)](reports/docker-custom-image/screenshots/build.png)
- [x] [커스텀 컨테이너 실행 확인](reports/docker-custom-image/screenshots/run.png)
- [x] [실습 보고서 작성](reports/docker-custom-image/README.md)

---

## 🔗 관련 저장소

| 저장소 | 설명 |
|--------|------|
| [Codyssey_code](https://github.com/auderyai/Codyssey_code) | 코드 · Dockerfile · 실행 화면 |
| [Codyssey](https://github.com/auderyai/Codyssey) | 문서 · 실습 로그 · Git 설정 보고서 |