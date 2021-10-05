from tkinter import filedialog
from tkinter import messagebox as mb
import os
import sys

def openfolder(List,lb,entry):
    folder=filedialog.askdirectory()
    if folder:
        get_folder(folder,List,lb)
        entry.set(folder)
        # label.configure(text="folder")

def openfiles(List,lb,label):
    files=filedialog.askopenfilenames()
    if files:
        get_files(files,List,lb,label)

def insertfiles(folder,List,lb):
    for filename in os.listdir(folder):
        ext=os.path.splitext(filename)[1]
        if os.path.isdir(f'{folder}/{filename}'):
            isfolder=True
            sym='+'
        else:
            isfolder=False
            sym='-'
        List.append({'folder_path':folder,'filename':filename,'isfolder':isfolder,'sym':sym,'ext':ext})
        lb.insert('end',f'{sym} {filename}')

def get_folder(folder,List,lb):
    if folder:
        try:
            insertfiles(folder,List,lb)
            print(List)
        except Exception as e:
            print(e)
        return

def get_files(files,List,lb,label):
    if files:
        try:
            for fn in files:
                folder=os.path.dirname(fn)
                filename=os.path.basename(fn)
                ext=os.path.splitext(fn)[1]
                List.append({'folder_path':folder,'filename':filename,'isfolder':False,'sym':'-','ext':ext})
                lb.insert('end',f'- {filename}')
            label.configure(text='files')
        except Exception as e:
            print(e)
        return

def get_filesinfolder(folder,lb,List):
    try:
        lb.delete(0,'end')
        List.clear()
        insertfiles(folder,List,lb)
        return True
    except Exception as e:
        print(e)
        return False

def removefiles(lb,List):
    sel=lb.curselection()
    for index in sel[::-1]:
        lb.delete(index)
        del List[index]

def delete_files(lb,List):
    sel=lb.curselection()
    res=mb.askquestion('Delete','do you really want to delete these files from the system?')
    if res=='yes':
        try:
            for index in sel[::-1]:
                filepath=f"{List[index]['folder_path']}/{List[index]['filename']}"
                os.remove(filepath)
                lb.delete(index)
                del List[index]
        except Exception as e:
            mb.showerror('error',e)
    else:
        print('aborted')

def rename(fileList,episodeList,btn,var,lb):
    if (len(fileList) == len(episodeList)):
        print(len(fileList))
        res=mb.askquestion('rename','do you really want to rename these files ps. make sure to close files')
        if res=='yes':
            try:
                for fn,ep in zip(fileList,episodeList):
                    newfilename=f"{fn['folder_path']}/{ep['episode_name']}{fn['ext']}"
                    oldfilename=f"{fn['folder_path']}/{fn['filename']}"
                    print(f'{oldfilename} to {newfilename}')
                    os.rename(oldfilename,newfilename)
                if (btn['relief']=='sunken'):
                    oldfolderpath=var.get()
                    op=os.path.dirname(oldfolderpath)
                    newfolderpath=f"{op}/{episodeList[0]['season_name']}"
                    os.rename(oldfolderpath,newfolderpath)
                mb.showinfo('Rename',f'{len(fileList)} files renamed')
                folder=var.get()
                get_filesinfolder(folder,lb,fileList)
            except Exception as e:
                mb.showerror('error',e)
                folder=var.get()
                get_filesinfolder(folder,lb,fileList)
        else:
            print('aborted')
    else:
        mb.showerror('unequal lists','the item to rename are not the same lenght as the other list')

