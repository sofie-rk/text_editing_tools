
def PEG(filename, title, noAtoms, lattice):

    file = open(filename, 'w')

    file.write(title+'\n')
    file.write(str(noAtoms)+'\n')

    x_pos_init = 0.000
    y_pos_init = 0.000
    z_pos_init = 0.000

    spacing = 0.497

    counter = 1
    for i in range(lattice):
        for j in range(lattice):

            res_number = f'{1:5}'
            res_name = 'PEG  '
            atom_name = '   EC'
            atom_number = f'{counter:5}'

            x_pos = f'{x_pos_init+spacing*j:8,.3f}'
            y_pos = f'{y_pos_init+spacing*i:8,.3f}'
            z_pos = f'{z_pos_init:8,.3f}'


            file.write(res_number+res_name+atom_name+atom_number+x_pos+y_pos+z_pos+'\n')

            counter += 1

    file.write('0.000 0.000 0.000')
    file.close()

PEG('PEG_text.txt', 'PEG_surface', 100, 10)

