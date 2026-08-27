import subprocess
def run(cmd):
    subprocess.call(cmd, shell=True)   # 위험: 셸 인젝션
