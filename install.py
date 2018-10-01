# installer for meteorx driver
# Copyright 2016 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from setup import ExtensionInstaller

def loader():
    return MeteoRXInstaller()

class MeteoRXInstaller(ExtensionInstaller):
    def __init__(self):
        super(MeteoRXInstaller, self).__init__(
            version="0.49",
            name='meteorx',
            description='Collect data from the custom Davis PWS receiver via serial port',
            author="Jon Otaegi",
            files=[('bin/user', ['bin/user/meteorx.py', 'bin/user/windcal.dat'])]
            )
