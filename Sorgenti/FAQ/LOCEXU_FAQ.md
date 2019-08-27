- **Come viene definito il componente grafico di un campo?**

 :  : VOC Id="00001" Txt="Come viene definito il componente grafico di un campo?"
Per la definizione del componente grafico da usare per mostrare un oggetto, nei dati che vengono inviati alla matrice di aggiornamento, sono presenti due attributi importanti : 
- la tipologia di oggetto (es :  J4ICO, J4IMG, J4PGB, V2SI/NO ...)
- la tipologia di IO

L'attributo IO fornisce informazioni importanti relative al tipo di cella : 
- IO="O" :  campo non modificabile. verrò mostrato il componente grafico dipenderà dalla tipologia oggetto.
- IO="H" :  campo nascosto.
- IO="G" :  definisce parametri grafici, campo non visualizzato
- IO="M" :  definisce editabilità, campo non visualizzato
- IO="C" :  visualizzazione tramite componente combo
- IO="E" :  visualizzazione tramite componente autocomplete
- IO="B" :  visualizzazione tramite componente ricerca

Il servizio di aggiornamento può inoltre cambiare la modalità di interazione ridefinendo il parametro IO.

Il modo migliore è però specificare esplicitamente il componente di interazione tramite l'attributo Cmp.
Questo attributo può essere specificato : 
1) nelle colonne dell'xml di griglia dei dati
2) nell risposta alla chiamata *SETUP al servizio di aggiornamento
3) nel layout
La precedenza viene data a quanto specificato nel layout (3) poi nell'ordine (2) e (1).

Utilizzando l'attributo Cmp è inoltre possibile definire una serie di opzioni tramite l'attributo CmpExt

- **Come posso definire la tipologia di componente nei dati di griglia?**

 :  : VOC Id="00002" Txt="Come posso definire la tipologia di componente nei dati di griglia?"
Per definire il componente direttamente nei dati di griglia devono essere utilizzate la copy  £JAXDSCO3 in più alla £JAXDSCOL

D £JAXDSCO3       DS          1000
     D  £JAX3CD                      10                                         Codice (chiave)
      * Componente
     D  £JAX3CO                       3                                         Componente
      * Configurazione componente
     D  £JAX3EC                     246                                         Configurazione Cmp

- **Posso nascondere il pulsante di conferma/submit in Webup?**

 :  : VOC Id="00003" Txt="Posso nascondere il pulsante di conferma/submit in Webup?"
Sì, è possibile impedire la visualizzazione del pulsante di conferma/invio tramite il parametro SubmitButton impostato a "No"


- **Qual'è la relazione tra componente EXB e componente EXU?**

 :  : VOC Id="00004" Txt="Qual'è la relazione tra componente EXB e componente EXU?"
In Loocup per avere una matrice di aggiornamento è sufficiente avere un componente matrice EXB ed agire su alcuni parametri dell'istruzione G.SET.MAT nello script della scheda stessa.
I parametri minimi da impostare sono : 
- ReadOnly="No"
- UpdSvc="Nome del servizio di aggiornamento"

Questa cosa non è supportata in WebUP, dove esiste una separazione netta tra ciò che è matrice di visualizzazione (componente EXB/MAT) e matrice di aggiornamento (componente EXU)

ATTENZIONE! Non bisogna inoltre confondere il componente con l'xml gestito dal componente di dati.
EXB e EXU utilizzano lo stesso xml di dati :  xml di griglia, che viene fornito da chiamate F(EXB;<servizio_dati>;<metodo>)


- **Devo avere un Layout per utilizzare una matrice di aggiornamento?**

 :  : VOC Id="00005" Txt="Devo avere un Layout per utilizzare una matrice di aggiornamento?"
No! Il layout serve per definire come deve essere visualizzato un record di una matrice di aggiornamento :  posizione, componente grafico, presenza di valori/etichette fisse... etc ... etc ...
Una matrice di aggiornamento funziona però anche senza :  il layout offre però molte possibilità in più per personalizzare l'interazione e migliorare la user-experience.
Inoltre, per i dati di una matrice possono essere definiti più Layout o viceversa uno stesso Layout potrebbe essere utilizzato su più matrici.

ATTENZIONE! Alcuni servizi (as esempio il LOA36) costruiscono l'xml di griglia partire dalla definizione di uno script di Layout! Ovviamente però questo  non è sempre vero :  servizio di reperimento dati e layout sono concetti indipendenti!



