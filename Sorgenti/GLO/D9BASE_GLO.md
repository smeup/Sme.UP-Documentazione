- \*\*Analisi multi-dimensionale dei dati\*\*

 :  : VOC Id="001" Txt="Analisi multi-dimensionale dei dati"
Permette di estrarre dati da un Data Warehouse senza avere conoscenza di linguaggi di interrogazione (SQL), o della struttura relazionale del DataBase. Permette di formulare la richiesta ai sistemi informativi in un linguaggio che è molto vicino al corrente modo di formulare interrogativi dell'uomo. I concetti base dell'analisi multi-dimensionale sono : 
  Fatti :  i concetti sui quali centrare l'analisi
   Dimensioni :  prospettive lungo le quali aggregare i concetti da analizzare
   Misure :  unità quantificabili dei concetti da analizzare (fatti) Ciò significa che un'ipotetica domanda simile a questa :  "fatturato in quantità e valore, diviso per mese, agente e categoria prodotto" viene semplicemente tradotta in una selezione di fatti e dimensioni :  fatti = fatturato valore, fatturato quantità dimensioni = mese, agente, categoria prodotto Senza un sistema di analisi multi-dimensionale dei dati, la domanda dell'esempio avrebbe dovuto essere formulata con una frase di linguaggio SQL.

- \*\*Business Analytics\*\*

 :  : VOC Id="002" Txt="Business Analytics"
Tutte le tecnologie e le metodologie necessarie alla gestione e all'utilizzo in maniera strategica del bagaglio di dati aziendali disponibili.
Business Intelligence Tutti i processi, le tecnologie e i tool grazie ai quali è possibile trasformare i dati in informazioni necessarie per creare conoscenza e quindi piani d'azione.




- \*\*Data Mining\*\*

 :  : VOC Id="003" Txt="Data Mining"
Letteralmente "estrazione da una miniera di dati", si compone di applicativi e tecniche software in grado di estrarre delle "regolarità" in modo automatico da ingenti quantità di dati. Tali regolarità vengono ricercate dagli applicativi software in base a regole di elaborazione introdotte dagli utenti. Tipico esempio di applicazione lo si ritrova nelle grandi catene di distribuzione, che utilizzano le tessere fedeltà per raccogliere dati sulle abitudini di acquisto dei clienti (grande quantità di dati) da mettere in relazione con le caratteristiche del cliente (sesso, età, nucleo famigliare, ...), allo scopo di indirizzare con tecniche di marketing le abitudini d'acquisto.


- \*\*Database\*\*

 :  : VOC Id="004" Txt="Database"
Insieme di dati riguardanti lo stesso argomento (o argomenti correlati), strutturato in modo tale che possano essere utilizzati da applicazioni software. Oltre ai dati, il database contiene informazioni sulla loro rappresentazione e sulle relazioni tra gli stessi

- \*\*DataBase Management Systems (DBMS)\*\*

 :  : VOC Id="005" Txt="DataBase Management Systems (DBMS)"
Letteralmente sistemi di gestione dei database, quindi applicazioni software in grado di gestire il database ed i dati in esso contenuti.
- \*\*DataBase Relazionali\*\*

 :  : VOC Id="006" Txt="DataBase Relazionali"
DataBase strutturati secondo il modello relazionale di organizzazione logica dei dati. Il modello è basato su concetti di tabella e relazione :  i dati sono immagazzinati nel database sotto forma di tabelle legate tra loro da relazioni logiche.
- \*\*Data Warehouse\*\*

 :  : VOC Id="007" Txt="Data Warehouse"
