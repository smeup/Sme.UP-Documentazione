- \*\*Salto pagina\*\*

 :  : VOC Id="NPG" Txt="Salto pagina"
Sta ad indicare l'esecuzione di un salto pagina.

- \*\*Include file di schema\*\*

 :  : VOC Id="INC" Txt="Include file di schema"
Sta ad identificare l'include di un file di schema, per effettuare la sovrapposizione dell'output con un file PDF che rappresenta il modulo elettronico.

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|INC |
| Posiz. 11|Pagina da selezionare nel PDF multipagina |
| Posiz. 24|Nome del file del file da includere (path completo) |
| 

Dalla posizione 24 in poi va indicato il path del file da includere che verrà utilizzato come overlay di pagina, nel caso di file con estensione .pdf, dalla versione del 1/12/2004, verrà assunto interamente tale file come overlay. Nel caso di un PDF multipagina verranno scandite tutte le pagine ed aggiunte al documento. Se si fa riferimento ad un PDF multipagine è possibile utilizzare una specifica pagina di quest'ultimo indicando alla posizione 11;

__Esempio__
 :  : >INC........1............/Smedoc/Moduli/Fattura.pdf

- \*\*Importazione di un immagine\*\*

 :  : VOC Id="PAG" Txt="Importazione di un immagine"
Sta ad indicare la specifica per importare un'iimagine.

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|PAG |
| Posiz. 24|coordinate (assolute nel foglio) StartX;StartY;EndX;EndY ed a seguire nome file immagine da includere |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo in cui verrà inserita l'immagine nel documento PDF (il separatore delle coordinate, nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.

__Esempio__
>PAG.....................18;796;577;817;\\192.168.1.201\img\AZ\01.JPG

- \*\*Riga di testo\*\*

 :  : VOC Id="ROW" Txt="Riga di testo"
Sta ad indicare la definizione di una riga ed il testo in essa contenuto.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|ROW |
| Posiz. 3| Tipo Font |
| Posiz. 4| Dimensione Font |
| Posiz. 5| Stile Font |
| Posiz. 6| Colore Font |
| Posiz. 7| Altezza riga |
| Posiz. 8| Salta questa riga |
| Posiz. 9| Colore sfondo |
| Posiz. 10| Colore bordi |
| Posiz. 24|Testo della riga |
| 

E' possibile modificare inline le specifiche grafiche della riga, vale a dire modificare il tipo font, il colore, la dimensione, etc ad un certo punto della riga. Si può fare ciò inserendo nella parte racchiusa fra [[ e ]] il testo di cui modificare lo stile separato dalla sezione di definizione dello stile da un punto (.) (es. :  ROWC7AA8?JB              Testo iniziale riga [[ROWEF-Dd?JB.Testo secondo stile]]  ritorno allo stile iniziale [[ROWC5AM6?JB.Testo terzo stile]] ancora stile iniziale [[ROWCeCAf?JD.Testo quarto stile]]) .
La Posiz. 8 può servire (assegnandogli il valore F) per omettere lo spaziatore di default di quattro carattere che viene premesso alla riga, rinunciando a questo offset di default, il testo verrà posizionato a partire dal bordo del foglio.

__Esempio__
>ROWCA-AC?BA.............Testo della riga

- \*\*Rettangolo\*\*

 :  : VOC Id="BOX" Txt="Rettangolo"
Sta ad indicare la definizione di un rettangolo (BOX appunto) e l'eventuale etichetta in esso contenuto.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|BOX |
| Posiz. 3|Tipo Font |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|Salta questa riga |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY;EndX;EndY ed a seguire il testo da inserire nel box |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e, opzionalmente, il testo dell'etichetta (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.

__Esempio__
>BOXCA-AC?BA...........333;679;571;690;Testo nel box

- \*\*Rettangolo con angoli arrotondati\*\*

 :  : VOC Id="ROX" Txt="Rettangolo con angoli arrotondati"
Sta ad indicare la definizione di un rettangolo con gli angoli arrotondati (Round bOX appunto) e l'eventuale etichetta in esso contenuto.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|ROX |
| Posiz. 3|Tipo Font |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|Salta questa riga |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY;EndX;EndY ed a seguire il testo da inserire nel box |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e, opzionalmente, il testo dell'etichetta (il separatore delle coordinate) nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.
Per una questione di raggio di curvatura degli angoli le dimensioni devono essere ambedue superiori a 8 unità, quindi EndX-StartX>8 e EndY-StartY>8.

__Esempio__
 :  : >ROXCA-AC?BA...........333;679;571;690;Testo nel box ad angoli arrotondati

- \*\*Testo racchiuso in un rettangolo\*\*

 :  : VOC Id="BTX" Txt="Testo racchiuso in un rettangolo"
Sta ad indicare la definizione di testo racchiuso in un rettangolo.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|BTX |
| Posiz. 3|Tipo Font |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|Salta questa riga |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY;EndX;EndY ed a seguire il testo da inserire nel box |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e che racchiude il testo indicato che viene indicato successivamente alle coordinate.

