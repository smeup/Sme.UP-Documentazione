- **Sai qual'è la tabella principale di impostazione dei movimenti?**

 :  : VOC Id="SKIA0010" Txt="Sai qual'è la tabella principale di impostazione dei movimenti?"
La tabella GMC dove sono definite tutte le causali di movimentazione.
Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)

- **Conosci gli archivi di riferimento?**

 :  : VOC Id="SKIA0020" Txt="Conosci gli archivi di riferimento?"
Il file GMMOVI0F dove sono registrati tutti i movimenti di magazzino.
Il file GMMOAR0F, parallelo al GMMOVI, dove per ciascun movimento abbiamo area e tipo giacenza (nota :  un una delle ultime revisioni del tracciato di GMMOVI area e tipo giacenza sono state aggiunte anche in GMMOVI). Se si utilizzano le giacenze secondarie, il GMMOAR mantiene traccia anche dei movimenti sulle giacenze secondarie.

Anche se non si usano le giacenze secondarie, il GMMOAR è indispensabile e deve essere congruente rispetto al GMMOVI perchè viene usato nelle ricostruzioni giacenza alla data (£GMC - £GMD) :  non eseguire mai cancellazioni / modifica di record del GMMOVI con funzioni SQL, usare solo le funzioni standard GM.
Esiste una funzione di rifasatura del GMMOAR a partire dal GMMOVI (progamma B£RF01T).

- **Conosci i vari modi con cui si possono inserire i movimenti di magazzino?**

 :  : VOC Id="SKIA0030" Txt="Conosci i vari modi con cui si possono inserire i movimenti di magazzino?"
Esistono : 
- movimenti manuali che possono essere inseriti direttamente dall'operatore con una apposita funzione.
- movimenti manuali che possono essere inseriti dalla interrogazione giacenze
- movimenti automatici dal collegamento di documenti del ciclo esterno (es. bolle di vendita)
- movimenti automatici dalla produzione (versamento da ordine, prelievo backflush, prelievo alla fase)
- movimenti automatici da esito di collaudo (qualità in accettazione)
- movimenti automatici da esecuzione di richieste movimentazione
- movimenti automatici da registrazione attività di produzione

- **Sai cos'è la giacenza secondaria?**

 :  : VOC Id="SKIA0040" Txt="Sai cos'è la giacenza secondaria?"
La giacenza secondaria è una giacenza che si movimenta in parallelo alla giacenza principale. Si una la gaicneza secondaria nei casi in cui la stessa attività elementare ha effetto su più giacenze, ad esempio nel caso in cui si voglia tener conto della giacenza in diverse unità di misura, oppure tenere più livelli di sintesi (giacenza in dettaglio per ubicazione e giacenza a totale di articolo)

- **Sai come si movimenta la giacenza secondaria?**

 :  : VOC Id="SKIA0050" Txt="Sai come si movimenta la giacenza secondaria?"
Impostando la "Causale collegata" nella tabella GMC

- **Sai che impostazione serve per inserire movimenti manuali?**

 :  : VOC Id="SKIA0060" Txt="Sai che impostazione serve per inserire movimenti manuali?"
I movimenti manuali vengono lanciati con il programma B£GFP10.
Deve esistere un elemento della tabella B£H che richiama delle funzioni B£J specifiche.
Nelle funzioni B£J devono essere richiamati i programmi : 
- GMMV01I, per lanciare __movimentazioni ad 1 causale__ (se nei parametri aggiuntivi della B£J si inserisce anche la causale allora si esegue un movimento con quella specifica causale, altrimenti il programma la chiede);
- GMMV02I, per lanciare __movimentazioni a 2 causali__, tipicamente trasferimenti di giacenza dove una causale esegue uno scarico e l'altra un carico (se nei parametri aggiuntivi della B£J si inseriscono anche le causali allora si esegue un movimento per ogni specifica causale, altrimenti il programma le chiede);
Nota; nella movimentazione a 2 causali si consiglia di inserire nella funzione della B£J anche il programma GMMV06G che permette un data entry più facilitato.
- GMMV50I, per lanciare __movimentazioni da distinta base__, (con o senza versamento del prodotto).

Per una documentazione completa : 
- [B£H - Gruppi di azioni di tab B£J](Sorgenti/OG/TA/B£H)
- [B£J - Gruppi di azioni](Sorgenti/OG/TA/B£J)

- **Sai che impostazione serve per inserire movimenti manuali da interrogazion**

 :  : VOC Id="SKIA0070" Txt="Sai che impostazione serve per inserire movimenti manuali da interrogazione giacenze?"
