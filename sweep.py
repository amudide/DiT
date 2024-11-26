import os

#commands = [
#    f"python sample_fgee.py --image-size 256 --device 7 --num-sampling-steps 10 --cfg-scale 10 --ee {i}" for i in range(27, -1, -1)
#]

#commands = [
#    f"python sample_vanilla.py --image-size 256 --device 7 --num-sampling-steps {i}" for i in range(1, 26)
#]

#commands = [
#    f"python sample_cfg.py --image-size 256 --device 7 --num-sampling-steps {i} --cfg-scale 4" for i in range(1, 26)
#]

#commands = [
#    f"python sample_bad.py --image-size 256 --device 7 --skip {i}" for i in range(28)
#]

#commands = [
#    f"python sample_unconditional.py --image-size 256 --device 7"
#]

commands = [
    f"python sample_fg_unconditional.py --image-size 256 --cfg-scale {i} --skip {j}" for i in [1.5, 4.0] for j in range(28)
]

#commands = [
#    f"python sample_fg.py --device 7 --cfg-scale {i} --skip {j} --seed 1" for i in [1.5, 4.0] for j in range(28)
#]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)

'''
python sample_fg.py --device 7 --cfg-scale 1.5 --skip 14

torchrun --nnodes=1 --nproc_per_node=4 sample_ddp_fg.py --model DiT-XL/2 --num-fid-samples 50000



'''


