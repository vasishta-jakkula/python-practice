print('Welcome to the Life Series(version 1)!\n There are three gamemodes so far, Third Life, Last Life, and Limited Life')
input_lifeseries_version = input(' (input a num) Which life series type will you do? 1.Third Life, 2. Last Life 3. Limited Life')
if input_lifeseries_version == "1":
    from lifeseriesThirdLife import *

elif input_lifeseries_version == "2":
    pass

elif input_lifeseries_version == "3":
    pass

else:
    print("Is not a valid version of the life series , pls try again or update to latest version")

