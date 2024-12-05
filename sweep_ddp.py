import os

commands = [
    f"torchrun --nnodes=1 --nproc_per_node=4 sample_ddp_fg.py --per-proc-batch-size 32 --num-fid-samples 5000 --skip {i} --cfg-scale {j}" for j in [1.5, 1.25] for i in range(28)
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)
