import os
import numpy as np
from nibabel.testing import data_path
path = './ADNI_003_S_0908_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20081015153156378_S46187_I121108.nii'
example_filename = os.path.join(data_path, path)
import nibabel as nib

filename, file_extension = os.path.splitext(os.path.basename(path))
image_data_id = filename.split("_")[-1]
img = nib.load(path)

hdr = img.header.structarr

import matplotlib.pyplot as plt
epi_img_data = img.get_fdata()
from time import sleep

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

for i in range(0, 150, 10):
    slice_0 = epi_img_data[i, :, :]
    slice_1 = epi_img_data[:, i, :]
    slice_2 = epi_img_data[:, :, i]
    show_slices([slice_0, slice_1, slice_2])
    plt.suptitle("Center slices for EPI image")
    plt.show()
    sleep(0.05)
    plt.close()


import pandas as pd

data = pd.read_csv("../ADNI1_Complete_1Yr_1.5T_11_23_2020.csv")

print(data[data['Image Data ID'] == image_data_id].head())