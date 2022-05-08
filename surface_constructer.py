
def hphob_hphil_surface(filename_coordinates, filename_topology, title, type_of_surface, number_of_layers=3, lattice=20):

    file_coordinates = open('./results/'+filename_coordinates, 'w')
    file_coordinates.write(title+'\n')

    number_of_atoms = number_of_layers * lattice * lattice
    file_coordinates.write(str(number_of_atoms)+'\n')

    x_spacing = 0.497
    y_spacing = 0.497
    z_spacing = 0.497

    x_pos_init = 0.0
    y_pos_init = 0.0
    z_pos_init = 0.0

    tilting = x_spacing/2

    counter = 1

    for i in range(number_of_layers):
        for j in range(lattice):
            for k in range(lattice):

                res_number = f'{1:5}'
                res_name = 'SURF '
                atom_name = '   '+str(type_of_surface)
                atom_number = f'{counter:5}'

                x_pos = f'{x_pos_init+(i%2)*tilting+j*x_spacing:8,.3f}'
                y_pos = f'{y_pos_init+(i%2)*tilting+k*y_spacing:8,.3f}'
                z_pos = f'{z_pos_init+i*z_spacing:8,.3f}'

                file_coordinates.write(res_number+res_name+atom_name+atom_number+x_pos+y_pos+z_pos+'\n')

                counter += 1

    file_coordinates.write('   '+f'{0.0:.4f}' +' '+f'{0.0:.4f}'+' '+f'{0.0:.4f}' + '\n')
    file_coordinates.close()

    file_itp = open('./results/'+filename_topology, 'w')
    file_itp.write('[ moleculetype ]\n')
    file_itp.write(title + '\t' + str(3) + '\n\n')
    file_itp.write('[ atoms ]\n')

    counter = 1

    if type_of_surface == 'C1':
        atom_type = '         C1'
        mass = f'{72:8.2f}'
    elif type_of_surface == 'EC':
        atom_type = '       SN3r'
        mass = f'{45:8.2f}'
    elif type_of_surface == 'P1':
        atom_type = '         P1'
        mass = f'{72:8.2f}'
    elif type_of_surface == 'SP2':
        atom_type = '        SP2'
        mass = f'{54:8.2f}'
    elif type_of_surface == 'C6':
        atom_type = '         C6'
        mass = f'{72:8.2f}'
    for i in range(number_of_layers):
        for j in range(lattice):
            for k in range(lattice):
                atom_number = f'{counter:5}'
                res_number = f'{1:6}'
                resiude = ' 1SURF'
                atom = '     '+str(type_of_surface)
                cg_nr = f'{1:5}'
                charge=f'{0:8.5f}'
                file_itp.write(atom_number+atom_type+res_number+resiude+atom+cg_nr+charge+mass+ '\n')

                counter+=1


    file_itp.close()


