- **Processo**

 :  : VOC Id="00001" Txt="Processo"
È la descrizione di un processo aziendale. Dice : 
 * di quali compiti è composto, e in che ordine vengono eseguiti.
 * chi li può eseguire.
 * cosa va fatto per ogni passo.
Sulla base del processo vengono istanziati ed eseguiti gli ordini di workflow.

Un processo viene descritto mediante una rete di Petri, composta da luoghi e transizioni.

Oggetto Sme.up :  TAWFA + script relativo in SCP_WFA.
- [WFA - Processi workflow](Sorgenti/OG/TA/WFA)


- **Transizione**

 :  : VOC Id="00002" Txt="Transizione"
È un componente delle reti di Petri, utilizzate per descrivere i processi.
In questo contesto è il modello degli impegni di un processo.

Oggetto Sme.up :  F5


- **Luogo**

 :  : VOC Id="00003" Txt="Luogo"
È un componente delle reti di Petri, utilizzate per descrivere i processi.
Indica lo stato di avanzamento del processo nell'esecuzione di un ordine.
In letteratura sulle reti di Petri viene chiamato anche "Posto" ("Place").

Oggetto Sme.up :  F6


- **Ordine di workflow**

 :  : VOC Id="00004" Txt="Ordine di workflow"
È un'istanza di un processo.

Oggetto Sme.up :  F1
- [WFORTE0F Testate ordini di workflow](Sorgenti/OJ/FILE/WFORTE0F)

- **Impegno**

 :  : VOC Id="00005" Txt="Impegno"
È un compito elementare da eseguire nel corso di un ordine di workflow; è l'istanza di una transizione.
Deve essere eseguito da una persona tra le n abilitate nel processo per la transizione equivalente.
La scheda dell'impegno è il luogo dove viene eseguito facendo avanzare l'ordine relativo.

Lo stesso impegno di un medesimo ordine può essere eseguito più volte nello svolgimento di un workflow, generando così più attività.

Oggetto Sme.up F2
- [WFIMPE0F Impegni ordini di workflow](Sorgenti/OJ/FILE/WFIMPE0F)


- **Attività**

 :  : VOC Id="00006" Txt="Attività"
È la traccia di un'attività elementare su un ordine di workflow.
Generano attività, ad esempio : 
 * l'esecuzione di un'azione su un impegno (es. presa in carico, avanzamento).
 * l'esecuzione di un'azione su un ordine (modifica dei dati di testata, cambio di stato).
 * azioni personali definite specificamente per un processo.

La storia di un ordine di workflow è l'insieme delle attività su di esso. Analizzando le attività di un ordine si può quindi sapere chi ha fatto cosa e quando.

Oggetto Sme.up :  F4
- [WFATTI0F Attività ordini di workflow](Sorgenti/OJ/FILE/WFATTI0F)


- **Extra rete**

 :  : VOC Id="00007" Txt="Extra rete"
Una transizione extra-rete non è collegata nella rete di Petri, cioè non ha luoghi nè in ingresso, nè in uscita.
La creazione e la gestione di impegni extra-rete sono manuali, cioè non effettuate dal motore di workflow ma da programmi specifici creati durante l'esecuzione dell'ordine.
La transizione extra-rete quindi modella gli impegni per quanto riguarda chi li può svolgere e cosa deve fare, ma non relativamente a quanti impegni vanno creati e quando vanno eseguiti.


- **Master**

 :  : VOC Id="00008" Txt="Master"
Particolari tipi di transizione / impegni, che generano uno o più impegni slave implementando in questo modo le liste di distribuzione.
La generazione degli impegni slave è decisa in modo dinamico nell'esecuzione di un ordine.
La dichiarazione (automatica) di impegni extra-rete è subordinata al completamento degli impegni slave associati.


- **Slave**

 :  : VOC Id="00009" Txt="Slave"
Le transizioni slave sono un modello per gli impegni slave, generati da impegni master.
Sono simili alle extra-rete nel senso che sono fuori dalla rete di Petri (no a luoghi in/out), ma la loro creazione e gestione è a carico del motore di workflow sulla base dei parametri con cui è compilato lo script delle relative transizioni master.


- **Azione esterna**

 :  : VOC Id="00010" Txt="Azione esterna"
Sono chiamate di funzioni (F() oppure A()) che vengono presentate nella scheda di un impegno, nella sezione di destra "Azioni esterne", oppure, nel caso di chiamate a schede, direttamente nella parte principale della scheda di impegno.
Servono a portare all'utente le informazioni e le azioni necessarie ad eseguire un impegno.
La loro esecuzione NON è controllata dal motore di workflow.


- **Azione di attività (di workflow)**

 :  : VOC Id="00011" Txt="Azione di attività (di workflow)"
Sono le azioni con cui viene avanzato lo stato di un impegno e di conseguenza quello del workflow.
Possono essere automatiche (ad esempio l'attivazione) oppure eseguite da parte di un utente abilitato sull'impegno.
La loro esecuzione avviene sotto controllo di allocazione dell'ordine da parte del motore di workflow.
Le azioni di attività standard sono : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00017) I(Attivazione) O(I)
 :  : DEC T(VO) P(WFBASE_GLO) K(00018) I(Presa in carico) O(I)
 :  : DEC T(VO) P(WFBASE_GLO) K(00019) I(Assegnazione) O(I)
 :  : DEC T(VO) P(WFBASE_GLO) K(00020) I(Dichiarazione) O(I)
 :  : DEC T(VO) P(WFBASE_GLO) K(00021) I(Distribuzione) O(I)
 :  : DEC T(VO) P(WFBASE_GLO) K(00022) I(Disattivazione) O(I)
