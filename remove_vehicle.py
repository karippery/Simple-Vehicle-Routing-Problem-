def remove_vehicle():
#capacity1 = np.insert(capacity, 0,1)
    existing_vehicle = np.array(location_xy_ink_depot)[capacity.astype(bool),:]
    return existing_vehicle
remove_vehicle = remove_vehicle()
#print(np.sort(remove_vehicle,axis=1)
remove_vehicle = remove_vehicle.transpose((1, 0, 2))
