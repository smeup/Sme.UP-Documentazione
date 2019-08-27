- **Perchè il componente INT è deprecato?**

 :  : VOC Id="00001" Txt="Perchè il componente INT è deprecato?"
L'utilizzo del componente INT è deprecato in quanto è più corretto, quando si usa un servizio interno, specificare nella chiamata che componente dovrà gestire l'xml di risposta (es :  EXB, TRE, FBK ...)
Ad esempio inoltre, alcuni servizi interni (es :  JA_00_05) a parità di metodo modificano l'xml di risposta a seconda del componente specificato nel richiamo della fun F(TRE;JA_00_05;<metodo>) o F(MAT;JA_00_05;<metodo>)

- **L'uso dei servizi interni è deprecato!?!?**

 :  : VOC Id="00002" Txt="L'uso dei servizi interni è deprecato!?!?"
No è deprecato l'utilizzo del componente INT nella chiamata ad un servizio interno a favore della specificazione di un componente più descrittivo e appropriato. Es :  F(TRE;JA_00_05;<metodo>)
I servizi interno sono importanti in SmeUP perchè permettono di accedere a funzioni esposte da un agente esterno al server altrimenti inaccessibili (sia esso l'applicativo client, un provider .. etc ).
