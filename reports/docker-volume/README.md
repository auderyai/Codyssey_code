# Docker Volume 실습

## 실습 목표
- Docker 볼륨 생성 및 마운트
- 컨테이너 삭제 후에도 데이터 영속성 확인

## 실습 환경
- OS: Ubuntu 22.04.5 LTS
- Docker: 29.9.2

## 실습 과정

### 1. 볼륨 생성
```bash
docker volume create myvolume
```

### 2. 볼륨 마운트 후 데이터 저장
```bash
docker run -it --name vol-test --mount source=myvolume,target=/data ubuntu bash
echo "hi" > /data/hello.txt
```

### 3. 컨테이너 삭제 후 재생성
```bash
docker rm -f vol-test
docker run -it --name vol-test2 --mount source=myvolume,target=/data ubuntu bash
```

### 4. 데이터 영속성 확인
```bash
cat /data/hello.txt
# 출력: hi
```

## 스크린샷
