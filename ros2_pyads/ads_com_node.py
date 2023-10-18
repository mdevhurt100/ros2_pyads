import yaml
import rclpy
from rclpy.node import Node
from ros2_pyads.ads_com import AdsCom
import pyads


class ADSComNode(Node):

    def __init__(self):
        super().__init__('ads_com_node',
                         allow_undeclared_parameters=True,
                         automatically_declare_parameters_from_overrides=True)

        # Get the parameters from the launch file
        com_config = self.get_parameter('com_config').value
        plc_admin = self.get_parameter('plc_admin').value

        if not com_config:
            self.get_logger().fatal('Failed to get "com_config" parameter')
            exit(2)

        if not plc_admin:
            self.get_logger().fatal('Failed to get "plc_admin" parameter')

        # Load the config data from the YAML file
        with open(com_config, 'r') as file:
            com_config_data = yaml.safe_load(file)

        # Load the PLC admin data from the YAML file
        with open(plc_admin, 'r') as file:
            plc_admin_data = yaml.safe_load(file)

        # Initialize the ADS communication object
        self.ads_com = AdsCom(com_config_data, plc_admin_data)

        new_value = 10

        # Example write call to the PLC
        success = self.ads_com.write_by_name('MAIN.testVar', new_value, pyads.PLCTYPE_DWORD)

        b_success = self.ads_com.write_by_name(
            var_name='MAIN.bTestThing',
            var_value=not self.ads_com.read_by_name('MAIN.bTestThing', pyads.PLCTYPE_BOOL),  # Toggle the existing value
            var_type=pyads.PLCTYPE_BOOL)

        if not success:
            self.get_logger().error('Failed to write variable to PLC')

        if not b_success:
            self.get_logger().error('Failed to write variable to PLC')

        # Example read call from the PLC
        var = self.ads_com.read_by_name('MAIN.testVar', pyads.PLCTYPE_DWORD)

        if var is None:
            self.get_logger().error('Failed to read variable from PLC')
        elif var != new_value:
            self.get_logger().error('Read variable from PLC does not match written value')
        else:
            self.get_logger().info('Successfully wrote and read variable from PLC')


def main():
    rclpy.init()
    node = ADSComNode()
    # rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
