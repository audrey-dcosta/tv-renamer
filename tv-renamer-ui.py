from tkinter import *
from tkinter import filedialog
# from tv-renamer import *
# import func
from func import *
from filefunc import *

fileList=[]
files=[]
seriesList=[]
seasonList=[]
episodeList=[]
directory=''

def clear_right():
    lbR.delete(0,'end')
    seriesList.clear()
    seasonList.clear()
    episodeList.clear()
    name_var.set('')
    typelabel.configure(text="series")
def clear_left():
    lbL.delete(0,'end')
    fileList.clear()
    entryLvar.set('')
    filelabel.configure(text="none")
def clear_both():
    clear_left()
    clear_right()

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        print(self['state'])
        self['background'] = self['activebackground']
        self['foreground']=self.defaultBackground

    def on_leave(self, e):
        if (self['state']!=ACTIVE):
            self['background'] = self.defaultBackground
            self['foreground']=self.defaultForeground

dark='black'
dark2='#080808'
light='#e0e0e0'

root = Tk()
root.state('zoomed')
root.configure(background='black')
btnlist=['renamebtn','addfilesbtn','addfolderbtn']
entryLvar=StringVar()
name_var=StringVar()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
wid=int((screen_width*42)/100)
wid2=int((screen_width*13)/100)-10
wid3=int(wid-20)

# Left Box
boxL=Frame(root,bg=dark2,width=wid,height=screen_height)
boxL.pack(side=LEFT,padx=10,pady=10)

backbtnL=HoverButton(boxL,text="<",bg=dark,fg=light,relief="flat",activebackground=light,font=('verdana','10','bold'))
backbtnL.place(x=10,y=10,width=30,height=30)

entryboxL=Frame(boxL,bg=dark)
entryboxL.place(x=50,y=10,width=wid3-110,height=30)

entryL = Entry(entryboxL,textvariable=entryLvar,bg=dark,relief="flat",font=('Verdana',9),fg=light)
entryL.place(x=4,y=6,width=wid3-120)

entrybtnL=HoverButton(boxL,bg=dark,fg=light,text='Search',relief="flat",activebackground=light)
entrybtnL.place(x=wid3-50,y=10,height=30,width=60)

lbL = Listbox(boxL,bg=dark,selectmode=MULTIPLE,highlightthickness=0,relief="flat",fg=light)
lbL.place(x=10,y=50,width=wid3,height=(screen_height-200))

btnframeL=Frame(boxL,bg=dark2)
btnframeL.place(x=10,y=(screen_height-140),width=wid3,height=44)

deleteL=HoverButton(btnframeL,command=lambda:delete_files(lbL,fileList),bg=dark,fg=light,text='Delete',height=44, width=14,relief="flat",activebackground=light)
deleteL.pack(side=LEFT,pady=2)
removeL=HoverButton(btnframeL,command=lambda:removefiles(lbL,fileList),bg=dark,fg=light,text='Remove',height=44, width=14,relief="flat",activebackground=light)
removeL.pack(side=LEFT,padx=10,pady=2)
clearL=HoverButton(btnframeL,command=lambda:clear_left(),bg=dark,fg=light,text='Clear',height=44, width=14,relief="flat",activebackground=light)
clearL.pack(side=RIGHT,pady=2)

# Center Box
boxC=Frame(root,bg=dark2,width=wid2,height=screen_height)
boxC.pack(side=LEFT,padx=5,pady=10)

btnframeC=Frame(boxC,bg=dark2)
btnframeC.place(y=((screen_height*15)/100),x=10,width=(wid2-20),height=(screen_height-200),)

addfilesbtn=HoverButton(btnframeC,command=lambda:openfiles(fileList,lbL,filelabel) ,bg=dark,fg=light,text='+Files',height=5,relief="flat",activebackground=light,font=('verdana',10))
addfilesbtn.pack(side=TOP,pady=5,padx=5,fill="both")
addfolderbtn=HoverButton(btnframeC,command=lambda:openfolder(fileList,lbL,entryLvar),bg=dark,fg=light,text='+Folder',height=5,relief="flat",activebackground=light,font=('verdana',10))
addfolderbtn.pack(side=TOP,pady=5,padx=5,fill="both")
renamebtn=HoverButton(btnframeC,command=lambda:rename(fileList,episodeList,selecbtn,entryLvar,lbL),bg=dark,fg=light,text='Rename',height=5,relief="flat",activebackground=light,font=('verdana',10))
renamebtn.pack(side=TOP,pady=5,padx=5,fill="both")
clearallbtn=HoverButton(btnframeC,command=lambda:clear_both(),bg=dark,fg=light,text='Clear All',height=5,relief="flat",activebackground=light,font=('verdana',10))
clearallbtn.pack(side=TOP,pady=5,padx=5,fill="both")

typelabel=Label(btnframeC,bg=dark2,fg=dark2,text="series")
typelabel.pack(side=TOP)
filelabel=Label(btnframeC,bg=dark2,fg=dark2,text="none")
filelabel.pack(side=TOP)

