### **Sai quali sono le tabelle guida?**

La tabella GMO è quella di impostazione delle testate richieste movimentazione (TRIM).
La tabella GMZ è quella di impostazione delle righe richieste movimentazione (RRIM).

Per una documentazione completa : 
- [GMO - Tipo documento movimentazione](Sorgenti/DOC/OG/TA/GMO)
- [GMZ - Tipo riga movimentazione](Sorgenti/DOC/OG/TA/GMZ)

### **Sai quali sono gli archivi di riferimento?**

Per le testate il file GMTRIM0F.
Per le righe il file GMRRIM0F.

### **Sai quali sono le classi di autorizzazione utilizzate?**

Per le testate
- Classe = GMRM01
- Funzione = GMRM01G per il formato guida, Funzione = GMRM01L per la lista.
Per le righe
- Classe = GMRM10
- Funzione = GMRM10G per il formato guida, Funzione = GMRM10L per la lista.

### **Conosci il significato di quantità allocata?**

La quantità allocata è quella quota della giacenza che è stata riservata per un determinato obiettivo (es. per essere trasferita in produzione, per essere spedita a fronte di un ordine di vendita, per andare in C/L a un terzista, .....).

Di solito, abbiamo l'allocazione giacenza se sono attivate le richieste di movimentazione quando viene gestita dal motore inferenziale (cfr. più avanti domanda specifica sul motore inferenziale).

### **Conosci il significato di quantità attesa?**

La quantità attesa è quella giacenza che è in arrivo, arriverà quando sarà reso esecutivo il trasferimento (eseguito attraverso le richieste di movimentazione) proveniente da una giacenza origine con quantità allocata.

Di solito, abbiamo quantità attesa se sono attivate le richieste di movimentazione quando viene gestita dal motore inferenziale.

### **Sai cos'è l'assegnazione?**

L'assegnazione è la funzione attraverso la quale il motore inferenziale : 
- per una richiesta di movimentazione da versare a magazzino (azione = versamento), assegna una chiave di destinazione e valorizza la quantità attesa
- per una richiesta di movimentazione da prelevare da magazzino (azione = prelievo), assegna una chiave di origine valorizza la quantità allocata
- per una richiesta di movimentazione da prelevare da una parte e versare in un'altra (azione = trasferimento) si valorizzano sia la quantità allocata (record origine) che quella attesa (record destinazione).


### **Sai cos'è l'esecuzione?**

L'esecuzione è la funzione che esegue il completamento dell'attività iniziata con l'assegnazione :  esegue i movimenti (origine e destinazione) previsti nella RRIM e ne cambia lo stato.

Es. la conferma del versamento a magazzino di una richiesta di movimentazione

### **Conosci il significato del motore inferenziale?**

Il motore inferenziale è un programma che può attivare, anche ciclicamente, dei passi di elaborazione per l'esecuzione ottimizzata della movimentazione di un magazzino complesso gestito ad ubicazioni.

Per movimentazione si intendono le attività di prelievo da magazzino, versamento a magazzino e trasferimento (es. da un'ubicazione ad un'altra).

Il motore inferenziale elabora una serie di passi che, partendo dal passo iniziale, procedono al passo successivo in base al risultato dell'elaborazione del passo precedente, fino ad arrivare al passo conclusivo.

Un esempio tipico è la scelta dell'ubicazione di versamento in base a criteri diversi, es. : 
- come peso articolo (più pesanti in basso, più leggeri in alto);
- volume (volume che può essere contenuto degli scaffali);
- indice di rotazione dell'articolo (più movimentati vicino, meno movimentati in fondo);
- materiale particolare (deperibile da mettere in cella);
- ecc.

### **Sai quali sono le tabelle utilizzate dal motore inferenziale?**

La tabella GMH è la testata del processo ed identifica il primo passo da eseguire.
La tabella GMK è la tabella dei passi di esecuzione dove viene indicato il programma da eseguire con i relativi parametri di condizionamento ed il passo successivo.

Per una documentazione completa : 
- [GMH - Modelli £GMI](Sorgenti/DOC/OG/TA/GMH)
- [GMK - Passi £GMI](Sorgenti/DOC/OG/TA/GMK)

### **Sai trovare dei programmi esempio di utilizzo del motore inferenziale?**

In SMESTD/GMSRC c'è una serie di sorgenti GMGMI0_xx.

### **Sai che possono esistere RRIM senza TRIM?**

