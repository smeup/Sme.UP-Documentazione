# TRACE

## OBIETTIVI
 Gestire il trace di elaborazioni centralizzando le operazioni di calcolo della durata delle
 elaborazioni e la relativa memorizzazione. Questa API utilizza la struttura QQ per avere
 il minimo indispensabile dell'infrastruttura Sme.UP al fine di evitare possibili allocazioni
 o errori di ricorsione.

**Si ricorda che come tutte le nuove routine i parametri di INPUT sono cancellati ad ogni
**esecuzione e che sono presenti 2 ds, una di input e una di output.

## UTILIZZO DELL'API
 L'API è utilizzata per reperire il tempo iniziale dell'elaborazione, calcolare la durata
 alla fine dell'elaborazione, per infine memorizzarla nel JALOGT0F.


## FUNZIONI E METODI

### INI.CAL   Inizializzazione con calcolo del tempo iniziale
**Restituisce l'istante attuale in formato timestamp UTC, tempo coordinato universale, che
**corrisponde al fuso orario di greenwich, con accuratezza al microsecondo (milionesimo di
**secondo).

### DUR.CAL   Calcola la durata rispetto al tempo passato in input
**Restituisce la durata tra il timestamp UTC passato in input ed il timestamp attuale.

### TRC.WRI   Memorizza la traccia
La memorizzaione della traccia avviene sul file B£LQ060F, la durata è memorizzata nel campo
Q6TTOT, la descrizione della traccia nel campo Q6LIBE (Max 256 caratteri).

### TEX.WRI   Memorizza la traccia di esecuzione
La memorizzaione della traccia avviene sul file B£LQ060F, a differenza della traccia in questo
log verranno totalizzati sullo stesso record le sequenti informazioni : 
Numero di esecuzioni Q6NUME
Tempo Minimo         Q6TMIN
Tempo Massimo        Q6TMAX
Tempo Medio          Q6TMED
Tempo totale         Q6TTOT
Raggruppato per Q6LIBE.
Verrà sempre generato un totale, identificato dal campo Q6LIBE vuoto.

### TIM.WRI   Memorizza la traccia di un timestamp
La memorizzaione della traccia avviene sul file B£LQ060F, a differenza della traccia in questo
log non c'è una durata ma solo il timestamp

## Annotazioni
Questa API è gestita dal pre-compilatore attraverso le annotazioni : 

### Trace
Sono state attivate le seguenti annotazioni : 
 :  : PAR
@StartTrace
@StopTrace

Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione della traccia. L'utilizzo della traccia deve essere fatto quando si vuole inserire un monitor delle performance.
L'attivazione della traccia avviene durante la compilazione, attraverso apposito parametro, oppure attraverso l'opzione \*TRACE da impostare nei parametri di compilazione (COP\*), in questa maniera la traccia è aggiunta solo quando è necessario monitoriuzzare le performance.
E' comunque possibile accenderla o spegnerla tramite l'apposito flag in JA1.

Il parametro della annotazione **@StartTrace** è il momento **M(<NomeMomento>)**
Il nome momento viene convertito in una variabile che contiene il tempo di inizio della traccia, per questo motivo non inserire spazi o cartteri speciali nel nome.

I parametri della annotazione **@StopTrace** sono il momento **M(<NomeMomento>)** e il testo **T(<Testo>)**.
Il nome momento deve essere lo stesso utilizzato nello @StartTrace, da cui deriva il tempo trascorso tra l'inizio e la chiusura della traccia.
Il testo non deve contenere apici singoli e si possono aggiungere variabili attraverso la seguente nomenlcatura
**e**=e commerciale
**eA(<Variabile di Testo>)**
**eN(<Variabile Numeica>)**

Il risultato è memorizzato nel file B£LQ06 con tipo record TRC.

### Trace di esecuzione
Sono state attivate le seguenti annotazioni : 
 :  : PAR
