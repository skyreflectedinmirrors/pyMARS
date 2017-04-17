#test create_trimmed_model

"""
file:
    create_trimmed_model

test parameters:
    number of species eliminated
    number of reactions eliminated
"""

"""Note: this test can ONLY be run from py.test"""

#import modules
import cantera as ct
from pyMARS import create_trimmed_model as func

#define function inputs
data_file = ('gri30.xml')
exclusion_list = ['O2', 'CO2']
#def trim(solution_object, exclusion_list, file_name):
soln = ct.Solution('gri30.xml')
#call function
result = func.trim(soln, exclusion_list, data_file,)
initial_solution = result[0]
new_solution = result[1]


def test_n_species():
    n_initial_species = initial_solution.n_species
    n_new_species = new_solution.n_species
    assert n_initial_species > n_new_species
    print('%s initial species, %s final species')\
            %(n_initial_species, n_new_species)


def test_n_reactions():
    n_initial_reactions = initial_solution.n_reactions
    n_new_reactions = new_solution.n_reactions
    assert n_initial_reactions > n_new_reactions
    print('%s initial reactions, %s final reactions')\
            %(n_initial_reactions, n_new_reactions)
