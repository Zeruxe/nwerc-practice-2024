
small_number = 1e-6

def calculate_optimal_height(H, R, density_air, density_water):
    def center_of_mass(hw):
        ha = H - hw  #* Height of the air
        cw = hw / 2  #* Center of mass of the water
        ca = H - ha / 2  #* Center of mass of the air
        return (ca * density_air * ha + cw * density_water * hw) / (density_air * ha + density_water * hw)
            #* above i compute the center of mass

    left, right = 0, H
    while right - left > small_number:  
        middle1 = left + (right - left) / 3
        middle2 = right - (right - left) / 3
        
        center1 = center_of_mass(middle1)
        center2 = center_of_mass(middle2)
        if center1 < center2:
            right = middle2
        else:
            left = middle1
    return (left + right) / 2

H, R, density_air, density_water = map(int, input().split())
optimal_height = calculate_optimal_height(H, R, density_air, density_water)
print(f"{optimal_height:.10f}")


#* Some comments are added in the code incase of code review so I can easier remember what I did