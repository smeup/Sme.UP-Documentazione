# encoding: utf-8 
from AreeApplicative import nomiAreeApplicative, areeApplicative, areeApp
import os
import shutil

def creaCartelle():
    # Primo livello di navigazione
    if not os.path.exists('DocumentazioneSmeUP/DOC'):
        os.mkdir('DocumentazioneSmeUP/DOC')
    if not os.path.exists('DocumentazioneSmeUP/DOC_OPE'):
        os.mkdir('DocumentazioneSmeUP/DOC_OPE')
    if not os.path.exists('DocumentazioneSmeUP/DOC_VIS'):
        os.mkdir('DocumentazioneSmeUP/DOC_VIS')
    if not os.path.exists('DocumentazioneSmeUP/GLO'):
        os.mkdir('DocumentazioneSmeUP/GLO')
    if not os.path.exists('DocumentazioneSmeUP/NWS'):
        os.mkdir('DocumentazioneSmeUP/NWS')
    if not os.path.exists('DocumentazioneSmeUP/FAQ'):
        os.mkdir('DocumentazioneSmeUP/FAQ')

    # Secondo livello di navigazione
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_APP'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_APP')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SER'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SER')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG')
    if not os.path.exists('DocumentazioneSmeUP/NWS/News'):
        os.mkdir('DocumentazioneSmeUP/NWS/News')
    if not os.path.exists('DocumentazioneSmeUP/NWS/NTI'):
        os.mkdir('DocumentazioneSmeUP/NWS/NTI')

    # Terzo livello di navigazione
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/Applicazioni'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/Applicazioni')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/Componenti'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/Componenti')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/UPP'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/UPP')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/Oggetti'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/Oggetti')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/Altro'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/Altro')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/File'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/File')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/Costruttori'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/Costruttori')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/Classi'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/Classi')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/Programmi'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/Programmi')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/Tabelle'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/Tabelle')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/ValoriFissi'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/ValoriFissi')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/VAloriDinamici'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/ValoriDinamici')
    if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_OGG/Altro'):
        os.mkdir('DocumentazioneSmeUP/DOC/DOC_OGG/Altro')

    for i in range(len(areeApplicative)): # Navigazione per aree applicative e applicazioni
        for codice, nome in areeApp.items(): 
            if nome == nomiAreeApplicative[i]:
                dirName = codice
                if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_APP/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/DOC/DOC_APP/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/DOC_VIS/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/DOC_VIS/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/DOC_OPE/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/DOC_OPE/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SER/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/DOC/DOC_SER/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/DOC/DOC_SCH/Applicazioni/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/DOC/DOC_SCH/Applicazioni/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/NWS/NTI/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/NWS/NTI/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/NWS/News/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/NWS/News/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/FAQ/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/FAQ/' + dirName)
                if not os.path.exists('DocumentazioneSmeUP/GLO/' + dirName):
                    os.mkdir('DocumentazioneSmeUP/GLO/' + dirName)
                for j in range(len(areeApplicative[i])):
                    dirName = areeApplicative[i][j]
                    pathApplicazione = 'DocumentazioneSmeUP/DOC/DOC_APP/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/DOC_VIS/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/DOC_OPE/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/DOC/DOC_SER/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/DOC/DOC_SCH/Applicazioni/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/NWS/NTI/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/NWS/News/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/FAQ/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'DocumentazioneSmeUP/GLO/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)

def organizzaFile():
    basepath = './'
    for singleFile in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, singleFile)) and singleFile.endswith('.md') and singleFile != 'README.md' and singleFile != 'notFoundPage.md':
            print(singleFile[:2])

            for i in range(len(areeApplicative)):
                for j in range(len(areeApplicative[i])):
                    if areeApplicative[i][j] == singleFile[:2]:
                        for codice, nome in areeApp.items(): 
                            if nome == nomiAreeApplicative[i]:
                                pathApplicazione = 'DocumentazioneSmeUP/' + codice + '/' + areeApplicative[i][j]
                                pathModulo = pathApplicazione + '/' + singleFile[:6]
                                #print(pathModulo)
                                if not os.path.exists(pathModulo):
                                    os.mkdir(pathModulo)
                            
                        shutil.copy(singleFile, pathModulo)
                        os.remove(singleFile)

def generaIndici():
    basepath = './'
    pathGeneraIndice = os.path.abspath('generaIndici.py')
    for dirname, dirnames, _ in os.walk(basepath):
        if 'immagini' in dirnames: 
            dirnames.remove('immagini') # Esclude la cartella dal controllo
        if '.git' in dirnames: 
            dirnames.remove('.git') # Esclude la cartella dal controllo
        if 'Sorgenti' in dirnames: 
            dirnames.remove('Sorgenti') # Esclude la cartella dal controllo
        if '__pycache__' in dirnames: 
            dirnames.remove('__pycache__') # Esclude la cartella dal controllo
        for subdirname in dirnames: 
            if len(subdirname) != 6 or subdirname in areeApp: # Se subdirname in moduli, non creo l'indice perchè esiste già
                os.system(pathGeneraIndice + " \"" + os.path.abspath(dirname) + "/" + subdirname + "\" -o")

creaCartelle()
#organizzaFile()
generaIndici()     

'''
sidebar = os.path.abspath('DocumentazioneSmeUP/_sidebar.md')
basepath = 'Sorgenti'
with open(sidebar, "a+",  encoding='utf8') as f: # Trick per indicizzare tutti i doc senza visualizzarli nella sidebar
    f.write('- [](.)\n')
    f.write('<trick>\n')
    f.write('\n')
    for dirname, dirnames, filenames in os.walk(basepath):
        for singleFile in filenames:
            f.write('  - [' + singleFile + '](' + dirname.replace('\\','/').replace(' ','%20')  + '/' + singleFile +  ')\n')
    f.write('</trick>')
'''