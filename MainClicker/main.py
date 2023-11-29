from tkinter import *
from PIL import Image, ImageTk  
import pygame
import random
import sys
sys.setrecursionlimit(5000)
print(sys.setrecursionlimit(5000))

pygame.mixer.init()



def Win_End():
   win_end = Tk()
   win_end.geometry('500x250+270+200')
   win_end.title('Конец игры')
   win_end.iconbitmap('iconki\Menu.ico')
   win_end.resizable(False, False)
   
   image = Image.open("image/Menu.png")
   resize_image = image.resize((500, 250))
   img = ImageTk.PhotoImage(resize_image)
   L = Label(win_end,image = img)
   L.place(relx=0.5, rely=0.5, anchor=CENTER)    
   
   def Quit_in_Menu():
      win_end.destroy()
      
   
   Quit_in_Menu = Button(win_end,text = '<--- Выход',font = 'Roman',command = Quit_in_Menu, relief = RAISED,bg = '#20B2AA')
   Quit_in_Menu.place(x = 20,y = 210)
   Ochki_Lable_end = Label(win_end,text = f'Cчёт:{Ochki}',font = 'Times',bg = '#20B2AA', relief = RAISED)
   Ochki_Lable_end.place(x = 20,y = 20)
   L_itoms_chek = Label(win_end,text = f'Глаина:{itom_glina} \n Дерево:{itom_derevo} \n Земля:{itom_gry} \n Листья:{itom_listva} \n Песок:{itom_send}',font = 'Times',bg = '#20B2AA', relief = RAISED)
   L_itoms_chek.place(x = 120, y = 20)                 
                        
     
   
   
   
   win_end.mainloop()






def Open_inventar():
       if False in Chek_Inventar:
         win.bind('e',Inventar)
         win.focus()
     
def Inventar(event):
  
  if False in Chek_Inventar:
   Music_Menu(1,0.05)
   global win_inventar
   win_inventar = Tk()
   win_inventar.geometry('300x500+0+200')
   win_inventar.overrideredirect(1)
   win_inventar.configure(bg = '#008B8B')   
   
   kol_vo_glina = Label(win_inventar,text = f'Глина: {itom_glina}',font = 'Times',bg = 'grey',width = 10, height = 1, relief = RAISED)
   kol_vo_glina.grid(row = 0,column = 0)
   kol_vo_derevo = Label(win_inventar,text = f'Дерево: {itom_derevo}',font = 'Times',bg = 'Brown',width = 10, height = 1, relief = RAISED)
   kol_vo_derevo.grid(row = 1,column = 0)
   kol_vo_gry = Label(win_inventar,text = f'Земля: {itom_gry}',font = 'Times',bg = 'Brown',width = 10, height = 1, relief = RAISED)
   kol_vo_gry.grid(row = 2,column = 0)
   kol_vo_listva = Label(win_inventar,text = f'Листва: {itom_listva}',font = 'Times',bg = '#ADFF2F',width = 10, height = 1, relief = RAISED)
   kol_vo_listva.grid(row = 3,column = 0)
   kol_vo_send = Label(win_inventar,text = f'Песок: {itom_send}',font = 'Times',bg = '#FAFAD2',width = 10, height = 1, relief = RAISED)
   kol_vo_send.grid(row = 4,column = 0)
   Logo = Label(win_inventar,text = 'Инвентарь',font = 'Times 15',bg = '#008B8B')
   Logo.place(x = 70, y = 215)
   Ochki_Lable2 = Label(win_inventar,text = f'Счёт: {Ochki}',bg = '#20B2AA', relief = RAISED)
   Ochki_Lable2.place(x = 150,y = 120)
   
   def Craft_Topor():
     global itom_glina,itom_listva,itom_derevo,Instrumenti
     if  itom_glina >= 3 and itom_listva >= 4 and itom_derevo >= 2:
      itom_glina -= 3
      itom_listva -= 4
      itom_derevo -= 2
      Instrumenti.append('Топор')
      Music_Menu(777,1)
      
      Button_instru_Topor.destroy()
     else:
      Button_instru_Topor.configure(fg = 'red')
   def Craft_Lopata():
     global itom_glina,itom_send,itom_derevo,Instrumenti
     if  itom_glina >= 3 and itom_derevo >= 5 and itom_send >= 1 and 'Топор' in Instrumenti:
      itom_glina -= 3
      itom_derevo -= 5
      itom_send -= 1
      Instrumenti.append('Лопата')
      Music_Menu(777,1)
      
      Button_instru_Lopata.destroy()
     else:
      Button_instru_Lopata.configure(fg = 'red')
   
   
   
   
   if not 'Топор' in Instrumenti:
    Button_instru_Topor = Button(win_inventar,text = 'Создать Топор:Глина x 3 \n Листва х 4 \n Дерево x 2',font = 'Times',bg = '#1E90FF',command = Craft_Topor)
    Button_instru_Topor.grid(row = 0,column = 1,rowspan = 2)
   if not 'Лопата' in Instrumenti:
    Button_instru_Lopata = Button(win_inventar,text = 'Создать Лопату:Глина x 3 \n Дерево x 5 \n Песок x 1 \n Топор',font = 'Times',bg = '#1E90FF',command = Craft_Lopata)
    Button_instru_Lopata.grid(row = 3,column = 1,rowspan = 2)
   
   
   
   
   
   
   
   Chek_Inventar.append(True)
   Chek_Inventar.remove(False)
   if True in Chek_Inventar:
    def Zakr_inventar(event):
       Chek_Inventar.append(False)
       Chek_Inventar.remove(True)
       Music_Menu(1,0.05)
       win_inventar.destroy()
       Open_inventar()
       
   win.bind('e',Zakr_inventar)
   win.focus()

      
   win_inventar.mainloop()

