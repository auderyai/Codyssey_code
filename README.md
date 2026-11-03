\# 1주차 과제 - 웹 서버 컨테이너화



Python 표준 라이브러리로 만든 웹 서버를 Docker 컨테이너로

실행하는 1주차 과제입니다.



\## 개발 환경



\- Windows 11

\- Python 3.11

\- Docker

\- Git / GitHub



\## 폴더 구조



Codyssey\_code/

├── README.md

├── Dockerfile

├── src/

│   └── server.py

├── tests/

└── images/



\## 실행 방법



\### 1. 로컬 실행



python src/server.py



브라우저에서 http://localhost:8080 접속



\### 2. Docker 실행



docker build -t codyssey-web:latest .

docker run -d -p 8080:8080 codyssey-web:latest



\## 실행 화면



!\[로컬 실행](images/01\_local\_8080.png)

!\[Docker 실행](images/02\_docker\_ps.png)



\## 관련 저장소



\- 문서 저장소: https://github.com/auderyai/Codyssey

