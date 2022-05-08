from surface_constructer import *

hphob_hphil_surface('C1-surface.gro', 'C1-surface.itp', title='C1-surface', type_of_surface='C1', number_of_layers=2)

hphob_hphil_surface('EC-surface.gro', 'EC-surface.itp', title='EC-surface', type_of_surface='EC', number_of_layers=2, lattice=20)

hphob_hphil_surface('P1-surface.gro', 'P1-surface.itp', title='P1-surface', type_of_surface='P1', number_of_layers=2)

hphob_hphil_surface('SP2-surface.gro', 'SP2-surface.itp', title='SP2-surface', type_of_surface='SP2', number_of_layers=2)

hphob_hphil_surface('C6-surface.gro', 'C6-surface.itp', title='C6-surface', type_of_surface='C6', number_of_layers=2)