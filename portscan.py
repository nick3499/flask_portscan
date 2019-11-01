# **NOTE**: try/except block iterates through 65535 ports!! maximum scan!
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime, timedelta
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    hostAddress = '127.0.0.1'  # loopback address for scanning localhost
    start_time = datetime.now()  # port scan start time
    data = []  # lists open port strings
    try:
        for port in range(1, 65535):
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(2)  # scan for 2 secs
            result = sock.connect_ex((hostAddress, port))
            if result == 0:
                data.append(f'Port {port}: OPEN')  # Port __: OPEN
            sock.close()
    except OSError as e:
        if e.errno != errno.ENOENT:
            print(f'{e}')
            sys.exit()
    end_time = datetime.now()  # port scan ends: mark time
    duration = end_time - start_time  # port scan duration
    data.append(f'Scan duration: {round(duration.total_seconds(), 2)}secs')
    return render_template('portscan.html', data=data, address=hostAddress)

if __name__ == '__main__':
    app.run()
