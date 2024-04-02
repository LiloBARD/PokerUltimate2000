


def victoire(mainJ,cartetable):
    """Fonction qui test la combinaison que possède une main avec la table de poker

    

    
    *carteTotale est une liste contenant 7 cartes, les 2 premières la main du joueur et le reste la table"""
    carteTotale=mainJ
    for i in cartetable:
        carteTotale.append(i)
    combi=[]
    Cmb1=0
    Couleur4=['Hand','Judo','PingPong','Arc']
    NombreQFR= ['1','10','11','12','13']
    for color in Couleur4:                                            #Test de la Quinte Flush Royale
        QFR1=0
        for nombre in NombreQFR :
            if (nombre,color) in carteTotale :
                QFR1=QFR1+1
                if QFR1==5:
                    Cmb1=9
    fin=False
    if Cmb1==0:                                                         #Test Quinte FLush
        for color in Couleur4:    
            if fin == False :
                for i in range(1,11) :
                    if (str(i),color) in carteTotale:
                        i +=1
                        if (str(i),color) in carteTotale:
                            i += 1
                            if (str(i),color) in carteTotale:
                                i +=1
                                if (str(i),color) in carteTotale:
                                    i +=1
                                    if i > 13:
                                        pass
                                    else:
                                        if (str(i),color) in carteTotale:
                                            Cmb1=8
                                            fin=True
                                            break
                                        
    if Cmb1==8:
        Cmb1 = Cmb1 + i*0.01      
                

    combi=[]

    if Cmb1==0:                                                      #Test du carre si il n'y a pas de QF 
        o=0
        for i in range(1,14):
            if fin==False:
                o=0
                combi=[]
                for main in carteTotale:
                    if str(i) == main[0]:
                        combi.append(str(i))
                        o=o+1
                        if o==4:
                            Cmb1=7
                            rang=i
                            fin=True
                            break
                
                        
    if Cmb1==7:
        if rang == 1: 
            rang=14
        Cmb1 += rang*0.01   

    combi=[]
    brelan = False  
    paire2 = False  
    if Cmb1==0:                                                     #Test du Full si pas de carre 
        o=0
        for i in range(1,14):
            if brelan == False:
                o=0
                combi1=[]
                
                for main in carteTotale:
                    if str(i) == main[0]:
                        combi1.append(str(i))
                        o=o+1
                        if o==3:
                            Nop=i
                            brelan=True
                            break
        if brelan ==True :                
            for i in range(1,14):
                if paire2 != True:
                    o=0
                    combi2=[]
                    if i!=Nop:
                        for main in carteTotale:
                            if str(i) == main[0]:
                                combi2.append(str(i))
                                o=o+1
                                if o==2:
                                    Cmb1=6
                                    paire2 = True

    if Cmb1==6:
        i=1
        for main in combi1:
            if i==int(main) : 
                i=14
                Cmb1 = Cmb1+i*0.01
                break
        for i in range(13,1,-1):
            if Cmb1==6 :
                for main in combi1:
                    if i == int(main):
                        Cmb1 = Cmb1+i*0.01
                        break   

        i=1
        for main in combi2:
            
            if i==int(main) : 
                i=14
                Cmb1 = Cmb1+i*0.0001
                break
        for i in range(13,1,-1):
            for main in combi2:
                if i == int(main):
                    Cmb1 = Cmb1+i*0.0001
                    break   

    combi=[]
    rang=0
    if Cmb1==0:                                                        #Test du Couleur si pas de Full 
        o=0
        for color in Couleur4:
            o=0
            combi=[]
            for main in carteTotale:
                if color in main:
                    combi.append(str(i))
                    o=o+1
                    if int(main[0]) > rang or int(main[0]) == 1:
                        if rang == 1:
                            pass
                        else:
                            rang = int(main[0])
                    if o==5:
                        Cmb1=5           

    if Cmb1==5:
        if rang == 1: 
            rang=14
        Cmb1 += rang*0.01  

    combi=[]
    fin=False
    if Cmb1==0:                                                  #Test de la Suite si pas de Couleur 
        listenombre=[main[0] for main in carteTotale]                                              
        for i in range(13,3,-1) :
            if fin == False:
                combi=[]
                
                if str(i) in listenombre:
                    combi.append(str(i))
                    i -=1
                    if str(i) in listenombre:
                        combi.append(str(i))
                        i -= 1
                        if str(i) in listenombre:
                            combi.append(str(i))
                            i -= 1
                            if str(i) in listenombre:
                                combi.append(str(i))
                                i -= 1
                                if i > 13:
                                    i=1
                                    combi.append(str(i))
                                    
                                    if str(i) in listenombre:
                                        Cmb1=4

                                else:
                                    if str(i) in listenombre:
                                        combi.append(str(i))
                                        Cmb1=4
                                        fin=True
                                        break

    if Cmb1==4:
        if combi[-1]==1:
            Cmb1=Cmb1+14*0.01
        else :
            Cmb1=Cmb1+int(combi[0])*0.01         











    combi=[]  

    fin= False                              
                                    
    if Cmb1==0:                                                     #Test du Brelan si pas de Suite 
        o=0
        for i in range(1,14):
            if fin == False:
                combi=[]
                o=0
                for main in carteTotale:
                    if str(i) == main[0]:
                        o=o+1
                        combi.append(str(i))
                        if o==3:
                            Cmb1=3
                            fin=True
                            break
                        
    if Cmb1==3:
        i=1
        for main in combi:
    
            if i==int(main) : 
                
                i=14
                Cmb1 = Cmb1+i*0.01
                break
        for i in range(13,1,-1):
            if Cmb1==3 :
                for main in combi:
                    if i == int(main):
                        Cmb1 = Cmb1+i*0.01
                        break












    combi=[]
    paire1=False
    rang=0
    if Cmb1==0:
        i=1
        o=0 
        for main in carteTotale:
            if str(i) == main[0]:
                o=o+1
                if o==2:
                    rang=i
                    nop=i
                    paire1=True


                    
        for i in range(13,1,-1):
            if rang== 0:
                o=0
                for main in carteTotale:                # double paire
                    if str(i) == main[0]:
                        o=o+1
                        if o==2: 
                            rang=i
                            nop=i
                            paire1=True
                            break
    
    if paire1==True:
        rang2 = 0
        o = 0          
        for i in range(13,1,-1):
            if nop!=i :
                if rang2 == 0:
                    o=0
                    for main in carteTotale:
                        if str(i) == main[0]:
                            o=o+1
                            if o==2:
                                Cmb1=2  
                                rang2=i
                                break

        
                

    if Cmb1==2:
        if rang == 1:
            Cmb1 += 14*0.01
        Cmb1 += rang*0.01
        Cmb1 += rang2*0.0001
                            
    combi=[]

    rang=0
    if Cmb1==0:
        i=1
        o=0
        for main in carteTotale:
            if str(i) == main[0]:
                o=o+1
                if o==2:
                    Cmb1=1   
                    rang=i
                    
        for i in range(13,1,-1):
            if rang== 0:
                o=0
                for main in carteTotale:                #paire
                    if str(i) == main[0]:
                        
                        o=o+1
                        if o==2:
                            Cmb1=1   
                            rang=i
                            break

    if Cmb1==1:
        if rang == 1:
            Cmb1 += 14*0.01
        else:
            Cmb1 += rang*0.01

    combi=[]

    if Cmb1==0:
        a=0.01
        i=1
        test=0.15
        for main in carteTotale:
            if i==int(main[0]) : 
                i=14
                Cmb1 = Cmb1+i*a
                i=1                                       #carte haute
                if Cmb1<test:
                    test=(test/100)+test
                    a=a/100
        
        for i in range(13,1,-1):
            for main in carteTotale:
                if i == int(main[0]):
                    Cmb1 = Cmb1+i*a
                    if Cmb1<test:
                        test=(test/100)+test
                        a=a/100

    return Cmb1