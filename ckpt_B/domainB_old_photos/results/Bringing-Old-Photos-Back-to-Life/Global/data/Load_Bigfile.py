# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import io
import os
import struct
from PIL import Image


class BigFileMemoryLoader(object):
    def __load_bigfile(self):
        # print('start load bigfile (%0.02f GB) into memory' % (os.path.getsize(self.file_path) / 1024 / 1024 / 1024))
        self._images = []
        folder_path = self.file_path
        for file in os.listdir(folder_path):
            path = os.path.join(folder_path, file)
            self._images.append(path)

    def __init__(self, file_path):
        super(BigFileMemoryLoader, self).__init__()
        self.file_path = file_path
        self.__load_bigfile()

    def __getitem__(self, index):
        try:
            img = Image.open(self._images[index]).convert('RGB')
            img_name = self._images[index].split('/')[-1]
            return img_name, img
        except Exception:
            print('Image read error for index %d' % (index))
            return self.__getitem__((index + 1))

    def __len__(self):
        return len(self._images)
