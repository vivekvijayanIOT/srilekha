import time
for a in range(0,20):
    b = "\t\tCharging [" + "*" * a +"]"
    print(b,end="\r")
    time.sleep(1)
print()"\n")