Da interrogazione giacenze possono essere lanciati movimenti di rettifica, in questo caso è necessario che ci siano delle causali di movimentazione (tab. GMC) di tipo movimento = "Rettifica inventario" compatibili con il record di giacenza (area/tipo giacenza).
Si possono anche lanciare altre movimentazioni a 1 o 2 causali, per fare questo nella tabella ad elemento singolo GM1 si deve inserire l'elemento di B£H opportuno nel campo "Gruppo azioni movimenti magazzino".

Per una documentazione completa : 
- [GM1 - Parametri gestione magazzini](Sorgenti/OG/TA/GM1)

- **Sai che impostazione serve per inserire movimenti  automatici da documenti**

 :  : VOC Id="SKIA0080" Txt="Sai che impostazione serve per inserire movimenti  automatici da documenti V5?"
Nelle tabelle tipo riga (V5B) devono essere inserite le causali di movimentazione.

Per una documentazione completa : 
- [V5B - Tipo riga](Sorgenti/OG/TA/V5B)

- **Sai che impostazione serve per inserire movimenti  automatici da ordini pr**

 :  : VOC Id="SKIA0090" Txt="Sai che impostazione serve per inserire movimenti  automatici da ordini produzione?"
Per il versamento da ordine produzione devono essere compilati opportunamente i parametri logistici di versamento (categoria £P2, con risalita a 1P2 e 2P2)

Per il prelievo dei componenti (alla fase o backflush) devono essere compilate opportunamente le tabelle degli impegni materiali (P5I)

Per una documentazione completa : 
- [&-x2a; P5I - Tipo impegno materiali](Sorgenti/OG/TA/P5I)

- **Sai che impostazione serve per inserire movimenti  automatici da richieste**

 :  : VOC Id="SKIA0100" Txt="Sai che impostazione serve per inserire movimenti  automatici da richieste movimentazione?"
Deve essere compilata opportunamente la tabella del tipo riga di movimentazione (GMZ)

Per una documentazione completa : 
- [GMZ - Tipo riga movimentazione](Sorgenti/OG/TA/GMZ)

- **Sai che impostazione serve per inserire movimenti  automatici da attività **

 :  : VOC Id="SKIA0110" Txt="Sai che impostazione serve per inserire movimenti  automatici da attività di produzione?"
Deve essere compilata opportunamente i flag "Scarico impegni" e "Carico assieme" nella tabella delle causali attività produzione (P5C)

Per una documentazione completa : 
- [&-x2a; P5C - Causali attivita  produttive](Sorgenti/OG/TA/P5C)

- **Sai che impostazione serve per inserire movimenti  automatici da esito di **

 :  : VOC Id="SKIA0120" Txt="Sai che impostazione serve per inserire movimenti  automatici da esito di collaudo?"
Devono essere compilate opportunamente le tabelle di movimentazione per tipo lotto (CRP) e la movimentazione deve essere attivata nella tabella a elemento unico CQ1.

Per una documentazione completa : 
- [CRP - Integrazione Q9000 con magazzino](Sorgenti/OG/TA/CRP)
- [CQ1 - Personal.controllo qualita  1](Sorgenti/OG/TA/CQ1)

- **Sai autorizzare singoli tipi movimento?**

 :  : VOC Id="SKIA0130" Txt="Sai autorizzare singoli tipi movimento?"
Nella tabella GMC c'è il campo "Gruppo autorizzazione" che deve essere compilato con un valore da 0 a 9.
Le autorizzazioni possono essere date con classe = ABILITA e funzione = MOV-MAGx (x è il gruppo autorizzazione).

__Suggerimento__, se ci sono distinzioni tra causali "automatiche" utilizzate nelle transazioni del gestionale (es. versamento da ordine produzione, collegamento bolla di vendita, ...) e causali "manuali" lanciate manualmente dall'operatore è consigliabile dare un gruppo autorizzazione specifico (es. 9) alle causali manuali e non autorizzare nessun utente al gruppo 9, in questo modo abbiamo la sicurezza che queste causali siano usate solo dalle transazioni del gestionale.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)

- **Sai come modificare il formato video di input del movimento?**

 :  : VOC Id="SKIA0140" Txt="Sai come modificare il formato video di input del movimento?"
Nella tabella GMC c'è il campo "Forma di presentazione" che è un elemento della tabella B£Q dove viene impostato il programma specifico di visualizzazione.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)
- [B£Q - Forme di rappresentazione](Sorgenti/OG/TA/B£Q)

- **Sai usare la scheda movimenti?**

 :  : VOC Id="SKIA0150" Txt="Sai usare la scheda movimenti?"

- **Sai impostare una causale in modo che la variazione qtà allocata avvenga s**

 :  : VOC Id="SKIA0160" Txt="Sai impostare una causale in modo che la variazione qtà allocata avvenga solo se la causale è lanciata con R.M.?"
