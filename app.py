import http.server
import socketserver
import os

# Получаем номер порта из переменной окружения PORT (Heroku запишет туда доступный нам порт)
# Если в переменной PORT пусто, то по дефолту установим возьмем порт 8443
PORT = int(os.environ.get('PORT', 8443))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
