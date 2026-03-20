import http.server
import socketserver
import webbrowser
import os
import threading
import socket

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def find_free_port(start=8080):
    for port in range(start, start + 20):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("", port))
                return port
        except OSError:
            continue
    return None

PORT = find_free_port()

if PORT is None:
    input("No free port found. Restart PC and try again.")
    exit(1)

def open_browser():
    import time
    time.sleep(1.5)
    webbrowser.open(f'http://localhost:{PORT}/adaptive-onboarding-engine.html')

print("=" * 50)
print("  BridgeSkill AI Onboarding Engine")
print("=" * 50)
print(f"\n  Starting server on http://localhost:{PORT}")
print("  Opening browser automatically...")
print("\n  Press Ctrl+C to stop the server\n")

threading.Thread(target=open_browser, daemon=True).start()

handler = http.server.SimpleHTTPRequestHandler
handler.log_message = lambda *args: None

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")