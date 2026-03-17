#!/usr/bin/env python3

import subprocess
import os
from pathlib import Path

# Change working dir to the script path
script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Formula files are stored one directory up from this script.
formula_dir = script_dir.parent / 'Formulas'

# Run the formulas on the generic implementation of the first orchard game.
subprocess.run(['mcrl22lps', '-v', 'first_orchard.mcrl2', 'generic.lps'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max win prob.mcf'),  'generic.lps', 'generic max win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'generic max win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max defeat.mcf'),  'generic.lps', 'generic max defeat.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'generic max defeat.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min win small.mcf'),  'generic.lps', 'generic min win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'generic min win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min turns classic.mcf'),  'generic.lps', 'generic min turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'generic min turns.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max turns classic.mcf'),  'generic.lps', 'generic max turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'generic max turns.pres'], check=True)