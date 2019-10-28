### **Posso far vedere gli anni di inizio ammortamento nella stampa del libro cespiti a dettaglio?**

 Se non esistono gli OAV dei cespiti, costruirli col comando T OAV impostando : 
 \* FUNZIONE :  COS
 \* METODO :  ATB
 \* TIPO 1 :  CE
 oppure mediante la seguente opzione automatica : 

### **Perchè l'anno di inizio ammortamento di un cespite è più recente di quello d'acquisto?**

 Nella tabella PER vanno codificati tutti gli esercizi a partire da quello relativo al cespite più vecchio.

### **Perchè registrando l'acquisto del cespite il programma non calcola gli ammortamenti previsti?**

 Nella tabella PER vanno codificati anche gli esercizi futuri (tenere presente che, solitamente, i fabbricati hanno piani di ammortamento di 33 anni, perciò può essere utile codificare elementi fino al 2040).

### **Un cespite deve cambiare categoria fiscale?**

 Bisogna preparare alcune causali che consentano di effettuare una sorta di 'giroconto' del valore iniziale del bene, della quota fino a quel momento ammortizzata e dell'eventuale residuo da ammortizzare.
 Inoltre va codificato un nuovo cespite avente categoria fiscale 'nuova', che sostituirà quello che si chiude :  nella descrizione del nuovo cespite (o nelle note) è opportuno inserire un richiamo al codice del vecchio cespite.

 Per ciò che riguarda la prima operazione (chiusura vecchio cespite), si deve eseguire sostanzialmente una alienazione, perciò si può duplicare la causale relativa modificando la descrizione in modo opportuno (es. 'Giroconto chiusura cespite').
 Si tenga presente che la causale di alienazione esegue movimenti derivati grazie al campo 'Causali collegate' presente in tabella :  vedere nella tabella A5G quali causali sono pianificate sotto tale gruppo; meglio duplicare anch'esse, associandovi una nuova descrizione.
 A questo punto si può eseguire il movimento di alienazione/chiusura cespite.
 Per riaprire la stessa situazione su un cespite nuovo, vanno codificate due causali apposite :  una per eseguire un movimento simile ad un acquisto (pertanto si può duplicare la PA0 standard) ed un'altra per riportare l'ammortamento eseguito con relativo fondo (si può duplicare la causale standard NA0 aggiungendovi il totalizzatore 17 con segno '+' e nuova descrizione).
 Si eseguiranno quindi due movimenti, il primo con importo pari al valore del bene, il secondo pari alla quota di ammortamenti eseguiti.

### **Serve un libro cespiti riclassificato secondo un nuovo piano di ammortamento?**

 Si può operare come segue : 
 1. codificare una nuova linea di ammortamento (tabella A5C) e relativi parametri;
 2. codificare un piano di ammortamento PER LINEA, con parametri che regolino il calcolo ammortamenti secondo le esigenze;
 3. codificare, nella tabella B£4, un nuovo elemento che contenga la data ultimo consolidamento per la nuova linea, posizionandola al giorno prima la data da cui si vuole effettuare il calcolo (volendo è possibile, quindi, riclassificare tutto il libro cespiti partendo dal primo anno di gestione);
 4. eseguire il calcolo cespiti per la nuova linea.

### **Serve una nuova linea di ammortamento?**

 Si può operare come segue : 
 1. nella tabella A5Cxx codificare la nuova linea di ammortamento e stabilirne le caratteristiche di funzionamento;
 2. se differiscono da quelli di legge, codificare i piani di ammortamento per la nuova categoria;
 3. accertarsi che, durante la conversione, i movimenti di tipo AI, AO, AA, AR, AC, AF, AP, AN, AQ, VC, VA, VN, LC, LA, LN, PV e MV convertiti abbiano preso linea '01' (se no, assegnarla mediante sql, programmino, ecc.);
 4. utilizzando il programma A5UT03A duplicare i movimenti esistenti dalla linea '01' alla linea 'XX', fino alla data della ultima chiusura libro cespiti;
 5. eseguire, per la nuova linea, un calcolo cespiti.

 Fatto questo, si potranno interrogare le schede o stampare il libro cespiti anche per la nuova linea.
