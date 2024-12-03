import os

commands = [
    f"CUDA_VISIBLE_DEVICES=2,3,4,5,6,7 torchrun --nnodes=1 --nproc_per_node=6 sample_ddp_fgee.py --per-proc-batch-size 64 --num-fid-samples 5000 --ee {i} --cfg-scale {j}" for i in [22, 21] for j in [1.05, 1.1, 1.15, 1.2, 1.25]
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)