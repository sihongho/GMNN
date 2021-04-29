'''
Author: your name
Date: 2021-04-09 21:57:45
LastEditTime: 2021-04-28 21:52:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
'''
import sys
import os
import copy
import json
import datetime

opt = dict()

opt['dataset'] = '../data/data_format2'
opt['hidden_dim'] = 16
opt['input_dropout'] = 0.5
opt['dropout'] = 0
opt['optimizer'] = 'rmsprop'
opt['lr'] = 0.05
opt['decay'] = 5e-4
opt['self_link_weight'] = 1.0
opt['pre_epoch'] = 100
opt['epoch'] = 100
opt['iter'] = 1
opt['use_gold'] = 1
opt['draw'] = 'smp'
opt['tau'] = 0.1

def generate_command(opt):
    cmd = 'python3 train.py'
    for opt, val in opt.items():
        cmd += ' --' + opt + ' ' + str(val)
    return cmd

def run(opt):
    opt_ = copy.deepcopy(opt)
    os.system(generate_command(opt_))

from datetime import datetime
start = datetime.now()
start_time = start.strftime("%H:%M:%S")
print("Start Time =", start_time)

for k in range(100):
    seed = k + 1
    opt['seed'] = seed
    run(opt)

end = datetime.now()
end_time = end.strftime("%H:%M:%S")
print("End Time =", end_time)
# t = end - start
# print("Comsuming Time =", t.strftime("%H:%M:%S"))
