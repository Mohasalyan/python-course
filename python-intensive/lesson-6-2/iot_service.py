home_task_text = """ 
<div id='intro'>For the current exercise we gonna extend our SmartHouse application with a monitoring service for our SmartHouse application</div>

<div>Please find a brand new abstraction of <b>Device</b> class and use it for your devices.
Implement all the missing methods and do modifications to your existing methods.
The inital state of the device, should be <font color="blue" style="font-style:italic">Disconnected</font>.</div>
<br>
<div>
Create a new service 
<b>SmartHouseMonitoringService </b> in <i>smart_house_monitoring_service.py</i>.
Implement methods of the service:
<ul>
    <li>
<b>get_all_devices_serials(self) -> list[str]</b><br>
  Should return the list of serial numbers for devices
</li>
<li>
<b>check_state(self, devices: list[Device], serial_number: str) -> ConnectionState: </b><br>
  Should get the state of a device
</li>
</ul>
</div><br>
<div>
Update <b>SmartHouseService</b> with the following:
<li> inside <font font-weight="bold" color="#906090">__init__(self)</font> method create an instance of 
SmartHouseMonitoringService
</li>
<li> inside <font font-weight="bold" color="blue">start()</font> method if device was not connected, then we log with warning such information and remove the device from the list of devices. Else, we change the state of a device to <font color="blue" style="font-style:italic">Connected</font>. After that we log with information the list of connected devices.</li>
<li>inside <font font-weight="bold" color="blue">stop()</font> when device disconneted,
log with info that device has been disconnected and change its state to <font color="blue" style="font-style:italic">Disconnected</font>.</li>
</div><br>
<div>
Create another device <b>Computer</b> with the method <font font-weight="bold" color="blue">hybernate()</font>.
Update the service so that if a device can
hybernate, then during the stop we are <font font-weight="bold" color="red">NOT</font> changing its state, but log information that the device is hybernated and still connected to our service.
</div>
"""


def html_wrap(text: str) -> str:
    return f"""
<html>
<head>
<title>Hometask IOT Service</title>
</head>
<body>
{text}
</body>
</html>
    """


if __name__ == "__main__":
    html_file_path = "/mnt/data/Hometask.html"  # Save in /mnt/data/
    with open(html_file_path, "w") as hometask_file:
        hometask_file.write(html_wrap(home_task_text))
