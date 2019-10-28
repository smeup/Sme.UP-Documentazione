
### **Se nella struttura dati ad albero c'è più di una radice come viene rappresentata graficamente la mappa mentale?**


Il componente MindMap è in grado di gestire anche un albero con più oggetti radice (a livello teorico questa struttura non è propriamente un albero ma è detta 'foresta'). In questo caso viene generato fittiziamente dal sistema un nodo radice, a cui vengono aggiunti come figli le radici della foresta. Il testo di tale nodo è personalizzabile attraverso l'attributo di setup FakeRootTxt.

### **Il componente Albero è espandibile dinamicamente. Lo può essere anche la MindMap?**


Anche la MindMap è espandibile dinamicamente, configurando l'attributo di setup DynExpand=Yes. Si consiglia di visualizzare l'esempio sull'espansione dinamica per i dettagli di funzionamento.

### **E' possibile eseguire una funzione al click su un nodo foglia?**


Sì, esistono due possibilità per farlo : 
- far si che tale funzione sia presente nell'Exec del nodo
- aggiungere un dinamismo di tipo click alla MindMap con una Exec contenente una fun
Si consiglia di visualizzare gli esempi sui dinamismi per i dettagli di impostazione.


