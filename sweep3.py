import os



commands = [
    f"python sample_cfg.py --image-size 256 --device 5 --cfg-scale 1.25 --seed {i}" for i in range(1, 11)
]

#commands = [
#    f"python sample_vanilla.py --image-size 256 --device 6"
#]

#commands = [
#    f"python sample_cfg.py --image-size 256 --device 6 --cfg-scale {i}" for i in [1, 1.25, 1.5]
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

#commands = [
#    f"python sample_fg.py --device 6 --cfg-scale {j} --skip 24 25 26 27 --seed {i}" for i in [0, 1, 2, 3, 4] for j in [1.02, 1.04, 1.05, 1.06, 1.08, 1.1, 1.15, 1.2, 1.25]
#]

#commands = [
#    f"python sample_fg.py --device 6 --cfg-scale {i} --skip 27 --seed {j}" for i in [1 + i / 100 for i in range(26)] for j in [1, 2, 3, 4]
#]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)

'''
python sample_fg.py --device 7 --cfg-scale 1.5 --skip 14

CUDA_VISIBLE_DEVICES=4,5,6,7 torchrun --nnodes=1 --nproc_per_node=4 sample_ddp_fg.py --model DiT-XL/2 --num-fid-samples 50000 --skip 12 --cfg-scale 4



'''


