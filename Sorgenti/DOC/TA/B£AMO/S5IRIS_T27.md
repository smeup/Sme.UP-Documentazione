
# Generalità
I sistemi multipallet, che svolgono lavorazioni meccaniche con asportazione di truciolo, sono caratterizzati dall'essere dotati di supporti portapezzi di forma cubica (nel seguito pallet) su cui si fissano gli oggetti da lavorare, e dall'avere più postazioni sulle quali caricare i pallet stessi.
In questo modo, mentre viene lavorato un pallet, contemporaneamente vengono caricati e scaricati quelli delle altre postazioni.
Il pallet può montare uno o più articoli (le sue caratteristiche principali sono l'elenco dei codici e la loro quantità, oltre al tempo totale di lavoro, che è indipendente dalla presenza degli articoli in tutte le postazioni).

Fisicamente la lavorazione avviene nel seguente modo : 

1. si carica un pallet con gli articoli opportuni
2. lo si monta in macchina su di una postazione
3. la macchina lo lavora
4. contemporaneamente si carica un pallet e lo si monta sull'altra postazione
5. la macchina termina l'operazione :  fa uscire il pallet, prende in carico e lavora il pallet dell'altra postazione
6. contemporaneamente si scarica il pallet appena lavorato dell'altra postazione, lo si  ricarica e lo si monta
7. si ritorna al passo 5

Ogni batch viene lavorato in più fasi di caricamento :  si definisce cubo il numero di volte che deve essere caricato il pallet per ogni batch :  ad esempio, se un batch ha 60 pezzi ed il suo pallet ne porta 10, il batch sarà composto da 6 cubi.

Come esposto in precedenza, una scelta del processo è decidere se caricare entrambe le postazioni con lo stesso batch (funzionamento in disaccoppiamento) oppure alternare due batch (funzionamento in accoppiamento).

Ad esempio, in presenza di due batch A e B (di cui A è più urgente), ciascuno di 4 cubi, il funzionamento disaccoppiato prevede : 
Postazione 1     x  --A--       ------    --A--    ------   x  --B--      -------   --B--    -------
Postazione 2         ------   x  --A--    ------    --A--       -----   x   --B--    -------   --B--
dove x è un attrezzaggio.

Il funzionamento accoppiato prevede invece : 
Postazione 1     x  --A--       ------    --A--    ------    --A--     ------   --A--   -------
Postazione 2         ------   x  --B--    -------   --B--    ------     --B--   -------   --B--

Come si può notare, il funzionamento disaccoppiato fa terminare prima il batch A, ma richiede quattro attrezzaggi invece che due. Il batch B termina alla stessa data in entrambi i casi. Per questo motivo il funzionamento disaccoppiato va selezionato soltanto nel caso di batch che altrimenti andrebbero in ritardo (previa verifica della disponibilità fisica di due pallet dello stesso tipo).

# Impostazioni
## Impostazione Multipallet
L'attivazione è pilotata dal Gruppo risorsa che deve avere per la risorsa principale il campo T$BRMQ impostato a "2".
In MUP devono essere presenti le risorse specifiche, in corrispondenza 1/1 con quelle principali.
Il flag T$BRMQ si mette sulla risorsa principale, il numero di postazioni su quella specifica (è il campo C§NRRS).
Attenzione :  queste informazioni non possono essere modificate all'interno della BCD. Se cambiano i flag di tabella BRM occorre rifasare gli impegni risorse, se cambia il numero di postazioni basta uscire e rientrare.

Il multipallet e il multipostazione possono essere presenti nella stessa schedulazione (naturalmente in risorse diverse).


# Note Tecniche
I campi delle impostazioni della tabella BRM  sono letti da S5FURIT_SC copia i flag da tabella a S5IRIS
  T$BRMP in S6FL23
  T$BRMQ in S6FL24


Informazioni numeriche
S6CC06 - Numero split se // rigido
S6CC07 - Numero pezzi per cubo


Il programma che contiene la logica del calcolo Multipallet è S5SMES_90. Quello che implementava la logica multipostazione era S5SMES_73.

Per ora il flag 23 con il corrispondente numero di postazioni (il campo S6CC06) viene depositato nelle memorie del S5SMES_90 ma non viene utilizzato nel calcolo. Se lo si dovrà fare, si dovrà intervenire solo in questo programma che ha già le informazioni per operare.


Valori
£BCDFL(8) = '1' se c'è il MUP potenziale (almeno una risorsa a "2").
Impostato all'atto del lancio della BCD la prima volta (le risorse non vengono lette ad ogni rischedulazione, in quanto si presume che un loro cambiamento sia sporadico).

£BCDFL(9) =  '1' se c'è il MUP effettivo (almeno un impegno caricato su una risorsa con MUP potenziale).
Impostato ad ogni rischedulazione (se ad esempio dall'interno si cambiano gli- impegni di un ordine, può verificarsi che ne entrino o ne escano con MUP).


NB :  tutti questi valori dipendono dalla congruenza dei dati.

S5SMES_01R - Caricamento risorse. Lancia il 90 in memorizzazione se principale con T$BRMQ a '2' o specifica con Numero di postazioni. Il numero di postazioni della specifica hanno il significato che le viene dal flag della principale.

Il Flag T$BRMQ viene usato in S5SMES_01R (caricamento memoria risorse) per lanciare il 75 dove si memorizzano le risorse con T$BRMQ a '1'.
In questo programma viene lanciato il 90 se T$BRMQ a '2'.

S5SMES_01P - Costruzione puntatori a risorse. Se c'è flag 5 lancia il 90 in completamento.

S5SMES_01I.- Caricamento Impegni Risorse NB :  questo pgm prima di modificarlo l'ho copiato da P_BCD_ALF (che è più avanti di quello in DEV).

S5SMES_03 - Reinizializzazione DS. NB :  questo pgm prima di modificarlo l'ho copiato da P_BCD_ALF (che è più avanti di quello in DEV).


S5SMES_06 - Completamento inizializzazioni. Qui toglie dalla memoria iniziate (DSOPIN) i dettagli delle risorse MUP, che andranno trattate insieme all'inizio della coda.


NB :  quando si schedula potrebbe darsi che un dettaglio successivo finisca prima di uno precedente (ha meno cubi) e quindi l'istante di fine occupazione della risorsa arretrerebbe. Questo è impedito nel 13 perché aggiorna questo istante solo se maggiore del precedente (poteva verificarsi anche in caso di impegni dipendenti di un batch).




Nuovo programma di gestione multipallet
S5SMES_90

La schedulazione del MUP viene eseguita in questo programma. Per non cambiate l'11E (cuore della schedulazione) è stata creata una EXIT standard (S5SMX_141) che questo pgm lancia nativamente, e che a sua volta lancia il 90.
STATO DELL'ARTE



# VINCOLI MUP

C'è una sola risorsa specifica per risorsa generale. Il sistema non esegue scelte di risorse specifiche.
In linea generale potrebbero esserci anche solo risorse generali.

Non attive le RSV (risorse secondarie di vincolo)

Non gestiti i batch.

Un impegno risorse va solo su una postazione.

Gli impegni di un ordine visitano una risorsa MUP una sola volta (Flow Shop e non Job Shop).

Il numero di pezzi per cubo è stabilito a priori nell'impegno.

Una risorsa ha un numero fisso di postazioni.



