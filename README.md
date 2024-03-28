[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14512004)
# Project Optimystics

Closed loop optimization of hydrogel formulations using dynamic light scattering

## Overview

Hydrogels are hydrophilic crosslinked polymer networks with applications in cell cultures, drug delivery, and tissue engineering. Hydrogels' mechanical and rheological properties depend on the application and are a function of the hydrogel formulation, which consists of water, polymer, crosslinking agents, and other additives – which firmly control gelation. The convoluted interplay between the input parameters severely limits the ability to synthesise hydrogels with desired properties. Thus, a self-driving lab with machine-learning-assisted optimisation of the input parameters could optimise the gel formulation to synthesise gels with properties customised for specific applications. Unfortunately, the automated processing of soft, fragile hydrogels is challenging and further established gelation monitoring techniques are data-intensive and often unreliable. Herein, we propose using high-throughput compatible dynamic light scattering (DLS) to monitor gelation. The concentrations of various components and the crosslinking parameters can be varied using Bayesian optimisation to ‘discover’ the hydrogel formulations with the target mechanical and rheological properties using DLS.

## Youtube Video
https://youtu.be/Qbvq7uolQr8?si=ywHLhoCG1i3bCDJO

## Other Files 
Video Script.docx - Script for the youtube video <br>
PROJECT_POSTER.png - Poster for the project <br>
hydrogel background.docx - Background research <br>
BO_hackathon_example.py - Example code for integration <br>
Presentation_PDF.pdf - The presentation slides (plus some extra) for the video


## Setup command

See `postCreateCommand` from [`devcontainer.json`](.devcontainer/devcontainer.json).

## Run command
`pytest`

## Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
