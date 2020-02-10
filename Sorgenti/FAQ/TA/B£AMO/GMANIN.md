### **Come posso cancellare una foto?**

 \* Entrare nella chiave di menù "Creazione foto";
 \* Scegliere la foto da cancellare (Foto e data);
 \* Scegliere la funzione "L".
### **Sai cos'è una foto giacenza?**

Una foto giacenza è la copia della situazione giacenza "congelata" (fotografata) ad una certa data.
Tra i possibili utilizzi della foto ci può essere quello di congelare delle chiusure mensili di magazzino, ad esempio per delle valorizzazioni, oppure per verificare l'andamento delle giacenze nel tempo.
### **Conosci i vari metodi per calcolare una foto?**

Una foto può essere calcolata : 
-  partendo dalla giacenza attuale all'indietro :  sottrae alla giacenza attuale i movimenti fino alla data foto
-  partendo dall'inizio in avanti :  somma tutti i movimenti fino alla data foto
-  copia della giacenza attuale
-  come differenza tra 2 foto
-  come differenza tra una foto e la giacenza attuale
-  come differenza tra la giacenza attuale e una foto
-  come copia del LIFO (giacenza corrente nel file GNSIAN)
-  come differemza tra una foto e il LIFO (giacenza corrente nel file GNSIAN)

### **Sai come cancellare una foto?**

Utilizzando la funzione "L" nel programma di creazione / completamento foto.
### **Sai qual'è la tabella guida?**

La tabella GMW, dove vengono inseriti gli indentificativi delle foto, dove possono essere fissate le date foto, dove possono essere fissati i parametri per la valorizzazione di default della foto ed i parametri (sottosettore) dove recuperare le informazioni per valorizzazioni differenziate.

Per una informazione più completa vedi documentazione tabella : 
- [GMW - Foto di giacenze alla data](Sorgenti/DOC/OG/TA/GMW)
### **Sai qual'è l'archivio di riferimento?**

Il file GMFOTO0F.
### **Sai come stampare dinamicamente una foto senza codificare un elemento in tabella GMW?**

Si utilizza il programma di stampa foto senza inserire l'identificativo foto ma solo la data.
### **Sai come fare foto con lo stesso nome e date diverse?**

Nella tabella GMW non si imposta la data foto, così nel programma di costruzione foto GMFO01A il campo data è libero (anche se viene preimpostato con data = oggi)
### **Sai come fissare la data di una foto?**

Basta inserire la data in tabella GMW.
### **Sai come valorizzare una foto in fase di costruzione?**

Nel programma di creazione foto GNFO01A impostare il flag di "Completamento costi". Nota bene per avere la valorizzazione della foto è necessario che almeno una delle condizioni seguenti sia verificata : 
-  tipo costo / livello impostati in Tab. GM1
-  tipo costo / livello impostati nella Tab. GMW della foto
-  tipo costo / livello impostati in Tab. GMY (vedi domande successive)
### **Sai come valorizzare una foto successivamente alla costruzione?**

Esistono 2 modi : 
-  per rendere la valorizzazione permanente, usare il programma GMFO01A con "Esecuzione funzione" = blanks (così non ricalcola le giacenze e "Completamento costi" = 1
-  si possono anche avere valorizzazioni dinamiche usando il programma di stampa GMQU01A
### **Sai dove impostare regole differenziate di valorizzazione foto?**

Nella tabella GMY che è per sottosettore (nella tab. GMW si deve inserire il sottosettore da usare per le valorizzazioni di questa foto) possono essere inseriti n. elementi ciascuno con proprie regole di valorizzazione.

Per una informazione più completa vedi documentazione tabella : 
- [GMY - Metodi valorizzaz. inventari](Sorgenti/DOC/OG/TA/GMY)
### **Sai come impostare un attributo articolo in modo che la valorizzazione abbia regole diverse in funzione dei valori assunti dall'attributo nei vari articoli?**

Nella tabella GMW si deve impostare qual'è l'attributo articolo da controllare.
### **Sai come forzare le regole di valorizzazione per articoli aventi una caratteristica specifica?**

Nella tab. GMY inserire un elemento con codice = "area/tipo giacenza/valore dell'attributo articolo". La regola è dentro l'elemento della tab. GMY.
### **Sai come forzare le regole di valorizzazione di un'area?**

Nella tab. GMY inserire un elemento con codice = "area". La regola è dentro l'elemento della tab. GMY.
### **Sai come modificare una foto dopo averla costruita?**

Nella tab. GMW è possibile inserire un suffisso del programma GMFO01U_ (vedi esempio pgm GMFO01U_X) che viene lanciato dopo l'esecuzione del programma GMFO01A.
