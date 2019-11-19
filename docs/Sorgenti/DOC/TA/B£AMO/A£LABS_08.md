# Le sezioni (o funzioni) standard di un modulo
Queste sezioni sono funzionalià comuni a tutti i moduli e quindi raggiungibili dalle esplorazioni.
Tali sezioni sono catalogate nell'oggetto V2 - A£SSC.

## Dettaglio delle sezioni
Alcune sezioni hanno un solo livello di dettaglio per modulo. Altre ne possono avere più di uno.
Ad esempio la sezione "video formativi" può avere più di un elemento di dettaglio per ogni modulo, ogni modulo può avere più di un video associato. La sezione "glossari" invece ha un unico dettaglio per ogni modulo. Ogni modulo ha un solo glossario (che può comunque essere composto da più voci).

## aggiunta di una nuova sezione
Per aggiungere una nuova sezione è necessario : 
 \* Aggiungerla nel B£G15G
 \* Aggiungere nel programma LOSER_04 un elemento nella schiera FUM indicante : 
 \*\* Codice
 \*\* File che contiene i membri relativi
 \*\* Suffisso dei membri
 \*\* Descrizione
 \*\* DET/GEN (uno o più membri per modulo)
 \*\* Modulo di apprtenenza
 \*\* Sottoscheda specifica per la gestione del dettaglio
 \* Definire la scheda di dettaglio
 \* Scrivere la documentazione relativa

La documentazione si trova in un membro del file DOC, il cui nome è composto dal nome file (definito precedentemente) con suffisso _cod (dove cod è il codice della sezione).
La scheda di dettaglio si trova nel membro MB+nomefile. Il nomefile è quello definito precedentemente nella schiera.
Se nella schiera non è stata indicata una sottoscheda, allora la scheda main sarà la scheda di dettaglio. Altrimenti lo sarà, appunto, la sottoscheda.

# La documentazione di un modulo
- [Documentare un modulo](Sorgenti/DOC/TA/B£AMO/B£DOCU_17)
