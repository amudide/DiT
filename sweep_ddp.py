import os

commands = [
    f"torchrun --nnodes=1 --nproc_per_node=8 sample_ddp_fgee.py --per-proc-batch-size 64 --num-fid-samples 5000 --ee 25 --cfg-scale 1.1 --interval {i / 10}" for i in range(11)
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)
