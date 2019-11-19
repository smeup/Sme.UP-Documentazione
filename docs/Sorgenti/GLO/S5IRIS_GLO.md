### **Algoritmo costruttivo**


### **Alternativa di fase**

L'alternativa di una fase di lavorazione indica il centro/i alternativi ed i relativi tempi su cui è possibile eseguire l'operazione.

### **Alternativa di Risorsa specifica**

L'alternativa di risorsa specifica identifica tutte le "n" macchine su cui può essere eseguito un Task.


### **Appuntamento**

L'appuntamento è quell'istante in cui un Task può considerarsi pronto per effetto delle esecuzione completa o parziale (sovrapposizione) dei task precdenti dello stesso Job oppure per completamento dei Job di livello inferiore di distinta materiale. Parliamo infatti di appuntamenti tra fasi e/o appuntamenti tra ordini di produzione

### **Backtracking**


### **Batch**

Si definisce batch un insieme di ordini di produzione che vengono lavorati contemporaneamente sulla stessa risorsa :  hanno un attrezzaggio comune, iniziano e finiscono contemporaneamente.
Un esempio di batch è uno stampo multiplo, che contiene più di un tipo di impronta (ad esempio n impronte dell'articolo A, e m impronte dell'articolo B).
Un altro esempio è costituito da un forno, in cui il limite di carico è costituito dal volume del forno.

### **Buffer**

In termini matematici, il buffer è una spezzata che congiunge una serie di punti di un diagramma cartesiano che riporta in ascisse il tempo ed in ordinate i pezzi (o il valore equivalente precedentemente esposto).

Il profilo di carico o scarico di ogni singolo evento può essere : 
  a gradino :  retta parallela all'asse delle ascisse, se è una quantità costante nel tempo (se è una giacenza parte dall'istante zero, se è un carico senza sovrapposizione parte dall'istante di fine esecuzione della fase)
  a rampa :  segmento che parte dall'istante di inizio dell'esecuzione della fase, con ordinata zero, ed arriva all'istante di fine, con ordinata pari alla quantità della fase (cambiata di segno se è uno scarico).

Si distinguono due tipi di buffer : 
  Buffer interno :  di una risorsa che non è quella iniziale dell'ordine
  Buffer tra livelli :  di una risorsa iniziale dell'ordine.

Se una risorsa è, per alcuni ordini, iniziale, e per altri intermedia, il suo buffer è dato dalla somma dei due.

### **Capacità finita (schedulazione a)**

La schedulazione a capacità finità è una tecnica che si propone di datare quando un Task deve essere fatto da un centro di lavoro considerando la capacità finita del centro di Lavoro.
Ci sono molti metodi si schedulaziona a Capacità Finita ma i più conosciuti sono i tre seguenti : 

- Event Based
- Resource Based
- Job Based

I tre metodi ciascuno in modo differente consentono alla fabbrica di : 

- Ottimizzare l'utilizzazione delle risorse
- Diminuire i costi di stock materiale
- Produrre una to-do list
- Migliorare il servizio ai clienti
- Migliorare comunicazione e coordinazione

Prendendo come riferimento i due estremi  Event Based ed Job Based, il primo privilegia la saturazione dell'impianto mentre il secondo il livello di servizio.
Nel primo metodo è possibile differenziare le urgenze (dispatching rules) per fase, mentre nel secondo un ordine deve avere la stessa urgenza per tutte le fasi.

Il modo di congelamento deve essere congruente al metodo.
Nel primo si congelano le code sulle risorse, nel secondo si congelano gli ordini più urgenti.




### **Capacità infinita (schedulazione a)**

La schedulazione a capacità infinita  è una modalità di datazione approssimativa di un ciclo (sia di un articolo, sia di un ordine pianificato o rilasciato), con lo scopo di determinarne
l'inizio o la fine (tramite la datazione delle singole fasi) e di valutare il carico delle varie risorse nel tempo, senza ricorrere a strumenti più complessi, quali la schedulazione a capacità finita.
La Schedulazione a Capacità Infinita si basa su questi due assunti : 
- Un task può essere iniziato in qualsiasi momento arriva sul centro di lavoro
- Il tempo medio di coda può essere stimato




### **Caricamento orizzontale**

Si prende l'ordine più urgente e si caricano in sequenza tutte le sue fasi sulla loro risorsa. Se vi sono alternative si sceglie la risorsa più scarica.
Un raffinamento di questo metodo è lo sfruttamento completo di una hole da parte di una fase di un ordine successivo creata da un ordine precedente.

### **Caricamento verticale**

Si carica l'impegno con vincolo al più presto più basso (se il vincolo al più presto è inferiore alla data disponibilità risorse viene portato a questo valore) più urgente.

### **Coda**