global Chek_Inventar
Chek_Inventar = [False]

def Start():
    win.title('Игра')
    win.iconbitmap('iconki\Game.ico')
    global Fon_l
    image = Image.open("image/Zadni_fon/Fon_Lobi.jpg")
    resize_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resize_image)
    Fon_l = Label(win,image = img)
    Fon_l.place(relx=0.5, rely=0.5, anchor=CENTER) 
    
    Game_menu = Menu(win) 
    win.config(menu=Game_menu)
    global pertmtn
    pertmtn = ['Обычный мир'] 
     
    def Nazat_in_Menu2(): 
       Ochki_Lable.destroy()
       suund_Button.play()
       B_Nazad.destroy()
       Game_menu.destroy()
       Game_Button.destroy()
       Vizen_Progress.destroy()
       L.destroy()
       
       
       WIN_Menu()
   
    def Normol_world():
     
     win.title('Обычный мир')
     win.iconbitmap('iconki\Game.ico')
     
     if 'Обычный мир' in pertmtn: 
      suund_Button.play()
      Fon_l.destroy()
      
      global B_Nazad,Game_Button, L
      
      Fon_world = {1:'Мир.jpg',2:'Мир2.jpg',3:'Мир3.jpg',4:'Мир4.jpg',5:'Мир5.png',}
      image = Image.open(f"image/Zadni_fon/{Fon_world[random.randint(1, 5)]}")
      resize_image = image.resize((500, 500))
      img = ImageTk.PhotoImage(resize_image)
      L = Label(win,image = img)
      L.place(relx=0.5, rely=0.5, anchor=CENTER)
      pertmtn.append('нет обычный мир')
      pertmtn.remove('Обычный мир')
      
      
      image_Button4 = ImageTk.PhotoImage(file="image/Button_Fon 4.png")
      B_Nazad = Button(win,fg = '#20B2AA',image = image_Button4,padx = 50,pady = 10,highlightthickness=0,relief = RAISED,bg = '#1E90FF',activebackground = '#1E90FF',command = Nazat_in_Menu2)
      B_Nazad.place(x = 10,y = 450)
      
      Texture_objact = {1:'Глина.png',2:'Дерево.png',3:'Земля.png',4:'Листва.png',5:'Песок.png',11:'grey',22:'#8B4513',33:'#8B4513',44:'#32CD32',55:'#EEE8AA'}
      
      def bloki_Normal_world():
         global blok ,Progress,list_blok,itom_send, itom_gry, itom_glina, itom_listva, itom_derevo, Instrumenti
         
         if 'Топор' in Instrumenti:
            Progress += 40
            if 'Лопата' in Instrumenti:
              Progress += 30
         else:
            Progress += 25
         
         
         
         Vizen_Progress.configure(text = f'{Progress}%')
         if 1 in list_blok:
            Music_Menu(blok+10,1)
         elif 2 in list_blok:
            Music_Menu(blok+20,1)
         elif 3 in list_blok:
            Music_Menu(blok+30,1)
         elif 4 in list_blok:
            Music_Menu(blok+40,1)
         elif 5 in list_blok:
            Music_Menu(blok+50,1)
         else:
            Music_Menu(11,1)

         if Progress >= 100:
          if 1 in list_blok:
               itom_glina += 1
          elif 2 in list_blok:
               itom_derevo += 1
          elif 3 in list_blok:
               itom_gry += 1
          elif 4 in list_blok:
               itom_listva += 1
          elif 5 in list_blok:
               itom_send += 1
          else:
               itom_glina += 1
         
         if Progress >= 100:
           global Ochki,Tip_world
           
           Ochki += 1
           
           Progress = 0
           Music_Menu(66,1)
           Vizen_Progress.configure(text = f'{Progress}%')
           Ochki_Lable.configure(text = f'Счёт:{Ochki}')
           blok = random.randint(1, 5)
           image_objact = ImageTk.PhotoImage(file=f"image/Texsture_Objact/Normal_world/{Texture_objact[blok]}")
           Game_Button.configure(image = image_objact,bg = Texture_objact[blok*11],activebackground = Texture_objact[blok*11])
           Vizen_Progress.configure(text = f'{Progress}%',bg = Texture_objact[blok*11])
           
           list_blok.append(blok)
           
           if len(list_blok) > 1:
            list_blok.pop(0)
         
           if True in Tip_world: 
             if Ochki >= 10:
               win.destroy()
               Win_End()
           else:
             pass 
         win.mainloop()
           
      
      global Progress, Vizen_Progress, Ochki_Lable, list_blok
      Progress = 0
      list_blok = []
      
      image_objact = ImageTk.PhotoImage(file=f"image/Texsture_Objact/Normal_world/{Texture_objact[1]}")
      Game_Button = Button(win,fg = '#20B2AA',command = bloki_Normal_world,image = image_objact,padx = 50,pady = 10,highlightthickness=0,relief = RAISED,bg = 'grey',activebackground = 'grey')
      Game_Button.place(x=200, y= 170)
      
      Open_inventar()
      
      Vizen_Progress = Label(win,text = '0%',font = 'Times',bg = 'grey',relief = RAISED)
      Vizen_Progress.place(x=232, y= 210)
      
      Ochki_Lable = Label(win,text = f'Cчёт:{Ochki}',font = 'Times',bg = '#20B2AA', relief = RAISED)
      Ochki_Lable.place(x=400, y= 470)

      mainloop()
    
    
    if 'Обычный мир' in pertmtn:
     Game_plashka = Menu(Game_menu, tearoff=0)
     Game_plashka.add_command(label='Обычный мир',command = Normol_world)
    
    Game_menu.add_cascade(label='Места',menu=Game_plashka)
    Game_menu.add_cascade(label='Инвентарь[E]')
                     
    
    mainloop() 


