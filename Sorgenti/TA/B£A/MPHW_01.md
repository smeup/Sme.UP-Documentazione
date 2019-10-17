# Gestione previsioni con il metodo Holt Winters
E' stato realizzato uno strumento avanzato di previsioni (con il metodo di Holt Winters, nel seguito HW), utilizzabile sia in applicazioni personali, sia in apposite funzioni MPS.

- [Previsioni con Holt Winters](Sorgenti/DOC/TA/B£AMO/B£MATE_01)

- [Azioni tra due viste](Sorgenti/OJ/PGM/MPAP03)

- [Test statistiche](Sorgenti/OJ/PGM/TSTG56)

## Previsioni con HW
Sono stati realizzati nuovi passi MPS che implementano il calcolo della previsione con metodo HW
- [Previsioni con HW](Sorgenti/OJ/PGM/MPAP48)

- [Previsioni con RL](Sorgenti/OJ/PGM/MPAP51)

- [Previsioni con scelta metodo](Sorgenti/OJ/PGM/MPAP52)

- [Previsioni&-x3a; correzione serie](Sorgenti/OJ/PGM/MPAP53)

## Indici Previsioni articolo
Per la previsione HW sono stati scritti nuovi indici di D5COSO. Sono stati quindi modificati i programmi generali di rifasatura contesti e temi, i programmi contenenti la descrizione degli indici, e la documentazione degli indici.

### Descrizione Indici Previsioni articolo
- [Indici Previsioni articolo](Sorgenti/MB/DOC_VOC/D5_AR_£P1 )

## Classe previsiva articolo
Ad ogni articolo/plant oggetto di previsione, viene assegnata una classe previsiva in base alle impostazioni immesse in tabella MP2 (settore \*\*). La classe previsiva viene ritornata come OAV dell'articolo/plant, e come OAV dell'articolo (nel planti di competenza).

## Scorta minima e calcolo / utilizzo scorta minima dinamica
Come "sottoprodotto" della previsione HW è stato implementato il calcolo dinamico della scorta minima, che è stato utilizzato nell'analisi disponibilità (nel ritorno della scorta minima e della scorta datata). La routine £GMA di ritorno dati articolo/plant può ricevere il parametro di modalità di calcolo e risalita scorta minima. E' stato realizzato un nuovo OAV per la scelta della risalita
### Scorta minima
- [Scorta minima](Sorgenti/DOC/TA/B£AMO/M5_015)

### Fonti esistenti e future
- [&-x2a; M5E - SC - Scorta minima](Sorgenti/OG/TA/M5E_SC )
- [&-x2a; M5F - SD - Scorta datata](Sorgenti/OG/TA/M5F_SD )

## Popolamento dati articolo/plant
La scorta dinamica viene calcolata se è stato impostato, nell'archivio articolo/plant, il criterio £01 nel campo "Calcolo scorta lotti". Dato che il comportamento di default non può variare, per attivare questo calcolo è necessario valorizzare il campo con una funzione ad hoc (ad esempio con un UPDATE di SQL). Non è stato realizzato un programma standard di popolamento in quanto le situazioni possono essere le più diversificate :  si può voler calcolare la scorta dinamica solo sugli articoli di una determinata classe, oppure ad un determinato livello di risalita, solo per un plant, ecc ...

## Analisi azione utente MPAP01_X
Il programma di azioni utente MPAP01_X deve esistere, perchè viene richiamato dal programma standard a cui ritorna le eventuali azioni utente, e quindi, se non modificato, resta nella libreria standard. Dato che erroneamente, nel febbraio 2008, sono stati aggiunti gli operatori standard SIV2 e NOV2, si è creato una certa confusione in presenza di azioni utente (programma MPAP01_X in una libreria specifica).
Se il programma MPAP01_X è nella libreria personale : 

- Se contiene i soli operatori SIV2 e NOV2 lo si cancella (sia come sorgente sia come oggetto) e si lascia il programma nella libreria standard.
- Se contiene altri operatori : 
-- Lo si rinomina come MPAP01_XO
-- Si copia il nuovo MPAP01_X dalla libreria standard in quella di personalizzazione.
-- Si copiano gli operatori da MPAP01_XO in MPAP01_X (ad eccezione di SIV2 e NOV2, se presenti).

NB :  gli operatori vanno inseriti nella SELECT, nella routine ESExxx, e nella schiera in fondo
