from flask import Flask,request,g
from .notification import notification
import logging
import time
import datetime
from rfc3339 import rfc3339

app =  Flask(__name__)

logging.basicConfig(filename='server.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.before_request
def start_timer():
    g.start = time.time()

@app.route('/notification/dataUsageThresholdMet',methods=["POST"])
def dataUsageThresholdMet():
    data = request.get_json()
    if data["type"] == "userPurchaseLowData":
        notification(data,"80%")
    return "success"

@app.route('/notification/dataConsumed',methods=["POST"])
def dataConsumed():
    data = request.get_json()
    if data["type"] == "userPurchaseNoData":
        notification(data,"100%")
    return "success"

@app.after_request
def log_request(response):
    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.get_json())
    
    request_id = request.headers.get('X-Request-ID')
    log_params = {
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "duration": duration,
        "time": timestamp,
        "ip": ip,
        "host": host,
        "data": args,
        "request_id": request_id,
    }
    
    line = ""
    for param in log_params:
        line += f"{param}: {log_params[param]} "
    

    app.logger.info(line)

    return response
