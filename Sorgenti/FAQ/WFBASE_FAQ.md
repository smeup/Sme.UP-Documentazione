- **Sai i diversi punti di creazione di un ordine di workflow?**

 :  : VOC Id="SKICO010" Txt="Sai i diversi punti di creazione di un ordine di workflow?"
Da pop.up di oggetto, da scheda Inserimento o gestito dall'utente.
Fare riferimento all'help del campo "Punto di creazione" della tabella WFA.

- **Sai i diversi modi di creazione di un ordine di workflow?**

 :  : VOC Id="SKICO020" Txt="Sai i diversi modi di creazione di un ordine di workflow?"
Una volta creato l'ordine di workflow può partire o no in automatico la sua esecuzione.
Fare riferimento all'help del campo "Modo di creazione" della tabella WFA.

- **Sai come attivare l'integrazione forte di un oggetto con il workflow?**

 :  : VOC Id="SKICO030" Txt="Sai come attivare l'integrazione forte di un oggetto con il workflow?"
È necessario : 
* Attivare la nuova gestione azioni in tabella B£2, almento per gli oggetti gestiti a workflow.
* Avere dei processi di workflow, in tabella WFA, attivi sull'oggetto e con il flag "Disabilita gestione" impostato a 1.
Si veda anche : 
- [Integrazione con gli oggetti](Sorgenti/DOC/TA/B£AMO/WFBASE_029)

- **Sai come dire che un impegno è ad esecuzione automatica?**

 :  : VOC Id="SKICO040" Txt="Sai come dire che un impegno è ad esecuzione automatica?"
Non compilando nè codice esecutore nè classe esecutori.
Si veda, nel seguente script di esempio, la transizione T04 : 
 :  : DEC T(TA) P(WFA) K(ESE_001)

- **Sai come fare eseguire delle conseguenze esterne all'avanzamento?**

 :  : VOC Id="SKICO050" Txt="Sai come fare eseguire delle conseguenze esterne all'avanzamento?"
È necessario inserire, nella parte di script della transizione, una parte di tipo CSG.EXT.
Si veda anche : 
- [Sintassi script WF](Sorgenti/DOC/TA/B£AMO/WFBASE_007)
Si veda, nel seguente script di esempio, la transizione T01 : 
 :  : DEC T(TA) P(WFA) K(ESE_003)

- **Sai come cambiare l'azione di dichiarazione di un impegno?**

 :  : VOC Id="SKICO060" Txt="Sai come cambiare l'azione di dichiarazione di un impegno?"
È necessario definire, nella parte di script della transizione, una istruzione di tipo DIC.FUN.
Si veda anche : 
- [Sintassi script WF](Sorgenti/DOC/TA/B£AMO/WFBASE_007)
Si veda, nel seguente script di esempio, la transizione T03 : 
 :  : DEC T(TA) P(WFA) K(ESE_003)

- **Sai come modificare il contenuto della scheda di un impegno?**

 :  : VOC Id="SKICO070" Txt="Sai come modificare il contenuto della scheda di un impegno?"
È necessario definire, nella parte di script della transizione, una parte di tipo EXT, seguita da definizioni di funzioni di scheda.
Si veda anche : 
- [Sintassi script WF](Sorgenti/DOC/TA/B£AMO/WFBASE_007)
Si veda, nel seguente script di esempio, la transizione T02 : 
 :  : DEC T(TA) P(WFA) K(ESE_003)

- **Sai come lanciare un sottoworkflow?**

 :  : VOC Id="SKICO080" Txt="Sai come lanciare un sottoworkflow?"
Dall'esecuzione di un workflow :  si può definire una conseguenza esterna, all'avanzamento di un impegno, che lanci il sottoworkflow.
Si veda anche : 
- [Costruzione modulare di workflow](Sorgenti/DOC/TA/B£AMO/WFBASE_012)
Si veda, nel seguente script di esempio, la transizione T01 : 
 :  : DEC T(TA) P(WFA) K(ESE_008)
Se si vuole lanciare la creazione in maniera indipendente da qualunque avanzamento, invece, si può utilizzare il deviatore WFDV01X - fare riferimento all'help in testa al programma.


