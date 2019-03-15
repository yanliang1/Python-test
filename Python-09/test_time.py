import time

while True:
    print("hello python")
    time.sleep(1)
    print(time.time())
    tm = time.localtime()
    print(type(tm))
    print(tm.tm_year)
    print(tm.tm_wday+1)
    