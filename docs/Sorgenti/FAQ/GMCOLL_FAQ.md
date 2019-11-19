### **Sai cos'è la movimentazione per UdC/UdM (Unità di carico/Unità di movimentazione?**

Una modalità di movimentazione di magazzino che, attraverso lo spostamento delle UdC (UdM), esegue la movimentazione di magazzino degli articoli/quantità contenuti nella UdC.
Esempio si possono utilizzare le UdC per : 
-  versare in una ubicazione di magazzino gli articoli ricevuti da un fornitore
- spostare da un'area/ubicazione in un'altra area/ubicazione
- spostare da magazzino all'area di spedizione
- alimentare la lina di produzione (trasferimento da ubicazione di magazzino a ubicazione bordo-linea)

### **Conosci il significato di contenitore padre?**

Nella gestione per unità di movimentazione è prevista la possibilità di utilizzare contenitori di contenitori in modo da comporre una distinta di contenitori (es. pallet e scatole) dove il contenitore che contiene gli altri è il contenitore padre.

### **Sai quando è utile avere la giacenza per collo?**

Quando si ha la necessità di identificare univocamente una giacenza. Per esempio in una gestione a Radio Frequenza. Dove sparando il numero di collo si vuole determinare automaticamente tutte le informazioni di giacenza per semplificare i processi di prelievo e/o trsferimento materiali. Naturamenente bisogna prestare attenzione a che un collo sia prelevato interamente.  Se necessario un prelievo parziale bisonga creare un nuovo collo per la parte prelevata o residua.

### **Sai quali sono le tabelle guida?**

La tabella principale è la GMD (Tipo collo) che definisce le specifiche del collo (collegamento a oggetti SmeUP, parametri, note, numerazione, ...)
L'altra tabella guida è la GMB (Unità di movimentazione) che è relativa alle caratteristiche fisiche (misure, peso max consentito, matricolazione, bar-code, ...).

Per una informazione più completa vedi documentazione tabelle : 
- [GMD - Tipo collo](Sorgenti/OG/TA/GMD)
- [GMB - Unita](Sorgenti/OG/TA/GMB)

### **Sai quali sono gli archivi di riferimento?**

L'anagrafico di colli è il file GMCOLL0F.

Esiste un secondo archivio di riferimento (file GMCOCO0F) dove mantenere il dettaglio giacenza del contenuto dei colli, in alternativa alla gestione dettaglio giacenze per collo in GMQUAN.

Per una informazione più completa vedi documentazione files : 
- [GMCOLL0F Colli](Sorgenti/OJ/FILE/GMCOLL0F)
- [GMCOCO0F Giacenze per Packing list (prova Query)](Sorgenti/OJ/FILE/GMCOCO0F)

### **Sai come collegare un documento ad un collo?**

Nella tabella GMD ad un tipo collo in questione si possono abbinare 2 enti di riferimento e 2 tipi documento.

### **Sai come impostare la codifica guidata di un collo?**

In tabella GMD c'è la possibilità di inserire un numeratore colli (tab. CRNGM) oppure l'elemento di tab. B£F con la domanda iniziale per il flusso costruzione codice colli.

### **Sai come evitare di avere i dettagli  giacenze per collo in GMQUAN?**

In tabella GMD si può impostare se il contenuto colli viene gestito a dettaglio in GMQUAN.
La stessa impostazione si ha con il "gruppo flag" :  flag 1. Il gruppo flag vince sulla tabella GMD.

### **Sai perchè evitare di avere i dettagli  giacenze per collo in GMQUAN?**

Per avere il dettaglio del contenuto di un collo non è necessario gestire in GMQUAN le giacenze per collo :  si attiva la gestione del dettaglio in GMCOCO. In questo modo la gestione delle giacenze ne risulta alleggerita. Il dettaglio contenuto nel collo è necessario per la gestione della packing list.

### **Sai come associare parametri esterni ad un collo?**

Inserendo la categoria parametri in tab. GMD.

### **Sai come associare parametri interni ad un collo?**

Inserendo la categoria parametri impliciti (tab. C£I) in tab. GMD.

### **Sai come associare date particolari ad un collo?**

Inserendo in tab. GMD il prefisso degli elementi di tab. C£JCZ dove sono descritti i significati delle date implicite.
La stessa impostazione si ha con il "gruppo flag" :  flag 2. Il gruppo flag vince sulla tabella GMD.

### **Sai come associare etichette diverse a colli diversi?**

In tab. GMB per un tipo UdM si può inserire un elemento della tab. GMP che richiama uno specifico programma di stampa etichette.

### **Conosci l'esistenza della Copy K35?**

La /Copy K35 è una /copy generalizzata che permette la creazione di un collo, il suo "riempimento" con un articolo / quantità, la movimentazione.

### **Sai qual'è la tabella di riferimento per la K35?**

La tabella GNK, nella quale sono definite tutte le azioni previste nell'utilizzo della K35.

Per una informazione più completa vedi documentazione tabella : 
 :  : DEC T(MB) P(DOC_OGG) K(TA_GNK)

### **Sai quali sono le principali azioni catalogate?**

- Creazione collo
- Annullamento collo
- Riempimento collo
- Svuotamento collo
- Accorpamento collo
- Suddivisione collo
- Inventario fisico collo
