Le attività svolte dai Sistemi Informativi Gestionali devono poter avere comportamenti eterogenei sia per potersi adeguare alle naturali evoluzioni che per rappresentare al meglio una realtà aziendale. Possiamo sintetizzare le operazioni in due attività principali : 

- inserimento di un'informazione :  questa attività può comportare sia delle verifiche precedenti, su informazioni già presenti, che abilitano l'esecuzione dell'inserimento o la condizionano a seconda dell'azione che si intende effettuare, oppure genera effetti successivi;
- reperimento di un'informazione :  questa attività può essere concretizzata attraverso diverse vie, come l'inserimento dall'utente o la derivazione da altre informazioni attraverso calcoli.
Per permettere il normale svolgimento delle attività, nonostante la complessità che ne deriva, è sufficiente non predefinire in modo rigido i vincoli e le modalità in cui l'informazione entra nel sistema o nel modo in cui viene ottenuta.
Centralizzando il punto in cui l'informazione è introdotta o ritornata stabilendo un'entità che si occupa di inserire l'informazione ed un'altra che si occupa di reperirla, si ottiene un beneficio percepito da tutto il sistema informativo perchè chi ritorna l'informazione può avere la necessità di chiedere informazioni ad altri implementando un colloquio a più livelli. In questo modo è possibile non variare la richiesta anche nel caso in cui cambi il modo di soddisfarla. In Sme.up abbiamo chiamato queste entità Oggetti Applicativi.
Gli Oggetti risiedono permanentemente nel sistema; sono le entità con cui gli utenti interagiscono quotidianamente :  gli articoli, gli ordini, i movimenti di magazzino. Ogni oggetto è individuato dalla classe di appartenenza e, per alcune classi, dalla sottoclasse e dall'identificativo, che è univoco all'interno della classe/sottoclasse. Si possono definire, al livello di classe, azioni eseguibili all'atto dell'inserimento, variazione, copia e annullamento di un oggetto. Sono inoltre definite delle funzioni sia specifiche della classe, sia generali, tramite le quali si eseguono variazioni ai singoli attributi di un oggetto. La classe interviene inoltre nel reperimento delle informazioni di un oggetto :  per ogni classe esiste un insieme di attributi primari, il cui reperimento avviene tramite un'interfaccia predefinita. Si possono inoltre definire liberamente ulteriori attributi, inseriti dall'utente, e attributi derivati, di cui si imposta la modalità di reperimento.

# Caratteristiche
-  Elemento :  corrisponde ad uno degli elementi definiti dalla tabella \*CNTT
-  File Master :  file di database che definisce gli elementi della classe. La sua determinazione dipende da quanto definito da :  pgm B£G60G, Tabella B§O, pgm B£IVD0.
-  Oggetto Parametro :  definzione delle sottoclassi. La sua determinazione dipende da quanto descritto nel programma B£DEC3.
-  Interfaccia :  api/programma di controllo determinazione degli elementi della classe. La sua determinazione dipende dal richiamo specifico della £DEC.
-  Classe d'Autorizzazione :  definisce la classe di autorizzazione utilizzata per il controllo delle azioni di gestione sugli elementi della classe. La sua determinazione dipende dal pgm B£GES0.
-  Funzione d'Autorizzazione :  definisce la funzione d'autorizzazione da applicare alla classe d'autorizzazione. La sua determinazione dipende dal pgm B£GES0.
-  Deviatore :  programma che gestisce a basso livello l'esecuzione delle funzioni di gestione sull'oggetto. La sua determinazione dipende dal pgm B£GES0.
-  Tipo Tracciato :  definizione degli attributi intrinseci di ogni elemento della classe. La sua determinazione dipende dalla £IVD.
-  Libreria File :  se l'oggetto corrisponde ad un file indica la libreria in cui il file è stato trovato. La sua determinazione dipende dalla £IVD.
-  Codice ID :  se l'oggetto corrisponde ad un file indica il campo del tracciato che definisce in modo univoco l'elemento della classe. La sua determinazione dipende dalla £IVD.
-  Descrizione ID :  se l'oggetto corrisponde ad un file indica il campo del tracciato che definisce la descrizione dell'elemento della classe. La sua determinazione dipende dalla £IVD.
-  Filtro Job Attivo :  indica se al momento il filtro di job per l'oggetto è valorizzato o meno.
-  Classi di Parametri :  integrano le informazioni intrinseche della classe. La loro determinazione è legata ai parametri P/ dell'oggetto.
-  Contenitore Note :  indica il contenitore utilizzato per le note degli elementi della classe.

- [Creare un nuovo oggetto](Sorgenti/OG/OG/OG_N)

# Gli oggetti custom
Gli oggetti custom possono essere creati attraverso la classe oggetto \*D, di cui si riporta a seguire il link alla documentazione.
- [Oggetti da Definizione Utente (UFO)](Sorgenti/OG/OG/_D)

# Dettagli implementativi
- [Definizione](Sorgenti/OG/OG/OG_D)

