<<<<<<< HEAD
""" Climate Analysis Toolkit"""
=======
" Climate analysis tool"
>>>>>>> 6c7532e8480c54526faccd0d2fb7fca3e6a79a06

import sys
import temp_conversion
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, script + ": requires filename"
filename = sys.argv[1]

climate_data = open(filename, 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        # don't process invalid temperature readings of -9999
        if fahr != -9999:
            celsius = temp_conversion.fahr_to_celsius(fahr)
            kelvin = temp_conversion.fahr_to_kelvin(fahr)

            print(str(celsius)+", "+str(kelvin))
<<<<<<< HEAD
# TODO: "Addd a fucntios to process rainfall data"
=======

#TODO(smanghan): Add call to process rainfall
>>>>>>> 6c7532e8480c54526faccd0d2fb7fca3e6a79a06
