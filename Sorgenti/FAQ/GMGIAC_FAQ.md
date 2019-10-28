### **Sai cos'è un plant/magazzino?**

Il plant o magazzino è l'unità di pianificazione, cioè l'entità a fronte della quale viene eseguita la pianificazione materiali : 
- tutti gli ordini cliente (domanda) e gli ordini di produzione (componenti) sottraggono materiali all'unità di pianificazione
- tutti gli ordini di produzione (prodotto) od acquisto apportano materiale all'unità di pianificazione
- le giacenze costituiscono il materiale presente nell'unità di pianificazione
- i parametri di pianificazione (lottizzazione, lead times, politica di riordino, scorta minima, punto di riordino, ecc..) sono validi per un articolo in una unità di pianificazione.

La tabella di riferimento è la tabella MAG, per una informazione più completa vedi documentazione : 
- [MAG - Magazzino](Sorgenti/OG/TA/MAG)
### **Conosci la definizione di area?**

L'area è un luogo logico e/o fisico dove le giacenze materiali hanno un trattamento univoco dal punto di vista fiscale e della movimentazione.
Es. : 
- area accettazione/collaudo
- area materiali non conformi
- area magazzino centrale
- area resi clienti
- area consignment stock fornitori
- area giacenza terzisti

La tabella di riferimento è la tabella GMR, per una informazione più completa vedi documentazione : 
- [GMR - Area](Sorgenti/OG/TA/GMR)
### **Conosci la definizione di tipo giacenza?**

In Sme.UP la giacenza può avere, oltre a plant / area / articolo, anche altre informazioni che la identificano, es. : 
- ubicazione di magazzino
- lotto qualità
- fornitore
- cliente
- commessa
- matricola
- collo / contenitore
- ....

L'archivio prevede di poter avere fino a quattro di queste caratterizzazioni oltre al collo/contenitore.
Queste caratterizzazioni sono codificate come "Tipo giacenza" e sono gestite nella tabella di riferimento  GMQ, per una informazione più completa vedi documentazione : 
- [GMQ - Tipo giacenza](Sorgenti/OG/TA/GMQ)
### **Sai cosa sono le forme di presentazione usate nell'interrogazione giacenze?**

Le forme di presentazione dell'interrogazione giacenze servono per configurare i parametri di chiamate del programma e la lista giacenze che viene visualizzata.
La tabella di riferimento è la GMF a cui si rimanda per una documentazione completa : 
- [GMF - Forme presentazione giacenze](Sorgenti/OG/TA/GMF)

### **Sei capace di fissare alcuni elementi nella forma di presentazione, es. l'area?**

Nella tabella GMF si possono impostare :  magazzino e/o area e/o tipo giacenza di default. Si possono anche proteggere in modo che chiamando quella forma di presentazione il sistema presenti solo le giacenze compatibili e che non ci sia la possibilità di cambiare i codici protetti.
### **Sai perchè nella tabella GMF ti viene chiesto di inserire un file logico?**

Una delle impostazioni previste nella tabella GMF è l'ordine con cui la lista giacenze viene presentata. L'ordine è quello del file logico che viene richiesto e deve corrispondere alla sequenza dei campi impostati nella tabella (se logico e sequenza campi sono incongruenti avremo anche delle inconguenze nella lista giacenze che viene presentata).

Se si crea una nuova forma di presentazione con una nuova sequenza particolare di campi si può anche indicare un logico insistente, il programma lo creerà al primo lancio dell'interrogazione giacenza con quella particolare forma di presentazione.
### **Sai cosa significa visualizzazione estesa in interrogazione giacenza?**

La giacenza può avere tre campi quantità : 
- giacenza
- quantità attesa
- quantità allocata

Se non è attiva la visualizzazione estesa in lista viene mostrata solo la giacenza, se c'è la visualizzazione estesa vengono mostrate anche le altre quantità.
### **Conosci il significato di quantità allocata?**