__Esempio__
>BTXHB-AC BB.............18;752;186;766;Testo nel box

- \*\*Testo racchiuso in un rettangolo con angoli arrotondati\*\*

 :  : VOC Id="RTX" Txt="Testo racchiuso in un rettangolo con angoli arrotondati"
Sta ad indicare la definizione di testo racchiuso in un rettangolo con angoli arrotondati.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|RTX |
| Posiz. 3|Tipo Font |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|Salta questa riga |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY;EndX;EndY ed a seguire il testo da inserire nel box |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e che racchiude il testo indicato che viene indicato successivamente alle coordinate.

__Esempio__
>RTXHB-AC BB.............18;752;186;766;Testo nel box

- \*\*Riga diagonale\*\*

 :  : VOC Id="LIN" Txt="Riga diagonale"
Sta ad indicare la definizione di una riga diagonale.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|LIN |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY;EndX;EndY partenza ed arrivo della riga |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che identificano i punti di partenza e di arrivo della riga da inserire nel documento PDF.

__Esempio__
>LIN.....................18;752;186;752

- \*\*Testo libero\*\*

 :  : VOC Id="TXT" Txt="Testo libero"
Sta ad indicare la definizione di un testo libero da inserire ovunque del documento PDF.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|TXT |
| Posiz. 3|Tipo Font |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|Salta questa riga |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| Posiz. 24|Coordinate (assolute nel foglio) StartX;StartY ed a seguire il testo da inserire |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY; che definiscono il punto di inserimento del testo nel documento PDF (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre

__Esempio__
>TXTCA-AC?BA.............18;752;186;752;Testo libero

- \*\*Barcode\*\*

 :  : VOC Id="BCD" Txt="Barcode"
Sta ad indicare la definizione di un'immagine Barcode da inserire nel PDF.
Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito).

__Formato__

| - \*\*Cod.\*\*


| .COL Txt="Cod." Lun="0" A="L" |
| ---|----|
| - \*\*Descr.\*\*


| .COL Txt="Descr." Lun="0" LunAut="1" |
| Posiz. 0|BCD |
| Posiz. 3|Tipo Barcode |
| Posiz. 4|Dimensione Font |
| Posiz. 5|Stile Font |
| Posiz. 6|Colore Font |
| Posiz. 7|Altezza riga |
| Posiz. 8|R per ruotare di 90° il barcode |
| Posiz. 9|Colore sfondo |
| Posiz. 10|Colore bordi |
| 

Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo che conterrà il barcode da inserire nel documento PDF (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.
__Esempio : __
Per un barcode semplice : 
>BCDCC-AC?BA.............130,340,200,420,9780201615883
Per un Barcode ruotato : 
>BCDCCRACRBA.............230,140,330,320,9780201615883

**Attenzione : **Il valore che viene passato al barcode deve essere compatibile con il tipo di barcode che si vuole visualizzare, quindi per l'EAN13 è prevista una stringa alfanumerica di 13 caratteri, per l'UPCA una stringa alfanumerica di 12 caratteri, etc.. Per maggiori informazioni sulla sintassi dei vari codici barcode, si rimanda a documentazione specializzata.
E' inseribile un barcode in una riga di tipo ROW con lo stesso meccanismo con cui si cambia lo stile inline (vedere spiegazione nella sezione relativa alla specifica ROW) :  quindi con la specifica [[BCDC5AM6?JB.9780201615883]] inserita in un punto di una riga di tipo ROW si ottiene il barcode nella riga di testo e, venendo inserito direttamente nella riga, non vanno espresse le coordinate assolute del foglio per il posizionamento.
Nel caso del barcode la posizione che gestisce il Tipo Font (posiz. 3) è utilizzata per identificare la codifica del barcode (CODE39, EAN13, UPC, etc.). Vedere alle sezione TIPO BARCODE i valori da utilizzare per utilizzare per visualizzare i vari tipi di barcode.

- \*\*Definizione colori personalizzati\*\*

 :  : VOC Id="RGB" Txt="Definizione colori personalizzati"
Permette di specificare dei colori personalizzati da utilizzare nel documento che si vuole generare. I colori saranno utilizzabili dal momento in cui vengono definiti in avavnti nel documento che si vuole generare, quindi è consigliabile definirli ad inizio documento. Se dovessero essere ridefiniti, la modifica avrà luogo dal momento della loro ridefinizione in avanti.

__Formato ed esempio__
La sintassi è la seguente : 
>RGBTR225G067B118

Dal momento della sua definizione sarà disponibile, oltre ai colori standard, il colore utilizzabile con l'indicatore T di valore (nella codifica RGB) :  255, 067, 118
Qualsiasi riga di specifica ha due possibilità per essere ignorata dal parser, la prima utilizzando il simbolo X per specificare il flag Posiz.8, la seconda è commentando la riga mettendo in prima posizione il simbolo - o ; .

