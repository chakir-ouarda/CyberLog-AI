import os
import time
import subprocess
import sys


LOG_DIR = "../logs/input"


def list_logs():

    files = []

    for file in os.listdir(LOG_DIR):

        path = os.path.join(LOG_DIR, file)

        if os.path.isfile(path):
            files.append(path)

    return files



def watch():

    print("[+] CyberLog AI Real-Time Monitor Started")

    last_modified = {}


    while True:

        for file in list_logs():

            current = os.path.getmtime(file)


            if file not in last_modified:

                last_modified[file] = current


            elif current != last_modified[file]:

                print(f"[+] New activity detected: {file}")

                print("[+] Launching CyberLog AI Pipeline...")


                subprocess.run(
                    [
                        sys.executable,
                        "pipeline.py"
                    ]
                )


                last_modified[file] = current


        time.sleep(2)



if __name__ == "__main__":

    watch()
