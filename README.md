# Taller-IDF-y-TF


# Descripción

Este proyecto implementa un motor de búsqueda utilizando el algoritmo TF-IDF, con el objetivo de permitir a los estudiantes encontrar artículos relevantes dentro de un reglamento académico.

# Objetivo

Construir un sistema que permita buscar información sobre temas como:

Admisión
Reserva de cupo
Transferencias
Procesos académicos

#¿Por qué usar TF-IDF?

Una búsqueda simple solo encuentra palabras sin importar su relevancia.

# TF-IDF permite:

Identificar palabras importantes
Ignorar palabras comunes
Ordenar los resultados según relevancia

#Tecnologías utilizadas
Python
Algoritmo TF-IDF

# Fórmulas

TF (Term Frequency):

TF = frecuencia_palabra / total_palabras

IDF (Inverse Document Frequency):

IDF = log(N / df)
# Cómo ejecutar el proyecto
Clonar repositorio:
git clone https://github.com/TU-USUARIO/motor-busqueda-tfidf.git
Entrar a la carpeta:
cd motor-busqueda-tfidf
Ejecutar:
python main.py

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


El sistema muestra los documentos ordenados por relevancia (score TF-IDF), indicando los más importantes según la consulta.

<img width="331" height="244" alt="image" src="https://github.com/user-attachments/assets/1327d814-f8cd-4274-8cc0-df84642532df" />

 Limitaciones
No entiende el contexto
No reconoce sinónimos
Sensible a errores ortográficos
Dataset pequeño

El sistema se puede integrar en un flujo RAG de la siguiente forma:

Usuario hace una consulta
TF-IDF busca documentos relevantes
Se envían al modelo de lenguaje (LLM)
El modelo genera una respuesta más completa