# Right Box
boxR=Frame(root,bg=dark2,width=wid,height=screen_height)
boxR.pack(side=RIGHT,padx=10,pady=10)

backbtnR=HoverButton(boxR,text="<",bg=dark,fg=light,relief="flat",activebackground=light,font=('verdana','10','bold'))
backbtnR.place(x=10,y=10,width=30,height=30)

entryboxR=Frame(boxR,bg=dark)
entryboxR.place(x=50,y=10,width=wid3-110,height=30)

entryR = Entry(entryboxR,bg=dark,textvariable=name_var,relief="flat",font=('Verdana',10),fg=light)
entryR.place(x=4,y=6,width=wid3-78)

entrybtnR=HoverButton(boxR,command=lambda:get_search_results(entryR.get(),seriesList,lbR),bg=dark,fg=light,text='Search',relief="flat",activebackground=light)
entrybtnR.place(x=wid3-50,y=10,height=30,width=60)

lbR = Listbox(boxR,bg=dark,fg=light,highlightthickness=0,relief="flat")
lbR.place(x=10,y=50,width=wid3,height=(screen_height-200))

btnframeR=Frame(boxR,bg=dark2)
btnframeR.place(x=10,y=(screen_height-140),width=wid3,height=44)

selecbtn=Button(btnframeR,command=lambda:setactive(selecbtn),bg=dark,fg=light,text='+folder rename',activebackground=light,height=44, width=14,relief="flat")
selecbtn.pack(side=LEFT,pady=2)
removeR=HoverButton(btnframeR,command=lambda:remove(lbR,episodeList),bg=dark,fg=light,text='Remove',activebackground=light,height=44, width=14,relief="flat")
removeR.pack(side=LEFT,padx=10,pady=2)
clearR=HoverButton(btnframeR,command=lambda:clear_right(),bg=dark,fg=light,text='Clear',height=44, width=14,relief="flat",activebackground=light)
clearR.pack(side=RIGHT,pady=2)

def setactive(btn):
    print(btn['relief'])
    if btn['relief']=='sunken':
        btn.config(bg=dark, fg=light, relief=FLAT,text='+folder rename')
    else:
        btn.config(bg=light, fg=dark, relief=SUNKEN,text='selected')

def on_doubleR(event):
    listtype=typelabel.cget("text")
    selected=lbR.curselection()[0]
    if listtype=='series':
        id=seriesList[selected]['series_id']
        if get_seasons(id,seasonList,lbR):
            configlabel("seasons")
            # typelabel.configure(text="seasons")
    elif listtype=='seasons':
        id=seasonList[selected]['season_id']
        series_name=seasonList[selected]['series_name']
        season_name=seasonList[selected]['season_name']
        if get_episodes(id,episodeList,series_name,lbR,season_name):
            configlabel('episodes')
            # typelabel.configure(text="episodes")
    else:
        print('err')
        configlabel('series')
        # typelabel.configure(text='series')

def on_enter(event):
    get_search_results(entryR.get(),seriesList,lbR)

def on_backR(event):
    listtype=typelabel.cget("text")
    if listtype=='episodes':
        lbR.delete(0,'end')
        for item in seasonList:
            lbR.insert('end',item['season_title'])
        configlabel('seasons')
        # typelabel.configure(text="seasons")
    elif listtype=='seasons':
        lbR.delete(0,'end')
        lbR.insert('end',*[x['series_name'] for x in seriesList])
        configlabel('series')
        # typelabel.configure(text="series")

def configlabel(title):
    print(title)
    if title=='series':
        typelabel.configure(text=title)
        renamebtn['state']=DISABLED
    elif title=='seasons':
        typelabel.configure(text=title)
        renamebtn['state']=DISABLED
    elif title=='episodes':
        typelabel.configure(text=title)
        renamebtn['state']=NORMAL
    else:
        print('smth wrong')

def on_backL(event):
    var=entryLvar.get()
    if var!='':
        f=entryLvar.get()
        folder=os.path.dirname(f)
        if get_filesinfolder(folder,lbL,fileList):
            entryLvar.set(folder)
            filelabel.configure(text="folder")

def on_doubleL(event):
    print(lbL.curselection())
    sel=lbL.curselection()[0]
    if sel !='':
        print(sel)
        if fileList[sel]['isfolder']:
            folder=f"{fileList[sel]['folder_path']}/{fileList[sel]['filename']}"
            if get_filesinfolder(folder,lbL,fileList):
                entryLvar.set(folder)

if (typelabel.cget("text")=='series'):
    renamebtn["state"]=DISABLED

lbR.bind('<Double 1>',on_doubleR)
lbL.bind('<Double 1>',on_doubleL)
entryR.bind('<Return>',on_enter)
backbtnL.bind('<Button 1>',on_backL)
backbtnR.bind('<Button 1>',on_backR)

root.mainloop()