La coda è la sequenza di operazioni da eseguire su una macchina.
Nella schedulazione a capacità finita la coda viene calcolata (è un valore che varia nel tempo, in base al completamento del task in corso, ed all'arrivo dei task dalle fasi precedenti). Nella schedulazione a capacità infinita, la coda è un valore medio che viene impostato (in base a misurazioni), a livello di risorsa, espresso usualmente in ore o (meon frequentemente) in giorni.

### **Collo di bottiglia**

Una risorsa è chiamata collo di bottiglia se la sua è l'unica capacità produttiva  critica per l'esecuzione delle lavorazioni.

### **Congelamento**

Definisce una sequenza di schedulazione su di una risorsa specifica che viene mantenuta nelle successive schedulazioni.

### **Cubo**


### **Drum Buffer Rope**


### **Deadlock**

Il DeadLock è una situazione che si può verificare in una schedulazione event based tale per cui è impossibile completare l'algoritmo di schedulazione.
A questa condizione ci si può portare quando si congelano gli impegni risorse dopo interventi manuali di spostamento che modificano la proposta dello schedulatore.
Supponiamo di avere uno scenario di schedulazione come descritto dalla tabella seguente : 



|  Nam="Scenario Esempio" |
| ### **Ordine Produzione**

### **Fase**

### **Risorsa**

### **Criterio Ordinamento**

 |
| OP0A|010|RISO01|00001 |
| OP0A|020|RISO02|00001 |
| OP0B|010|RISO02|00002 |
| OP0B|020|RISO01|00002 |
|  |
| 


Lo schedulatore in uno situazione ideale produrrebbe il seguente risultato sulle due risorse : 


|  Nam="Risorsa" |
| ### **Risorsa**

### **Sequenza 1**

### **Sequenza 2**

 |
| RISO01|OP0A-010|OP0B-020 |
| RISO02|OP0B-010|OP0A-020 |
|  |
| 


Ipotizziamo un intervento manuale dal gantt  che congela le code in quest'altro modo : 


|  Nam="Risorsa" |
| ### **Risorsa**

### **Sequenza 1**

### **Sequenza 2**

 |
| RISO01|OP0B-020|OP0A-010 |
| RISO02|OP0A-020|OP0B-010 |
|  |
| 

La modifica viene accettata dallo schedulatore perchè ogni spostamento non implica una successiva rischedulazione e pertanto è solo al termine degli spostamenti che scopriremo che la schedulazione non potrà essere portata a compimento.
La  schedulazione si blocca perche nessuno degli impegni riesce a portarsi nella condizione di "Pronto " alla schedulazione infatti : 
-  L'operazione 020 di OP0B aspetta  la schedulazione della fase 010 di OP0B
-  L'operazione 010 di OP0B aspetta  la schedulazione della fase 020 di OP0A
-  L'operazione 020 di OP0A aspetta  la schedulazione della fase 010 di OP0A
-  L'operazione 010 di OP0A aspetta  la schedulazione della fase 020 di OP0B
-  .........

E' chiaro a questo punto che si genera un nodo di schedulazione la cui unica soluzione è lo scongelamento dei degli impegni che hanno generato il Dead Lock.


### **Dispatching rule**

Dispatching Rule sono le regole con cui viene data una priorità ai task dei Job che possono essere eseguiti da una risorsa.  Lo schedulatore ci mette a disposizione regole che tengono in considerazione i tempi di lavorazione e di set.up , regole che considerano la data di consegna, regole che considerano il tempo di processo e la consegna e regole che considerano la situazione dell'impianto.

### **Event based**

E' uno dei tre principali metodi  di schedulazione. Nel metodo Event Based (EBM)  data una risorsa  viene scelto il Task(operazione)  che può essere eseguito per primo nel tempo. Se  ci sono più Task che possono essere eseguiti contemporaneamente viene scelto quello con la priorità più alta.
Questo metodo di schedulazione privilegia la saturazione. Il congelamento è il congelamento della coda di una risorsa.

### **Flow shop**

Flow Shop è una definizione del processo produttivo in cui ogni Job è caratterizzato da un ciclo tecnologico che richiede l'intervento di più macchine diverse.  L'ordine con cui le operazioni devono essere effettuate sulle diverse macchine è uguale per tutti i Job. Tutti i Job visitano le macchine nello stesso ordine.


### **Forzatura**

Definisce una risorsa specifica su cui viene eseguito obbligatoriamente un impegno.

### **Gantt (diagramma di)**

Il diagramma di Gantt è uno strumento di supporto alla gestione dei progetti, così chiamato in ricordo dell'ingegnere statunitense  che lo ideò nel 1917, Henry Laurence Gantt (1861 - 1919).
Il diagramma di Gantt, usato principalmente nelle attività di project management, è costruito da un asse orizzontale che  rappresenta l'arco temporale totale del progetto e da un asse verticale che rappresenta le mansioni o attività che costituiscono il progetto.

### **Greedy**


### **Gruppo temporaneo**


### **Hole**


### **Istante al più presto**

E' l'istante al più presto per cui può essere eseguito un Task tenendo conto della disponibilità della risorsa e dei vincoli di esecuzione del Task stesso.
Il vincolo di esecuzuione è il valore più alto tra l'istante in cui può essere iniziato il Task (in funzione della fine del Task precedente dello stesso Job), e un istante di vincolo esterno, impostato manualmente dall'utente.


### **Job **

Un Job è un documento di produzione che descrive tramite le sue operazioni il ciclo produttivo che deve essere eseguito per fabbricare un prodotto.

### **Job based**


### **Job shop**

Ogni Job è caratterizzato da un ciclo tecnologico che attraversa più macchine in un preciso ordine. L'ordine con cui le operazioni sono effettuate sulle macchine è diverso da job a job al contraio del Flow Shop.
Il flusso di lavorazione non è "unidirezionale" come ad esempio in un reparto di lavorazione meccanica in cui i pezzi sono lavarati da più macchine utensili ciascuno in base al suo ciclo di lavorazione.

### **Lazy evaluation**

E' una strategia di schedulazione (valutazione pigra) che non controlla, ad ogni passo, eventualità di produrre in futuro delle situazioni insostenibili ma, solo al loro verificarsi, "torna sui propri passi" per ripartire dal passo che l'ha verificata e prendere un altra strada.
E'quindi la causa scatenante del backtracking.

### **Look ahead**

E' una strategia tale per cui dopo aver schedulato un Job su una risorsa si guarda avanti sulle operazioni eseguibili sulla stessa risorsa per capire se è conveniente tirarne una successiva non rispettando la priorità ma per l'ottimazzione di altri obiettivi(esempio tempi attrezzaggi)

### **Macchina singola**


Si parla di macchina singola per classificare un processo produttivo in cui  la schedulazione riguarda un'unica risorsa produttiva.
La schematizzazione a macchina singola è applicabile in quelle situazioni in cui l'impianto è schematizzabile con unica macchina(non ci sono giacenze di item interoperazionali) oppure in quei casi in cui una sola delle fasi del processo produttivo è critica per quanto riguarda la capacità produttiva.

### **Makespan**


### **Multipallet**


### **Parallelismo**

Parliamo di parallelismo quando un job può essere eseguito su più macchine

### **Parallelismo rigido**

Parliamo di parallelismo rigido quando il job può essere eseguito su più postazioni della stessa risorsa

### **Partenza mossa**


### **Preemption**

Preemption ammessa(Job Splitting) significa che è possibile l'interruzione di un Job ed una sua successiva ripresa dopo la lavorazione di altri job.

### **Real time (schedulazione)**


### **Resource based**

E' uno dei tre principali metodi di schedulazione. Il metodo Resource Based (RBM) si basa sul principio di schedulare per primo il centro di lavoro "Bottle Neck". La schedulazione del centro di lavoro bottleneck è fatta come nel metodo Event Based.  Il RBM suppone che tutti i centri di lavoro non critici sono schedulati a capacità infinita.

### **Ricerca locale (nel tempo)**


### **Ricerca locale (nello spazio)**


### **Risorsa primaria**

La risorsa primaria è la risorsa oggetto della schedulazione.

### **Risorsa principale**

La risorsa principale può essere una aggregazione di risorse specifiche che hanno la medesima tecnologia e pertanto possiamo considerarle "indistinguibili"

### **Risorsa specifica**

La risorsa specifica è risorsa appartenente ad una risorsa principale.

### **Risorsa secondaria**

La risorsa secondaria è una risorsa secondaria ai fini della schedulazione ma di cui è necessario tenere conto per considerare la bontà della schedulazione. Esempi di risorse secondarie sono gli attrezzi , gli stampi, le risorse umane, tec..

### **Risorsa secondaria di segnalazione**



### **Risorsa secondaria di vincolo**



### **Saturazione**


### **Scenario**


### **Sorpasso subdolo**

E'una condizione prodotta da variazioni alla strategia tramite exit utente.
Si verifica quando, su una risorsa primaria, viene eseguto un task a priorità più bassa di un altro che, per vincoli di date, potrebbe essere ugualmente eseguito.



### **Sottofase**


### **Sovrapposizione**


### **Sovrapposizione tra fasi**


### **Sovrapposizione tra livelli**


### **Spinta**


### **Task**

E'la singola attività che viene eseguita su una risprsa primaria.
Più task in sequenza, con eventuali parallelismi, compongono un Job.

### **Tiro**


### **Vincolo esterno**


### **Vincolo interno**



