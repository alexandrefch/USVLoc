<div align="center">

# USVLoc: Infrared Topographic Based Cross-view Localization Dataset in Maritime Environment

</div>

USVLoc is a dataset designed for research in autonomous surface vehicle localization.
The dataset provides paired visual data (RGB and infrared) with precise geographical coordinates and heading information.

## Data Format

### Directory Structure

```
usvloc/
├── train/
│   ├── data.csv          # Metadata: id, lat, lon, hdt
│   ├── rgb/              # RGB images
│   └── ir/               # Infrared images
├── val/
│   ├── data.csv
│   ├── rgb/
│   └── ir/
├── test-0/ through test-4/
│   ├── data.csv
│   ├── rgb/
│   └── ir/
├── grid.csv              # Grid reference metadata
└── grid/                 # Topographic grid images
```

### CSV Format

Each split contains a `data.csv` file with the following columns:

- **id**: Unique identifier for the image pair
- **lat**: Latitude in decimal degrees (WGS84)
- **lon**: Longitude in decimal degrees (WGS84)
- **hdt**: Heading/bearing in degrees (0-360, True heading)

## Downloads

| File Name | Size (GB) | Image Count | Description | Download |
|-----------|-----------|-------------|-------------|----------|
| train.tar.gz | 36.0 | 57 804 | Training split with RGB and IR image pairs and metadata | [Download][download-train] |
| val.tar.gz | 4.0 | 6 423 | Validation split for hyperparameter tuning | [Download][download-val] |
| test_0.tar.gz | 0.6 | 900 | Test split 0 for evaluation | [Download][download-test0] |
| test_1.tar.gz | 0.6 | 900 | Test split 1 for evaluation | [Download][download-test1] |
| test_2.tar.gz | 0.5 | 901 | Test split 2 for evaluation | [Download][download-test2] |
| test_3.tar.gz | 0.6 | 901 | Test split 3 for evaluation | [Download][download-test3] |
| test_4.tar.gz | 0.2 | 753 | Test split 4 for evaluation | [Download][download-test4] |
| grid.tar.gz | 1.2 | 91 290 | Topographic grid reference images for cross-view localization | [Download][download-grid] |

[download-train]: #
[download-val]: #
[download-test0]: #
[download-test1]: #
[download-test2]: #
[download-test3]: #
[download-test4]: #
[download-grid]: #

## :black_nib: Usage and Citation

If you use this dataset in your research, please cite it as:

```bibtex
@inproceedings{foucher2026usvloc,
  title={USVLoc: Infrared Topographic Based Cross-view Localization in Maritime Environment},
  author={Foucher, Alexandre and Seguin, Cédric and Heller, Dominique and Laurent, Johann},
  booktitle={Workshop on Perception, Interaction and Decision-Making for Human Cyber-Physical Systems, International Conference on Pattern Recognition},
  year={2026}
}
```

## :handshake: Remerciements

<div align="center">

| ![AID](.github/aid.png) | ![Lab-STICC](.github/lab-sticc.svg) | ![UBS](.github/ubs.svg) |
|:---:|:---:|:---:|

Ces travaux sont réalisés dans le cadre d'une thèse au laboratoire [Lab-STICC](https://labsticc.fr) au sein de l'[Université de Bretagne Sud (UBS)](https://univ-ubs.fr).
Ces travaux sont soutenus financièrement par l'Agence Innovation Défense (AID).

</div>

## :page_with_curl: License

[![CC BY-NC-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. 
See LICENSE file for details.