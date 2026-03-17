#!/usr/bin/env python3

import subprocess
import os
from pathlib import Path

# Change working dir to the script path
script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Formula files are stored one directory up from this script.
formula_dir = script_dir.parent / 'Formulas'

# Run the formulas on the optimal strategic implementation of the first orchard game.
subprocess.run(['mcrl22lps', '-v', 'first_orchard optimal.mcrl2', 'optimal.lps'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max win prob.mcf'),  'optimal.lps', 'optimal max win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'optimal max win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max defeat.mcf'),  'optimal.lps', 'optimal max defeat.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'optimal max defeat.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min win small.mcf'),  'optimal.lps', 'optimal min win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'optimal min win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min turns classic.mcf'),  'optimal.lps', 'optimal min turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'optimal min turns.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max turns classic.mcf'),  'optimal.lps', 'optimal max turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'optimal max turns.pres'], check=True)