- **Sai come associare un'autorizzazione alla classe esecutori di un impegno?**

 :  : VOC Id="SKICO090" Txt="Sai come associare un'autorizzazione alla classe esecutori di un impegno?"
È necessario impostare la classe esecutori con tipo e parametro TAB£P, dando il codice (classe) ed opzionalmente funzione e valore.
Si veda anche : 
- [Autorizzazioni Work.up](Sorgenti/DOC/TA/B£AMO/WFBASE_006)
- [Definizione delle responsabilità](Sorgenti/DOC/TA/B£AMO/WFBASE_031)
Si veda, nel seguente script di esempio, la transizione T04 : 
 :  : DEC T(TA) P(WFA) K(ESE_002)


- **Sai come attivare l'annullamento utente di un passo?**

 :  : VOC Id="SKICO100" Txt="Sai come attivare l'annullamento utente di un passo?"
Tramite l'apposito flag sulla istruzione della transizione; si veda la sottoscheda "Modalità operative" del wizard dell'istruzione TRA.
Si veda anche : 
- [Flessibilità, annullamenti ed eccezioni](Sorgenti/DOC/TA/B£AMO/WFBASE_027)
Si veda, nel seguente script di esempio, la transizione T04 : 
 :  : DEC T(TA) P(WFA) K(ESE_002)

- **Sai come dire che un impegno è da assegnare?**

 :  : VOC Id="SKICO110" Txt="Sai come dire che un impegno è da assegnare?"
Basta definire una classe di assegnatori, ovvero di utenti abilitati all'assegnazione dell'impegno.
- [Definizione delle responsabilità](Sorgenti/DOC/TA/B£AMO/WFBASE_031)
Si veda, nel seguente script di esempio, la transizione T02 : 
 :  : DEC T(TA) P(WFA) K(ESE_004)


- **Sai come rendere saltabile un impegno?**

 :  : VOC Id="SKICO120" Txt="Sai come rendere saltabile un impegno?"
Tramite l'apposito flag sulla istruzione della transizione; si veda la sottoscheda "Modalità operative" del wizard dell'istruzione TRA.
Si veda anche : 
- [Flessibilità, annullamenti ed eccezioni](Sorgenti/DOC/TA/B£AMO/WFBASE_027)


- **Sai come mandare una mail all'attivazione di un impegno?**

 :  : VOC Id="SKICO130" Txt="Sai come mandare una mail all'attivazione di un impegno?"
Si aggiunge un'opportuna conseguenza esterna di tipo attivazione alla relativa transizione.
Vedere l'opportuna azione catalogata AZ.B£.0010 tra le istruzioni di workflow e il relativo wizard.


- **Sai come fare cambiare lo stato di un oggetto all'avanzamento di un impegn**

 :  : VOC Id="SKICO140" Txt="Sai come fare cambiare lo stato di un oggetto all'avanzamento di un impegno?"
Si aggiunge un'opportuna conseguenza esterna alla relativa transizione.
Vedere l'opportuna azione catalogata AZ.B£.0050 tra le istruzioni di workflow e il relativo wizard.


- **Sai come dichiarare l'avanzamento di un impegno?**

 :  : VOC Id="SKIIN010" Txt="Sai come dichiarare l'avanzamento di un impegno?"
Se è un impegno con avanzamento da scheda devi cliccare il pulsante in alto a destra (tipicamente si chiamerà "Avanza" a meno di ridefinizioni).
Se è un impegno di gestione oggetto (es. modifica di un articolo) la conferma della gestione (es. F6 nel visualizzatore) dichiarerà in automatico l'avanzamento.


- **Sai come leggere la storia delle attività di un ordine di workflow?**

 :  : VOC Id="SKIFO010" Txt="Sai come leggere la storia delle attività di un ordine di workflow?"
Dalla scheda dell'ordine di workflow clicca, nelle sottoschede a metà schermo, la scheda "Log attività".


- **Sai come leggere la storia delle attività di workflow di un oggetto di Sme**

 :  : VOC Id="SKIFO020" Txt="Sai come leggere la storia delle attività di workflow di un oggetto di Smeup?"
