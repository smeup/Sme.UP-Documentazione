- \*\*Sai quali sono gli archivi interessati?\*\*

 :  : VOC Id="SKIS0005" Txt="Sai quali sono gli archivi interessati?"
L'archivio è il P5IRIS0F.
- \*\*Sai quali sono le tabelle principali?\*\*

 :  : VOC Id="SKIS0010" Txt="Sai quali sono le tabelle principali?"
La tabella principale è la P5S Tipo impegno risorse.
- \*\*Sai come si legano gli Impegni di risorsa ad un Ordine di produzione?\*\*

 :  : VOC Id="SKIS0015" Txt="Sai come si legano gli Impegni di risorsa ad un Ordine di produzione?"
Per legare gli Impegni risorse ad un Ordine di produzione è necessario : 
1. impostare nella tabella P5T (Tipo ordine di produzione) il tipo impegno (Tabella P5S) precedentemente definito;
2. impostare, se non già creati, nei flussi dell'Ordine di produzione le azioni di Creazione, Nettificazione e Annullamento impegni.
- \*\*Sai come si crea il Ciclo specifico di un Ordine di produzione?\*\*

 :  : VOC Id="SKIS0020" Txt="Sai come si crea il Ciclo specifico di un Ordine di produzione?"
Il Ciclo di un Ordine di produzione è il Ciclo associato a quello specifico Ordine. In particolare l'assieme del ciclo è l'ordine di produzione stesso e il tipo ciclo è definito nell'elemento di P5S corrispondente al tipo ordine di riferimento.
Per creare il ciclo è necessario impostare fra i passi del Flusso di Inserimento Ordine di produzione l'azione Creazione Ciclo, con programma P5FUCDC, Funzione 'CRE' e Metodo : 
CIE :  Creazione cieca
RIC :  Creazione con Richiesta
CIEGES :  Cieca con successiva gestione
RICGES :  Con richiesta e successiva gestione
- \*\*Sai se per creare gli Impegni risorse è sufficiente definire correttamente\*\*

 :  : VOC Id="SKIS0025" Txt="Sai se per creare gli Impegni risorse è sufficiente definire correttamente le Tabelle?"
Non è sufficente intervenire solo sulle tabelle, ma bisogno aggiungere i passi di gestione degli impegni risorse sul flussi di inserimento, post-modifica e pre-annullamento degli ordini di produzione.
- \*\*Sai se annullo un ordine di produzione si annullano anche gli Impegni riso\*\*

 :  : VOC Id="SKIS0030" Txt="Sai se annullo un ordine di produzione si annullano anche gli Impegni risorse ad esso riferiti?"
Si se nel Flusso Pre Eliminazione ho inserito il passo di Cancellazione impegni (P5FUALL Funzione CAN).
- \*\*Sai se modifico un ordine di produzione si aggiornano anche gli impegni di\*\*

 :  : VOC Id="SKIS0035" Txt="Sai se modifico un ordine di produzione si aggiornano anche gli impegni di risorsa ad esso riferiti?"
Si se nel Flusso di Post Modifica ho inserito il passo di Aggiornamento impegni (P5FUIMT Funzione CRE e metodo NETT).
- \*\*Sai quali sono le modalità con cui vengono creati gli impegni di risorse p\*\*

 :  : VOC Id="SKIS0040" Txt="Sai quali sono le modalità con cui vengono creati gli impegni di risorse per l'assieme di un Ordine di produzione?"
Le principali modalità con cui vengono creati gli impegni per un assieme sono : 
'CO'  :  a partire dal Ciclo dell'oggetto
'C1'  :  a partire dal Ciclo del documento, e se fosse assente dal Ciclo dell'oggetto
'C2'  :  a partire dal Ciclo del documento.

Per le altre modalità si rimanda all'Help della tabella P5S.
- \*\*Sai come vengono nettificati e rifasati gli impegni di risorse.\*\*

 :  : VOC Id="SKIS0045" Txt="Sai come vengono nettificati e rifasati gli impegni di risorse."
Gli impegni di risorse vengono nettificati e rifasati leggendo le Attività inserite per l'Ordine di produzione di riferimento e utilizzando il programma P5FS01A.
Affinche la rifasatura avvenga è necessario settare correttamente la Modalità di rifasatura impegni nella tabella P5S. Le modalità sono : 
-    se impostato a 'A', gli impegni di risorse vengono rifasati automaticamente.
-    se impostato un altro valore qualsiasi, gli impegni vengono rifasati, previa richiesta di conferma.
-    se lasciato in bianco, non viene eseguita nessuna rifasatura.
