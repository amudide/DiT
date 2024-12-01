import os

commands = [
    f"torchrun --nnodes=1 --nproc_per_node=8 sample_ddp_fgee.py --per-proc-batch-size 64 --num-fid-samples 5000 --ee {i} --cfg-scale {j}" for i in [23, 24, 25, 26, 27] for j in [1.05, 1.1, 1.15, 1.2, 1.25]
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)