@TrcExe

Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione della traccia di esecuzione. In assenza di una definizione verranno tracciati tutti i campi ricevuti in ingresso. Per una corretta attribuzione del valore numerico, lo stesso deve essere definito sulla parm, in assenza di definizione sara assunto come carattere.
L'attivazione della traccia avviene durante la compilazione, attraverso apposito parametro, oppure attraverso l'opzione \*TRCEXE da impostare nei parametri di compilazione (COP\*), in questa maniera la traccia è aggiunta solo quando è necessario monitoriuzzare le performance.
E' comunque possibile accenderla o spegnerla tramite l'apposito flag in JA1.

I parametri della annotazione **@TrcExee** sono i parametri che si vogliono tracciare **<Testo>**.
Il testo non deve contenere apici singoli e si possono aggiungere variabili attraverso la seguente nomenlcatura
**e**=e commerciale
**eA(<Variabile di Testo>)**
**eN(<Variabile Numeica>)**

Il risultato è memorizzato nel file B£LQ06 con tipo record TEX o TED.
TEX sono i livelli di totale mentre TED sono i livelli di dettaglio

### Trace di tempo
Sono state attivate le seguenti annotazioni : 
 :  : PAR
@TraceTime

Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione della traccia di tempo.
L'attivazione del log avviene sempre, deve essere lo sviluppatore a condizionare l'annotazione.
E' comunque possibile accenderla o spegnerla globalmente tramite l'apposito flag in JA1.

I parametri della annotazione **@TraceTime** sono i parametri che si vogliono tracciare **<Testo>**.
Il testo non deve contenere apici singoli e si possono aggiungere variabili attraverso la seguente nomenlcatura
**e**=e commerciale
**eA(<Variabile di Testo>)**
**eN(<Variabile Numeica>)**

Il risultato è memorizzato nel file B£LQ06 con tipo record TIM.

### Log
Sono state attivate le seguenti annotazioni : 
 :  : PAR
@StartLog
@StopLog

Attraverso queste annotazioni, gestite in RPG come commenti, è possibile attivare la registrazione dei log. L'utilizzo del log deve essere fatto quando si vuole monitorizzare in modalità dettagliata l'esecuzione del servizio.
L'attivazione del log avviene sempre, deve essere lo sviluppatore a condizionare l'annotazione.
E' comunque possibile accenderla o spegnerla globalmente tramite l'apposito flag in JA1.

Il parametro della annotazione **@StartLog** è il momento **M(<NomeMomento>)**
Il nome momento viene convertito in una variabile che contiene il tempo di inizio della traccia, per questo motivo non inserire spazi o cartteri speciali nel nome.

I parametri della annotazione **@StopLog** sono i seguenti : 
-   **M(**<NomeMomento>**)**
-   **LIBE(**<Testo>**)**
-   **ORIG(**<Origine>**)**
-   **WEFU(**<funzione>**)**
-   **WEME(**<Metodo>**)**
-   **TPO1(**<1 oggetto>**)**
-   **CDO1(**<1 istanza>**)**
-   **TPO2(**<2 oggetto>**)**
-   **CDO2(**<2 istanza>**)**
-   **TPO3(**<3 oggetto>**)**
-   **CDO3(**<3 istanza>**)**
-   **TPO4(**<4 oggetto>**)**
-   **CDO4(**<4 istanza>**)**
-   **TPO5(**<5 oggetto>**)**
-   **CDO5(**<5 istanza>**)**
Il nome momento deve essere lo stesso utilizzato nello @StartLog, da cui deriva il tempo trascorso tra l'inizio e la chiusura della traccia.
Se non definita un'origine verrà assunto '???'.
Il testo non deve contenere apici singoli e si possono aggiungere variabili attraverso la seguente nomenlcatura
**e**=e commerciale
**eA(<Variabile di Testo>)**
**eN(<Variabile Numeica>)**

Il risultato è memorizzato nel file JALOGT con le informazioni ricevute

## Attivazione
L'attivazione della traccia è attivabile tramite la tabella JA1. Fare riferimento alla
stessa per la relativa documentazione.
- [JA1 - Parametri java](Sorgenti/OG/TA/JA1)
