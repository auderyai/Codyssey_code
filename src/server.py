# src/server.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 200 OK 응답 헤더 전송
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '<h1>Hello, Codyssey!</h1><p>Docker 웹 서버 동작 중</p>'
        self.wfile.write(html.encode('utf-8'))  # 본문 전송

if __name__ == '__main__':
    # 0.0.0.0 으로 열어야 컨테이너 외부에서 접속 가능
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    print('Server running on port 8080...')
    server.serve_forever()