Raccolta di dati (è un database) che provengono da altri database utilizzati da applicazioni. In particolare le caratteristiche che distinguono un Data Warehouse dal DataBase di un'applicazione sono le seguenti : 
  Integrato :  contiene dati riguardanti argomenti diversi, ma correlati (metodi di codifica uniformi, omogeneità semantica,...);
  Subject Oriented :  orientato secondo temi specifici di analisi, oppure alle diverse attività di Business, ma non alle applicazioni;
  Time Variant :  l'orizzonte temporale dei dati nel DWH è in genere più esteso o diverso dell'orizzonte dei dati gestiti dal gestionale, e anche gli aggiornamenti / inserimenti sono gestiti in modo differente;
   Non volatile :  i dati in un DWH, una volta caricati, non sono modificabili.


- \*\*ETL :  (Extraction, Transformation, Loading)\*\*

 :  : VOC Id="008" Txt="ETL :  (Extraction, Transformation, Loading)"
E' un processo strettamente legato al caricamento di dati in un Data Warehouse. Nel dettaglio i dati vengono Estratti da database relazionali dedicati ad applicazioni, file, altre fonti dati; vengono Trasformati per realizzarne l'integrazione e per renderli pronti per le analisi; infine vengono caricati nel Data Warehouse.

- \*\*Modelli Applicativi\*\*

 :  : VOC Id="009" Txt="Modelli Applicativi"
Soluzioni preconfigurate contenente vere logiche e regole applicative che sintetizzano e è pubblicano i dati presenti nel Data Warehouse, rivolte all'ottimizzazione di alcune decisioni operative oppure finalizzate alle previsioni e predizioni del futuro.

- \*\*OLTP :  (On Line Transaction Processing)\*\*

 :  : VOC Id="010" Txt="OLTP :  (On Line Transaction Processing)"
insieme di tecniche software finalizzate all'analisi dei dati. Le analisi con tecniche OLTP vengono condotte direttamente sui dati in "produzione". Ciò permette di non costruire "repliche" dei dati e di disporre sempre dei dati aggiornati, ma proprio a causa dell'utilizzo diretto dei dati in "produzione" si hanno forti limitazioni nella tipologia e nella potenza delle analisi nonché prestazioni non soddisfacenti.
- \*\*OLAP :  (On Line Analytical Processing)\*\*

 :  : VOC Id="0011" Txt="OLAP :  (On Line Analytical Processing)"
insieme di tecniche software finalizzate all'analisi complessa e veloce di grandi quantità di dati. E' una componente tecnologica fondamentale dell'analisi dei dati di un Data Warehouse.


- \*\*Qlik\*\*

 :  : VOC Id="012" Txt="Qlik"
Impresa di software statunitense con sede a Radnor ma fondata a Lund in Svezia nel 1993. Qlik offre QlikView e QlikSense, software di visualizzazione e Business intelligence. Nel 2010 viene quotata nella Borsa di New York.



- \*\*QlikSense\*\*

 :  : VOC Id="013" Txt="QlikSense"
Software innovativo per la Business intelligence prodotto dalla Qlik che sta sostituendo il prodotto consolidato QlikView. Qlik Sense è un software per la visualizzazione e la discovery dei dati, perfetta per le esigenze di analisi dati di gruppi, reparti e intere organizzazioni.

- \*\*QlikView\*\*

 :  : VOC Id="014" Txt="QlikView"
Software per la Business intelligence prodotto dalla Qlik arrivato alla versione 12. Con Qlikview è possibile produrre analisi di Business intelligence e creare reportistiche per tutti i livelli di governance di un'azienda. Dal 2016 QlikView sta lasciando spazio al nuovo software QlikSense.
- \*\*Query\*\*

 :  : VOC Id="015" Txt="Query"
Interrogazione di un DataBase in modo da ottenere una parte dei dati in esso contenuti. Una query relazionale deve essere formulata in linguaggio SQL.
- \*\*Reporting\*\*

 :  : VOC Id="016" Txt="Reporting"
Soluzione per la rappresentazione grafica delle informazioni analizzate.

- \*\*SQL :  (Structured Query Language)\*\*

 :  : VOC Id="017" Txt="SQL :  (Structured Query Language)"
linguaggio per l'accesso ai dati memorizzati in un database.

