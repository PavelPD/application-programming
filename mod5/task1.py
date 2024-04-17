from typing import List
from flask import Flask
import subprocess
import os
import signal

app = Flask(__name__)

def get_pids(port: int) -> List[int]:
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    result = subprocess.run(["lsof", "-i", ":" + str(port)], capture_output=True, encoding='utf-8')


    for row in result.stdout.split("\n")[1:]:
        if row:
            pids.append(int(row.split()[1]))
    return pids

def free_port(port: int) -> None:
    pids: List[int] = get_pids(port)
    for i_pid in pids:
        os.kill(i_pid, signal.SIGKILL)

def run(port: int) -> None:
    free_port(port)
    app.run(port=port)

if __name__ == '__main__':
    run(5000)