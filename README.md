## weewx-meteorx

### About this Repository

This repository is a fork of [https://github.com/matthewwall/weewx-meteostick](https://github.com/matthewwall/weewx-meteostick) for use with custom receiver modules. It has been modified and fixed in numerous ways to better support these custom receivers. It strives to maintain compatibility with the Meteostick driver as much as possible and should be compatible with either the custom receiver or the one described in the [https://github.com/kobuki/VPTools](https://github.com/kobuki/VPTools) repo.  


### Installation

0) Install weeWX, select Simulator as the weather station

http://weewx.com/docs/usersguide.htm

1) Download the driver

wget -O weewx-meteorx.zip https://github.com/jonotaegi/weewx-meteorx/archive/master.zip

2) Install the driver

sudo wee_extension --install weewx-meteorx.zip

3) Configure the driver

sudo wee_config --reconfigure

4) Start weeWX

sudo /etc/init.d/weewx start
