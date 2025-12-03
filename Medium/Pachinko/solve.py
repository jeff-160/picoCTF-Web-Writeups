#!/usr/bin/env python3
import requests
import sys
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

HOST = "http://activist-birds.picoctf.net:62397/"     # change if needed
URL  = HOST + "/check"

THREADS = 32                       # increase if your machine can handle it
BITS = 64                          # 4 words * 16 bits

# TUNE THESE RANGES FOR MAX SPEED
IN_MIN, IN_MAX   = 1, 100
OUT_MIN, OUT_MAX = 1, 100


def make_base_circuit():
    """Prebuild a circuit with 64 placeholders (0,0,0)."""
    return [{"input1": 0, "input2": 0, "output": 0} for _ in range(BITS)]


BASE = make_base_circuit()


def make_circuit(in_base, out_base):
    """Fast offset fill without reallocating list structure."""
    c = []
    for i in range(BITS):
        wire_in = in_base + i
        wire_out = out_base + i
        c.append({"input1": wire_in, "input2": wire_in, "output": wire_out})
    return c


session = requests.Session()


def try_pair(in_base, out_base):
    circuit = make_circuit(in_base, out_base)
    try:
        r = session.post(URL, json={"circuit": circuit}, timeout=4)
    except Exception:
        return None

    if r.status_code != 200:
        return None

    try:
        data = r.json()
    except:
        return None

    flag = data.get("flag", "")
    if "FLAG" in flag:
        return flag
    return None


def brute():
    tasks = []

    with ThreadPoolExecutor(max_workers=THREADS) as exe:
        for ib in range(IN_MIN, IN_MAX + 1):
            for ob in range(OUT_MIN, OUT_MAX + 1):
                tasks.append(exe.submit(try_pair, ib, ob))

        for future in as_completed(tasks):
            result = future.result()
            if result and "FLAG" in result:
                print("[+] FLAG FOUND!")
                print(result)
                sys.exit(0)

    print("[-] No flag in tested range. Increase IN/OUT ranges.")


if __name__ == "__main__":
    print("[*] Starting fast brute-force…")
    brute()