Nella tabella GMC c'è il campo "Applica solo se IDDM" che controlla questa funzionalità.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)

- **Sai come impostare la causale in modo che la movimentazione avvenga con le**

 :  : VOC Id="SKIA0170" Txt="Sai come impostare la causale in modo che la movimentazione avvenga con le qtà in unità di misura alternativa?"
Nella tabella GMC c'è il campo "Tipo quantità" che va messo = A.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)

- **Sai come condizionare il comportamento della causale di movimentazione sot**

 :  : VOC Id="SKIA0180" Txt="Sai come condizionare il comportamento della causale di movimentazione sotto determinate condizioni?"
Nella tabella GMC c'è il campo "Programma specifico" dove può essere inserito un programma di "exit" (esiste un sorgente di esempio :  GMTR00X_ES ).

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)

- **Sai come modificare o cancellare movimenti già inseriti in precedenza?**

 :  : VOC Id="SKIA0190" Txt="Sai come modificare o cancellare movimenti già inseriti in precedenza?"
Nel menù della movimentazione esiste la funzione di "Revisione movimenti", simile all'interrogazione e con la quale si può andare in manutenzione di un movimento di magazzino.

__Attenzione__, la manutenzione è ammessa solo se per la causale in questione esiste una forma di presentazione valida.

- **Sai come fare in modo che la modifica di un movimento si traduca in due nu**

 :  : VOC Id="SKIA0200" Txt="Sai come fare in modo che la modifica di un movimento si traduca in due nuovi movimenti (uno uguale all'originale con qtà negativa ed uno con la nuova quantità)?"
Nella tabella ad elemento unico GM1 c'è il campo "Revisione movimenti a storno" che se impostato determina questo comportamento.

Per una documentazione completa : 
- [GM1 - Parametri gestione magazzini](Sorgenti/OG/TA/GM1)

- **Se lanciando l'interrogazione giacenze ti esce una segnalazione che ci son**

 :  : VOC Id="SKIA0210" Txt="Se lanciando l'interrogazione giacenze ti esce una segnalazione che ci sono delle transazioni non applicate sai come agire?"
Questa è una forma di controllo sull'esistenza di transazioni in sospeso nell'archivio GMTRAN0F, che viene attivata da un flag nella tabella GM1 di impostazione generale dell'applicazione GM.
Bisogna lanciare la funzione "Gestione transazioni" ed analizzare le transazioni in sospeso che vengono presentate.

- **Sai come controllare la codifca delle causali di magazzino?**

 :  : VOC Id="SKIA0220" Txt="Sai come controllare la codifca delle causali di magazzino?"
La convenzione di codifica delle causali di magazzino prevede che il codice sia del tipo AAXX, dove AA è l'area e XX è il tipo di movimentazione codificato in tab. GM*CM.
Se il tab. GM1 il campo "Controllo inserimento GMC" è impostato a 1 si attiva il controllo formale.

Per una documentazione completa : 
- [GM1 - Parametri gestione magazzini](Sorgenti/OG/TA/GM1)

- **Il numeratore movimenti è obbligatorio e fornisce la chiave univoca del mo**

 :  : VOC Id="SKIA0230" Txt="Il numeratore movimenti è obbligatorio e fornisce la chiave univoca del movimento (N.ro transazione), sai dove deve essere impostato?"
Nel campo "Numeratore movimenti" della tab. GM1.

Per una documentazione completa : 
- [GM1 - Parametri gestione magazzini](Sorgenti/OG/TA/GM1)
- [CRN - Numeratori](Sorgenti/OG/TA/CRN)

- **Sai come attivare una segnalazione quando la movimentazione manda in negat**

 :  : VOC Id="SKIA0240" Txt="Sai come attivare una segnalazione quando la movimentazione manda in negativo una giacenza?"
In tabella GM1 si imposta il campo "Tipo evento segnalazione negativi".

Per una documentazione completa : 
- [GM1 - Parametri gestione magazzini](Sorgenti/OG/TA/GM1)
- [P5D - Tipo evento](Sorgenti/OG/TA/P5D)

- **Sai come usare impostare le causali di movimentazione in modo che si possa**

 :  : VOC Id="SKIA0250" Txt="Sai come usare impostare le causali di movimentazione in modo che si possano utilizzare le stesse sia nelle richieste di movimentzione che nei movimenti manuali anche se le causali movimentano sia giacenza che allocato o atteso?"
Nella tabella GMC c'è il campo "Applica solo se IDDM" che, se impostato e sono presenti le azioni (+ o -) sulla qtà allocata e/o sulla qtà attesa, esegue le azioni in questione solo se la causale è stata lanciata da un richiesta di movimentazione.

Per una documentazione completa : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)
