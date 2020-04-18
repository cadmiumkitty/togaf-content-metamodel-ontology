# TOGAF Content Metamodel Ontology

This is version 2.0 of the TOGAF Content Metamodel ontology. It is based on the Content Metamodel of the TOGAF Version 9.2 standard. See [TOGAF 9.2 Content Metamodel](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap30.html) for the complete set of entities, attributes and relationships.

## Changes in version 2 of the ontology

 1. Uses the name `Business Service` instead of `Service` to stay consistent with the original ontology and TOGAF 9.2 Metamodel Figure 30-7.
 1. Adds decomposition and relevant inverse properties that were missing in the version 1 of the metamodel ontology.
 1. Adds `Business Capability` decomposition and inverse properties that are absent in TOGAF 9.2 to make this ontology more practical. In most cases, people are interested in business capabilities breakdown and impact assessment.
 1. Adds inverse property flag for `communicates with` and `related to` properties for `Logical Application Component`, `Function` and `Physical Application Component`.
 1. Collapses multiple properties from TOGAF 9.2 using AndOr` convention to improve the usability of the ontology. Properties can be sub-classed later if needed.
 1. Keeps `precedes of follows` as a single property of `Process` as per TOGAF 9.2 section 30.7. Properties can be sub-classed later if needed.
 1. Fixes inconsistent property naming in TOGAF 9.2 section 30.7 to create `togaf:informationSystemServiceIsUsedByDataEntity`, `togaf:logicalApplicationComponentIsUsedByLogicalDataComponent` and `togaf:physicalApplicationComponentIsUsedByPhysicalDataComponent` to improve usability of the ontology.
 1. Fixed inconsistent property naming for `Business Capability` in TOGAF 9.2 by using `togaf:businessCapabilityIsUsedByOrganizationUnit`
 1. Removes duplicate `togaf:logicalTechnologyComponentServesLogicalApplicationComponent` found in TOGAF 9.2 section 30.7.
 1. Adds `category` property with domain of `togaf:ContentClassification` and no range specified to improve usability. Although linking to SKOS `Concept` is preferred, there are no limitations as to what resource can be used to specify the category of an entity.

## Ontology Versioning Choices

Given low prior adoption of the ontology and disruptive changes to many classes disjoint statements due to Location moving to General Entities, the decision is to adopt entirely new Ontology URI for TOGAF 9.2. For earlier discussion on ontology versioning see (http://ontologydesignpatterns.org/wiki/Community:Versioning_and_URIs) and (https://www.w3.org/TR/owl-guide/#OntologyVersioning).

## Prior Work

Original from https://sites.google.com/site/ontologyprojects/home/togaf-core-content-metamodel is used with permission from Aurona Gerber. Subsequent modifications are released with Creative Commons Attribution-ShareAlike 4.0 International license.

Based on the paper [Towards the Formalisation of the TOGAF Content Metamodel using Ontologies](https://www.researchgate.net/publication/220708864_Towards_the_Formalisation_of_the_TOGAF_Content_Metamodel_using_Ontologies) by Aurona Gerber, Paula Kotze and Alta van der Merwe which is using [TOGAF 9.1 Content Metamodel](https://pubs.opengroup.org/architecture/togaf91-doc/arch/chap34.html).

A regulatory impact analysis solution based on the ontology was presented at the [Semantic Web London](https://www.meetup.com/semantic-web-london/) meetup. Source code is available on https://github.com/cadmiumkitty/ontologies-for-enterprise-architecture, and the slides are on https://www.slideshare.net/EugeneMorozov/documenting-enterprise-architectures-using-ontologies.

## Immediate Next Steps

 1. Include the SKOS version of TOGAF concepts.
 1. Add [Semantic MediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) mappings to the repository.