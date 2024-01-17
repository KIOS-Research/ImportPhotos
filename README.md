<a href="http://www.kios.ucy.ac.cy"><img src="https://www.kios.ucy.ac.cy/wp-content/uploads/2021/07/Logotype-KIOS.svg" width="200" height="100"/><a>

![ImportPhotos Downloads](https://img.shields.io/badge/dynamic/json?formatter=metric&color=green&label=ImportPhotos-downloads&query=%24.ImportPhotos.downloads&url=https://raw.githubusercontent.com/Mariosmsk/qgis-plugins-downloads/main/data/plugins.json) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3384824.svg)](https://doi.org/10.5281/zenodo.3384824)

## How to cite 

If you find the **"ImportPhotos" QGIS plugin** useful in your research or work, we kindly request that you cite our paper. This helps support our work and ensures that we can continue developing and maintaining the plugin. Here's the citation for your convenience:

Kyriakou, M., Christou, G., & Kolios, P. (2019). *ImportPhotos: a QGIS plugin to visualise geotagged photos*. Zenodo. [DOI:10.5281/zenodo.3384824](https://doi.org/10.5281/zenodo.3384824)

Thank you for your support!

```
@INPROCEEDINGS{kyriakou2019,
author={Kyriakou, Marios and Christou, Georgios and Kolios, Panayiotis},
title={ImportPhotos: a QGIS plugin to visualise geotagged photos},
month= {jul},
year= {2019},
DOI= {10.5281/zenodo.3384824}}
```

# ImportPhotos

QGIS plugin

This tool can be used to import Geo-Tagged photos (jpg or jpeg) as points to QGIS. The user is able to select a folder with photos and only the geo-tagged photos will be taken. Then a layer will be created which it will contain the name of the picture, its directory, the date and time taken, altitude, longitude, latitude, azimuth, north, camera maker and model, title, user comment and relative path. The plug-in doesn’t need any third party applications to work. It has two buttons; the one is to import geotagged photos, and the other one is to be able to click on a point and display the photo along with information regarding the date time and altitude. The user can create one of the following file types: GeoJSON, SHP, GPKG, CSV, KML, TAB. When the user saves a project and wants to reopen it, the folder with the pictures should stay at the original file location or moved at the same location of the project (e.g. *.qgz) in order to be able to view the pictures.* The new version of Import photos gives the ability to the user to use several basic filters on the image and save the picture. To use additional filters, the user needs to use the python package *opencv-python*.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Y3R8gHJUrrk/0.jpg)](https://www.youtube.com/watch?v=Y3R8gHJUrrk)

QGIS 3
Mac Users. Requires the following Python Modules to be installed: UnixImageIO, FreeType, PIL Please visit: http://www.kyngchaos.com/software/python

## Updated version
<img src="https://raw.githubusercontent.com/KIOS-Research/ImportPhotos/v2.2/icons/edges.PNG" width="500" height="400">
<img src="https://raw.githubusercontent.com/KIOS-Research/ImportPhotos/v2.2/icons/redband.PNG" width="500" height="400">
<img src="https://raw.githubusercontent.com/KIOS-Research/ImportPhotos/v2.2/icons/example.png" width="500" height="400">

# Contributors #
* Marios S. Kyriakou, [KIOS Research Center for Intelligent Systems and Networks, University of Cyprus (KIOS CoE)](http://www.kios.ucy.ac.cy/)
* George A. Christou, [KIOS Research Center for Intelligent Systems and Networks, University of Cyprus (KIOS CoE)](http://www.kios.ucy.ac.cy/)
* Panayiotis S. Kolios, [KIOS Research Center for Intelligent Systems and Networks, University of Cyprus (KIOS CoE)](http://www.kios.ucy.ac.cy/)

* [QGIS Cyprus](https://www.facebook.com/qgiscyprus/)
