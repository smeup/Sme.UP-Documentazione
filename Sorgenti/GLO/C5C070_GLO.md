- \*\*Importo Documento\*\*

 :  : VOC Id="IMDO" Txt="Importo Documento"

E' l'importo totale effettivo del documento, compresivo dell'iva.

- \*\*Imponibile Documento\*\*

 :  : VOC Id="IMTT" Txt="Imponibile Documento"

E' il totale imponibile del documento (in sostanza l'importo documento al netto dell'iva).

- \*\*Imponibile Soggetto\*\*

 :  : VOC Id="IMSG" Txt="Imponibile Soggetto"

E' la quota dell'imponibile documento (IMTT) che è soggetta alle ritenute. Può o meno coincidere con l'imponibile documento. Nel caso non coincida la differenza figurerà come imponibile non soggetto.

- \*\*Imponibile Soggetto Ritenuta\*\*

 :  : VOC Id="IMRA" Txt="Imponibile Soggetto Ritenuta"

E' la quota di imponibile soggetto (IMSG) soggetto a ritenuta d'acconto. Rispetto all'imponibile soggetto, vi può essere applicata una % in diminuzione. In questo caso la differenza verrà considerata come quota non soggetta da dichiarare nel 770 ai fini dei calcoli sulle ritenute d'acconto. E' su questo importo che verrà applicata la % della ritenuta d'acconto per calcolare l'importo della ritenuta stessa.

- \*\*Imponibile Soggetto Ritenuta Previdenziale\*\*

 :  : VOC Id="IMPRT" Txt="Imponibile Soggetto Ritenuta Previdenziale"

E' la quota di imponibile soggetto (IMSG) soggetto a ritenuta previdenziale. Rispetto all'imponibile soggetto, vi può essere applicata una % in diminuzione. In questo caso la differenza verrà considerata come quota non imponibile ai fini dei calcoli sulle ritenute previdenziale. E' su questo importo che verrà applicata la % della ritenuta d'acconto per calcolare l'importo della ritenuta stessa.

- \*\*Non Soggetto da Dichiarare in 770\*\*

 :  : VOC Id="IMNS" Txt="Non Soggetto da Dichiarare in 770"

E' la quota della differenza data da imponibile soggetto (IMSG)  e imponibile soggetto ritenuta (IMRA) che va dichiarata nel modello 770.

- \*\*Altre Somme Non Soggette\*\*

 :  : VOC Id="IMNO" Txt="Altre Somme Non Soggette"

E' la quota della differenza data da imponibile soggetto (IMSG)  e imponibile soggetto ritenuta (IMRA) che non va dichiarata nel modello 770. La sommatoria di questo importo e dell'imponibile non soggetto da dichiarare in 770 (IMNS) deve coincidere esattamente alla sopracitata differenza.

- \*\*Netto a Pagare\*\*

 :  : VOC Id="NETT" Txt="Netto a Pagare"

Rappresenta l'importo che a tutti gli effetti corrisposto al percipiente. Tale importo è dato dall'importo documento (IMDO) nettificato di :  importo ritenuta d'acconto, importo ritenuta previdenziale a carico del percipiente, enasarco a carico del percipiente.

- \*\*770 - Lordo Corrisposto\*\*

 :  : VOC Id="770L" Txt="770 - Lordo Corrisposto"

Nel 770 sotto l'accezione dell'importo "Lordo Corrisposto", finisce la sommatoria dell'imponibile soggetto a ritenuta (IMSG) e dell'importo non soggetto da dichiarare in 770 (Voce IMNS).

- \*\*770 - Importo Non Soggetto\*\*

 :  : VOC Id="770N" Txt="770 - Importo Non Soggetto"

Nel 770, sotto l'accezione dell'importo "Non Soggetto", finisce la differenza fra il lordo corrisposto (770L) e l'imponibile della ritenuta d'acconto (IMRA). In questo modo confluisce nel concetto di "non soggetto" anche la quota di imponibile soggetto, che è stata esclusa per l'applicazione di una percentuale all'imponibile soggetto a ritenuta (IMRA).


