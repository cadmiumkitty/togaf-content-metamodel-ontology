import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, RDFS, SKOS, DCTERMS

# Read vocabulary content
df = pd.read_csv('VocabularyTOGAFContentMetamodelV2.csv', index_col = '@id', keep_default_na = True)

# Graph to store the set of schemas
graph = Graph()

# Bind namespaces for clean serialization
namespace_manager = NamespaceManager(graph)
namespace_manager.bind('rdfs', RDFS, override = False)
namespace_manager.bind('skos', SKOS, override = False)
namespace_manager.bind('dcterms', DCTERMS, override = False)
namespace_manager.bind('togaf', Namespace('http://www.semanticweb.org/ontologies/2020/4/OntologyTOGAFContentMetamodel.owl#'), override = False)
namespace_manager.bind('togafvoc', Namespace('http://www.semanticweb.org/ontologies/2020/4/VocabularyTOGAFContentMetamodel.skos#'), override = False)
namespace_manager.bind('pav', Namespace('http://purl.org/pav/'), override = False)

g = rdfpandas.to_graph(df, namespace_manager)

# Serialize into ttl
ttl = g.serialize(format = 'turtle', indent = 2)

# Write out ttl into a file
ttl_file_name = 'VocabularyTOGAFContentMetamodelV2.ttl'
with open(ttl_file_name,'wb') as ttl_file:
    ttl_file.write(ttl)

# Serialize into JSON-LD with SKOS context to simplify development work
context = {'source': {'@id': 'http://purl.org/dc/terms/source', '@type': '@id'},
           'broader': {'@id': 'http://www.w3.org/2004/02/skos/core#broader', '@type': '@id'},
           'related': {'@id': 'http://www.w3.org/2004/02/skos/core#related', '@type': '@id'},
           'inScheme': {'@id': 'http://www.w3.org/2004/02/skos/core#inScheme', '@type': '@id'},
           'topConceptOf': {'@id': 'http://www.w3.org/2004/02/skos/core#topConceptOf', '@type': '@id'},
           'hasTopConcept': {'@id': 'http://www.w3.org/2004/02/skos/core#hasTopConcept', '@type': '@id'},
           'label': {'@id': 'http://www.w3.org/2000/01/rdf-schema#label'},
           'comment': {'@id': 'http://www.w3.org/2000/01/rdf-schema#comment'},
           'definedBy': {'@id': 'http://www.w3.org/2000/01/rdf-schema#definedBy', '@type': '@id'},
           'version': {'@id': 'http://purl.org/pav/version'},
           '@vocab': 'http://www.w3.org/2004/02/skos/core#'}

json = g.serialize(format = 'json-ld', context = context, indent = 2)

# Write out json into a file
json_file_name = 'VocabularyTOGAFContentMetamodelV2.json'
with open(json_file_name,'wb') as json_file:
    json_file.write(json)