Per gli oggetti per cui è già integrata la gestione a worfklow è presente a standard, come sottoscheda della scheda di oggetto, una scheda "Workflow".
Tale scheda ha, come sottoscheda, una scheda "Attività".
Ad esempio, scheda di articolo, sottoscheda "Workflow", sottoscheda "Attività".


- **Sai quali sono le tre cose di cui si occupa il workflow?**

 :  : VOC Id="SKIFO030" Txt="Sai quali sono le tre cose di cui si occupa il workflow?"
Flusso, responsabilità, contenuto applicativo.


- **Sai quali sono i 3 files importanti del workflow?**

 :  : VOC Id="SKICO150" Txt="Sai quali sono i 3 files importanti del workflow?"
WFORTE0F (Oggetto F1), WFIMPE0F (Oggetto F2), WFATTI0F (Oggetto F4).


- **Sai qual è la tabella più importante del workflow?**

 :  : VOC Id="SKICO160" Txt="Sai qual è la tabella più importante del workflow?"
Tabella WFA (e relativo script collegato SCP_WFA).


- **Sai come entrare in modifica grafica di un processo di workflow?**

 :  : VOC Id="SKICO170" Txt="Sai come entrare in modifica grafica di un processo di workflow?"
Dalla scheda del processo (TA/WFA/codice del processo), sottoscheda "Script", pulsante "Modifica - grafica".


- **Sai come aggiungere graficamente una transizione a un processo?**

 :  : VOC Id="SKICO180" Txt="Sai come aggiungere graficamente una transizione a un processo?"
Cliccando lo strumento Transizione (secondo a sinistra nell'editor grafico) e piazzandolo graficamente.


- **Sai come aggiungere graficamente un luogo a un processo?**

 :  : VOC Id="SKICO190" Txt="Sai come aggiungere graficamente un luogo a un processo?"
Cliccando uno degli strumenti Luogo (Iniziale/Normale/Finale - terzo, quarto, quinto da sinistra nell'editor grafico) e piazzandolo graficamente.


- **Sai dove documentare applicativamente un processo?**

 :  : VOC Id="SKICO200" Txt="Sai dove documentare applicativamente un processo?"
Nel file DOC_WFA, membro=nome del processo.
È possibile arrivare velocemente alla gestione del membro dalla scheda del processo, sottoscheda "Processo", sottoscheda "Modifica istruzioni".


- **Sai dove documentare tecnicamente un processo?**

 :  : VOC Id="SKICO210" Txt="Sai dove documentare tecnicamente un processo?"
All'interno dello script in SCP_WFA, nella parte che segue l'istruzione DOC.


- **Sai come fare scegliere all'utente come procedere con un ordine di workflo**

 :  : VOC Id="SKICO220" Txt="Sai come fare scegliere all'utente come procedere con un ordine di workflow?"
È necessario : 
* Prevedere diversi luoghi in uscita a una transizione;
* Attivare una selezione di tipo utente mediante l'attributo Tip="C" dell'istruzione TO;
* Associare i luoghi di uscita a diverse scelte utente, mediante le istruzioni WHN e OTH;
* Abilitare, nella transizione, la scelta standard con l'opportuno flag ("Scelta standard" nella prima schermata del wizard dell'istruzione TRA).
Si veda, nel seguente script di esempio, la transizione T03 : 
 :  : DEC T(TA) P(WFA) K(ESE_001)


- **Sai come parametrizzare un processo mediante le variabili di workflow?**

 :  : VOC Id="SKICO230" Txt="Sai come parametrizzare un processo mediante le variabili di workflow?"
Si veda : 
- [Variabili utilizzabili nel workflow](Sorgenti/DOC/TA/B£AMO/WFBASE_009)
Si veda ad esempio lo script : 
 :  : DEC T(TA) P(WFA) K(ESE_012)


- **Sai come attivare degli esecutori di backup?**

 :  : VOC Id="SKICO240" Txt="Sai come attivare degli esecutori di backup?"
Tramite l'opportuno flag nell'istruzione di transizione TRA.
Si veda : 
- [Definizione delle responsabilità](Sorgenti/DOC/TA/B£AMO/WFBASE_031)
Si veda ad esempio lo script : 
 :  : DEC T(TA) P(WFA) K(ESE_011)


- **Sai come precalcolare in maniera parametrica l'esecutore di un impegno?**

 :  : VOC Id="SKICO250" Txt="Sai come precalcolare in maniera parametrica l'esecutore di un impegno?"
Utilizzando delle variabili di workflow.
Si veda ad esempio lo script, transizione T02 : 
 :  : DEC T(TA) P(WFA) K(ESE_002)


- **Sai la differenza tra esecutore e classe esecutori?**

 :  : VOC Id="SKIFO040" Txt="Sai la differenza tra esecutore e classe esecutori?"
L'esecutore è l'utente individuato per l'esecuzione di un particolare impegno.
La classe esecutori è l'insieme delle papabili scelte - se presente deve contenere anche l'esecutore.


- **Sai cosa è un processo?**

 :  : VOC Id="SKIFO050" Txt="Sai cosa è un processo?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00001)


- **Sai fare 3 esempi di processi?**

 :  : VOC Id="SKIFO060" Txt="Sai fare 3 esempi di processi?"
Ad esempio : 
* Approvazione di una richiesta di acquisto, dall'inserimento fino alla sua estraibilità in ordine.
* Inserimento e completamento di un articolo.
* Domanda/risposta tra un utente dell'ufficio tecnico e un utente dell'ufficio commerciale.


- **Sai cosa è un ordine di workflow?**

 :  : VOC Id="SKIFO070" Txt="Sai cosa è un ordine di workflow?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00004)


- **Sai cosa è un impegno?**

 :  : VOC Id="SKIFO080" Txt="Sai cosa è un impegno?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00005)


- **Sai cosa è un'attività?**

 :  : VOC Id="SKIFO090" Txt="Sai cosa è un'attività?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00006)


- **Sai la differenza tra transizione e impegno?**

 :  : VOC Id="SKIFO100" Txt="Sai la differenza tra transizione e impegno?"
La transizione è : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00002)
In sostanza la transizione è un MODELLO di impegno. Da una transizione nascono n impegni, in genere uno per ordine.


