## RAW File Storage Manager

##### Project for Photographers who have problem dealing with the managing RAW files.
##### Project for fun :)


#### Functionalities:
- Manage unsorted messy folders with JPG/PNG and RAW/RAF files by moving RAF/RAW files into another place.
- Iterate over sub directories and remain the same structure as JPG/PNG files.
- If a JPG file is deleted, the corressponding RAW/RAD file will also be removed, ensuring better garbage RAF photos collection.
- If folders are renamed, the corressponding RAF folder will also be removed.
- If a JPG/PNG file is moved to another folder, the related RAF/RAW file will also be moved corresspondingly.
- Finish in several seconds.

#### Usage
- Put this python file under the folder containing files, directories, photos, then run this python file.
- Rename the folder name on line `5`, which will be where RAF/RAW files are stored.
- Be careful about the RAW file type(RAF or RAW)



#### Restrictions
- Cannot deal with RAW and RAF at the same time, only one type of raw file suppported, change it at line `47` and `57`.
- Cannot change JPG name, every JPG/PNG's name must be unique.


