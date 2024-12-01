import os

#commands = [
#    f"python sample_fgee.py --image-size 256 --device 7 --num-sampling-steps 10 --cfg-scale 10 --ee {i}" for i in range(27, -1, -1)
#]

#commands = [
#    f"python sample_vanilla.py --image-size 256 --device 7 --num-sampling-steps {i}" for i in range(1, 26)
#]

#commands = [
#    f"python sample_cfg.py --image-size 256 --device 7 --cfg-scale 1.5 --seed {i}" for i in range(5)
#]

#commands = [
#    f"python sample_bad.py --image-size 256 --device 7 --skip {i}" for i in range(28)
#]

#commands = [
#    f"python sample_unconditional.py --image-size 256 --device 7"
#]

#commands = [
#    f"python sample_fg_unconditional.py --image-size 256 --cfg-scale {i} --skip {j}" for i in [1.5, 4.0] for j in range(28)
#]

commands = [
    f"python sample_fgee.py --device 7 --cfg-scale {i} --ee {j} --seed {k}" for i in [1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55] for j in range(27, 20, -1) for k in range(1, 5)
]

#commands = [
#    f"python sample_fg.py --device 6 --cfg-scale {i} --skip 27 --seed {j}" for i in [1 + i / 100 for i in range(26)] for j in [1, 2, 3, 4]
#]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)

'''
python sample_fg.py --device 7 --cfg-scale 1.5 --skip 14

CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 torchrun --nnodes=1 --nproc_per_node=6 sample_ddp.py --model DiT-XL/2 --num-fid-samples 1000



'''


