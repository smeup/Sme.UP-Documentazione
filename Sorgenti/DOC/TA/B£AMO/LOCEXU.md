# Componente Matrice di aggiornamento

- [Abstract Matrice di aggiornamento](Sorgenti/DOC/TA/B£AMO/LOCEXU_F00)


## Principali Funzionalità

- [Visualizzazione](Sorgenti/DOC/TA/B£AMO/LOCEXU_F01)
- [Opzioni](Sorgenti/DOC/TA/B£AMO/LOCEXU_F02)
- [Funzionalità sui dati](Sorgenti/DOC/TA/B£AMO/LOCEXU_F03)
 :  : DEC T(MB) P(DOC) K(LOCEXU_F04) //Funzionamento sui dati

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Update :  L'evento scatta una volta che le informazioni sono arrivate al server AS400 ed è confermato che sono state accettate.
- Check :  L'evento scatta ogni volta che si scambiano informazioni con il server AS400 (ma non quando scatta l'Update). E' utilizzato per verificare lato server la correttezza delle informazioni inserite prima di confermarle, o per completare automaticamente campi non ancora valorizzati, tramite informazioni mandate dal server
- Click :  scatta al click su una cella e alla selezione di una riga
- Doubleclcik :  in Loocup scatta al doppio click su una cella
- Changerow :  L'evento scatta al cambio di riga
- Changecol :  In Loocup questo evento scatta al cambio di colonna
- Change :  scatta la cambio riga e in Loccup al cambio colonna
- Drop :  scatta al drop su una riga della matrice di aggiornamento

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(\*\*;;&AM.LL) 3(OJ;\*USRPRF;&AM.UT) 4(\*\*;;DOCSETUP) P(SECLS(G.SET.EXU))) L(1)

## Schede di esempio
Gli esempi del componente EXU sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;\*SCO;) 1(V2;JAGRA;EXU) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;\*SCO;) 1(V2;JAGRA;TRE) 2(MB;SCP_SCH;WETEST_EXU)) L(1)

## Documenti applicativi
- [Introduzione](Sorgenti/DOC/TA/B£AMO/LOCEXU_A)
- [Servizi di aggiornamento :  funzionamento](Sorgenti/DOC/TA/B£AMO/LOCEXU_B)
- [Collegamento EXB/EXU](Sorgenti/DOC/TA/B£AMO/LOCEXU_T01)
- [Costruzione di un servizio di aggiornamento](Sorgenti/DOC/TA/B£AMO/LOCEXU_T02)
- [Utilizzo Matrice d'Aggiornamento su Device Mobile](Sorgenti/DOC/TA/B£AMO/LOCEXU_MO)
