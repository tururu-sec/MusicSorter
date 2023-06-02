import music_tag
from os import listdir, walk, path
from shutil import copyfile
from GetAlbumArt import get_artwork
from alive_progress import alive_bar
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(
        description='I`m edit metadata music. I add there title, artist and image \
            (search in internet and download)')

    parser.add_argument('path_src', type=str,
                    help='Source folder')
    parser.add_argument('path_dst', type=str,
                    help='Destination folder')
    parser.add_argument('-r', '--recursive', action='store_true',
                help='Recursive search music in folder')
    return parser.parse_args()

def checkToExists(pathSrc:str, pathDst:str):
    if not(path.exists(pathSrc)):
        print(f"File '{pathSrc}' not exists!")
        exit(1)
    if not(path.exists(pathDst)):
        print(f"File '{pathDst}' not exists!")
        exit(1)


def recursiveSearch(pathSrc: str, recursion: bool):
    folders = []
    if recursion:
        listMelodies = []
        foldersTemp=[]
        for path, currentDirectory, files in walk(pathSrc):
            foldersTemp.append(path)

        folders = list(dict.fromkeys(foldersTemp)) ## remove dublicates
        
        for folder in folders:
            listMelodies.append( [n for n in listdir(folder) if '.mp3' in n] )

    else:
        listMelodies = [n for n in listdir(pathSrc) if '.mp3' in n]
        folders.append(pathSrc)
        
    return listMelodies, folders

def addMetadata(pathDest:str , listMelodies:list , folders: list, recursive:bool ):
    try:
        with alive_bar(len(listMelodies),bar = 'bubbles', spinner = 'notes2') as bar:
            for folder in folders:
                if recursive:
                    namesMel = listMelodies[ folders.index(folder) ]
                else:
                    namesMel = listMelodies
                
                for name in namesMel:
                    src = folder + '/' + name
                    dst = pathDest+ '/' + name
                    copyfile(src, dst)

                    title, artist = name.split(' - ')[1][:-4], name.split(' - ')[0]
                    melody = music_tag.load_file(dst)
                    artwork = get_artwork(title, artist)
                    melody['title'] = title
                    melody['artist'] = artist
                    melody['artwork'] = artwork
                    melody.save()

                    notif=''
                    if artwork != None:
                        notif = ' (+ image)'
                    print(artist + ' : '+ title + notif)

                    bar()
    except KeyboardInterrupt:
        exit(1)

args = parseArgs()
checkToExists(args.path_src, args.path_dst)
listMelodies, folders = recursiveSearch(args.path_src, args.recursive)
addMetadata(args.path_dst, listMelodies, folders, args.recursive)




