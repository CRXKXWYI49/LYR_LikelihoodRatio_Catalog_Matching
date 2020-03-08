# PythonLikelihoodRatio (LYR)
Likelihood ratio test for matching astronomical object counterparts in different wavelengths. The code was used to match the X-ray counterparts in the J1030 field, as described in Nanni et al. 2020.
If you use LYR please cite Nanni et al. 2020 and Peca et al. 2020 (in prep).

## The method
Source matching between different catalogs at different wavelengths can be computed using the Likelihood-Ratio (LR) technique. For the statistical and matematical background of the procedure, described firstly by Sutherland and Saunders 1992, we refer to e.g., Zamorani et al. 1999; Ciliegi et al. 2003; Brusa et al. 2007; Luo et al. 2010.

## Installation
LYR is written in Python 3.x. A proper operation with Python 2 is not guaranteed.
No installation required.
#### Packages
LYR is created with the following packages:
- numpy v1.15 (required)
- scipy v1.1 (required)
- sklearn v0.20 (required)
- matplotlib v3.0 (required)
- os (optional)
- time (optional)
- mpldatacursors (optional)
If you decide not to use the optional packages, the code obviously needs some changes.

## Settings
LYR requires two catalogs (input and output). The mandatory quantities are the positions (RA and Dec) in both catalogs and the magnitudes (or fluxes) in the input catalog.
For positional errors, fluxes, and flux uncertainties the user can choose from several options. Please refer to the manual.

The only file to be modified by the user is LYR input parameters.py. Every entry of this file is commented. All the parameter are also explained in the manual.

#### to run LYR, simply open the terminal and write python LYR_main.py


A very preliminary draft of the manual can be read and downloaded in the repository.
For questions and info write to: alessandro.peca@miami.edu
