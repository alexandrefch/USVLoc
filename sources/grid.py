import pathlib

import pandas as pd
import numpy as np
from scipy.spatial import KDTree

from idataset import IDataset, TRASNFORM_TENSOR

class Grid(IDataset):
    def __init__(self,
        path      : pathlib.Path|str,
        img_size  : tuple[int, int]  = (224, 224),
        img_ext   : str              = 'png',
        transform                    = None
    ):
        path        = path if isinstance(path, pathlib.Path) else pathlib.Path(path)
        labels      = pd.read_csv( str(path / 'grid.csv'), sep=',', dtype={0:'int', 1:'float', 2:'float', 3:'float'})
        img_path    = path / 'grid'
        self.kdtree = KDTree(labels[['lat','lon']].to_numpy())
        super().__init__(labels, img_path, img_size, img_ext, transform)

    def get_items(self, indexes: list[int]|np.ndarray) -> np.ndarray:
        items = self.labels.iloc[indexes].to_numpy()
        return items


    def get_nearests_from_position(self, lat:float, lon:float, k:int, workers:int=1):
        _, indexes = self.kdtree.query([lat, lon], k, workers=workers)
        nearest    = self.labels.iloc[indexes].to_numpy()

        return nearest, indexes