def Sating():
    win.title('Опции')
    win.iconbitmap('iconki\Seting.ico')
    image = Image.open("image/Fon_Seting.png")
    resize_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resize_image)
    L = Label(win,image = img)
    L.place(relx=0.5, rely=0.5, anchor=CENTER)   
    
    
    def Nazat_in_Menu(): 
       suund_Button.play()
       scal.destroy()
       L.destroy()
       B_Seting.destroy()
       L_Seting.destroy()
       L_Seting2.destroy()
       Rad_Button1.destroy()
       Rad_Button2.destroy()
       Rad_Button3.destroy()
       L_Seting3.destroy()
       WIN_Menu()

    image_Button4 = ImageTk.PhotoImage(file="image/Button_Fon 4.png")
    B_Seting = Button(win,fg = '#20B2AA',image = image_Button4,padx = 50,pady = 10,highlightthickness=0,relief = RAISED,bg = '#1E90FF',activebackground = '#1E90FF',command = Nazat_in_Menu)
    B_Seting.place(x = 10,y = 450)
    
    L_Seting = Label(win,fg = '#1E90FF',padx = 10,pady = 5,highlightthickness=0,relief = RAISED,bg = '#00FFFF',text = 'Громкость музыки',font = 'Tims')
    L_Seting.place(x = 10,y = 15)

    
    scal = Scale(win,bg = '#00FFFF',activebackground = '#00FF7F',orient=HORIZONTAL,length=300,from_=0,to=100,tickinterval=10,resolution=1,font = 'Tims',variable = 10)
    scal.place(x = 180,y = 0)

   
    
    var_svz = IntVar()
    var_svz.set(0)
    
    
    L_Seting2 = Label(win,text = 'Музыка:',fg = '#1E90FF',padx = 30,pady = 5,highlightthickness=0,relief = RAISED,bg = '#00FFFF',font = 'Tims')
    L_Seting2.place(x = 195,y = 130)
    
    Rad_Button_ico1 = ImageTk.PhotoImage(file="image\Music1.png")
    Rad_Button_ico2 = ImageTk.PhotoImage(file="image\Music2.png")
    Rad_Button_ico3 = ImageTk.PhotoImage(file="image\Music3.png")
    
                
    
    
    
    def Gromkos(event):
     h = scal.get()
     if var_svz.get() == 1: 
       if h == 0:
        pygame.mixer.music.stop()
       elif h >= 10:
        Music_Menu(2,0.1)
       elif h >= 20:
        Music_Menu(2,0.2)
       elif h >= 30:
        Music_Menu(2,0.3)
       elif h >= 40:
        Music_Menu(2,0.4)
       elif h >= 50:
        Music_Menu(2,0.5)
       elif h >= 60:
        Music_Menu(2,0.6)
       elif h >= 70:
        Music_Menu(2,0.7)
       elif h >= 80:
        Music_Menu(2,0.8)
       elif h >= 90:
        Music_Menu(2,0.9)
       elif h >= 100:
        Music_Menu(2,100)
     elif var_svz.get() == 2:
       if h == 0:
        pygame.mixer.music.stop()
       elif h >= 10:
        Music_Menu(20,0.1)
       elif h >= 20:
        Music_Menu(20,0.2)
       elif h >= 30:
        Music_Menu(20,0.3)
       elif h >= 40:
        Music_Menu(20,0.4)
       elif h >= 50:
        Music_Menu(20,0.5)
       elif h >= 60:
        Music_Menu(20,0.6)
       elif h >= 70:
        Music_Menu(20,0.7)
       elif h >= 80:
        Music_Menu(20,0.8)
       elif h >= 90:
        Music_Menu(20,0.9)
       elif h >= 100:
        Music_Menu(20,1)
     elif var_svz.get() == 3:
       if h == 0:
        pygame.mixer.music.stop()
       elif h >= 10:
        Music_Menu(30,0.1)
       elif h >= 20:
        Music_Menu(30,0.2)
       elif h >= 30:
        Music_Menu(30,0.3)
       elif h >= 40:
        Music_Menu(30,0.4)
       elif h >= 50:
        Music_Menu(30,0.5)
       elif h >= 60:
        Music_Menu(30,0.6)
       elif h >= 70:
        Music_Menu(30,0.7)
       elif h >= 80:
        Music_Menu(30,0.8)
       elif h >= 90:
        Music_Menu(30,0.9)
       elif h >= 100:
        Music_Menu(30,1)
    
    
    
    
    Rad_Button1 = Radiobutton(win,variable=var_svz, value=1,bg = '#00FFFF',fg = '#7CFC00',relief = RAISED,image = Rad_Button_ico1,activebackground = '#00FFFF')
    Rad_Button1.place(x = 30,y = 170)              
    Rad_Button2 = Radiobutton(win,variable=var_svz, value=2,bg = '#00FFFF',fg = '#FF8C00',relief = RAISED,image = Rad_Button_ico2,activebackground = '#00FFFF')
    Rad_Button2.place(x = 200,y = 180)                
    Rad_Button3 = Radiobutton(win,variable=var_svz, value=3,bg = '#00FFFF',fg = '#FF8C00',relief = RAISED,image = Rad_Button_ico3,activebackground = '#00FFFF')
    Rad_Button3.place(x = 370,y = 170)  


    scal.bind("<B1-Motion>",Gromkos)
   
    global var_svz2,Tip_world
    
    var_svz2 = IntVar()
    var_svz2.set(0)

   
    
    L_Seting3 = Label(win,text = 'Тип игры:' ,fg = '#1E90FF',padx = 30,pady = 5,highlightthickness=0,relief = RAISED,bg = '#00FFFF',font = 'Tims')
    L_Seting3.place(x = 195,y = 300)
    
    Rad_Tip_world_ico_1 = ImageTk.PhotoImage(file="image\Tip_world_defold_world.png")
    Rad_Tip_world_ico_2 = ImageTk.PhotoImage(file="image\Tip_world_while_world.png")
    
    def _True_():
      Tip_world.append(True)
      Tip_world.remove(False)
      print(Tip_world)
    
    def _False_():
      Tip_world.append(False)
      Tip_world.remove(True)
      print(Tip_world)
    
    Rad_Tip_world1 = Radiobutton(win,variable=var_svz2, value=1,bg = '#00FFFF',fg = '#7CFC00',relief = RAISED,image = Rad_Tip_world_ico_1,activebackground = '#00FFFF',command = _True_)
    Rad_Tip_world1.place(x = 30,y = 350)
    Rad_Tip_world2 = Radiobutton(win,variable=var_svz2, value=0,bg = '#00FFFF',fg = '#7CFC00',relief = RAISED,image = Rad_Tip_world_ico_2,activebackground = '#00FFFF',command = _False_)
    Rad_Tip_world2.place(x = 370,y = 350)
    
    
    
    
    
    mainloop()

