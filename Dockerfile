# 베이스 이미지: 가벼운 파이썬 공식 이미지
FROM python:3.11-slim

# 컨테이너 안 작업 폴더 지정
WORKDIR /app

# 소스코드 복사 (호스트 src/ → 컨테이너 /app/src/)
COPY src/ ./src/

# 컨테이너가 사용하는 포트 명시 (문서화 목적)
EXPOSE 8080

# 컨테이너 시작 시 실행할 명령
CMD ["python", "src/server.py"]