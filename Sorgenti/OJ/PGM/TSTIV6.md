# OBIETTIVO
L'obiettivo della £IV6 è poter gestire in Sme.UP ERP degli oggetti il cui codice è più lungo di 15 caratteri tramite un hash univoco che ne consenta quindi la gestione come un normale codice oggetto (ad esempio salvataggio negli archivi, riferimento nei parametri ecc.)

# FUNZIONI E METODI
##     - Ricerca, controllo, lettura
Esegue le funzioni di ricerca, controllo e lettura dell'oggetto lungo a partire dal suo codice hash.

## LET - Lettura
Legge l'oggetto lungo a partire dal suo codice hash

## DEL - Elimina Hash
Cancella l'hash richiesto.

## CHG - Modifica descrizione dell'Hash
Modifica la descrizione dell'Hash richiesto.

## WRI - Scrittura
Riceve il tipo origine, il codice origine e la descrizione e crea un identificativo univoco dato dall'insieme del tipo origine e del codice origine dell'oggetto lungo.
La funzione può essere eseguita anche più volte; se la scrittura verifica l'esistenza dell'hash e la sua compatibilita (stesso oggetto già inserito) viene ritornato l'hash generato altrimenti ne verrà segnalata l'incompatibilità (hash duplicato).

## SCA - Scansione
La scansione viene fatta solo per codice hash.
I metodi abilitati sono : 
-  **SL** - Posizionati
-  **SG** - Posizionati dopo
-  **RD**- Leggi successivo
-  **RP** - Leggi precedente

