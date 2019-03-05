---
title: 'Onyx: Automatic calculation of isotope effects'
tags:
  - Python
  - chemistry
  - organic chemistry
  - isotope effect
  - graphical user interface
authors:
  - name: Alexander C. Brueckner
    orcid: 0000-0001-5866-0878
    affiliation: 1
  - name: O. Maduka Ogba
    orcid: 0000-0002-5718-6761
    affiliation: “1, 2, 3”
  - name: Sebastian L. Cevallos
    orcid: 0000-0002-1983-9522
    affiliation: “2, 4”
  - name: Daniel W. Walden
    orcid: XXXX-XXXX-XXXX-XXXX
    affiliation: “1, 5”
  - name: Daniel J. O’Leary
    orcid: 0000-0002-2887-2957
    affiliation: 2
  - name: Paul H.-Y. Cheong
    orcid: 0000-0001-6705-2962
    affiliation: 1
affiliations:
  - name: Department of Chemistry, Oregon State University, United States
    index: 1
  - name: Chemistry Department, Pomona College, United States
    index: 2
  - name: Schmid College of Science and Technology, Chapman University, United States
    index: 3
  - name: Atlassian, United States
    index: 4
  - name: Chemistry Department, École Normale Supérieure de Lyon, France
    index: 5
date: DD Month 2019 # TODO: update this
bibliography: paper.bib
---

# Summary

Validation of theoretical models is crucial to the success of computational-experimental collaborative research projects. The juxtaposition of computed isotope effects to experiments (enriched or natural abundance; kinetic or equilibrium) is a proven, robust way to achieve this [Ref]. When performed correctly, experiments and computations reveal the exact atomic motions and positions in equilibrating structures and during rate-determining steps in chemical transformations. Unfortunately, the steps required to calculate isotope effect values from quantum mechanically (QM) computed structures are labor intensive, tedious, and error-prone.

Onyx is a Python package for the automatic calculation of isotope effects from theoretical models. Although several widely-distributed software packages for isotope effect calculations exist (e.g., BEBOVIB, ISOEFF, QUIVER),[Ref] Onyx provides unparalleled functionality and usability to computational and experimental scientists. It implements both the Bigeleisen-Mayer[Ref] and rigid-rotor[Ref] methods, calculates the Bell tunneling correction[Ref], and breaks down the isotope effect into chemically-relevant terms (e.g. enthalpy, entropy, zero-point energy). Additionally, Onyx provides the ability to calculate the theoretical proton chemical shift difference. By leveraging the data from theoretical models, Onyx allows the user to identify isomers of interest in an efficient and cost-effective manner.

For ease of use, Onyx features both a graphical user interface (GUI) and an optional command-line interface to facilitate routine calculations of isotope effects for users with and without programming expertise. Onyx was designed for chemistry/biochemistry researchers and students in courses focused on chemical mechanisms. Several recent scientific publications use Onyx [Ref], and ongoing research projects continue to implement it. The unique functionality and usability of the Onyx program will streamline and enable future scientific explorations in complex chemical systems. GitHub archived the source code for Onyx with the linked DOI: [Ref]

# Acknowledgements

PHYC is the Bert and Emelyn Christensen professor of OSU and gratefully acknowledges financial support from the Vicki & Patrick F. Stone family. ACB, OMO, DMW, and PHYC acknowledge the National Science Foundation (NSF, CHE-1352663), and the computing infrastructure in part provided by the NSF Phase-2 CCI, Center for Sustainable Materials Chemistry (NSF CHE-1102637). Pomona team & other acknowledgements.

# References
