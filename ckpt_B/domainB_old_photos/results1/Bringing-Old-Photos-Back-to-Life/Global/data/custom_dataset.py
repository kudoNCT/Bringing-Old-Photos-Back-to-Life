import os

from PIL import Image


class OldPhotoDataset(object):

    """
    Old photos dataset
    """

    def __int__(self, folder_path):
        self._images = []
        folder_path = self.file_path
        for file in os.listdir(folder_path):
            path = os.path.join(folder_path, file)
            self._images.append(path)

    def __getitem__(self, index):
        img = Image.open(self._images[index]).convert('RGB')
        img_name = self._images[index].split('/')[-1]
        return img_name, img

    def __len__(self):
        return len(self._images)