- **Sai la differenza tra ordine e processo?**

 :  : VOC Id="SKIFO110" Txt="Sai la differenza tra ordine e processo?"
Il processo è il MODELLO da cui nascono gli ordini di workflow.
Da un processo nascono n ordini di workflow.
Ad esempio ho : 
* 1 processo che definisce cosa succede nella mia azienda alla creazione di un nuovo articolo;
* n ordini di workflow, derivanti dal processo - uno per ogni articolo che viene creato.


- **Sai da quali due punti standard si può eseguire un impegno?**

 :  : VOC Id="SKIES010" Txt="Sai da quali due punti standard si può eseguire un impegno?"
Da : 
* Sottoscheda "Worklist" della scheda "Workflow".
* Se il workflow agisce su un oggetto master (es. articolo A01) dal pop.up dell'oggetto o dalla scheda dell'oggetto, sottoscheda "Workflow".


- **Sai dove andare per verificare gli impegni che puoi assegnare?**

 :  : VOC Id="SKIES020" Txt="Sai dove andare per verificare gli impegni che puoi assegnare?"
Nella sottoscheda "Impegni da assegnare" della scheda "Workflow.


- **Sai cosa è una rete di Petri?**

 :  : VOC Id="SKICO260" Txt="Sai cosa è una rete di Petri?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00013)


- **Sai la differenza tra push e pull nella determinazione di un esecutore?**

 :  : VOC Id="SKICO270" Txt="Sai la differenza tra push e pull nella determinazione di un esecutore?"
Il push è : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00015)
Il pull è : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00016)
In sostanza determinano se la scelta di chi deve eseguire un impegno avviene dall'alto (assegnatori), dal basso (esecutori) o entrambi.

- **Sai dove trovare i tutorial di costruzione dei processi?**

 :  : VOC Id="SKICO280" Txt="Sai dove trovare i tutorial di costruzione dei processi?"
Si tratta degli script di esempio ESE*, presenti in SMEDEV.
Per attivarli copiare i relativi elementi di tabella WFA dal modello e attivarli togliendo il flag "Spegni inserimento".


- **Sai come estendere le colonne della worklist in un'installazione?**

 :  : VOC Id="SKICO290" Txt="Sai come estendere le colonne della worklist in un'installazione?"
