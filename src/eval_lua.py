# Authored by Arjun Guha
# Copyright (c) 2022, Roblox Inc.
#
# This script runs the Luafied HumanEval programs in lua_humaneval.
import os
import subprocess

def main():
    total = 0
    successes = 0
    # For every file in lua_humaneval:
    for filename in os.listdir("lua_humaneval"):
        # If it's a .lua file:
        if filename == "luaunit.lua":
            continue
        total += 1
        # Run it with lua, suppressing all output
        p = subprocess.run(["lua", filename], cwd="lua_humaneval",
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        # Check exit code
        ok = p.returncode == 0
        if ok:
            successes += 1
        filename = filename.split(".")[0]
        print(f"Lua,{filename},{ok}")
    # print(f"{successes}/{total}")

if __name__ == "__main__":
    main()