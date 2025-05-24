# Crea un diccionario que almacene la cantidad de veces que aparece cada palabra en el texto
# y luego imprime la palabra que más veces aparece.
# Fuente https://elpais.com/tecnologia/2025-05-14/los-agentes-de-ia-son-capaces-de-generar-sus-propias-convenciones-sociales-o-linguisticas.html
text = """
Un estudio demuestra que un grupo de grandes modelos de lenguaje puede desarrollar preferencias colectivas a partir de sus interacciones sin haber sido programados para ello.

Los grandes desarrolladores de modelos de inteligencia artificial (IA) generativa, como OpenAI, Microsoft o Google, tienen claro que el futuro de la industria pasa por los llamados agentes. Se trata de herramientas basadas en la misma tecnología que ChatGPT o Gemini, pero con capacidad para tomar decisiones y realizar acciones en nombre del usuario, como comprar billetes de avión. Para llevar a cabo esas tareas, los agentes de IA deben relacionarse entre sí. Un estudio ha demostrado que los agentes de grandes modelos de lenguaje (LLM, por sus siglas inglesas) pueden desarrollar de forma autónoma convenciones sociales o lingüísticas sin haber sido programados para ello, lo que les ayuda a coordinarse y trabajar de forma conjunta.

Los autores del trabajo, publicado este miércoles en la revista Science Advances, advierten de que sus resultados no deben interpretarse como que los agentes de IA puedan organizarse entre sí, porque no pueden. “Nuestro estudio demuestra que las poblaciones de agentes pueden generar sesgos colectivos que no se detectan mirando a los agentes uno a uno, y que estos, además, son vulnerables a dinámicas de masa crítica, donde pequeñas minorías comprometidas pueden imponer normas al resto”, apunta Andrea Baronchelli, profesor del departamento de Matemáticas del City St George’s University of London y coautor del artículo.

Para Baronchelli y sus colegas, el hecho de que los agentes sean capaces de establecer por sí mismos normas no escritas de funcionamiento puede ayudar en un futuro a desarrollar sistemas de IA que se alineen con valores humanos y objetivos sociales. Se presupone que, si se logran entender los mecanismos por los que los agentes de IA popularizan una opción o generan una convención, entonces se podrán fomentar artificialmente. “Nuestro trabajo también destaca los desafíos éticos relacionados con la propagación de sesgos en los LLM”, escriben los autores. “A pesar de su rápida adopción, estos modelos representan riesgos serios, ya que los vastos datos no filtrados de internet utilizados para entrenarlos pueden reforzar y amplificar sesgos perjudiciales, afectando de manera desproporcionada a las comunidades marginadas”.

Las convenciones sociales, entendidas como “los patrones no escritos de comportamiento que son compartidos por un colectivo”, determinan el proceder de los individuos y la forma en que construyen sus expectativas. Estos patrones varían entre sociedades y están presentes en los juicios morales o en el lenguaje.

Varios estudios recientes demuestran que las convenciones sociales pueden surgir de forma espontánea, sin una intervención externa o centralizada, como resultado del esfuerzo de varios individuos para entenderse entre sí y coordinarse localmente. Baronchelli y sus compañeros han querido comprobar si este proceso se replica también entre agentes de IA. ¿Pueden generarse convenciones sociales de forma espontánea, sin prompting o instrucciones explícitas, entre agentes de IA?

Su conclusión es que sí. “Esta pregunta es fundamental para predecir y gestionar el comportamiento de la IA en aplicaciones del mundo real, dada la proliferación de grandes modelos de lenguaje que utilizan el lenguaje natural para interactuar entre sí y con los humanos”, afirman los autores del trabajo. “Responderla también es un requisito previo para garantizar que los sistemas de IA se comporten de manera alineada con los valores humanos y los objetivos sociales”.

Otra de las cuestiones analizadas en el estudio es cómo afectan los sesgos individuales, entendidos como preferencias estadísticas por una opción frente a otra equivalente, en la emergencia de convenciones universales. También se explora cuál es el proceso por el que un conjunto de actores minoritarios puede ejercer una influencia desproporcionada en el proceso, convirtiéndose en “masa crítica”. Investigar esas dinámicas entre agentes de LLM puede ayudar a anticiparlas y, potencialmente, “controlar el desarrollo de normas beneficiosas en sistemas de IA, así como mitigar los riesgos de normas perjudiciales”, sostienen.

El juego de los nombres
El estudio llega a sus conclusiones tras una serie de experimentos basados en el modelo del juego de los nombres (naming game), en el cual los agentes, con el objetivo de coordinarse en interacciones por pares, acumulan una memoria de jugadas pasadas que luego utilizan para “adivinar” las palabras que usarán sus próximos compañeros. Baronchelli y sus colegas han apostado por este juego porque es el que se ha usado en otros experimentos (con participantes humanos) que han aportado las primeras pruebas empíricas de la emergencia espontánea de convenciones lingüísticas compartidas.

En la simulación, se selecciona aleatoriamente a dos agentes de IA de un total de 24 y se les da el mismo prompt, o instrucción: tienen que elegir un nombre de entre una lista de diez. Luego se comparan los resultados y, si el nombre escogido por los dos es el mismo, obtienen una serie de puntos; si es distinto, se les restan puntos. “Eso aporta un incentivo para la coordinación en interacciones por pares, mientras que no existe ningún incentivo que promueva un consenso global. Además, el prompt no especifica que los agentes formen parte de una población ni proporciona información acerca de cómo se selecciona al compañero”, detallan los autores.

Los investigadores han observado que se llegan a establecer consensos incluso en grupos de 200 agentes jugando por parejas aleatorias y eligiendo nombres de una lista con hasta 26 opciones.

El prompt incluye una memoria que dura cinco jugadas para que los agentes de IA puedan recordar los nombres escogidos por ellos mismos y sus compañeros, así como si tuvieron éxito o no en cada jugada y la puntuación acumulada. Se anima a los agentes a tomar una decisión basada en su memoria reciente, pero no se les aportan datos sobre cómo deberían usar esa memoria para tomar las decisiones.

“Lo novedoso no es hablar de convenciones en agentes, eso ya se hace desde hace años con robots o agentes simples”, indica Baronchelli. “La diferencia clave es que nosotros no programamos a los LLMs para que jugaran al juego de los nombres, ni para que adoptaran una convención concreta. Les explicamos el juego, como hubiéramos hecho con humanos, y dejamos que resolvieran el problema a través de sus propias interacciones”.

Los modelos usados en el experimento para las simulaciones son cuatro: tres de Meta (Llama-2-70b-Chat, Llama-3- 70B-Instruct y Llama-3.1-70B-Instruct) y uno de Anthropic (Claude-3.5-Sonnet). Los resultados del estudio muestran que las convenciones lingüísticas espontáneas surgen en los cuatro modelos. Y que, tras un periodo inicial en el que varios nombres son casi igual de populares, se genera una convención tras la cual uno de ellos se hace dominante. Curiosamente, la velocidad de la convergencia es similar en los cuatro modelos.

Sesgos colectivos y convenciones sociales
¿Cómo llegan los agentes de IA a construir esas convenciones sociales? Los investigadores señalan dos hipótesis: el proceso de selección puede ser uniforme debido a sesgos intrínsecos de los modelos o a características del prompting (por ejemplo, el orden en que se muestran los nombres). La segunda hipótesis quedó descartada al presentar en los experimentos listas con un orden aleatorio de los nombres y obtener los mismos resultados.

Para estudiar los posibles sesgos de cada modelo, los investigadores se fijaron en las preferencias mostradas por los agentes en la selección del primer nombre, antes de que se genere memoria. “Comprobamos que los sesgos individuales son posibles. Por ejemplo, cuando los agentes pueden elegir cualquier letra del alfabeto inglés completo, la población converge sistemáticamente en la letra A porque los agentes individuales la prefieren abrumadoramente sobre todas las demás letras, incluso sin tener memoria previa”, escriben los autores.

Pero lo interesante no son los sesgos individuales, como la preferencia por la letra A, sino los colectivos. “Lo realmente sorprendente fue ver que, incluso cuando los agentes no tenían ninguna preferencia individual, el grupo acababa mostrando una preferencia colectiva hacia una opción concreta. Ahí nos dimos cuenta de que estábamos viendo algo nuevo: lo que llamamos sesgo colectivo, que no viene de los individuos, sino que emerge de las propias interacciones en grupo”, destaca Baronchelli. “Es un fenómeno que no se había documentado antes en IA”, añade.

¿Demuestran los experimentos reseñados en el estudio el surgimiento espontáneo de convenciones sociales entre agentes de IA? Carlos Gómez Rodríguez, catedrático de Computación e Inteligencia Artificial de la Universidad de La Coruña, cree que no. “Hay una enorme distancia entre el juego abstracto de los nombres y la demostración de ‘la emergencia espontánea de convenciones sociales universalmente adoptadas’ que se enuncia”, opina este experto en procesamiento del lenguaje natural, la rama de la IA que busca comprender y generar textos.

Para Gómez, en ciencia debe existir siempre una proporcionalidad entre las conclusiones que se sacan y lo que se ha estudiado. Esa proporcionalidad, en este caso, no existe. “El fenómeno que se observa (el alineamiento entre modelos para maximizar una recompensa en un entorno restringido) es interesante, pero está muy lejos de capturar la complejidad y riqueza de las convenciones sociales reales. En el paper no hay interacción multilateral, ni roles asimétricos (todos los agentes son clones del mismo LLM, no es extraño que converjan), ni dinámicas de poder o conflictos de interés reales”, enumera."""

word_count = {}
words = text.split()
for word in words:
    word_count[word] = words.count(word)

word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(word_count)
print(word_count_sorted[0])
