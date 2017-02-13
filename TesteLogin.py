# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
device.installPackage('/home/pmario/AndroidStudioProjects/ConnectUFSCar-master/app/build/outputs/apk')

# sets a variable with the package's internal name
package = 'br.ufscar.connect'

# sets a variable with the name of an Activity in the package
activity = 'br.ufscar.connect.activities.LoginActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)

MonkeyRunner.sleep(2)
device.wake()
#device.touch(100,260,MonkeyDevice.DOWN_AND_UP)
device.touch(100,200,MonkeyDevice.DOWN_AND_UP)
device.type('User_test')
MonkeyRunner.sleep(1)
device.touch(295,466,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
#device.press("KEYCODE_ENTER", MonkeyDevice.DOWN_AND_UP)
device.type('a')
#MonkeyRunner.sleep(1)
#device.touch(294,446,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
device.touch(171,332,MonkeyDevice.DOWN_AND_UP)
#device.press("FLAG_EDITOR_ACTION", MonkeyDevice.DOWN_AND_UP)
#aperta o ok denovo pra fazer login
#device.press("KEYCODE_ENTER", MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(4)
# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('testeLogin.png','png')



