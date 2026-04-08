# Taller-IDF-y-TF


# Descripción

Este proyecto implementa un motor de búsqueda utilizando el algoritmo TF-IDF, con el objetivo de permitir a los estudiantes encontrar artículos relevantes dentro de un reglamento académico.

# Objetivo
Desarrollar un sistema que permita a un estudiante encontrar información específica dentro de un reglamento, como:

Procesos de admisión
Reserva de cupo
Transferencias académicas
Normativas institucionales
#¿Por qué usar TF-IDF?

Una búsqueda simple solo encuentra palabras sin importar su relevancia.

# ¿Por qué usar TF-IDF?
Una búsqueda tradicional:
Solo verifica si una palabra existe en un texto 
No mide relevancia 

TF-IDF mejora esto porque:
Identifica palabras importantes dentro de un documento 
Reduce el impacto de palabras comunes 
Ordena los resultados según relevancia 

# Tecnologías utilizadas
Python
Algoritmo TF-IDF

# Fórmulas
TF (Term Frequency):
TF = frecuencia_palabra / total_palabras
IDF (Inverse Document Frequency):
IDF = log(N / df)
# Funcionamiento del sistema
Se cargan los documentos del reglamento
Se limpia el texto (minúsculas, eliminación de tildes y signos)
Se calcula TF e IDF para cada palabra
Se calcula un score TF-IDF para cada documento
Se ordenan los documentos según su relevancia

# Casos de prueba

Ejemplos de consultas:

reserva cupo admision
<img width="921" height="211" alt="image" src="https://github.com/user-attachments/assets/4fbecb7b-fccc-4146-898e-a7407c3701df" />

documentos aspirante admision
<img width="921" height="204" alt="image" src="https://github.com/user-attachments/assets/8bcf187a-0ed7-4242-83e7-dee098709ab9" />

proceso admision resultados
<img width="921" height="184" alt="image" src="https://github.com/user-attachments/assets/11ac31cb-8a05-4dcf-a516-ebed632acc37" />
transferencias homologacion asignaturas
<img width="921" height="224" alt="image" src="https://github.com/user-attachments/assets/2b38ac26-3d38-4d5e-832c-0670cb1e4448" />


# Análisis de resultados

El sistema permite identificar qué documentos son más relevantes según la consulta del usuario, gracias a la ponderación de términos importantes.
Además, se pueden observar:
Palabras con IDF alto → más específicas
Palabras con IDF bajo → más comunes
<img width="388" height="270" alt="image" src="https://github.com/user-attachments/assets/0977dec6-0ccc-40d6-b03a-07826d36984e" />

# Limitaciones
No entiende el contexto
No reconoce sinónimos
Sensible a errores ortográficos
Dataset pequeño

# El sistema se puede integrar en un flujo RAG de la siguiente forma:
Usuario hace una consulta
TF-IDF busca documentos relevantes
Se envían al modelo de lenguaje (LLM)
El modelo genera una respuesta más completa
