- **Sai quali sono gli obiettivi della gestione calendario?**

 :  : VOC Id="SKIA0010" Txt="Sai quali sono gli obiettivi della gestione calendario?"
Sono obiettivi diversi collegati alla disponibiltà di una risorsa e alla tipologia delle funzioni che la interrogano.
Es.
- la pianificazione necessita di conoscere i giorni lavorativi della produzione e i giorni di chiusura di terzisti e fornitori
- il carico macchine necessita di sapere la disponibilità giornaliera (ore utilizzabili) di una risorsa
- la schedulazione necessita di sapere gli orari di attività di una risorsa in un giorno
- la fatturazione necessita di conoscere i giorni di chiusura dei clienti per determinare le scadenze dei pagamenti

- **Conosci il concetto di orario lavorativo giornaliero e la tabella dove vie**

 :  : VOC Id="SKIA0020" Txt="Conosci il concetto di orario lavorativo giornaliero e la tabella dove viene gestito?"
L'orario lavorativo giornaliero rappresenta il tempo in cui una risorsa lavora in un giorno, è caratterizzato da una serie di coppie "ora/frazione inizio" - "ora/frazione fine" (la frazione può essere minuti o centesimi a seconda delle impostazioni).

I vari tipi di orario lavorativo sono definiti nella tabella OLG.

Per una informazione più completa vedi documentazione : 
- [OLG - Orari di lavoro giornalieri](Sorgenti/OG/TA/OLG)

- **Conosci il concetto di festività?**

 :  : VOC Id="SKIA0030" Txt="Conosci il concetto di festività?"
La festività è un giorno di chiusura, in questo giorno la risorsa non ha tempo disponibile.
La festività è una impostazione inserita a livello di calendario annuale della risorsa.

- **Conosci il concetto di eccezione di risorsa?**

 :  : VOC Id="SKIA0040" Txt="Conosci il concetto di eccezione di risorsa?"
L'eccezione è un giorno speciale in cui la risorsa ha un particolare tipo di orario diverso da quello standard settimanale.
Si imposta andando a inserire le eccezioni per risorsa (tipo orario diversi) in un dato periodo.

- **Conosci il concetto di eccezione di calendario?**

 :  : VOC Id="SKIA0050" Txt="Conosci il concetto di eccezione di calendario?"
Similmente all'eccezione per risorsa l'eccezione di calendario varia l'orario di lavoro in un particolare giorno dell'anno.
La differenza è che il cambiamento dell'orario è variabile in funzione della risorsa a cui si applica e dell'orario associato all'eccezione nei dati base per risorsa.

Es.
1 = Turno ridotto solo la mattina
2 = Fermo per manutenzione
3 = Fermo per inventario fisico
4 = ....

Sono possibili fino a 5 eccezioni per ogni risorsa, identificati dal numero 1,2,3,4,5 che deve essere inserito nel calendario annuale.
L'utilizzo del giorno speciale è utile solo se una giornata particolare, ad esempio l'inventario, deve avere codici orario diversi per diverse risorse ( es :  il magazzino lavora, mentre gli altri sono in ferie)

L'orario lavorativo associato ad una eccezione di una risorsa è sempre un elemento della tab. OLG.
Quando si creano i dati settimanali della risorsa si associano alla risorsa anche i 5 OLG corrispondenti alle eccezioni 1 > 5.

- **Conosci il concetto di Tipo risorsa gestita?**

 :  : VOC Id="SKIA0060" Txt="Conosci il concetto di Tipo risorsa gestita?"
Il tipo risorsa gestita rappresenta una categoria di risorse il cui comportamento, dal punto di vista dei tipi orario e delle eccezioni giornaliere  è simile.
Es. i centri di lavoro, le risorse di mautenzione, gli operatori di magazzino, i fornitori.

Il tipo risorsa gestita è codificato nella tabella TRG.

Per una informazione più completa vedi documentazione : 
- [TRG - Tipo risorsa gestita](Sorgenti/OG/TA/TRG)

- **Sai come viene determinata la disponibilità oraria e giornaliera di una ri**

 :  : VOC Id="SKIA0070" Txt="Sai come viene determinata la disponibilità oraria e giornaliera di una risorsa?"
Per ogni tipo risorsa gestita viene definito un calendario annuale in cui sono stabilite le festività (chiusure) e le eccezioni generali comuni a tutte le risorse dello stesso tipo.

Per ogni risorsa è definito un calendario settimanale dove sono impostati i vari tipi di orario giornaliero per tutti i giorni della settimana e sono anche stabiliti gli orari da associare alle 5 possibili eccezioni.

Per una risorsa si possono poi impostare delle "eccezioni per risorsa" che sono degli orari di lavoro particolari previsti per la risorsa in determinati giorni (es. fermo per manutenzione programmata).

Incrociando queste tre categorie di informazioni si può stabilire nel dettaglio la disponibilità di una risorsa alle diverse ore di ciascun giorno.

Sono possibili diversi tipi di risalita, attraverso i quali la risorsa eredita :  orari, festività ed eccezioni dai livelli superiori.

Per una informazione più completa vedi documentazione : 
- [TRG - Tipo risorsa gestita](Sorgenti/OG/TA/TRG)

