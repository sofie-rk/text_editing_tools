
def PDMS_find_dimensions(x, y):
    '''
        x (float):  size of box in x-direction in nm
        y (float):  size of box in y-direction in nm
    '''

    print("No of chains: ", y/0.6)
    print("Chain length: ", x/0.299)

    return 0

def PDMS_get_box_dimensions(noChains, chainLength):

    print("x-length: ", (chainLength-1)*0.299)
    print("y-length: ", (noChains-1)*0.6 + 0.25)

PDMS_find_dimensions(10,10)