def WIN_Menu(): 
 win.title('Меню')
 win.iconbitmap('iconki\Menu.ico')
 image = Image.open("image/Menu.png")
 resize_image = image.resize((500, 500))
 img = ImageTk.PhotoImage(resize_image)
 L = Label(win,image = img)
 L.place(relx=0.5, rely=0.5, anchor=CENTER)                        
                    
 def Button_1():
    B1.destroy()
    B2.destroy()
    B3.destroy()
    L.destroy()
    Music_Menu(1,0.05)
    Start()

 def Button_2():
    B1.destroy()
    B2.destroy()
    B3.destroy()
    L.destroy()
    Music_Menu(1,0.05)
    Sating()
    
 def Button_3():
    quit()
 
 image_Button = ImageTk.PhotoImage(file="image/Button_Fon.png")
 image_Button2 = ImageTk.PhotoImage(file="image/Button_Fon 2.png")
 image_Button3 = ImageTk.PhotoImage(file="image/Button_Fon 3.png")

 B1 = Button(win,fg = '#20B2AA',image = image_Button,padx = 50,pady = 10, command = Button_1,highlightthickness=0,relief = RAISED,bg = '#1E90FF',activebackground = '#1E90FF')
 B2 = Button(win,fg = '#20B2AA',image = image_Button2,padx = 50,pady = 10, command = Button_2,highlightthickness=0,relief = RAISED,bg = '#1E90FF',activebackground = '#1E90FF')
 B3 = Button(win,fg = '#20B2AA',image = image_Button3,padx = 50,pady = 10, command = Button_3,highlightthickness=0,relief = RAISED,bg = '#1E90FF',activebackground = '#1E90FF')
 B1.place(x = 220,y = 100)
 B2.place(x = 220,y = 200)
 B3.place(x = 220,y = 300)
 
 win.mainloop()

