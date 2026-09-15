import pathlib
import pandas as pd
import cv2
from torch.utils.data import Dataset
import torchvision.transforms as tf

TRASNFORM_TENSOR  = tf.Compose([
    tf.ToTensor(),
    tf.Normalize(
        mean = [0.485, 0.456, 0.406],
        std  = [0.229, 0.224, 0.225]
    )
])

class IDataset(Dataset):
    def __init__(self,
            labels    : pd.DataFrame,
            img_path  : pathlib.Path,
            img_size  : tuple[int, int],
            img_ext   : str,
            transform
        ):
        super().__init__()
        self.labels    = labels
        self.img_path  = img_path
        self.img_size  = img_size
        self.img_ext   = img_ext
        self.transform = transform
        self.length    = len(labels.index)

    def load_image(self, idx:int):
        path = str(self.img_path / f"{idx}.{self.img_ext}")
        img  = cv2.imread(str(path))
        img  = cv2.resize(img, self.img_size, interpolation=cv2.INTER_LINEAR)
        img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform:
            img = self.transform(img)

        return img

    def get_item(self, idx:int, load_image:bool=True) -> dict:
        item = self.labels.iloc[idx].to_dict()

        if load_image:
            item['img'] = self.load_image(int(item['id']))

        return item

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, idx) -> dict:
        return self.get_item(idx)