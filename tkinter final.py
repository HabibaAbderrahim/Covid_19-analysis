# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:58:14 2020

@author: hedia
"""

from tkinter import *
import csv
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import pandas as pd
import datetime
from IPython import get_ipython
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def tunisie():
    # read the data from the downloaded CSV file.
    data = pd.read_csv('coronaviruschiffres.csv' , delimiter=";")

   



    #data.loc[data['Pays'] == 'Tunisie',]
    #while (data['Pays'] == 'Tunisie'):
    #print(data)
    Tunisie = data.loc[data['Pays'] == 'Tunisie']
    #plt.plot(tunis,label="tunisie",linestyle='--',marker='o',alpha=0.5,color='k')
    #print(pd.DatetimeIndex(data['Date']).month )
    Tunisie['month'] = pd.DatetimeIndex(Tunisie['Date']).month
    Mars = Tunisie['month'] == 3
    Avril = Tunisie['month'] == 4
    #print(Tunisie)
    Infection =Tunisie['Infections']
    #print(Infection)
    
    Date = Tunisie['Date']
    
    
    dateRev = Date.reindex(index=Date.index[::-1]) 
    dateRev.reset_index(inplace=True, drop=True)
    
    infRev = Infection.reindex(index=Infection.index[::-1]) 
    infRev.reset_index(inplace=True, drop=True)
    
    #print(dateRev)
    
    
    #Date.columns[::-1]
    #Date.iloc[::-1]
    #print(Date)
    #print(MarAv)
    

    
    
    
    plt.rcParams["figure.figsize"] = (13, 5)
    plt.title("L’évolution des nouveaux cas d’infection en Tunisie") 
    plt.xlabel('Date')  
    plt.ylabel('Nombre d’infection')  
    
    plt.xticks(rotation=90)
    plt.plot(dateRev,infRev,  'r.-', color='green', solid_capstyle="round", linewidth="1", label='infection', markersize=5)
    plt.legend();
    plt.show()

    
    
    







    
def comparaison():
    
    
    data = pd.read_csv("coronaviruschiffres.csv",delimiter=';')
    # Preview the first 5 lines of the loaded data 
    #print(data.head())
    
    
  
    
    
    AllDate = data['Date']
    #AllDate
        
            
   

    
    Avril=AllDate.loc['01/04/2020':'30/04/2020']
    #print(Avril)
        
    
    # <h3> Les données au mois du Mars <h3>

   
    
    
    x = pd.to_datetime(data.Date, format='%d/%m/%Y')
    #print(x)
    
    MarsData=data[(x > '2020-03-01') & (x < '2020-03-30')]
    #MarsData
    
    
        # <h3> Les données au mois Avril  <h3>

    
    
    
    AvrilData=data[(x > '2020-04-01') & (x < '2020-04-30')]
    #AvrilData
    
    
    # <h3>Tunisie<h3>
    
    # <h3>Tunisie en Mars <h3>
    
    
    
    
    TunisieInMars = MarsData.loc[data['Pays']=='Tunisie']
    #TunisieInMars 
    
    
    # <h3>Tunisie en Avril<h3>
    
   
    
    
    TunisieInAvril = AvrilData.loc[data['Pays']=='Tunisie']
    #TunisieInAvril
    
    
    # <h3> Tunisie tout les données <h3>
    
    
    
    
    DateAvrilTun=TunisieInAvril['Date']
    #DateAvrilTun
    InfectAvr=TunisieInAvril['Infections']
    #InfectAvr
    
    
    
    
    
    DateMarsTun=TunisieInMars['Date']
    #DateMarsTun
    InfectMars=TunisieInMars['Infections']
    #InfectMars
    
    

    
    
    TunisData = data.loc[data['Pays']=='Tunisie']
    #TunisData
    
    
   
    
    
    MarsAvrDate = TunisData['Date']
    #MarsAvrDate
    
    
    
    
    
    NbInfectionTunis= TunisData['Infections']
    NbInfectionTunis
    
    
    # <h4>L’évolution des nouveaux cas d’infection en Tunisie(2020)<h4>

   
    
    '''
    plt.rcParams["figure.figsize"] = (13, 5)
    fig = plt.figure(0)
    fig.canvas.set_window_title('L’évolution des nouveaux cas d’infection en Tunisie(2020)')
    
    plt.title("L’évolution des nouveaux cas d’infection en Tunisie")  # Titre de la courbe
    plt.xlabel('Date')  # Axe des x
    plt.ylabel('Numbre d’infection')  # Axe des y

    plt.xticks(rotation=90)
    plt.plot(MarsAvrDate, NbInfectionTunis, 'r.-', color='green', solid_capstyle="round", linewidth="1", label='infection', markersize=3)
    plt.legend(loc='upper right');
    plt.show()
    '''
    
   
    
    '''
    plt.subplot(121)
    plt.plot(DateMarsTun, InfectMars, "g--")
    plt.title("L’évolution des nouveaux cas d’infection en Tunisie en  Mars")  # Titre de la courbe
    plt.xlabel('Mars')  # Axe des x
    plt.ylabel('Numbre d’infection')  # Axe des y
    
    
    plt.subplot(122)
    plt.plot(DateAvrilTun,InfectAvr , "b--")
    plt.title("L’évolution des nouveaux cas d’infection en Tunisie en Avril")  # Titre de la courbe
    plt.xlabel('Avril')  # Axe des x
    plt.ylabel('Numbre d’infection')  # Axe des y
    
    plt.show()
    '''
    
    # <h3> Italie<h3>
        
   
    
    
    ItAll = data.loc[data['Pays']=='Italie']
    #ItAll
    
    
  
    
    
    ItAllDeces=ItAll['Deces']
    #ItAllDeces
    
    
   
    
    
    ItInMars = MarsData.loc[data['Pays']=='Italie']
    #ItInMars 
    
    
  
    
    
    ItInAvr = AvrilData.loc[data['Pays']=='Italie']
    #ItInAvr
    
    
   
    
    
    ItInAvr_Date = ItInAvr['Date']
    #ItInAvr_Date
    
    
   
    
    
    ItInMars_Date=ItInMars['Date']
    #ItInMars_Date.shape
    
    
    # <h3>Deaths Italie<h3>
    
    
    
    
    DecesMars=ItInMars['Deces']
    #DecesMars.shape
    
    
   
    
    
    DecesAvr=ItInAvr['Deces']
    #DecesAvr
    
    
    # <h3>Espagne<h3>
    
   
    
    
    EsInMars = MarsData.loc[data['Pays']=='Espagne']
    #EsInMars 
    
    EsInAvril = AvrilData.loc[data['Pays']=='Espagne']
   
    
    
    EsDataMars =EsInMars ['Date']
    #EsDataMars.shape
        
    EsDataAvril = EsInAvril['Date']    

        
        
        #MarsDateForAll= MarsData['Date']
        #MarsDateForAll
        
        
       
        
        
    DecesEspMars = EsInMars['Deces']
    #DecesEspMars.shape
    DecesEspAvril = EsInAvril['Deces']  
        
        # <h3>France<h3>
        
       
    
    
    
    
    
    
    
    FrInMars = MarsData.loc[data['Pays']=='France']
    #FrInMars 
    FrInAvril = AvrilData.loc[data['Pays']=='France']
    
   
    

    frDateMars = FrInMars ['Date']
    #frDateMars.shape
    frDateAvril = FrInAvril ['Date']
    
   
    
    
    DecesFrMars = FrInMars['Deces']
    #DecesFrMars.shape
    DecesFrAvril = FrInAvril['Deces']
    
# <h3> Italie , France , Espagne Deces <h3>
    
    
    

    #plt.rcParams["figure.figsize"] = (13, 5)
    #fig = plt.figure(0)
    #fig.canvas.set_window_title('Total des décès(2020)')
    
    # mars
    # mars
    plt.subplot(121)
    plt.xticks(rotation=90)
    plt.xlabel('Date')  # Axe des x
    plt.ylabel('Nombre des morts')  # Axe des y
    plt.title("Total des décès(Mars)")
    plt.fill_between(ItInMars_Date, DecesMars, color="#0f510e", label='Italie Mars')
    plt.fill_between(EsDataMars, DecesEspMars, color="#dd2e2e", label='Espagne Mars')
    plt.fill_between(frDateMars, DecesFrMars, color="#194070", label='France Mars')
    plt.legend(loc='upper right');
    




    plt.subplot(122)
    plt.xticks(rotation=90)
    plt.xlabel('Date')  # Axe des x
    plt.ylabel('Nombre des morts')  # Axe des y
    plt.title("Total des décès(Mars)")
    plt.fill_between(ItInAvr_Date, DecesAvr, color="#0f510e", label='Italie Mars')
    plt.fill_between(EsDataAvril, DecesEspAvril, color="#dd2e2e", label='Espagne Mars')
    plt.fill_between(frDateAvril, DecesFrAvril, color="#194070", label='France Mars')
    plt.legend(loc='upper right');
    plt.show()





def soins():
    data = pd.read_csv("coronaviruschiffres.csv",delimiter=';')
    #print(data)
    
    AllDate = data['Date']
    #print(AllDate)
    Avril=AllDate.loc['01/04/2020':'30/04/2020']
    #print(Avril)
    x = pd.to_datetime(data.Date, format='%d/%m/%Y')
    #print(x)
    AvrilData=data[(x > '2020-04-01') & (x < '2020-04-30')]
    #print(AvrilData)
    TunAll = AvrilData.loc[data['Pays']=='Tunisie']
    AlgAll = AvrilData.loc[data['Pays']=='Algérie']
    MarAll = AvrilData.loc[data['Pays']=='Maroc']
    #print(TunAll)
    #print(AlgAll)
    #print(MarAll)
    TunAllDeces=TunAll['Guerisons']
    #print(TunAllDeces)
    AlgAllDeces=AlgAll['Guerisons']
    MarAllDeces=MarAll['Guerisons']
    #print(TunAllDeces)
        
        
    Tun_Date = TunAll['Date']
    Alg_Date = TunAll['Date']
    Mar_Date = TunAll['Date']
    #print(Tun_Date)
     
    TundateRev = Tun_Date.reindex(index=Tun_Date.index[::-1]) 
    TundateRev.reset_index(inplace=True, drop=True)
        
    TuninfRev = TunAllDeces.reindex(index=TunAllDeces.index[::-1]) 
    TuninfRev.reset_index(inplace=True, drop=True)
    
    

    AlgdateRev = Alg_Date.reindex(index=Alg_Date.index[::-1]) 
    AlgdateRev.reset_index(inplace=True, drop=True)
    
    AlginfRev = AlgAllDeces.reindex(index=AlgAllDeces.index[::-1]) 
    AlginfRev.reset_index(inplace=True, drop=True)
    
    
    
    MardateRev = Mar_Date.reindex(index=Mar_Date.index[::-1]) 
    MardateRev.reset_index(inplace=True, drop=True)
        
    MarinfRev = MarAllDeces.reindex(index=MarAllDeces.index[::-1]) 
    MarinfRev.reset_index(inplace=True, drop=True)
        
    
    
    plt.rcParams["figure.figsize"] = (13, 5)
    plt.title("Guéerrisons en nord Afrique")  # Titre de la courbe
    plt.xlabel('Date')  # Axe des x
    plt.ylabel('Nombre des guéeri')  # Axe des y
        
    plt.xticks(rotation=90)
    plt.plot(AlgdateRev,AlginfRev,  'r.-', color='green', solid_capstyle="round", linewidth="1", label='Algeria', markersize=5)
    plt.plot(MardateRev,MarinfRev,  'r.-', color='red', solid_capstyle="round", linewidth="1", label='Marocco', markersize=5)
    plt.plot(TundateRev,TuninfRev,  'r.-', color='black', solid_capstyle="round", linewidth="1", label='Tunisia', markersize=5)
    
    
    plt.legend();
    plt.show()
    #PAS JOLIE 
    '''
    plt.xticks(rotation=90)
    plt.xlabel('Date')  # Axe des x
    plt.ylabel('Nombre des guéerri')  # Axe des y
    plt.title("Total des Guéeri")
    plt.fill_between(Tun_Date, TunAllDeces, color="#0f510e", label='Tunisie')
    plt.fill_between(Alg_Date, AlgAllDeces, color="#dd2e2e", label='Algerie')
    plt.fill_between(Mar_Date, MarAllDeces, color="#194070", label='Maroc')
    plt.legend(loc='upper right');
    '''
    















class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom








root = Tk()
app=FullScreenApp(root)
root.geometry("1200x700")
root.title("Coronavirus StatisTIC")
root.resizable(False, False)

img = 'corona.jpg'

h1 = Frame(root,width=1200,height=700)




c1 = Canvas(h1,width=1200,height=700)
c1.pack()

i1 = ImageTk.PhotoImage(Image.open(img).resize((1200,700), Image.ANTIALIAS))
b1 = c1.create_image(0,0 , anchor=NW,image=i1)

h1.pack()








d1 = Button(h1,border=0,compound=CENTER,width=45,height=2,bg="#730028",text="Infections",fg='white',command=tunisie)

d1.place(relx=0.05,rely=0.70)


d2 = Button(h1,border=0,compound=CENTER,width=45,height=2,bg="#70549b",text="Deaths",fg='white',command=comparaison)

d2.place(relx=0.37,rely=0.70)

d3 = Button(h1,border=0,compound=CENTER,width=45,height=2,bg="#206323",text="Soins",fg='white',command=soins)

d3.place(relx=0.69,rely=0.70)



root.mainloop()









