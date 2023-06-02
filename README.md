# MusicSorter
I`m edit metadata music. I add there title, artist and image (search in internet and download)


## How to use
I am accepting files like `<Artist> - <Title>.mp4`

Run before the first run of the script. This is the installation of modules in python3:
  ```
  pip3 install -r requirements.txt
  ```
  
Usage:
```
python3 AddMetadata.py <Source_Folder> <Destination_Folder>
```
  

```
> python3 AddMetadata.py -h             
usage: AddMetadata.py [-h] [-r] path_src path_dst

I`m edit metadata music. I add there title, artist and image
(search in internet and download)

positional arguments:
  path_src         Source folder
  path_dst         Destination folder

options:
  -h, --help       show this help message and exit
  -r, --recursive  Recursive search music in folder
```
  