Tramite l'apposito programma di estensione WFWRK_01U - si veda l'esempio in WFSRC.


- **Sai utilizzare le diverse parti della scheda di un impegno?**

 :  : VOC Id="SKICO300" Txt="Sai utilizzare le diverse parti della scheda di un impegno?"
La scheda si divide in 3 sezioni principali : 
* Tutto il lato sinistro della scheda contiene informazioni applicative; l'esempio più tipico è la scheda dell'oggetto su cui si sta lavorando.
* Il pulsante in alto a sinistra è dove si dichiarano la presa in carico e l'avanzamento dell'impegno.
* L'eventuale bottoniera sotto il pulsante di avanzamento (lato in basso a destra dello schermo) contiene le azioni esterne, una sorta di menù contestuale all'impegno e che presenta azioni che possono essere utili per lo svolgimento del lavoro.
Si veda anche : 
- [Esecuzione di un impegno da scheda](Sorgenti/DOC/TA/B£AMO/WFBASE_024)


- **Sai qual è l'unica classe di autorizzazione standard del workflow?**

 :  : VOC Id="SKICO310" Txt="Sai qual è l'unica classe di autorizzazione standard del workflow?"
La classe WFORTE, che controlla le autorizzazioni sugli ordini di workflow (inserimento e gestione master).


- **Sai come annullare un ordine di workflow?**

 :  : VOC Id="SKICO320" Txt="Sai come annullare un ordine di workflow?"
Dalla scheda dell'ordine, sottoscheda "Gestione master" (a cui bisogna essere autorizzati tramite classe WFORTE), pulsante "Annulla".


- **Sai come annullare un'attività di un ordine di workflow come utente master**

 :  : VOC Id="SKICO330" Txt="Sai come annullare un'attività di un ordine di workflow come utente master?"
Dalla scheda dell'ordine, sottoscheda "Gestione master" (a cui bisogna essere autorizzati tramite classe WFORTE), si clicca un'attività nella matrice centrale ("Annullamento attività"), successivamente si clicca il pulsante "Annulla attività" che compare in basso.


- **Sai come scrivere delle attività solo documentative?**

 :  : VOC Id="SKICO340" Txt="Sai come scrivere delle attività solo documentative?"
Da qualunque programma utente, sia chiamato durante il workflow (es. conseguenza esterna), sia esterno al workflow. Si chiama la /COPY £WFC in CLEAR e poi in WRITE.


- **Sai come costruire un'azione di dichiarazione personalizzata?**

 :  : VOC Id="SKICO350" Txt="Sai come costruire un'azione di dichiarazione personalizzata?"
Fare riferimento al programma di esempio WFAZXX_NN in WFSRC, in particolare alla routine (commentata) ATTWFA.


- **Sai come costruire una conseguenza esterna personalizzata?**

 :  : VOC Id="SKICO360" Txt="Sai come costruire una conseguenza esterna personalizzata?"
Fare riferimento al programma di esempio WFAZXX_NN in WFSRC, in particolare alla routine (commentata) CSGEXT.


- **Sai la differenza tra integrazione forte e debole con gli oggetti di Sme.u**

 :  : VOC Id="SKIFO120" Txt="Sai la differenza tra integrazione forte e debole con gli oggetti di Sme.up?"
In sintesi, data una tipologia di oggetto : 
* Integrazione FORTE indica che il workflow SOSTITUISCE integralmente la gestione dell'oggetto. Si può e si deve disegnare la "vita" dell'oggetto in maniera molto controllata e precisa.
* Integrazione DEBOLE significa che il workflow AFFIANCA la normale gestione dell'oggetto. È più semplice ma meno potente dell'integrazione forte.
Per una descrizione più dettagliata si faccia riferimento a : 
- [Integrazione con gli oggetti](Sorgenti/DOC/TA/B£AMO/WFBASE_029)


- **Sai come gestire le date di fine richiesta di ordini e impegni?**

 :  : VOC Id="SKICO370" Txt="Sai come gestire le date di fine richiesta di ordini e impegni?"
