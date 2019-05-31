import os.path as osp


DATA_ROOT = './data'
RAW_POS_DIR = osp.join(DATA_ROOT, 'normal')
RAW_NEG_DIR = osp.join(DATA_ROOT, 'abnormal')

TRAIN_DATA_DIR = osp.join(DATA_ROOT, 'train')
VAL_DATA_DIR = osp.join(DATA_ROOT, 'val')