def Music_Menu(M,S):
    if M == 1:
     global suund_Button,suund_wood
     suund_Button = pygame.mixer.Sound('Souns\Souns_Button.mp3')
     suund_Button.set_volume(0.05)
     suund_Button.play()
    elif M == 2:
     pygame.mixer.music.stop()
     pygame.mixer.music.load('Music\Music_Menu1.mp3')
     pygame.mixer.music.set_volume(S)
     pygame.mixer.music.play()
    elif M == 20:
     pygame.mixer.music.stop()
     pygame.mixer.music.load('Music\Music_Menu2.mp3')
     pygame.mixer.music.set_volume(S)
     pygame.mixer.music.play()
    elif M == 30:
     pygame.mixer.music.stop()
     pygame.mixer.music.load('Music\Music_Menu3.mp3')
     pygame.mixer.music.set_volume(S)
     pygame.mixer.music.play()
    elif M == 3:
     pygame.mixer.music.stop()
    elif M == 11:
     suund_wood = pygame.mixer.Sound('Souns\Souns_blok\Глина.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 22:
     suund_wood = pygame.mixer.Sound('Souns\Souns_blok\Дерево.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 33:
     suund_wood = pygame.mixer.Sound('Souns\Souns_blok\Земля.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 44:
     suund_wood = pygame.mixer.Sound('Souns\Souns_blok\Листва.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 55:
     suund_wood = pygame.mixer.Sound('Souns\Souns_blok\Песок.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 66:
     suund_wood = pygame.mixer.Sound('Music\подбор предмета.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    elif M == 777:
     suund_wood = pygame.mixer.Sound('Music\Звук крафта.mp3')
     suund_wood.set_volume(S)
     suund_wood.play()
    else:
     pygame.mixer.music.stop()

global win,Ochki,Tip_world,var_svz2,Instrumenti
var_svz2 = 0
Tip_world = [False]
Ochki = 0
Instrumenti = []


win = Tk()
win.geometry('500x500+320+100')
win.resizable(False,False)

# Придметы:
itom_glina = 0 
itom_derevo = 0  
itom_gry = 0  
itom_listva = 0 
itom_send = 0 
# Инструменты:
Instru_Topor = 0
Instru_Lopata = 0 
Instru_Kirka = 0
Instru_Nojnci = 0

WIN_Menu()