La data fine richiesta dell'ordine viene calcolata, in fase di inserimento dell'ordine di workflow, avanzando la data/ora di creazione del lead time impostato in tabella WFA, mediante il calendario impostato in tabella WFA.
La data fine richiesta di un impegno viene calcolata, all'attivazione dell'impegno, avanzando la data/ora di attivazopne del lead time impostato nella transizione, mediante il calendario impostato in tabella WFA.
Possono essere usati a scopo informativo (sono campi presenti in worklist) oppure per il calcolo dei promemoria.
Per approfondimenti : 
- [Tempistiche](Sorgenti/DOC/TA/B£AMO/WFBASE_004)
Un esempio con lead time di impegno : 
 :  : DEC T(TA) P(WFA) K(ESE_005)


- **Sai cosa sono i requisiti esterni?**

 :  : VOC Id="SKIFO130" Txt="Sai cosa sono i requisiti esterni?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00012)
Per approfondimenti : 
- [Sintassi script WF](Sorgenti/DOC/TA/B£AMO/WFBASE_007)


- **Sai cosa è una lista di distribuzione?**

 :  : VOC Id="SKIFO140" Txt="Sai cosa è una lista di distribuzione?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00023)
Per approfondimenti : 
- [Liste di distribuzione](Sorgenti/DOC/TA/B£AMO/WFBASE_028)
Un esempio molto semplice è il seguente processo : 
 :  : DEC T(TA) P(WFA) K(ESE_007)


- **Sai la differenza tra gli stati 'pronto' e 'assegnabile' di un impegno?**

 :  : VOC Id="SKIFO150" Txt="Sai la differenza tra gli stati 'pronto' e 'assegnabile' di un impegno?"
Sono entrambi stati che rappresentano il fatto che un impegno eseguibile.
La differenza è che : 
* "Pronto" viene indicato quando è già calcolato un esecutore preciso (o un utente principale con altri utenti di backup).
* "Assegnabile" viene indicato quando è solo individuata la sola classe di esecutori.
Si presti attenzione al fatto che se è indicata la sola classe di esecutori (anche composta da un solo elemento, esempio un'autorizzazione data a una sola persona) ma non è esplicitato un esecutore viene attivato in ogni caso lo stato "assegnabile".

- **Sai qual è il modo suggerito di impostare classi di autorizzazione specifi**

 :  : VOC Id="SKICO380" Txt="Sai qual è il modo suggerito di impostare classi di autorizzazione specifiche per il workflow?"
Un buon modo di impostare una classe specifica è : 
* Funzione tipizzata come F5processo - in modo da avere una autorizzazione specifica per ogni transizione del processo.
* Valori :  T1 e T2, dalla B£SWF - in modo da potere autorizzare in maniera indipendente l'esecuzione e l'assegnazione degli impegni.
Per approfondimenti : 
- [Autorizzazioni Work.up](Sorgenti/DOC/TA/B£AMO/WFBASE_006)

- **Sai come rimuovere la 'presa in carico' di un impegno?**

 :  : VOC Id="SKICO390" Txt="Sai come rimuovere la 'presa in carico' di un impegno?"
Tramite il flag "Solo dichiarazione" sulla istruzione della transizione; si veda la sottoscheda "Modalità operative" del wizard dell'istruzione TRA.

- **Sai come ridenominare il bottone 'Avanza' per un impegno?**

 :  : VOC Id="SKICO400" Txt="Sai come ridenominare il bottone 'Avanza' per un impegno?"
Definendo una azione (istruzione DIC.FUN) di dichiarazione specifica, anche senza ridefinire la funzione di avanzamento.

- **Sai come evitare che alla riattivazione di un impegno esso venga assegnato**

 :  : VOC Id="SKICO420" Txt="Sai come evitare che alla riattivazione di un impegno esso venga assegnato all'ultimo esecutore?"
Imponendo, tramite l'apposito flag sulla istruzione della transizione, di pulire gli esecutori alla dichiarazione.
Si veda la sottoscheda "Esecutori" del wizard dell'istruzione TRA.
Si veda, nel seguente script di esempio, la transizione T01 : 
 :  : DEC T(TA) P(WFA) K(ESE_001)

- **Sai come eseguire un impegno senza passare per la scheda?**

 :  : VOC Id="SKICO430" Txt="Sai come eseguire un impegno senza passare per la scheda?"

Tramite il flag "Pop.up :  azione diretta" sulla istruzione della transizione; si veda la sottoscheda "Visibilità azioni" del wizard dell'istruzione TRA.

- **Sai come creare un impegno di gestione di un oggetto master?**

 :  : VOC Id="SKICO440" Txt="Sai come creare un impegno di gestione di un oggetto master?"
Sono necessari due passi.

1. Dire che l'esecuzione dell'impegno attiva la gestione dell'oggetto (e che si avanza solo a gestione eseguita).
A questo scopo bisogna ridefinire l'azione di dichiarazione (normalmente è un semplice avanzamento) sostituendola con un'azione che tratta la gestione dell'oggetto. Si può utilizzare l'opportuna azione catalogata DI.B£.0020 (fare riferimento al suo Wizard).

2. Associare l'esecuzione dell'impegno a un'azione di gestione, in modo che sia eseguibile direttamente come azione di gestione.
Utilizzando il flag "Azione di gestione", nelle istruzioni della transizione nella sottoscheda "Visibilità azioni" del wizard.
Un impegno qualificato come "Modifica", ad esempio, sarà accessibile anche come azione 02 sull'oggetto master (quando l'impegno è attivo, ovviamente).

