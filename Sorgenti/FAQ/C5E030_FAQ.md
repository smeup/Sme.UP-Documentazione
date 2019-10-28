### **Come attivare l'analitica Sme.UP in ambiente ACG ?**

 __Tabelle__
 B£1 :   Conti CO.GE.  A7
 Co.Generale   A7
 Co.Analitica    SM
 B£2 :   Controllare Codici divise e Azienda
 C51 :   Passo riga contabilità analitica (facoltativo)
 C52 :   Analitica attiva
 Presenta sempre analitica
 Riclassifica analitica
 CRNC5 :   Numeratore analitica, obbligatorio OG.MH
 C5D :  Fisso elemento ANA
 C5L :  Da costruire, per semplicità creato elemento ANA
 C5B :  Deviata su A7 in B£I elmento C5B : 
 campi F/A7/ / / / / /C5PDC_A7//1/1
 C6B :  Da costruire, creare almeno elemento default \*\*
 PER :  Da costruire, periodo 01
 G91 :  Programma contab.analitica G9FA07_SM
 Attivo analitica '1'

 __Programmi__
 _Interfaccia_
 C5PDC_A7 e relativo video per gestione COCOC e C5B in automatico
 _Interattivo_
 GRA10, GRA15, GRA24, GRA25, HRG21, D5CA50_SM
 \* Personalizzare il GRA10, GRA15, GRA24, GRA25 dallo standard ACG (o dallo standard attivo nell'azione), copiando le modifiche contrassegnate SMEUP dai relativi sorgenti del SRC_A7/SMEDEV
 \* Compilare il programma SMEUP HRG21 da SRC_A7/SMEDEV
 \* Compilare il programma SMEUP D5CA50_SM da D5SRC/SMEDEV
 _Batch (Ciclo passivo)_
 G9FA05_A7, G9FA05_SM, HRG24, D5CA55_SM
 \* Compilare il programma SMEUP G9FA05_SM da G9SRC/SMEDEV
 \* Compilare il programma SMEUP G9FA05_A7 da SRC_A7/SMEDEV
 \* Compilare il programma SMEUP HRG24 da SRC_A7/SMEDEV
 \* Compilare il programma SMEUP D5CA55_SM da D5SRC/SMEDEV

 __Flusso chiamata programmi__
 _Interattivo_
 GRA10 e GRA15 --> HRG21 --> D5CA50_SM  No IVA
 GRA24 e GRA25 --> HRG21 --> D5CA50_SM  Con IVA

 _Batch (Ciclo passivo)_
 G9CF60 Controllo bolle fattura  V5T/V5R ->G9DCON0F
 G9FA05_A7 --> G9FA05_SM  Contabilizzazione Sme.UP  G9DCON0F --> MOCOAB0F
 HRG24         --> D5CA55_SM  Contabilizzazione ACG       MOCOAB0F --> C5MOAN0F
### **Sai a cosa serve la contabilità analitica?**

E' uno strumento gestionale, solitamente viene utilizzata per rappresentare in maniera dettagliata o riepilogata (a seconda di come è fatto il piano dei conti e delle necessità) la struttura di una parte dei conti aziendali, molto spesso il conto economico. Ciò consente, ad esempio, di mantenere il piano dei conti con una struttura di base sintetica, per poi dettagliare a livello gestionale la natura di una operazione contabile.
### **Sai come attivare la contabilità analitica?**

Nella tabella C52 si stabilisce se la gestione è attiva o meno, previa configurazione generale della struttura che si vuol dare al servizio (ripartizioni, modelli, ecc.). Riferirsi alla documentazione del modulo per i dettagli.
### **Sai come fare in modo che un conto contabile richieda la compilazione dell'analitica?**

Accendendo l'apposito flag sul conto, poi definendone struttura ed eventualmente modello con l'apposito set'n'play nel menu di contabilità analitica.
### **Sai come configurare le ripartizioni che si vogliono ottenere sull'analitica?**

Definendo una o più strutture nella tabella C6B, da associare poi ai conti contabili nella definizione della struttura nella stessa tabella.
### **Sai quanti oggetti di Sme.UP possono esseri collegati come ripartizioni di analitica?**

Possono essere usate sia delle tabelle (frequente la definizione di D5C e D5S) che oggetti come articolo o commessa, ma in generale un qualsiasi oggetto di Sme.UP può essere definito come uno delle sei destinazioni configurabili.
### **Sai come differire le ripartizioni di analitica per conti o tipi conti diversi?**

Codificando strutture di analitica diverse ed assegnandole poi a conti o gruppi di conti diversi per caratteristiche o utilizzo.
### **Sai come creare la struttura ed il modello di analitica di un conto?**

Dal set'n'play di assegnazioni analitica si utilizza la funzione '11' per immettere la struttura da associare al conto (sempre modificabile), poi la funzione '21' per eventualmente definire un modello che si vuole corrisponda ad un certo conto.
### **Sai se è obbligatorio gestire modelli di analitica per ogni conto?**

No, se il conto non ha un modello verrà richiesto di compilarne completamente l'analitica.
### **Sai se è possibile ripartire l'analitica di un conto in quote % prestabilite?**

Si, definendo un modello personalizzato con destinazioni e % di ripartizione predefinite.
### **Sai se una volta impostato un modello per un conto, l'impostazione è modificabile per una singola registrazione?**

Si, se si sceglie di vedere sempre visualizzata l'analitica anche se compilata automaticamente, oppure successivamente in modifica.
### **Sai se deve esserci quadratura tra l'analitica di un conto e il valore di origine della registrazione?**

Si, l'analitica deve essere totalmente quadrata con il valore di input che la origina.
### **Se un conto deve avere un'analitica , sai se è possibile non immetterla al termine della registrazione?**

No, è obbligatorio immettere qualcosa.
### **Sai come interrogare l'analitica di un oggetto impostato come destinatario su una registrazione?**

Dal menu di analitica è possibile fare uso di interrogazioni predefinite (perchè più frequentemente utilizzate), oppure disporre di una interrogazione generica per tipo/codice oggetto.
### **Sai a cosa serve la data competenza presente sulle righe di analitica?**

Per imputare alla data desiderata la quota parte della riga di analitica, se diversa dalla data registrazione.
### **Sai come evitare di visualizzare l'analitica di una registrazione se predeterminata completamente da un modello?**

Impostando a '2' il parametro 'Presenta a conferma registrazione' nella tabella C52.
### **Sai se è possibile modificare l'analitica di una registrazione già consolidata su registri IVA e/o giornale?**

Si.
### **Nel caso l'analitica venga installata nel corso di un esercizio contabile, sai se è possibile recuperare i movimenti precedenti al momento dell'avvio?**

Si, o entrando in modifica sulle registrazioni che la richiedono, oppure utilizzando l'apposita funzione di calcolo che, ove possibile, genererà righe di analitica per quei conti per i quali è specificato un modello che consenta la ripartizione totale in % del valore origine.
