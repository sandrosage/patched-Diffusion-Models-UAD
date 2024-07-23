#!/bin/bash

echo "DDPM only"
python run.py experiment=MIDL23_DDPM/DDPM
echo "pDDPM (simplex)"
python run.py experiment=MIDL23_DDPM/DDPM_patched
echo "pDDPM (gaussian)"
python run.py experiment=MIDL23_DDPM/DDPM_patched_gaussian
echo "DONE"