### **Sai cos'è un cespite?**

Il cespite è un bene strumentale acquistato dall'azienda per sostenere la propria attività :  ad esempio, un computer, un fabbricato, il software gestionale, un impianto, ecc.
In quanto tale, un cespite non viene quindi messo a costo nell'esercizio di acquisto ma, permanendo nell'azienda per periodi più o meno lunghi, rappresenta una immobilizzazione sotto il profilo della destinazione contabile.
Il costo di un cespite viene poi spesato anno per anno attraverso l'ammortamento, concorrendo a formare gradualmente il reddito d'esercizio.
### **Sai perchè viene eseguita la gestione cespiti?**

Perchè l'insieme dei cespiti rappresenta le immobilizzazioni di un'azienda iscritte a bilancio, dunque la serie di beni censiti dalla gestione sottoposta ad ammortamento può essere richiesta dal fisco durante un accertamento, e fa parte delle stampe fiscali che l'azienda deve produrre insieme ad esempio al giornale di contabilità ed hai registri IVA.
### **Sai che differenza c'è tra un cespite materiale e un cespite immateriale?**

 Als="comm"
I cespiti materiali sono beni fisici (cioè con consistenza fisica), come ad esempio un fabbricato, un'attrezzatura, un computer, ecc. Hanno un costo di acquisto ed una deperibilità che ne determina l'usura, ovvero ciò che viene rappresentato dall'ammortamento nel tempo.
I cespiti immateriali non hanno consistenza fisica, come ad esempio il software, gli oneri pluriennali ammortizzabili, i marchi, i brevetti, ecc. ma hanno comunque un valore che ne determina la consistenza e, quindi, l'ammortamento nel tempo.
### **Sai a cosa servono le categorie fiscali di cespiti?**

Servono a suddividere i vari beni in tipologie omogenee, per poi attribuire loro una % di ammortamento comune (differibile per singolo cespite, se necessario). Solitamente le categorie ricalcano la struttura del piano dei conti nella parte inerente le immobilizzazioni (attività).
### **Sai a cosa può servire il cespite di riferimento?**

E' una caratteristica dei cespiti di Sme.UP, ovvero non richiesta fiscalmente, che consente di collegare un cespite (chiamiamolo 'figlio') ad un altro cespite (chiamiamolo 'padre') con un legame simile ad un componente verso il composto della distinta base. Ciò consente, successivamente, di interrogare il cespite 'padre' sia da solo che con l'apporto dei valori e ammortamenti dei cespiti ad esso collegati, tramite la scheda cespite e la stampa del libro cespiti.
### **Sai cos'è l'ammortamento di un cespite?**

E' la quota di costo che viene spesata nell'esercizio contabile, ed annotata come fondo (passività) ad incremento dell'ammortamento storico.
### **Sai a cosa servono i piani di ammortamento?**

Servono per codificare le regole di calcolo delle quote di ammortamento. Possono essere espresse per categoria fiscale (al livello più basso) e, per risalita, fino al singolo cespite nel singolo esercizio su una certa linea.
### **Sai come fare per bloccare l'ammortamento di un cespite?**

Nella gestione piani di ammortamento è possibile codificare il comportamento del calcolo per singolo cespite, senza indicare nè la causale nè la % o quota fissa di ammortamento. Tramite una forzatura si indica quindi un ammortamento nullo.
### **Sai cosa sono le linee di ammortamento?**

Codificate nella tabella A5C, sono il dispositivo tramite il quale ottenere calcoli di ammortamenti differenti per gestioni diverse e/o alternative a quella puramente fiscale.
In sintesi si pianificano comportamenti diversi e quote di ammortamento diverse per categoria fiscale/linea, per avere risultati diversi durante il calcolo ammortamenti.
### **Sai a cosa servono gli ammortamenti mensili?**

