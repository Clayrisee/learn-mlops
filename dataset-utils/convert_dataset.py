"""
Script for convert roboflow yolo darknet into yolo dataset format in yolox
"""
import argparse
import os
import shutil
from glob import glob

SUBSET_DATASET = ["train", "valid", "test"]
IGNORED_EXTENSIONS = ["labels"]
LABELS_EXTENSIONS = ["txt"]
IMGS_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']

def get_file_extenstions(filepath):
    ext = filepath.split(".")[-1]
    # print(f"File Extension {ext}")
    return ext

def is_ignored_extension(filepath):
    ext = get_file_extenstions(filepath)
    return ext.lower() in IGNORED_EXTENSIONS

def is_image_extenstion(filepath):
    ext = get_file_extenstions(filepath)
    return ext.lower() in IMGS_EXTENSIONS

def is_label_extension(filepath):
    ext = get_file_extenstions(filepath)
    return ext.lower() in LABELS_EXTENSIONS

def create_list_images_txt(list_filepaths, subset, out_dir="data"):
    list_filepath = []
    for filepath in list_filepaths:
        if is_image_extenstion(filepath=filepath):
            list_filepath.append(str(os.path.join(subset, out_dir,filepath)))
    return list_filepath

def read_and_write_obj_names(filepath, outdir):
    labels = []
    with open(filepath, "r") as f:
        labels = f.read().split("\n")
    
    with open(os.path.join(outdir, "obj.names"), "w") as f_labels:
        for label in labels:
            f_labels.write("%s\n" % label)

def write_image_list_path_txt(outdir, img_lists):
    with open(os.path.join(outdir, "images.txt"), "w") as f:
        for img_path in img_lists:
            f.write("%s\n" % img_path)

def move_img_label_to_new_folder(list_filepaths, output_directory, folder="data",replace=False):
    os.makedirs(os.path.join(output_directory, folder), exist_ok=True)
    for filepath in list_filepaths:
        if not is_ignored_extension(filepath):
            filename = filepath.split("/")[-1]
            if not replace:
                shutil.copy(filepath, os.path.join(output_directory, folder, filename))
            else:
                shutil.move(filepath, os.path.join(output_directory, folder, filename))
        else:
            read_and_write_obj_names(filepath, outdir=output_directory)
    

def parse_args():
    parser = argparse.ArgumentParser(description="SKU Multilabel Trainer MLflow")
    parser.add_argument("-d", "--directory", required=True, type=str,
                        help="path to roboflow yolo darknet dataset")
    parser.add_argument("-o", "--output", default="./outputs/", type=str,
                        help="path to output. Default: outputs/"
                        )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    dataset_name = args.directory.split("/")[-1]
    src_dir = args.directory
    output_dir = os.path.join(args.output, dataset_name)
    os.makedirs(output_dir, exist_ok=True)
    
    for subset in SUBSET_DATASET:
        subset_dir = os.path.join(src_dir, subset)
        # print(subset_dir)
        subset_output_dir = os.path.join(output_dir, subset)
        os.makedirs(subset_output_dir, exist_ok=True)
        list_files = os.listdir(subset_dir)
        # print(list_files)
        image_path_list = create_list_images_txt(list_files, subset)
        # print(image_path_list)
        list_files = glob(f"{subset_dir}/*")
        # print(list_files)
        write_image_list_path_txt(subset_output_dir, img_lists=image_path_list)
        move_img_label_to_new_folder(list_files, subset_output_dir)
        