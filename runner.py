import time;
import os;

while True:
    print("Hello from python")
    os.system("heroku ps:restart web.1")
    time.sleep(80)