Attivazione/disattivazione requisiti esterni.


- **Requisito esterno**

 :  : VOC Id="00012" Txt="Requisito esterno"
Sono requisiti aggiuntivi (relativi al mondo esterno) rispetto ai luoghi di ingresso per l'attivazione di un impegno di workflow.
Ad esempio si può fissare che un impegno si attiva, una volta che i luoghi in ingresso hanno il token, solo se lo stato di un oggetto di Sme.up assume un determinato valore.


- **Rete di Petri**

 :  : VOC Id="00013" Txt="Rete di Petri"
Sono il formalismo con cui rappresentiamo il flusso di esecuzione dei processi. Per ulteriori informazioni consultare la documentazione attiva.

- **Conseguenza esterna**

 :  : VOC Id="00014" Txt="Conseguenza esterna"
Le conseguenze esterne sono azioni "cieche" eseguite al completamento del lavoro su un impegno.
Non sono interattive, a meno di eventuali segnalazioni di errore.
Eventuali decisioni pertinenti allo svolgersi delle conseguenze esterne devono quindi essere prese nello svolgimento dell'impegno, prima della dichiarazione.

- **Push**

 :  : VOC Id="00015" Txt="Push"
Un impegno viene assegnato in push quando un utente (responsabile di assegnazione) forza quale utente lo dovrà eseguire, mediante un'azione di assegnazione, scegliendolo tra gli utenti appartenenti alla classe di esecutori.

- **Pull**

 :  : VOC Id="00016" Txt="Pull"
Un impegno viene assegnato in pull quando un utente tra gli appartenenti alla classe di esecutori decide di svolgerlo, mediante un'azione di presa in carico.

- **Attivazione**

 :  : VOC Id="00017" Txt="Attivazione"
Con l'attivazione di un impegno il motore di workflow segnala l'eseguibilità dello stesso.

- **Presa in carico**

 :  : VOC Id="00018" Txt="Presa in carico"
Con la presa in carico si assegna a se stessi un impegno, se questo non è ancora assegnato ad un utente specifico.
Contemporaneamente si segnala l'inizio formale del lavoro sull'impegno.
Azione obbligatoria a meno che nello script del processo non si indichi di saltarla per una determinata transizione.
La sua esecuzione genera un'attività di presa in carico.

- **Assegnazione**

 :  : VOC Id="00019" Txt="Assegnazione"
Con l'assegnazione un responsabile di assegnazione dell'impegno decide quale utente, tra gli appartenenti alla classe di esecutori, svolgerà l'impegno stesso.

- **Dichiarazione (avanzamento)**

 :  : VOC Id="00020" Txt="Dichiarazione (avanzamento)"
L'azione di dichiarazione segnala il completamento del compito associato ad un impegno, scatenando nell'ordine la chiusura dell'impegno, la registrazione dell'attività, l'esecuzione delle conseguenze e l'aggiornamento della rete.
Dopo la dichiarazione non è più possibile tornare indietro, a meno che la rete non lo preveda.
Azione obbligatoria, genera un'attività di dichiarazione.

- **Distribuzione**

 :  : VOC Id="00021" Txt="Distribuzione"
Con la distribuzione un utente attiva una lista di distribuzione, rendendo pronti tutti gli impegni slave di cui essa è composta.

- **Disattivazione**

 :  : VOC Id="00022" Txt="Disattivazione"
Con la disattivazione il motore di workflow "spegne" un impegno, rendendolo non eseguibile. Questo perchè non sono più validi alcuni dei requisiti per la sua eseguibilità (esempio token consumato da un altro impegno).

- **Lista di distribuzione**

 :  : VOC Id="00023" Txt="Lista di distribuzione"
È un modo per gestire, in un processo, impegni di presa visione a cardinalità variabile.
In altre parole :  c'è un punto, nel processo, in cui per potere andare avanti ho bisogno della presa visione da parte di n utenti, ma n varia tra un ordine e l'altro.
Con la lista di distribuzione si codifica una sola transizione che rappresenta gli impegni di presa visione, poi per ogni ordine di workflow verranno creati n impegni da questa transizione, con n variabile.

- **Check**

 :  : VOC Id="00024" Txt="Check"
È un controllo impostato all'avanzamento di un impegno (se il controllo non passa non è possibile avanzare l'impegno).
Può essere abbinato all'avanzamento in generale, oppure a una particolare scelta effettuata all'avanzamento.

- **Promemoria**

 :  : VOC Id="00025" Txt="Promemoria"
È una notifica presentata a un utente in una determinata data/ora.
Un esempio tipico è la segnalazione di attivazione o di scadenza di un impegno di workflow.

- **Azione catalogata**

 :  : VOC Id="00026" Txt="Azione catalogata"
Sono "azioni catalogate" le istruzioni degli script di workflow create allo scopo di evidenziare e aiutare nella compilazione di conseguenze esterne / azioni di dichiarazione con particolari valenze applicative.

- **Oggetto master**

 :  : VOC Id="00027" Txt="Oggetto master"
È l'oggetto (opzionale) di Sme.UP su cui opera un ordine di workflow.

- **Oggetto owner**

 :  : VOC Id="00028" Txt="Oggetto owner"
È l'oggetto di Sme.UP responsabile di un ordine di workflow. A standard è l'utente di inserimento dell'ordine di workflow.










