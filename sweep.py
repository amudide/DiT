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
#    f"python sample_bad.py --image-size 256 --device 7 --num-sampling-steps {i}" for i in range(1, 26)
#]

#commands = [
#    f"python sample_unconditional.py --image-size 256 --device 7 --num-sampling-steps {i}" for i in range(1, 26)
#]

commands = [
    f"python sample_fg.py --image-size 256 --device 7 --num-sampling-steps 250 --cfg-scale {i} --skip {j}" for i in [1.5, 4.0] for j in [14, 21, 25]
]

for c in commands:
    print(c)

for cmd in commands:
    os.system(cmd)
