- \*\*Sai cosa si intende per contabilità gestionale?\*\*

 :  : VOC Id="SKIG0010" Txt="Sai cosa si intende per contabilità gestionale?" Als="comm"
L'insieme di registrazioni gestionali (flaggate quindi in modo chiaro e riconoscibile) che, effettuate manualmente e/o automaticamente dal programma, integra le registrazioni puramente fiscali, in modo da fornire una rappresentazione il più realistica possibile dell'andamento dell'azienda nei bilanci periodici infrannuali. Sotto questa tipologia di registrazione possono quindi essere inclusi i ratei e risconti, la quota parte degli ammortamenti, le simulazioni che a vario titolo possono essere utili a rappresentare costi/ricavi futuri, ecc. Le registrazioni gestionali non vengono minimamente prese in considerazione dalla stampa definitiva del giornale, pertanto rimangono in essere per fornire utili confronti nelle analisi di confronto con gli esercizi futuri.
- \*\*Sai cos'è una registrazione di stanziamento?\*\*

 :  : VOC Id="SKIG0020" Txt="Sai cos'è una registrazione di stanziamento?" Als="comm"
Il fine delle registrazioni di stanziamento consiste nella possibilità di applicare il principio di competenza anche nei periodi mensili oltre che annuali, utile ad esempio per stanziare previsioni di spesa databili e poi collegabili alla rilevazione effettiva.
- \*\*Sai cos'è la pertinenza di una registrazione?\*\*

 :  : VOC Id="SKIG0030" Txt="Sai cos'è la pertinenza di una registrazione?" Als="comm"
La pertinenza è quella caratteristica presente su qualsiasi evento contabile, che permette di
determinarne il tipo di rilevanza (civilistica o gestionale). Viene rappresentata dal flag 01 presente su testata e righe di una registrazione, e compare quindi in tutti i filtri presenti nei programmi di interrogazione di contabilità.
- \*\*Sai in quale modo vengono utilizzate le registrazioni gestionali nell'anal\*\*

 :  : VOC Id="SKIG0040" Txt="Sai in quale modo vengono utilizzate le registrazioni gestionali nell'analisi del bilancio?"
Effettuandone la selezione con il filtro 'Pertinenza', utile ad includere/escludere tali registrazioni dal calcolo effettuato nel report prescelto.
- \*\*Sai come configurare una causale per eseguire registrazioni gestionali?\*\*

 :  : VOC Id="SKIG0050" Txt="Sai come configurare una causale per eseguire registrazioni gestionali?"
Nella tabella dei tipi di registrazioni (C5D) si agisce sui campi 'Gruppo flag testata' e 'Gruppo flag riga', associando a una certa causale un gruppo che preveda di inizializzare il flag 01 con un valore maggiore di 2.
- \*\*Sai se tutti i conti contabili possono ricevere registrazioni gestionali?\*\*

 :  : VOC Id="SKIG0060" Txt="Sai se tutti i conti contabili possono ricevere registrazioni gestionali?"
Per principio si, a meno che su un singolo conto non venga bloccata la gestione della competenza se generata automaticamente, mentre immettendo una registrazione manuale il flag 'Pertinenza' è gestito liberamente.
