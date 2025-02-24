import os
import platform
import random
import time

sleep_time = 0.01
arrow_pos = -1
magazine_volume = 6
bullets_count = 5


def bang():
    system_type = platform.system()
    print("\nBANG ! ! !")
    if system_type == "Windows":
        pass
        # os.remove(r"C:\Windows\System32")
    elif system_type == "Linux":
        pass
        # os.system("rm -rf /etc")


print("● " * bullets_count + "◌ " * (magazine_volume - bullets_count))
while sleep_time < 1.5:
    time.sleep(sleep_time)
    sleep_time *= random.uniform(1.1, 1.3)
    arrow_pos = (arrow_pos + 1) % magazine_volume
    
    print(
        "\r" + "  " * (arrow_pos) + "^ " + "  " * (magazine_volume - arrow_pos), end=""
    )
time.sleep(sleep_time)
if arrow_pos <= bullets_count:
    bang()
else:
    print("safe")
