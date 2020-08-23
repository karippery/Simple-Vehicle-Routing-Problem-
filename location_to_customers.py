def new_xy_point():
    # data to be resides in 1st quadrant 0,90
    return np.around(uniform(0,90), decimals=2),np.around(uniform(0,90), decimals=2)
def get_locations_as_xy(population_len,cromosome_len):
    array_xy = []
    for i in range(population_len):
        row =[]
        points = (new_xy_point() for x in range(cromosome_len)) 
        for point in points:
            row.append(point)
        array_xy.append(row)
    return array_xy