- **Sai come avvengono le risalite?**

 :  : VOC Id="SKIA0080" Txt="Sai come avvengono le risalite?"
**Risalita del calendario anno**
- Calendario anno stesso tipo risorsa gestita
-- Calendario anno tipo risorsa superiore
--- Calendario anno tipo risorsa deviata

**Risalita dati settimanali risorsa**
- Dati settimanali risorsa
-- Dati settimanali risorsa collegata
--- Dati settimanali risorsa = "\*\*"

**Risalita eccezioni per periodo**
- Eccezioni risorsa
-- Eccezioni risorsa collegata
--- Eccezioni risorsa = "\*\*"

**Eccezioni di default (anno 3000)**
Se impostato in tabella, TRG nella risalita eccezioni possono essere considerate anche le eccezioni dell'anno 3000. Far riferimento all'help della tabella TRG

- **Sai come fare per associare alle macchine il calendario del CDL che le con**

 :  : VOC Id="SKIA0090" Txt="Sai come fare per associare alle macchine il calendario del CDL che le contiene?"
Nella tabella TRG delle macchine si deve impostare l'OAV per deviazione (I/04 = codice di appartenenza) e nel tipo risorsa deviata "CDL".
In questo modo per la macchina si prende il calendario del CDL a cui la macchina appartiene.

- **Sai cos'è il tipo risorsa superiore?**

 :  : VOC Id="SKIA0100" Txt="Sai cos'è il tipo risorsa superiore?"
Se impostato in tabella TRG, è il tipo risorsa a cui si risale per leggere il calendario dell'anno quando manca quello del proprio tipo risorsa.

- **Sai cos'è il tipo risorsa deviata?**

 :  : VOC Id="SKIA0110" Txt="Sai cos'è il tipo risorsa deviata?"
Se impostato in tabella TRG unitamente all'OAV risorsa deviata, è il tipo risorsa a cui si risale per leggere i dati settimanali risorsa e le eccezioni quando mancano quelle del proprio tipo risorsa.

- **Sai cos'è il calendario anno 3000?**

 :  : VOC Id="SKIA0120" Txt="Sai cos'è il calendario anno 3000?"
Il calendario dell'anno 3000 è un calendario di riferimento dove si impostano tutti i giorni di ferie e le chiusure fisse per il tipo risorsa.
Ogni volta che viene eseguita l'interrogazione di un anno, se questo manca e nella tabella TRG è impostato il flag "Calendario base", il programma lo crea automaticamente per copia dell'anno 3000 (del tipo risorsa dipendente da come è impostata la tab. TRG origine).
In questo modo non è necessario creare manualmente tutti gli anni per impostare i giorni di chiusura fissi.
Basta, interrogare un nuovo anno (il programma automaticamente lo crea per copia dal 3000) e poi, se necessario, entrare in manutenzione per impostare i giorni di chiusura specifici dell'anno appena creato.

- **Sai cos'è il tipo risorsa calendario base?**

 :  : VOC Id="SKIA0130" Txt="Sai cos'è il tipo risorsa calendario base?"
La risalita all'anno 3000 avviene a parità di tipo risorsa gestita, a meno che in tabella TRG non sia specificato in diverso tipo risorsa calendario base, se esiste, per la risalita si usa quest'ultimo.

- **Conosci il concetto di squadra?**

 :  : VOC Id="SKIA0140" Txt="Conosci il concetto di squadra?"
La squadra è una impostazione che permette di variare il numero di risorse disponibili all'interno della giornata, mentre con le altre funzioni di calendario si determina quante e quali ore del giorno la risorsa è attiva :  nel giorno sono possibili fino a 6 intervalli di orario dove indicare il numero delle risorse presenti.

Un esempio di utilizzo è come risorsa produttiva secondaria "persone" in cui è necessario conoscere il numero di operai diponibili in una certa ora di un certo giorno.

- **Sai quali sono gli archivi utilizzati?**

 :  : VOC Id="SKIA0150" Txt="Sai quali sono gli archivi utilizzati?"
Archivi utilizzati : 
- CALANN0F, dove sono presenti i calendari annuali per tipo risorsa
- CALGIO0F, dove sono presenti i dati calcolati per risorsa
- CALBAS0F, dove sono presenti i dati base per risorsa
- CALRIS0F, dove sono presenti le eccezioni per risorsa
- CALSQU0F, dove sono presenti i dati delle squadre

- **Conosci le autorizzazioni necessarie (Classe / Funzione)?**

 :  : VOC Id="SKIA0160" Txt="Conosci le autorizzazioni necessarie (Classe / Funzione)?"
Per tutte le manutenzioni la classe utilizzata è CALENDARIO.

La funzione è diversa per i vari programmi di manutenzione : 
- gestione del calendario degli anni per tipo risorsa, funzione B£DIR1 (formato guida) e B£DIR1L (formato lista)
- gestione dei dati base settimanali per risorsa, funzione B£DIR2 (formato guida) e B£DIR2L (formato lista)
- gestione delle eccezioni per risorsa, funzione B£DIR0 (formato guida) e B£DIR0L (formato lista)
- gestione delle squadre, funzione B£DIRG

