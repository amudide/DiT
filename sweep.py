import os

commands = [
    f"python sample_fgee.py --image-size 256 --device 7 --num-sampling-steps 10 --ee {i}" for i in range(27, -1, -1)
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)
