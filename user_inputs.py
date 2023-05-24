## Create function for prompting the user to input the desired RPM and returns the value to be given to the VFD frequency address
## Returns the string "NaN" if the user input is not a number
## Returns the string "OL" if the user input is outside the limits of 0-60Hz
def set_user_speed(speed):
    try:
        speed_int = int(float(speed)*10)
    except ValueError:
        return "NaN"
    else:
        if isinstance(speed_int, int):
            if speed_int >=600 and speed_int <=1200:
                return speed_int
            else:
                return "OL"
        else:
            return "NaN"