Normalmente una o più righe richieste movimentazione (RRIM) appartengono ad un testata R. M. (TRIM). Esistono casi in cui la RRIM può esistere senza TRIM, tipicamente quando la RRIM è utilizzata per versare a magazzino un singolo materiale ricevuto e si utilizza il motore inferenziale per suggerire l'ubicazione, essendo una sola RRIM con un obiettivo specifico la testata non ha ragione di esistere.

Per creare RRIM senza testata usare la funzione CLEARN con la £GMZ.

### **Sai se una RRIM è di versamento come si comporta in assegnazione?**

Una RRIM è di versamento quando si verificano 2 condizioni : 
- in tab. GMZ il tipo riga ha il campo "Prelievo/Versamento/Trasferimento" impostato a V o T
- il gruppo flag di riga ha flag 3 (condizioni di assegnazione) impostato a V o O

Esempi : 
- __RRIM di versamento di un'entrata merci__, di solito il collegamento della BEM o l'esito del collaudo caricano la giacenza di un'area, il motore inferenzale propone un'ubicazione di magazzino e la RRIM esegue la movimentazione dall'area di carico al magazzino. Avremo Prelievo/Versamento/Trasferimento = T e Flag 3 = O (fisso origine calcolo destinazione)
- __RRIM di versamento di produzione__, il versamento di produzione potrebbe caricare direttamente il magazzino nell'ubicazione proposta dal motore inferenziale. Avremo Prelievo/Versamento/Trasferimento = V e Flag 3 = V (nessuna origine calcolo destinazione)

### **L'esecuzione della RRIM deve azzerare la quantità allocata/attesa valorizzata dall'assegnazione. Sai come fare questa azione?**

Nella causale di magazzino collegata al tipo riga movimentazione (TA GMZ), occorre compilare il campo "Azione q.allocata/attesa" con il segno "-".

### **Sai come usare le stesse causali movimentazione sia nelle RRIM che nei movimenti manuali, anche se le causali movimentano sia giacenza che allocato o atteso?**

Nella tabella GMC c'è il campo "Applica solo se IDDM" che, se impostato e sono presenti le azioni (+ o -) sulla qtà allocata e/o sulla qtà attesa, esegue le azioni in questione solo se la causale è stata lanciata da una richiesta di movimentazione.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/DOC/OG/TA/GMC)

### **Sai come creare righe documento da richieste movimentazione?**

Uno degli utilizzi delle richieste di movimentazione è quello della gestione dei prelievi per spedizione (vendita o invio in C/Lavoro).
In questi casi una funzione molto comoda è quella della creazione delle righe del documento V5 di spedizione direttamente dalle richieste di movimentazione preparate/assegnate/evase.

La funzione più utilizzata, che si attiva nei flussi documento, è svolta dal programma V5AT15E con tutte le sue funzioni/metodi.

In alternativa si può impostare l'azione V5AT15G con funzione RICMOV (o RICMOVC, RICMOB, RICACQ) o V5AT15E

### **Sai da dove si possono estrarre le TRIM/RRIM**

TRIM e RRIM possono essere create manualmente oppure da programmi che : 
- si attivano da menù (P5RM01A, per estrazione da impegni di produzione, V5RM01A, per estrazione da documenti del ciclo esterno)
- possono essere lanciati come azioni di flusso (P5FURIM, flusso ordini di produzione per estrazione da impegni di produzione; V5FURIM, flusso testate o righe documenti V5 per estrazione da documenti ciclo esterno)

ATTENZIONE :  Nelle azioni P5FURIM e V5FURIM è possibile impostare il tipo R.M. /Tab. GMO) mentre P5RM01A e V5RM01A non generano R.M. se non sono state compilate opportunamente le rispettive tabelle P55 e V55.


Per maggiori dettagli : 
- [? P55 - Parametri logistici](Sorgenti/DOC/OG/TA/P55)
- [V55 - Par. accantonamento/spedizione](Sorgenti/DOC/OG/TA/V55)

### **Sai che si può creare una TRIM senza eseguirla utilizzandola come prebolla di spedizione?**

Questo è uno dei possibili utilizzi, è da usare quando si vogliono tenere "leggeri" il processo di prelievo da magazzino e spedizione : 
- con V5RM01A o V5FURIM si estraggono le RRIM, queste RRIM devono avere il flag 4 = 2 o 3 (riga chiusa o cancellata alla spedizione)
- si stampano le RRIM e si utilizza la lista stampata come una "pre-bolla" per eseguire fisicamente il prelievo
- si annullano o modificano le righe RRIM in accordo al prelievo effettivamente eseguito
- si crea il documento di spedizione con l'azione V5AT15E (RICHI/R)
- il collegamento bolla esegue lo scarico del magazzino

