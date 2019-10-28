### **Sai quali sono le tabelle guida?**

La tabella GMU che determina la tipologia dell'ubicazione.
La tabella GMG che definisce il tipo gestione ubicazione.

Per una documentazione completa : 
- [GMU - Tipologia ubicazione](Sorgenti/OG/TA/GMU)
- [GMG - Tipo gestione ubicazione](Sorgenti/OG/TA/GMG)
### **Sai qual'è l'archivio di riferimento?**

Il file GMUBIC0F
### **Sai cosa significa multi item?**

Che nella stessa ubicazione è possibile mettere articoli diversi contemporaneamente.
### **Sai cosa significa multi lotto?**

Che nella stessa ubicazione è possibile mettere lotti diversi dello stesso articolo contemporaneamente.
### **Sai come si possono associare ad un'ubicazione delle causali di movimentazione?**

L'ubicazione nasce indipendente da una specifica area, quindi di solito non ci sono causali di movimentazione associate. Se una o più ubicazioni sono tipiche di un'area (es. abbiamo l'area di magazzino 10 che ha un tipo giacenza per ubicazioni e un gruppo di ubicazioni sono solo del magazzino) allora abbiamo 2 metodi per assiociare delle causali di carico e scarico di default : 
- in tabella GMU
- in tabella GMG
### **Sai come si possono associare ad un'ubicazione delle misure di default?**

Esistono 2 modi : 
- dalla tabella GMU
- per ereditarietà dall'ubicazione di riferimento.
### **Conosci il significato di metodo di accesso?**

Nella gestione ubicazioni il metodo di accesso rappresenta la sequenza con cui il motore inferenziale determina l'ubicazioni su cui eseguire : 
- il versamento (metodo di accesso x ubicazione)
- il prelievo (metodo di accesso x articolo)

Il codice del metodo di accesso è un elemento della tabella GMF, il metodo utilizza la vista logica presente in questo elemento.
### **Sai cosa significa bloccare un'ubicazione?**

Il blocco ubicazione è un flag in anagrafico GMUBIC. Può essere usata dalle regole del motore inferenziale per saltare le ubicazioni bloccate.
Oppure è possibile inibire movimenti di prelievo o versamento attraverso la Forma di presentazione definibile in tabella GMC.
### **Sai cosa significa che l'ubicazione è occupata?**

Che esiste almeno una giacenza (file GMQUAN). Nel motore inferenziale le regole di attribuzione ubicazioni possono eseguire un controllo tipo "ON/OFF" oppure quantitativo (es. quanto peso è già presente e quindi quanto ne posso ancora caricare) o anche considerando il valore dei flag "multi item" "multi lotto".
### **Sai come fare per impostare una codifica guidata ubicazioni?**

In tabella GMU c'è la "Domanda costruzione codice" che inizia il processo di costruzione automatica del codice ubicazione secondo i passi definiti nelle tabelle B£F, B£Cxx.
