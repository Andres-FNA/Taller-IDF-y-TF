import unicodedata
import math 

# ================================
# DATASET
# ================================
documentos = [
"ARTICULO 15: Los documentos que aporte el aspirante para su admision permaneceran en custodia del Departamento de Registro y Control Academico mediante el sistema de gestion academica.",

"ARTICULO 16: La documentacion allegada por los aspirantes no admitidos o que no se matriculen sera eliminada de los sistemas de informacion institucionales.",

"ARTICULO 14: La institucion se reserva el derecho de seleccionar a los estudiantes y define criterios de admision basados en el perfil aprobado por el Ministerio de Educacion Nacional.",

"ARTICULO 17: El proceso de admision se llevara a cabo bajo principios de diversidad, equidad e inclusion.",

"ARTICULO 19: Los resultados del proceso de admision son de reserva institucional y no se comunican a terceros salvo excepciones legales.",

"ARTICULO 18: Cuando un aspirante admitido no se matricule puede solicitar reserva de cupo hasta por dos periodos academicos consecutivos.",

"ARTICULO 24: En el caso de las transferencias el Director de Programa podra autorizar examenes de validacion para asignaturas aprobadas con calificacion entre treinta y treinta y cinco.",

"ARTICULO 27: Los estudiantes transferentes deben cumplir con los prerrequisitos de las asignaturas como condicion para cursarlas.",

"ARTICULO 28: El porcentaje maximo de creditos homologables sera del 60 por ciento.",

"ARTICULO 29: Los estudiantes que deseen cambiar de programa deben solicitar transferencia interna y homologacion de asignaturas."
]

# ================================
# LIMPIAR TEXTO
# ================================
def limpiar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.replace(":", "").replace(",", "").replace(".", "").split()

# ================================
# TF
# ================================
def calcular_tf(palabra, documento):
    palabras = limpiar_texto(documento)
    return palabras.count(palabra) / len(palabras)

# ================================
# IDF
# ================================
def calcular_idf(palabra, documentos):
    N = len(documentos)
    docs_con_palabra = 0
    
    for doc in documentos:
        if palabra in limpiar_texto(doc):
            docs_con_palabra += 1

    if docs_con_palabra == 0:
        return 0
    
    return math.log(N / docs_con_palabra)

# ================================
# SCORE TF-IDF
# ================================
def calcular_score(query, documento, documentos):
    palabras_query = limpiar_texto(query)
    score = 0
    
    for palabra in palabras_query:
        score += calcular_tf(palabra, documento) * calcular_idf(palabra, documentos)
        
    return score

# ================================
# BUSCADOR
# ================================
def buscar(query, documentos):
    resultados = []
    
    for i, doc in enumerate(documentos):
        score = calcular_score(query, doc, documentos)
        resultados.append((i, score, doc))
    
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

# ================================
# PROBAR VARIAS QUERIES
# ================================
def probar_queries(queries, documentos):
    for query in queries:
        print("\n==============================")
        print("🔍 Consulta:", query)
        print("==============================")
        
        resultados = buscar(query, documentos)
        
        for i, (idx, score, doc) in enumerate(resultados[:5]):
            print(f"Top {i+1} | Doc {idx} | Score: {round(score,4)}")
            print(doc)
            print("------")

# ================================
# IDF DE TODAS LAS PALABRAS
# ================================
def obtener_vocabulario(documentos):
    vocabulario = set()
    
    for doc in documentos:
        vocabulario.update(limpiar_texto(doc))
    
    return vocabulario

def calcular_idf_todas(documentos):
    vocabulario = obtener_vocabulario(documentos)
    idf_dict = {}
    
    for palabra in vocabulario:
        idf_dict[palabra] = calcular_idf(palabra, documentos)
    
    return idf_dict

def mostrar_idf(documentos):
    idf_valores = calcular_idf_todas(documentos)
    idf_ordenado = sorted(idf_valores.items(), key=lambda x: x[1], reverse=True)

    print("\n🔝 TOP 5 PALABRAS CON IDF ALTO:")
    for palabra, valor in idf_ordenado[:5]:
        print(palabra, ":", round(valor, 4))

    print("\n🔻 TOP 5 PALABRAS CON IDF BAJO:")
    for palabra, valor in idf_ordenado[-5:]:
        print(palabra, ":", round(valor, 4))

# ================================
# EJECUCIÓN
# ================================

queries = [
    "reserva cupo admision",
    "documentos aspirante admision",
    "proceso admision resultados",
    "transferencias homologacion asignaturas",

]

probar_queries(queries, documentos)

mostrar_idf(documentos)