La quantità allocata è quella quota della giacenza che è stata riservata per un determinato obiettivo (es. per essere trasferita in produzione, per essere spedita a fronte di un ordine di vendita, per andare in C/L a un terzista, .....).

Di solito, l'allocazione giacenza c'è se sono attivate le richieste di movimentazione e viene gestita dal motore inferenziale.
### **Conosci il significato di quantità attesa?**

La quantità attesa è quella giacenza che è in arrivo, arriverà quando sarà reso esecutivo il trasferimento (eseguito attraverso le richieste di movimentazione) proveniente da una giacenza origine con quantità allocata.

Di solito, la quantità attesa c'è se sono attivate le richieste di movimentazione e viene gestita dal motore inferenziale.
### **Sai come  fare per ottenere dei totali/subtotali in interrogazione giacenza?**

Nel formato di lancio, di fianco ad ogni codice digitabile c'è il flag di "totali", se impostato il programma presenta la relativa totalizzazione. I totali possono essere impostati anche in tab. GMF.
### **Se lanciando l'interrogazione ti esce una segnalazione che ci sono delle transazioni non applicate sai come agire?**

Questa è una forma di controllo sull'esistenza di transazioni in sospeso nell'archivio GMTRAN0F, che viene attivata da un flag nella tabella GM1 di impostazione generale dell'applicazione GM.
Bisogna lanciare la funzione "Gestione transazioni" ed analizzare le transazioni in sospeso che vengono presentate.
### **Sai come lanciare rettifiche di giacenza direttamente dall'interrogazione giacenza?**

Nella lista giacenze digitare R+ per rettifiche positive o R- per rettifiche negative.
Se, per quell'area / tipo giacenza, sono previste delle causali di rettifica il sistema le presenta per la scelta e si predispone a lanciare il movimento con la causale scelta.
### **Sai come fare per lanciare movimenti ad 1 causale direttamente dall'interrogazione giacenze?**

In tab. GM1 deve essere impostato il campo  "Gruppo azioni x mov. magazzino". Al gruppo azioni devono corrispondere delle azioni (B£Jxx - programma GMMV01I o similari) con una causale che è compatibile con l'area / tipo giacenza selezionata. L'utente deve essere autorizzato (Classe GMQU01).
### **Sai come fare per lanciare movimenti a 2 causali direttamente dall'interrogazione giacenze?**

In tab. GM1 deve essere impostato il campo  "Gruppo azioni x mov. magazzino". Al gruppo azioni devono corrispondere delle azioni (B£Jxx - programma GMMV02I o similari) con la causale di partenza che è compatibile con l'area / tipo giacenza selezionata. L'utente deve essere autorizzato (Classe GMQU01).
### **Sai come forzare l'utente, quando esegue l'interrogazione giacenza, a compilare i campi di selezione in modo che il sistema esegua una lettura ottimizzata dei dati?**

Nella tabella GMF c'è il flag "Riempimento progressivo dei campi" che se attivo non permette all'utente di compilare il formato di lancio in maniera disottimizzata rispetto alla forma di presentazione
### **Sai come modificare le descrizioni, presentate in interrogazione, dei campi chiave della giacenza?**

I campi chiave sono elementi della tabella GM\*SQ :  qui si possono modificare le descrizioni, es. 1 = fornitore.
### **Sai perchè nella lista delle giacenze che viene presentata a volte il campo opzione ha dei puntini altre volte ha dei trattini?**

I trattini vengono presentati, invece dei puntini, quando la riga che viene mostrata non è il dettaglio della giacenza (es. la mia giacenza ha un tipo giacenza per fonitore nel cod.1 e io sto usando una forma di presentazione che non prevede il cod. 1 tra i suoi campi chiave :  in una riga vedo il totale giacenza di tutti i fornitori). Inserendo 05 nell'opzione si apre la lista di dettaglio.
### **Sai come evitare il fenomeno precedente?**

Utilizzo la forma di presentazione più adatta.
### **Sai qual'è l'archivio di riferimento?**

Il file GMQUAN0F
