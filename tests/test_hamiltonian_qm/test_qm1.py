#*********************************************************************************
#* Copyright (C) 2015 Alexey V. Akimov
#*
#* This file is distributed under the terms of the GNU General Public License
#* as published by the Free Software Foundation, either version 2 of
#* the License, or (at your option) any later version.
#* See the file LICENSE in the root directory of this distribution
#* or <http://www.gnu.org/licenses/>.
#*
#*********************************************************************************/

###################################################################
# Tutorial: Here is another version of MD: RB-MD via Systems objects
###################################################################

import os
import sys
import math

# Fisrt, we add the location of the library to test to the PYTHON path
cwd = os.getcwd()
print "Current working directory", cwd
sys.path.insert(1,cwd+"/../../_build/src/mmath")
sys.path.insert(1,cwd+"/../../_build/src/chemobjects")
sys.path.insert(1,cwd+"/../../_build/src/hamiltonian")
sys.path.insert(1,cwd+"/../../_build/src/dyn")

print "\nTest 1: Importing the library and its content"
from cygmmath import *
from cygchemobjects import *
from cyghamiltonian import *
from cygdyn import *

from LoadPT import * # Load_PT
from LoadMolecule import * # Load_Molecule
from LoadUFF import*



# Create Universe and populate it
U = Universe()
verbose = 0
Load_PT(U, "elements.dat", verbose)


verb = 0
assign_rings = 1



#======= System ==============
for i in [1]:
    print "=================== System ",i,"======================="

    syst = System()
    Load_Molecule(U, syst, os.getcwd()+"/1water.ent", "pdb")
    
#    syst.determine_functional_groups(1)  # 
    syst.show_atoms()
#    syst.init_fragments()

    print "Number of atoms in the system = ", syst.Number_of_atoms
    atlst1 = range(1,syst.Number_of_atoms+1)


    # Creating Hamiltonian
    ham = Hamiltonian_Atomistic(1, 3*syst.Number_of_atoms)
#    ham.set_Hamiltonian_type("QM")

#    ham.set_interactions_for_atoms(syst, atlst1, atlst1, uff, verb, assign_rings)  
#    ham.show_interactions_statistics()
   
#    ham.set_system(syst)
#    ham.compute()


    print "Energy = ", ham.H(0,0), " a.u."
    print "Force 1 = ", ham.dHdq(0,0,0), " a.u."
    print "Force 3 = ", ham.dHdq(0,0,3), " a.u."




