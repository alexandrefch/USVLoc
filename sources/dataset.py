import pathlib
import pandas as pd
from typing import Literal

from idataset import IDataset

class Dataset(IDataset):
    def __init__(self,
        path      : pathlib.Path|str,
        name      : str,
        img_size  : tuple[int, int]              = (224, 224),
        img_ext   : str                          = 'png',
        img_type  : Literal['rgb', 'ir', 'both'] = 'rgb',
        transform                                = None
    ):
        self.name = name
        self.path = path if isinstance(path, pathlib.Path) else pathlib.Path(path)
        labels    = pd.read_csv( str(self.path / name / 'data.csv'), sep=',', dtype={0:'int', 1:'float', 2:'float', 3:'float'})
        img_path  = self.path / name / img_type
        super().__init__(labels, img_path, img_size, img_ext, transform)

        self.both = img_type == 'both'

        if self.both:
            self.length *= 2

    def __getitem__(self, idx) -> dict:
        if self.both:
            if idx < len(self.labels.index):
                self.img_path = self.path / self.name / 'rgb'
            else:
                self.img_path = self.path / self.name / 'ir'
                idx -= len(self.labels.index)

        return self.get_item(idx)