# OBIETTIVO
Gestire lo SmeUp hash degli oggetti lunghi.

# FUNZIONI E METODI

## LET - Lettura Hash
Legge l'hash richiesto e restituisce l'oggetto lungo corrispondente.

## DEL - Elimina Hash
Cancella l'hash richiesto.

## CHG - Modifica descrizione dell'Hash
Modifica la descrizione dell'Hash richiesto.

## WRI - Scrittura Hash
Riceve il tipo origine, il codice origine e la descrizione dell'hash e crea un identificativo univoco dato dall'insieme del tipo origine e del codice origine dell'oggetto lungo.
La funzione può essere eseguita anche più volte; se la scrittura verifica l'esistenza dell'hash e la sua compatibilita (stesso oggetto già inserito) viene ritornato l'hash generato altrimenti ne verrà segnalata l'incompatibilità (hash duplicato).
Una volta generato l'hash questo non può essere ne cancellato ne modificato.

## SCA - Scansione
La scansione viene fatta solo per codice hash.
I metodi abilitati sono : 
SL - Posizionati
SG - Posizionati dopo
RD - Leggi successivo
RP - Leggi precedente

## SIM - Simulazione
La simulazione viene eseguita per verificare che l'insieme passato non generi hash duplicati.
I metodi abilitati sono : 
INZ - Inizializza
HSH - Aggiunge hash
END - Chiude
POS - Legge 1° hash simulazione
LET - Legge hash successivo
