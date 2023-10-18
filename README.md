# ros2_pyads
This is a ros2 package that will be a wrapper around the pyads library to have communication between ros2 and beckhoff PLCs.

# Configuration

## Communications:

Read the [com_config.yaml](config/com_config.yaml) file in the config directory carefully and set up the inputs, here is an example:

```yaml
# This configuration file is used to set up the pyads library objects to establish communication between
# a machine with ROS2 and a machine running the TwinCat PLC Software.

# The IP address should match the machine with ROS2 with the
# added '.1.1' on the end of the IP address.
sender_ams: '192.168.33.10.1.1'
# This is the IP address of the host machine with the TwinCat Software
plc_ip: '192.168.33.4'
# This is arbitrarily named
route_name: 'ROS2PLC'
# This should match the plc_ip address
host_name: '192.168.33.4'
# This is gotten from the TwinCat System About menu "AMS Net id"
remote_ads: '10.100.101.14.1.1'
```

## Administrator Access:

