#!/usr/bin/env python3
"""Simple markdown file server for LAN access."""

import http.server
import os
import socket
import sys

HOST = "0.0.0.0"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DOCS_DIR, **kwargs)

    def guess_type(self, path):
        if path.endswith(".md") or path.endswith(".mdx"):
            return "text/html; charset=utf-8"
        return super().guess_type(path)

    def do_GET(self):
        if self.path.endswith(".md") or self.path.endswith(".mdx"):
            md_path = os.path.join(DOCS_DIR, self.path.lstrip("/"))
            if os.path.isfile(md_path):
                with open(md_path, encoding="utf-8") as f:
                    raw = f.read()
                html = self._render_html(self.path, raw)
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(html)))
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
                return
        super().do_GET()

    def _render_html(self, rel_path, markdown_text):
        lines = markdown_text.split("\n")
        title = rel_path.strip("/").split("/")[-1].replace(".md", "").replace("-", " ").title()
        body = self._simple_md_to_html(markdown_text)
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — docspage</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         line-height: 1.7; color: #222; max-width: 780px; margin: 0 auto; padding: 2rem 1.5rem; }}
  h1 {{ font-size: 1.8rem; margin: 1.5rem 0 0.8rem; }}
  h2 {{ font-size: 1.4rem; margin: 1.3rem 0 0.6rem; border-bottom: 1px solid #eee; padding-bottom: 0.3rem; }}
  h3 {{ font-size: 1.2rem; margin: 1.2rem 0 0.5rem; }}
  p, li {{ margin: 0.5rem 0; }}
  ul, ol {{ padding-left: 1.5rem; }}
  code {{ background: #f4f4f4; padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.9em; }}
  pre {{ background: #f4f4f4; padding: 1rem; border-radius: 5px; overflow-x: auto; margin: 0.8rem 0; }}
  pre code {{ background: none; padding: 0; }}
  a {{ color: #2563eb; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  nav {{ margin-bottom: 2rem; font-size: 0.9rem; }}
  nav a {{ color: #666; }}
</style>
</head>
<body>
<nav><a href="/">← Home</a></nav>
{body}
</body>
</html>"""

    def _simple_md_to_html(self, text):
        lines = text.split("\n")
        html = []
        in_code = False
        code_buf = []
        for line in lines:
            if line.startswith("```"):
                if in_code:
                    html.append(f"<pre><code>{''.join(code_buf)}</code></pre>")
                    code_buf = []
                    in_code = False
                else:
                    in_code = True
                continue
            if in_code:
                code_buf.append(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + "\n")
                continue
            if line.startswith("# "):
                html.append(f"<h1>{line[2:]}</h1>")
            elif line.startswith("## "):
                html.append(f"<h2>{line[3:]}</h2>")
            elif line.startswith("### "):
                html.append(f"<h3>{line[4:]}</h3>")
            elif line.startswith("- "):
                html.append(f"<li>{line[2:]}</li>")
            elif line.startswith("* "):
                html.append(f"<li>{line[2:]}</li>")
            elif line.startswith("1. "):
                html.append(f"<li>{line[3:]}</li>")
            elif line == "":
                html.append("</ul>" if html and html[-1].startswith("<li>") else "<br>")
            else:
                html.append(f"<p>{line}</p>")
        return "".join(html)


if __name__ == "__main__":
    srv = http.server.HTTPServer((HOST, PORT), Handler)
    ip = socket.gethostbyname(socket.gethostname())
    print(f"Serving http://{HOST}:{PORT}  →  LAN: http://192.168.1.104:{PORT}")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()
