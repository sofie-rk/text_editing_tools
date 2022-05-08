from math import tan, pi

def SAM_surface(filename_coordinates, filename_topology, title, surface_bead, number_of_layers=3, lattice=10, x_box=0, y_box=0, z_box=0):

    file_coordinates = open('./results/'+filename_coordinates, 'w')
    file_coordinates.write(title+'\n')

    number_of_atoms = number_of_layers * lattice * lattice
    file_coordinates.write(str(number_of_atoms)+'\n')


    x_spacing = 0.4#0.497
    y_spacing = 0.4#0.497

    z_layer1 = 0.0 #0.5
    z_spacing = 0.4#0.497 #tan(pi/3) / y_spacing

    tilting = z_spacing / tan(pi/3)

    x_pos_init = 0.0
    y_pos_init = 0.0
    z_pos_init = z_layer1

    resname = ''
    counter = 1
    for i in range(number_of_layers):
        for j in range(lattice):
            for k in range(lattice):

                res_number = f'{1:5}'
                res_name = 'SURF '
                atom_name = '   '+str(surface_bead)
                atom_number = f'{counter:5}'

                x_pos = f'{x_pos_init+i*tilting+j*x_spacing:8,.3f}'
                y_pos = f'{y_pos_init+k*y_spacing:8,.3f}'
                z_pos = f'{z_pos_init+i*z_spacing:8,.3f}'


                file_coordinates.write(res_number+res_name+atom_name+atom_number+x_pos+y_pos+z_pos+'\n')

                counter += 1


    file_coordinates.write('   '+f'{x_box:.4f}' +' '+f'{y_box:.4f}'+' '+f'{z_box:.4f}' + '\n')
    file_coordinates.close()

    file_itp = open('./results/'+filename_topology, 'w')
    file_itp.write('[ moleculetype ]\n')
    file_itp.write(title + '\t' + str(3) + '\n\n')
    file_itp.write('[ atoms ]\n')

    counter_2 = 1
    for i in range(number_of_layers):
        for j in range(lattice):
            for k in range(lattice):
                atom_number = f'{counter_2:5}'
                atom_type = '         P2'
                res_number = f'{1:6}'
                resiude = ' 1SURF'
                atom = '     P2'
                cg_nr = f'{counter_2:5}'
                charge=f'{0:8.5f}'
                mass = f'{45:8.2f}'
                file_itp.write(atom_number+atom_type+res_number+resiude+atom+cg_nr+charge+mass+ '\n')

                counter_2+=1


    file_itp.close()
    return 0


SAM_surface('surface_P2.gro', 'surface_P2.itp', surface_bead='P2', title='hphil_surface', number_of_layers=3, lattice=20)
