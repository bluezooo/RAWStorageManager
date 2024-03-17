### For Fujifilm's Folder Only
import os
import shutil

folder = "RAFs"
root = os.path.dirname(__file__)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
def move_files(src, dirs, files):
    # print(src, dirs, files)
    nameList = []
    for file in files:
        name, type = os.path.splitext(file)
        if type == '.JPG' or type == '.jpg' or type == '.PNG' or type == '.png':
            nameList.append(name)

    for file in files:
        name, type = os.path.splitext(file)
        if type == '.RAF' or type == '.raf' or type == '.RAW' or type == '.raw':

            realfile = os.path.join(src, file)
            # print(os.path.abspath(realfile))
            # print(os.path.relpath(realfile))
            fromFile = os.path.relpath(realfile)
            toFile = os.path.join(folder, os.path.relpath(realfile))
            toFolder, _ = os.path.split(toFile)
            
            create_folder(toFolder)
            shutil.move(fromFile, toFile)

    toFolder = os.path.join(folder, os.path.relpath(src))
    create_folder(toFolder)
    toFolderFiles = []
    for item in os.listdir(toFolder):
        if os.path.isfile(os.path.join(toFolder, item)):
            toFolderFiles.append(os.path.splitext(item)[0])
    deleteSet = set(toFolderFiles) - set(nameList)
    for delfile in toFolderFiles:
        if delfile in deleteSet:
            move_or_delete(delfile, toFolder)

                
def move_or_delete(delfile, toFolder):
    removeFile = os.path.normpath(os.path.join(toFolder, delfile)+".RAF")

    delete = True
    for srcjpg, dirs1, filejpgs in os.walk(root):
        for filejpg in filejpgs:
            
            if filejpg == delfile+'.JPG' or filejpg == delfile+'.jpg' or filejpg == delfile+'.PNG' or filejpg == delfile+'.png':
                
                srcjpgRelativePathRAF = os.path.join(folder, os.path.relpath(srcjpg))
                create_folder(srcjpgRelativePathRAF)
                toFile1 = os.path.normpath(os.path.join(srcjpgRelativePathRAF, delfile)+'.RAF')
                
                if os.path.isfile(removeFile) and removeFile != toFile1:
                    print("File moved from %s to %s" %(removeFile, toFile1))
                    shutil.move(removeFile, toFile1)
                
                delete = False
                break
    if delete == True:
        print("RAF File deleted: ", removeFile)
        os.remove(removeFile)


def main():
    RAFFolder = os.path.join(root, folder)
    create_folder(RAFFolder)
    for src, dirs, files in os.walk(root):
        if not src.startswith(os.path.join(root, folder)):
            move_files(src, dirs, files)
    for src, dirs, files in os.walk(RAFFolder):
        RAFfolderSrc= os.path.relpath(src)
        RAFfolderSrcLstrip = os.path.relpath(src)[5:]
        if RAFfolderSrcLstrip not in  os.listdir(root) and RAFfolderSrc!= folder:
            # print(RAFfolderSrc)
            for src, dirs, files in os.walk(RAFfolderSrc):
                for delfile in files:
                    toFolder = os.path.relpath(src)
                    delfile = os.path.splitext(delfile)[0]

                    move_or_delete(delfile, toFolder)

    for src, dirs, files in os.walk(root):
        if files == [] and dirs == []:
            print('Empty folder deleted: ', os.path.relpath(src))
            os.rmdir(os.path.relpath(src))


main()
print('finished')
input()