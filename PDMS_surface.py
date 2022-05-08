def PDMS(filename_coord, filename_itp, title, noChains, chainLength):


    ### COORDINATE FILE ###
    file_coord = open(filename_coord, 'w')
    
    file_coord.write(title+'\n')
    file_coord.write(str(chainLength*noChains*2)+'\n')

    x_pos_init = 0.000
    y_pos_init = 0.000
    z_pos_init = 0.000

    space_between_chains = 0.600
    methyl_spacing = 0.299

    counter = 1
    for i in range(noChains):
        for j in range(chainLength):
            for k in range(2):
                res_number = f'{1:5}'
                res_name = 'PDMS '
                atom_name = '   C1'
                atom_number = f'{counter:5}'    

                x_pos = f'{x_pos_init+j*methyl_spacing:8,.3f}'
                y_pos = f'{y_pos_init+k*0.25 + i*space_between_chains:8,.3f}'
                z_pos = f'{z_pos_init:8,.3f}'
                
                file_coord.write(res_number+res_name+atom_name+atom_number+x_pos+y_pos+z_pos+'\n')
                
                counter+=1
            
    # MUST BE GENERALIZED
    file_coord.write('   10.00000  10.00000  10.00000')
    
    file_coord.close()

    ### ITP - FILE ###
    file_itp = open(filename_itp, 'w')

    file_itp.write('[ moleculetype ]\n')
    file_itp.write('PDMS_surface        3\n\n')

    file_itp.write('[ atoms ]\n')

    counter = 1
    for i in range(noChains):
        for j in range(chainLength):
            for k in range(2):
                nr = f'{counter+1:6}'
                type = '       PDMS'


# PDMS('test.txt', 'PDMS_surface', 5, 16)

# PDMS("PDMS_16x33_101010.gro", 'PDMS_surface', 16, 33)

PDMS('test_coord.txt', 'test_itp.txt', 'PDMS_surface', 3, 3)

PDMS('small_surface.gro', 'small_surface.itp', 'PDMS_surface', 3, 3)