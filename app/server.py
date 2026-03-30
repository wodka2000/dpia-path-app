#!/usr/bin/env python3
"""
DPIA Path — Server locale per uso in aula
==========================================

Avvia il server dalla cartella app/:

    cd dpia-path-app/app
    python server.py

Poi:
  - Studenti aprono: http://<TUO-IP>:8080
  - Docente apre:    http://<TUO-IP>:8080/dashboard.html

Il server salva i report in submissions.json nella stessa cartella.
"""

import http.server
import json
import os
import socket
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

PORT = 8080
SUBMISSIONS_FILE = Path(__file__).parent / "submissions.json"


def load_submissions():
    if SUBMISSIONS_FILE.exists():
        try:
            return json.loads(SUBMISSIONS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_submissions(data):
    SUBMISSIONS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


class DPIAHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        # API: restituisci tutti i report
        if parsed.path == "/api/submissions":
            data = load_submissions()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
            return

        # Root -> index.html
        if parsed.path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/submit":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                submission = json.loads(body.decode("utf-8"))
                submissions = load_submissions()

                # Aggiungi timestamp server se mancante
                if "serverTimestamp" not in submission:
                    submission["serverTimestamp"] = datetime.now().isoformat()

                # Sostituisci se stesso studente ha già inviato, altrimenti aggiungi
                replaced = False
                for i, s in enumerate(submissions):
                    if s.get("id") == submission.get("id"):
                        submissions[i] = submission
                        replaced = True
                        break
                    if (s.get("studente") == submission.get("studente")
                            and submission.get("studente")):
                        submissions[i] = submission
                        replaced = True
                        break

                if not replaced:
                    submissions.append(submission)

                save_submissions(submissions)

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                response = {"status": "ok", "count": len(submissions)}
                self.wfile.write(json.dumps(response).encode("utf-8"))

                print(f"  [+] Report ricevuto da: {submission.get('studente', '?')} "
                      f"({submission.get('finalLabel', '?')})")

            except (json.JSONDecodeError, Exception) as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "msg": str(e)}).encode())
            return

        self.send_response(404)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        # Log pulito
        if "/api/" in (args[0] if args else ""):
            super().log_message(format, *args)


def get_local_ip():
    """Trova l'IP locale sulla rete Wi-Fi."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    local_ip = get_local_ip()

    os.chdir(Path(__file__).parent)

    server = http.server.HTTPServer(("0.0.0.0", port), DPIAHandler)

    print()
    print("=" * 58)
    print("  DPIA Path — Server Aula")
    print("=" * 58)
    print()
    print(f"  Studenti (dal telefono/laptop):")
    print(f"  -> http://{local_ip}:{port}")
    print()
    print(f"  Dashboard docente (sul proiettore):")
    print(f"  -> http://{local_ip}:{port}/dashboard.html")
    print()
    print(f"  In locale:")
    print(f"  -> http://localhost:{port}")
    print()
    print(f"  Report salvati in: {SUBMISSIONS_FILE}")
    print()
    print("  Premi Ctrl+C per fermare il server")
    print("=" * 58)
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server fermato.")
        server.server_close()


if __name__ == "__main__":
    main()
