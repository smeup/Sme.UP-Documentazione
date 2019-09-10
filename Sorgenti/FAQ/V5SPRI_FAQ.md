- **E' possibile estrarre con un flusso un documento su un ente, partendo da un d**

 :  : VOC Id="10001" Txt="E' possibile estrarre con un flusso un documento su un ente, partendo da un documento intestato a un altro ente?"
 Se si intende realizzare un'attività V5 (UP V5A) con i seguenti i passi di flusso standard : 
 1. impostazione nuova testata testata (V5AT11E)
 2. selezione righe (V5AT15G)
 e come risultato si vuole ottenere, selezionando ed evadendo le righe dell'ente **ENTE1**, un documento di destinazione intestato all'**ENTE2**
 (con criteri personali di scelta di ENTE2), è necessario configurare il flusso di attività nel modo seguente : 
 1. Nel passo di creazione testata (V5AT11E), impostare a '1' la posizione 5 dei parametri aggiuntivi (creazione testata in modalità clear)
 2. Nel passo di selezione righe (V5AT15G), impostare funzione VISM e togliere il controllo compatibilità enti.

 __Dal lato utente finale__ invece occorre operare come segue : 
 1. Inserire ENTE2 sul campo ente in "creazione documento"
 2. Inserire in "campo documento origine" il numero documento dell'ENTE1
 3. Alla segnalazione di incompatibilità fra enti di origine/destinazione, premere F6=forzatura e procedere.

 L'unica conseguenza "anomala" di un'impostazione del genere è che gli enti di spedizione che verranno scritti sulle righe di destinazione
 saranno derivati dal documento origine, quindi verosimilmente legati all'ENTE1, salvo che si intervenga manualmente o automaticamente tramite la exit
 del passo di selezione righe V5AT15_xy.

- ****

 :  : VOC Id="10002" Txt=""





- **Sai cosa sono i flussi V5 di spedizione / ricevimenti?**

 :  : VOC Id="SKIA0010" Txt="Sai cosa sono i flussi V5 di spedizione / ricevimenti?"
I flussi di spedizione e ricevimenti sono insiemi di programmi elaborati in sequenza che servono fondamentalmente per derivare un documento da un altro (es. estrazione di una bolla di spedizione da un ordine di vendita) e per eseguire delle azioni aggiuntive (es. stampa DDT).
- **Sai qual'è il programma che gestisce questi flussi?**

 :  : VOC Id="SKIA0020" Txt="Sai qual'è il programma che gestisce questi flussi?"
Il V5AT10A (UP V5A).
- **Sai quali sono le tabelle di riferimento?**

 :  : VOC Id="SKIA0030" Txt="Sai quali sono le tabelle di riferimento?"
La tabella principale è la V5G con sottosettore specifico per tipo di attività (es. previsioni > ordini, spedizioni ciclo attivo, entrate ciclo passivo, ...)

Alla V5G sono associate la tabella B£H che gestisce tutti i flussi e la tabella B£J con sottosettore specifico che contiene le varie azioni elementari.

Per una informazione più completa vedi : 
- [V5G - Tipo attivita](Sorgenti/OG/TA/V5G)
- [B£H - Gruppi di azioni di tab B£J](Sorgenti/OG/TA/B£H)
- [B£J - Gruppi di azioni](Sorgenti/OG/TA/B£J)
- **Sai come trovare programmi funzione/metodo da utilizzare nelle azioni dei **

 :  : VOC Id="SKIA0040" Txt="Sai come trovare programmi funzione/metodo da utilizzare nelle azioni dei flussi V5 SPRI?"
Utilizzando le "Funzioni applicative" (UP AZI) dell'applicazione e selezionando V5 - V5ATTI si apre la lista dei programmi che possono essere utilizzati nei flussi.
L'utility permette anche di creare un nuovo elemento di B£J.
- **Sai come passare ai flussi la lista dei plant su cui agire e la rispettiva**

 :  : VOC Id="SKIA0050" Txt="Sai come passare ai flussi la lista dei plant su cui agire e la rispettiva disponibilità?"
In tabella V5G si inserisce il gruppo fonti che determina sia i plant che la disponibilità
- **Sai come fissare nel flusso un ente?**

 :  : VOC Id="SKIA0060" Txt="Sai come fissare nel flusso un ente?"
In tabella V5G si inseriscono tipo/codice ente
- **Sai in quali modi si può condizionare il tipo riga di arrivo?**

 :  : VOC Id="SKIA0080" Txt="Sai in quali modi si può condizionare il tipo riga di arrivo?"
In tabella V5G il campo "Eredità tipo riga" fissa le regole con cui viene determinato il tipo riga del documento di destinazione (da tipo riga destinazione della V5B origine, da tipo riga assunto della V5A destinazione)
- **Sai come limitare il flusso ad una sola elaborazione?**

 :  : VOC Id="SKIA0090" Txt="Sai come limitare il flusso ad una sola elaborazione?"
In tabella V5G esiste il campo "Esegui 1 solo flusso"
- **Sai a cosa serve il programma di abbandono flusso (V5AT11R)?**

 :  : VOC Id="SKIA0100" Txt="Sai a cosa serve il programma di abbandono flusso (V5AT11R)?"
Nel caso di interruzione della catena dei programmi del flusso il programma V5AT11R serve per resettare la situazione all'inizio.
- **Conosci l'utilizzo del set'n play V5AT10A (o UP V5A)?**

 :  : VOC Id="SKIA0110" Txt="Conosci l'utilizzo del set'n play V5AT10A (o UP V5A)?"
Con il set'n play si possono visualizzare e gestire : 
* l'emento della tabella V5Gxx
* l'elemento della tabella B£H
* gli elementi della tabella B£Jxx
* leggere gli help associati alle azioni del flusso (elementi di B£Jxx)
- **Sai come leggere l'help delle azioni B£J richiamate in UP V5A?**

 :  : VOC Id="SKIA0120" Txt="Sai come leggere l'help delle azioni B£J richiamate in UP V5A?"
Con l'utility UP V5A funzione 1, metodo 3, opzione "H" sulle azioni