Normalmente la quota di ammortamento di un cespite nell'esercizio xxxx viene generata con data 31.12.xxxx. Se sulla linea di ammortamento si opta per la generazione di ammortamenti mensili, il calcolo genera 12 quote da 1/12 di quella unica, registrandole al 31.01.xxxx, 28.02.xxxx e così via.
Ciò consente di poter stampare un libro cespiti mese per mese, mentre nel primo caso l'unica opzione rilevante è quella di richiedere l'intero esercizio, non avendo movimenti intermedi.
La tecnica si rivela utile per avere l'ammontare trimestrale, semestrale, ecc. ed iscrivere a bilancio con un movimento gestionale l'esatta quota di competenza nel periodo da analizzare.
### **Sai se è possibile calcolare gli ammortamenti di un cespite iniziando da anni successivi a quello di acquisto?**

Si, nell'anagrafica cespite esiste infatti una 'Data inizio ammortamento' che, se valorizzata (di solito sempre dopo quella di acquisto) sposta la prima quota di ammortamento nell'esercizio della data stessa.
### **Sai che differenza c'è tra vendita e alienazione di un cespite?**

La vendita di un cespite, anche per un valore simbolico, è accompagnata dall'emissione di una fattura ad un cliente. L'alienazione è invece una rottamazione, quindi viene emessa solo una bolla a valore zero ed il cespite dovrebbe essere distrutto.
### **Sai cos'è una plusvalenza o una minusvalenza?**

Si tratta del ricavo o del costo che scaturisce dalla vendita/alienazione del cespite, viene calcolata automaticamente dal programma in base alla situazione residua del cespite al momento della dismissione. Si rimanda alla documentazione del modulo cespiti per le formule di calcolo.
### **Sai cos'è una rivalutazione o una svalutazione?**

Si tratta di una operazione atta ad aumentare (rivalutazione) o diminuire (svalutazione) il valore di un cespite, impattando quindi sull'ammontare delle quote di ammortamento eventualmente ancora da calcolare nei periodi successivi (aumenteranno in caso di rivalutazione, diminuiranno dopo una svalutazione).
Essendo le rivalutazioni regolate dalla normativa, vanno eseguite solo a fronte di essa.
Una svalutazione potrebbe essere invece indotta anche da deperimento di beni a fronte ad esempio di eventi naturali (alluvione), che danneggiano gravemente senza rendere inutilizzabili (quindi alienabili) i beni stessi, rendendone però possibile la diminuzione forzata del valore.
### **Sai in quale caso si esegue l'ammortamento istantaneo?**

Per tutti i cespiti con valore inferiore a Euro 516,46 (il vecchio milione di Lire) viene concesso di effettuare un ammortamento del 100% nell'anno di acquisto.
### **Sai cos'è l'ammortamento indeducibile?**

E' una quota parte dell'ammortamento di un cespite che, per normativa, non può essere messa a costo (cioè non è deducibile), e pertanto viene indicata separatamente dall'ammortamento ordinario.
E' possibile parametrizzare tale comportamento sulla linea (indicando la causale da utilizzare per questa rilevazione) e nella categoria fiscale (indicando la % di indeducibilità da calcolare).
### **Sai perchè i terreni non si ammortizzano?**

Perchè, salvo eventi naturali catastrofici, si presume che un terreno mantenga valore inalterato nel tempo, mentre per un qualsiasi altro cespite materiale si tende a misurarne l'usura nel tempo (che effettivamente c'è) mediante le quote di ammortamento.
### **Sai come far calcolare un ammortamento a quota valore fissa per un cepite?**

Nei piani di ammortamento è possibile indicare una regola di calcolo personalizzata per un singolo cespite, che a differenza di quella per categoria fiscale, esprimibile solo a %, può essere comandata anche da una quota fissa.
### **Sai come collegare la gestione cespiti alle gestione registrazioni contabili?**

