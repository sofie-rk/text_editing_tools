def PDMS(filename, title, noChains, chainLength):

    file = open(filename, 'w')
    
    file.write(title+'\n')
    file.write(str(chainLength*noChains*2)+'\n')

    x_pos_init = 0.000
    y_pos_init = 0.000
    z_pos_init = 0.000

    space_between_chains = 0.600
    methyl_spacing = 0.299

    counter = 1
    for i in range(noChains):
        for j in range(chainLength):
            for k in range(2):
                res_number = '    '+str(i+1)
                res_name = 'PDMS '
                atom_name = '   C1'
                atom_number = f'{counter:5}'    

                x_pos = f'{x_pos_init+j*methyl_spacing:8,.3f}'
                y_pos = f'{y_pos_init+k*0.25 + i*space_between_chains:8,.3f}'
                z_pos = f'{z_pos_init:8,.3f}'
                
                file.write(res_number+res_name+atom_name+atom_number+x_pos+y_pos+z_pos+'\n')
                
                counter+=1
            
    file.write('0.000 0.000 0.000')
    
    file.close()


PDMS('test.txt', 'PDMS_surface', 5, 16)