Tipicamente per impegni di questo tipo si spegne anche la presa in carico.

Si veda, nel seguente script di esempio, la transizione T01 : 
 :  : DEC T(TA) P(WFA) K(ESE_006)

- **Sai dove vedere una lista dei processi di workflow presenti in un'installa**

 :  : VOC Id="SKIIN020" Txt="Sai dove vedere una lista dei processi di workflow presenti in un'installazione?"
Dalla scheda del modulo WFBASE, "Cruscotto del modulo", "Lista processi"

- **Sai come fare partire la creazione di un nuovo processo?**

 :  : VOC Id="SKICO450" Txt="Sai come fare partire la creazione di un nuovo processo?"
Dalla scheda del modulo WFBASE, Cruscotto del modulo, scheda "Lista workflow", sottoscheda "Nuovo processo".
Si veda anche : 
- [Come si costruisce un workflow](Sorgenti/DOC/TA/B£AMO/WFBASE_018)

- **Sai come creare un nuovo processo copiandolo da un esistente?**

 :  : VOC Id="SKICO460" Txt="Sai come creare un nuovo processo copiandolo da un esistente?"
Dalla scheda del modulo WFBASE, Cruscotto del modulo, scheda "Lista workflow", sottoscheda Copia processo".
Si veda anche : 
- [Come si costruisce un workflow](Sorgenti/DOC/TA/B£AMO/WFBASE_018)

- **Sai dove vedere gli impegni per te attivi sui workflow di un oggetto di Sm**

 :  : VOC Id="SKIIN030" Txt="Sai dove vedere gli impegni per te attivi sui workflow di un oggetto di Sme.up?"
Dalla scheda dell'oggetto, sottoscheda "Workflow".

- **Sai dove vedere gli ordini di workflow su un oggetto di Sme.up?**

 :  : VOC Id="SKIIN040" Txt="Sai dove vedere gli ordini di workflow su un oggetto di Sme.up?"
Dalla scheda dell'oggetto, sottoscheda "Workflow".

- **Sai come vedere graficamente lo stato di avanzamento di un ordine?**

 :  : VOC Id="SKIIN050" Txt="Sai come vedere graficamente lo stato di avanzamento di un ordine?"
Dalla scheda dell'ordine di workflow, cliccando sul tasto "Rappresentazione grafica ordine".
In alternativa direttamente dal pop.up sull'ordine di workflow, selezionando "Rappresentazione grafica".

- **Sai dove vedere la lista degli utenti attivi su un impegno?**

 :  : VOC Id="SKIIN060" Txt="Sai dove vedere la lista degli utenti attivi su un impegno?"
Dalla scheda del corrispondente ordine di workflow, sottoscheda "Situazione ordine" :  cliccare sull'impegno, sulla destra apparirà una lista degli utenti abilitati ad eseguirlo.

- **Sai dove vedere la documentazione operativa di un processo?**

 :  : VOC Id="SKIIN070" Txt="Sai dove vedere la documentazione operativa di un processo?"
