#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
from torchio import Image, Subject
import torchio
from torchio.transforms import (ZNormalization,
                                Resample, Compose, Lambda)

data_dir = './data' # put data in specific location

subjects_list = []

# populate subject list
for i in range(200):
    imageFileToCheck = os.path.abspath(os.path.join(data_dir, 'volume-' + str(i) + '.nii.gz'))
    maskFileToCheck = os.path.abspath(os.path.join(data_dir, 'segmentation-' + str(i) + '.nii.gz'))
    if os.path.isfile(imageFileToCheck):
        subject_dict = {}
        subject_dict['image'] = Image(imageFileToCheck, type=torchio.INTENSITY)
        subject_dict['label'] = Image(maskFileToCheck, type=torchio.LABEL)
        subjects_list.append(Subject(subject_dict))

# populate transform list
transforms_list = []
transforms_list.append(Resample([1,1,1]))
transforms_list.append(ZNormalization())

transform = Compose(transforms_list)