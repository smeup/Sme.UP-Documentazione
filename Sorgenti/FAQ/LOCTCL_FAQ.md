
- **Quante diverse dimensioni di tag possono essere visualizzate nel **

 :  : VOC Id="10001" Txt="Quante diverse dimensioni di tag possono essere visualizzate nel componente TagCloud?"

La dimensione del tag (denominata strenght) può essere un valore da 1 a 5 (su parametro di setup è ammessa anche la classe speciale 0). Per approfondimenti sul calcolo della strenght vedere la documentazione relativa agli algoritmi di calcolo

- **E' possibile limitare il numero di tag visualizzati nella tag cloud?**

 :  : VOC Id="10002" Txt="E' possibile limitare il numero di tag visualizzati nella tag cloud?"

Sì è possibile settando l'attributo MaxSize.

- **E' possibile escludere dalla visualizzazione tag con peso inferiore ad una **

 :  : VOC Id="10003" Txt="E' possibile escludere dalla visualizzazione tag con peso inferiore ad una data soglia?"

Sì è possibile settando gli attributi LowerAndEqualsThreshold o LowerThreshold. Il primo esclude anche i tag con peso uguale al valore settato, il secondo solo quelli con peso minore.

- **E' possibile utilizzare un proprio algoritmo custom nel calcolo delle **

 :  : VOC Id="10004" Txt="E' possibile utilizzare un proprio algoritmo custom nel calcolo delle dimensioni dei tag?"

Sì è possibile settando Algorithm='Custom' e definendo come WeightCol una colonna che rappresenti la dimensione dei tag. Ovviamente in questo caso i valori di WeightCol ammessi potranno essere solo interi da 1 a 5. Su parametro di setup è ammessa anche la classe 0.