Nella scheda di un ordine di workflow appartenente al processo, sottoscheda "Istruzioni", vengono rappresentate le informazioni generali sul processo.
Nelle schede di impegno, sottoscheda "Istruzioni", viene esposta invece la documentazione relativa ai singoli passi.

- **Sai dove vedere la worklist specifica di un ordine di workflow?**

 :  : VOC Id="SKIIN080" Txt="Sai dove vedere la worklist specifica di un ordine di workflow?"
Nella scheda dell'ordine di workflow.

- **Sai dove annullare un'attività di un ordine di workflow se non sei utente **

 :  : VOC Id="SKIES030" Txt="Sai dove annullare un'attività di un ordine di workflow se non sei utente master?"
Si veda, alla voce "Annullamento da utente qualsiasi", il seguente documento : 
- [Flessibilità, annullamenti ed eccezioni](Sorgenti/DOC/TA/B£AMO/WFBASE_027)

- **Sai come forzare il salto di un impegno?**

 :  : VOC Id="SKIES040" Txt="Sai come forzare il salto di un impegno?"
Se sussistono le seguenti due condizioni : 
* L'impegno è configurato, a livello di processo, come impegno potenzialmente saltabile da parte di un utente;
* Appartengo alla lista di utenti che può saltare l'impegno.
Allora posso, da pop.up sull'impegno (accessibile ad esempio da worklist o dalla lista degli impegni del corrispondente ordine di workflow), selezionare "Forza salto impegno".
Si veda anche : 
- [Flessibilità, annullamenti ed eccezioni](Sorgenti/DOC/TA/B£AMO/WFBASE_027)

- **Sai come emettere un messaggio all'avanzamento di un impegno?**

 :  : VOC Id="SKICO480" Txt="Sai come emettere un messaggio all'avanzamento di un impegno?"
Se il messaggio è una conseguenza esterna (avviene dopo l'avanzamento) si utilizza l'azione catalogata AZ.B£.0030.
Se il messaggio è un'azione di dichiarazione (cioè fa parte dell'avanzamento - ad esempio è un messaggio di conferma) si utilizza invece l'azione DI.B£.0030.
Fare riferimento ai Wizard delle due istruzioni.

- **Sai cosa è un check?**

 :  : VOC Id="SKICO470" Txt="Sai cosa è un check?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00024)
Per approfondimenti : 
- [Check](Sorgenti/DOC/TA/B£AMO/WFBASE_040)
Per alcuni esempi si faccia riferimento al processi : 
 :  : DEC T(TA) P(WFA) K(ESE_013)

- **Sai cos'è un'azione catalogata?**

 :  : VOC Id="SKICO410" Txt="Sai cos'è un'azione catalogata?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00026)

- **Sai cosa è un promemoria?**

 :  : VOC Id="SKICO490" Txt="Sai cosa è un promemoria?"
Si veda la seguente voce di glossario : 
 :  : DEC T(VO) P(WFBASE_GLO) K(00025)
Per approfondimenti : 
- [Promemoria](Sorgenti/DOC/TA/B£AMO/WFBASE_039)
Per alcuni esempi si faccia riferimento al processi : 
 :  : DEC T(TA) P(WFA) K(ESE_014)

- **Sai quali sono i modi di definire insiemi di utenti nel workflow?**

 :  : VOC Id="SKICO500" Txt="Sai quali sono i modi di definire insiemi di utenti nel workflow?"
Non solo mediante autorizzazioni! Si vedano i casi gestiti nel membro di documentazione : 
- [Definizione delle responsabilità](Sorgenti/DOC/TA/B£AMO/WFBASE_031)

- **Sai come gestire una scelta multipla da parte di un utente all'avanzamento**

 :  : VOC Id="SKICO510" Txt="Sai come gestire una scelta multipla da parte di un utente all'avanzamento di un impegno?"
Si configura la scelta multipla sul passo in cui l'utente deve scegliere, ma bisogna anche prestare attenzione, nel seguito del processo, a considerare vincolanti per l'avanzamento solo le scelte che l'utente ha effettuato.
Si veda il seguente esempio : 
 :  : DEC T(TA) P(WFA) K(ESE_010)