Nella tabella C51 c'è un flag che consente di indicare se e come si desidera tale gestione, che poi viene regolata dai settaggi previsti sul conto contabile e nelle tabelle di configurazione della gestione cespiti.
### **Sai se è possibile impostare la costruzione automatica del codice cespite?**

Tramite un parametro sulla categoria fiscale, collegato a una struttura precedentemente codificata, è possibile far partire un questionario rispondendo al quale si otterrà un codice strutturato. Si rimanda alla documentazione del modulo cespiti per l'approfondimento.
### **Sai come effettuare la ripresa manuale dei dati storici da una gestione cartacea esterna?**

Se non si dispone di dati storici da convertire in formato elettronico, è possibile configurare apposite causali da impiegare per la registrazione manuale del valore cespite e del fondo di ammortamento storico. Al termine del lavoro di ripresa manuale si dovrebbe ottenere un libro cespiti identico a quello di provenienza.
### **Sai impostare una conversione cespiti da altro gestionale?**

Indipendentemente dalla struttura dei dati di provenienza, si deve comunque mirare a : 
- convertire le categorie fiscali nelle quali vengono suddivisi i cespiti;
- convertire l'anagrafica cespiti;
- convertire o generare dei movimenti che rappresentino almeno il valore storico ed il fondo storico di ogni cespite.
### **Sai cos'è il libro cespiti e come si stampa?**

E' l'inventario completo dei cespiti di proprietà dell'azienda, suddiviso per categoria fiscale di appartenenza e stratificato per esercizio di acquisto. Può essere stampato tutte le volte che lo si desidera in modalità normale, una volta sola in modalità 'Consolidata', per effettuare la chiusura periodica alla data (solitamente quella di fine esercizio contabile) in modo da rendere immodificabili i movimenti antecedenti tale data.
### **Sai in quali modi è possibile consolidare ad una certa data la gestione cespiti?**

Oltre che stampando in modalità 'Consolidata' il libro cespiti, nella tabella B£4 esiste una data di consolidamento per ogni linea presente nella tabella A5C, che può essere posizionata manualmente e, di fatto, è la stessa operazione fatta dalla stampa di cui sopra.
Naturalmente, arretrando tale data, si riapre la gestione completamente, non essendo previsti flag o altri meccanismi di protezione dei movimenti.
### **Sai come generare automaticamente le registrazioni contabili di ammortamento e derivate?**

Nella tabella A51 è presente un flag che determina il metodo con il quale si desidera venga eseguito il calcolo degli ammortamenti. Scegliendo l'automatismo, ogni volta che viene modificato il valore del cespite vengono ricalcolati gli ammortamenti futuri in tempo reale, fermo restando che quelli passati non vengono più elaborati perchè consolidati. Se il flag di cui sopra rimane spento si dovrà eseguire la funzione di 'Generazione ammortamenti' manualmente.
### **Sai perchè i movimenti di ammortamento/derivati non sono modificabili?**

Perchè sono movimenti calcolati da regole pianificate (ammortamenti da piani) oppure derivati automaticamente da regole fiscali (plusvalenze, minusvalenze, ecc.), pertanto se i movimenti vengono generati in maniera errata si deve risolvere il problema di base (sistemare i piani di ammortamento) o i settaggi che regolano la generazione automatica di movimenti derivati (tabella causali A5B).
### **Sai come spostare un cespite e relativi movimenti da una categoria fiscale ad un'altra?**

Attrezzando apposite causali di 'chiusura' dei valori del cespite e riregistrando il cespite con un altro codice anagrafico in un'altra categoria fiscale, come ad esempio viene fatto nella ripresa di dati storici da supporto cartaceo.
### **Sai se e' possibile annullare un cespite?**

No, se il cespite ha dei movimenti. Si, se invece ne è privo.
### **Sai se è possibile collegare la gestione cespiti agli oggetti della contabilità analitica e/o del controllo di gestione?**

Nell'anagrafica cespiti vi sono sei collegamenti liberi verso oggetti esterni di Sme.UP adatti a questo scopo.
