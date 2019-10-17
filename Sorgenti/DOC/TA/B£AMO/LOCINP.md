# Componente Input Panel

- [Abstract](Sorgenti/DOC/TA/B£AMO/LOCINP_F00)

## Principali Funzionalità

- [Visualizzazione](Sorgenti/DOC/TA/B£AMO/LOCINP_F01)
- [Opzioni](Sorgenti/DOC/TA/B£AMO/LOCINP_F02)
- [Dinamismi](Sorgenti/DOC/TA/B£AMO/LOCINP_F03)
- [Funzionalità sui dati](Sorgenti/DOC/TA/B£AMO/LOCINP_F04)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Update :  L'evento scatta una volta che le informazioni sono arrivate al server AS400 ed è confermato che sono state accettate.
- Check :  L'evento scatta ogni volta che si scambiano informazioni con il server AS400 (ma non quando scatta l'Update). E' utilizzato per verificare lato server la correttezza delle informazioni inserite prima di confermarle, o per completare automaticamente campi non ancora valorizzati, tramite informazioni mandate dal server
- Click :  Funziona solo quando si utilizza l'input panel senza servizio di aggiornament e scatta una volta premuto "Invio" o alla pressione del bottone di conferma. Serve per invaire al target del dinamismo le variabili di tutti i campi dell'input panel.

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(\*\*;;&AM.LL) 3(OJ;\*USRPRF;&AM.UT) 4(\*\*;;DOCSETUP) P(SECLS(G.SET.INP))) L(1)

## Documenti applicativi
- [Introduzione](Sorgenti/DOC/TA/B£AMO/LOCINP_A)
- [Come si utilizza un input panel](Sorgenti/DOC/TA/B£AMO/LOCINP_B)
- [Costruzione delle sezioni](Sorgenti/DOC/TA/B£AMO/LOCINP_C)
- [Aggiornamento Caratteristiche Griglia&-x2f;Setup Campi](Sorgenti/DOC/TA/B£AMO/LOCINP_D)
- [Funzionalità sui dati](Sorgenti/DOC/TA/B£AMO/LOCINP_F)
- [Utilizzo Input Panel su Device Mobile](Sorgenti/DOC/TA/B£AMO/LOCINP_MO)
