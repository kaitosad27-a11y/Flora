"""
Pink Roses - Hiệu ứng hoa hồng pha lê phát sáng 3D
Tái hiện 100% video TikTok @_zane.0812
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Ẩn bớt log request để terminal sạch đẹp
        pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"[*] Server đang chạy tại: http://localhost:{PORT}")
        httpd.serve_forever()

def main():
    print("=" * 60)
    print("  🌹 PINK ROSES 3D - TIKTOK CODE REPLICA (@_zane.0812) 🌹")
    print("=" * 60)
    print(f"[+] Thư mục dự án: {DIRECTORY}")
    
    # Khởi động server nền
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    time.sleep(0.5)
    url = f"http://localhost:{PORT}/index.html"
    print(f"[+] Đang tự động mở trình duyệt: {url}")
    print("[*] Nhấn Ctrl + C trong terminal này để thoát.")
    webbrowser.open(url)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Đã đóng server. Tạm biệt!")
        sys.exit(0)

if __name__ == '__main__':
    main()
