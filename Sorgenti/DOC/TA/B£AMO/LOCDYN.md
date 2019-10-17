# Componente Dinamico DYN

- [Abstract - DYN](Sorgenti/DOC/TA/B£AMO/LOCDYN_F00)

## Funzionalità principali
- [Caricamento componenti in sub DYN](Sorgenti/DOC/TA/B£AMO/LOCDYN_F01)

## Formato dati
Tipo di XML utilizzato :  in base al tipo di componente da caricare

## Eventi gestiti
Il componente DYN non gestisce direttamenti degli eventi.
Eventuali eventi definiti nello script di scheda verranno (ove possibile) associati e gestiti dal componente caricato.

## Attributi di setup
Il componente DYN non ha impostazioni o attributi specifici; possono però essere definiti setup relativi ai componenti che verranno caricati al suo interno (es :  MAT, BTN ..).
A seconda del componente che verrà poi effettivamente caricato verrà applicato il setup specifico.
Le funzionalità, le impostazioni e gli attributi per ogni tipo di componente sono consultabili attraverso il configuratore e la documentazione del componente stesso.

## Schede di esempio
Gli esempi del componente sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;\*SCO;) 1(V2;JAGRA;DYN) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;\*SCO;) 1(V2;JAGRA;DYN) 2(MB;SCP_SCH;WETEST_DYN)) L(1)

