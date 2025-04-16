import os
from glob import glob
import json
from tqdm import tqdm
import shutil

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

def sort_filenames(filenames):
    sorted_filenames = sorted(filenames, key=lambda x: tuple(map(int, x.rstrip('.png').split('_')[1:])))
    img_list = sorted_filenames
    mask_list = [filename.replace('.png', '_mask.png') for filename in img_list]
    new_img_list = [
        '_'.join(parts[0:1]) + '_S' + '6' + '_' + str(index + 1) + '.png'
        for index, parts in enumerate((filename.split('_') for filename in img_list))
    ]
    new_mask_list = [filename.replace('.png', '_mask.png') for filename in new_img_list]

    return img_list, mask_list, new_img_list, new_mask_list

# Example paths, replace with actual paths if needed
src_path = r'annotation_json'  # Example source path
dst_path = r'annotation_png'  # Example destination path

RGB = read_json('RGB_Value.json')

id_list = os.listdir(src_path)

# example scene
scene = '6'

for id in tqdm(id_list):
    check_dir(os.path.join(dst_path, id, 'S' + '6'))
    file_list = os.listdir(os.path.join(src_path, id))
    l = []
    for file in file_list:
        if '_mask' not in file:
            img_name = file
            if '_'+scene+'_' in img_name:
                l.append(img_name)
        else:
            pass
    img_list, mask_list, new_img_list, new_mask_list = sort_filenames(l)

    for i in range(len(img_list)):
        shutil.copy(os.path.join(src_path, id, img_list[i]), os.path.join(dst_path, id, 'S' + '6', new_img_list[i]))
        shutil.copy(os.path.join(src_path, id, mask_list[i]), os.path.join(dst_path, id, 'S' + '6', new_mask_list[i]))
