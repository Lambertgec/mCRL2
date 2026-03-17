#!/usr/bin/env python3

import subprocess
import os
from pathlib import Path

# Change working dir to the script path
script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Formula files are stored one directory up from this script.
formula_dir = script_dir.parent / 'Formulas'

# Run the formulas on the worst strategic implementation of the first orchard game.
subprocess.run(['mcrl22lps', '-v', 'orchard_L worst.mcrl2', 'worst.lps'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max win prob.mcf'),  'worst.lps', 'worst max win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'worst max win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max defeat.mcf'),  'worst.lps', 'worst max defeat.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'worst max defeat.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min win large.mcf'),  'worst.lps', 'worst min win.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'worst min win.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Min turns large.mcf'),  'worst.lps', 'worst min turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'worst min turns.pres'], check=True)
subprocess.run(['lps2pres', '-v', '-m', '-f', str(formula_dir / 'Max turns large.mcf'),  'worst.lps', 'worst max turns.pres'], check=True)
subprocess.run(['pressolve', '-am', '-p20', 'worst max turns.pres'], check=True)