### **Messaggi di controllo documenti**

In questo documento sono raccolti i messagggi che ritorna il controllo di un documento.
Il prefisso indica il tipo di azione
- A - Riga aggiunta
- C - Cambiamento (alla tag o al paragrafo)
- E - Riga eliminata
Ogni messaggio ha, come attributo, un livello di gravità di due caratteri.
Esso, preceduto dal carattere L, identifica una ulteriore voce :  in questo modo si può documentare il livello del messaggio. Ad esempio il livello 10 si documenta nella voce L10.
Il programma di controllo documentazione ritorna il livello massimo dei messaggi, che costituisce quindi il risultato del controllo.
Ci sono alcuni messaggi di massima gravità, che nnon derivano dal  livello degli altri messaggi 'di riga' ma sono attribuiti gobalmente dal controllo :  e sono L80, L90, L91 e L92.

### **Nessun errore**

Nessun errore o azioni previste nella sintassi

### **Sistemazioni **

Sistemazioni locali

### **Incongruenze eliminate**

Inconguenze locali eliminate :  righe in posizione non ammessa

### **Sviluppo incompleto**

Documento non completamente sviluppato :  Inclusioni non risolte


### **Documento vuoto**

Il documento originale è vuoto

### **Documento pieno**

Il documento originale è troppo grande

### **Documento riempito da include**

Il documento, durante le inclusioni, è diventato troppo grande

### **Documento riempito da espansione**

Il documento, durante i completamenti, è diventato troppo grande


### **Eliminazione prevista**

La riga viene eliminata perchè previsto :  riga di inclusione, TAGxxx, REMxxx

### **Inclusione di membro non eseguita**

L'inclusione di un membro (o di una parte di esso) non ha prodotto nessuna riga

### **Inclusione di servizio non eseguita**

L'inclusione del risultato di un servizio non ha prodotto nessuna riga

### **Inclusione eliminata**

L'inclusione all'interno di un inclusione non è ammessa

### **Riga di blocco eliminata**

All'interno di un blocco PAR/PAR.END non può esserci una riga di questo tipo.

### **Riga elminata :  fine blocco**

All'esterno di un blocco PAR/PAR.END non può esserci una riga di questo tipo.

### **Riga eliminata :  estranea alla tabella**

All'interno di un blocco TAB/TAB.END non può esserci una riga di questo tipo.

### **Riga di tabella eliminata**

All'esterno di un blocco TAB/TAB.END non può esserci una riga di questo tipo.

### **Riga eliminata :  sviluppata in colonne**

La prima riga all'interno di una tabella, se non presenti TAG.COL espliciti, viene sviluppata in colonne, e quindi eliminata come riga.

### **Commento**

Una riga di commento viene eliminata logicamente

### **Titolo unico eliminato**

Nel documento c'è un solo titolo che viene eliminato.
NB :  a differenza di tutte le altre eliminazioni logiche, di cui si tiene conto nel corso dell'elaborazione, questa è eseguita solo alla fine e quindi è opertiva all'interno del documento, quindi è utilizzata, ad esempio, come chiusura implicita.
Non si è ritenuto opportuno eseguire un giro iniziale, per individuare i soli titoli validi, che dovrebbe replicare le logiche di esclusione del successivo giro di controllo.

### **Eliminato titolo di livello troppo basso**

Il titolo, per congruenza con i precedenti, dovrebbe avere un livello minore di uno.
È stato quindi eliminato.

### **Eliminato titolo di livello troppo alto**

Il titolo, per congruenza con i precedenti, dovrebbe avere un livello maggiore di tre.
' stato quindi eliminato.

### **Eliminata TAG estranea ai book**

Nei documenti di tipo book sono ammesse unicamente le tag : 
- ..LNK
- ..DEC con oggetto di tipo membro (MB) e parametro DOCxx oppure voce (VO)
- ..T0x (titoli)
NB :  anche il puro testo (TAG vuota) non è ammesso e viene quindi eliminato.


### **Aggiunta inizio blocco prevista**

Riga aggiunta se per il blocco è stata scelta la sintassi abbreviata (-, \*)

### **Aggiunta fine blocco prevista**

Riga aggiunta se per il blocco è stata scelta la sintassi abbreviata (-, \*)

### **Aggiunta fine blocco interna**

Riga aggiunta se è stata trovato un titolo, all'interno di blocco aperto

### **Aggiunta fine blocco finale**

Riga aggiunta se alla fine del documento è ancora aperto un blocco

### **Aggiunta riga di colonna**

Riga di TAB.COL aggiunta perchè definita implictamente nella prima riga di dettaglio tabella


### **Riga di blocco modificata**

Riga di blocco modificata :  è stata scelta la sintassi abbreviata (-, \*)

### **Titolo modificato**

Il titolo è stato modificato per congruenza con i precedenti

### **Frequent asked question**

