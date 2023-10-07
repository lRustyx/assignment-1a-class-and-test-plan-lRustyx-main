'''
Computer_Shop.py


Computer_Shop is a class that represents a computer shop which contains its 
name, location, inventory and a method to place order for a computer with a list of components 
and verify if it creates a valid computer and return the price if it is. 
The specifications of the computer components are stored in objects of their respective classes.

Author: Justin Wong
Email: jxwong@uwaterloo.ca
Date: 6 October 2023
Student ID: 20701305

'''


class ComputerShop:

    def __init__(self, name, location, inventory={}):
        '''
        initialization of the computer shop takes in the name and location of the computer shop
        also creates an empty inventory if not given
        '''

        pass

    def get_name(self):
        '''
        returns the name of the computer shop 

        parameters:
            none
        return:
                name of computer shop: str

        '''
        pass

    def set_name(self, new_name: str):
        '''
        sets a new name for the computer shop
        throws exception if new_name is empty string
        parameters:
            new_name (string): new name of the computer shop
        return:
            none

        '''
        pass

    def get_location(self):
        '''
        returns the location of the computer shop

        parameters:
            none

        return:
            location of computer shop: str

        '''
        pass

    def set_location(self, new_location: str):
        '''
        sets a new location for the computer shop
        throws exception if location is empty string

        input: 
            new_location (str): new location of the computer shop

        return:
            none

        '''
        pass

    def add_stock(self, component: str, quantity: int):
        '''
        Increases the stock of an item in the inventory.
        Throws exception if item not in inventory

        parameters:
            name (string): name of component
            quantity(int): quantity of components

        return:
            none


        '''
        pass

    def remove_stock(self, component, quantity: int):
        '''
        Decreases the stock of an item in the inventory.
        Throws exception if item not in inventory, quantity is negative or greater than current stock
        parameters:
            component (string): name of component
            quantity(int): quantity of components
        return:
            if stock change is success: 

        '''
        pass

    def get_inventory(self):
        '''
        returns the inventory

        parameters:
            none
        return:
            inventory (dict): dictionary of components in inventory containing the component object and the stock

        '''
        pass

    def set_inventory(self, inventory):
        '''
        sets the inventory of the computer shop to the input
        throws an exception if format of input does not match the correct format and datatypes and if stock is negative
        parameters:
            inventory (dict): dictionary of components in inventory containing the component object and the stock
        return:
            none

        '''
        pass

    def add_to_inventory(self, component, quantity):
        '''
        add new item to the inventory
        throws an exception if item already exists in inventory or if stock is negative

        parameters:
            component (Computer_Component): component to be added 
            quantity (int): stock
        return:
            none

        '''
        pass

    def remove_from_inventory(self, component):
        '''
        remove an item from inventory
        throws an exception if item does not exist in inventory

        parameters:
            component (string): name of component to be removed 
        return:
            none

        '''
        pass

    def check_order(self, components: list):
        '''
        checks if the components are available in inventory and forms a valid computer and 
        returns the price of all the components if valid 
        Is a wrapper function for the checking process. Does not throw exceptions 

        parameters:
            components (list): list of components (string)

        return:
            price (float): the total price of all components


        '''
        pass

    def _available_in_inventory(self, components: list):
        '''
        checks if all the components are available in inventory
        Throws exception if any entry in the input is not a string

        parameters:
            components (list): list of components (string)

        return:
            availability (bool)

        '''
        pass

    @staticmethod
    def _get_price(components: list):
        '''
        Gets total price of the components

        parameters:
            components (list): list of components (Computer_Component)

        return:
            total price (float)

        '''
        pass

    @staticmethod
    def _validate_component_configuration(components: list):
        '''
        Validates if the components result in a valid computer.
        Is a wrapper function for all validation functions

        outputs True if configuration is valid and False otherwise

        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)
        '''
        pass

    @staticmethod
    def _validate_number_components(components: list):
        '''
        Checks that there are exactly 1 motherboard, CPU and power supply 
        and at least 1 storage device and RAM

        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)
        '''

        pass

    @staticmethod
    def _validate_cpu_motherboard_combination(components: list):
        '''
        Checks and returns if the socket type of the CPU matches the motherboard
        returns a boolean

        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)
        '''
        pass

    @staticmethod
    def _validate_ram_motherboard_combination(components: list):
        '''
        Checks if RAM and the motherboard have a compatible memory type and if there are
        sufficient slots on motherboard

        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)
        '''
        pass

    @staticmethod
    def _validate_storage_motherboard_combination(components: list):
        '''
        Checks if motherboard has sufficient slots to house all the storage devices


        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)
        '''
        pass

    @staticmethod
    def _validate_power_requirement(components: list):
        '''
        Checks if power supply is sufficient to power all the components

        parameters:
            components (list): list of components (Computer_Component)

        return:
            if validation is successful (bool)

        '''
        pass


class Computer_Component:

    def __init__(self, name: str, power: int, price: float):
        self._name = name
        self._power = power
        self._price = price

    def get_name(self):
        pass

    def get_price(self):
        pass

    def get_power(self):
        pass


class Mother_board(Computer_Component):

    def __init__(self, name: str, socket_type: str, ram_slots: int, ddr_version: int, nvme_slots: int, sata_slots: int, power: int, price: float):
        self._socket_type = socket_type
        self._ram_slots = ram_slots
        self._ddr_version = ddr_version
        self._nvme_slots = nvme_slots
        self._sata_slots = sata_slots
        super().__init__(name, power, price)

    def get_socket_type(self):
        pass

    def get_ram_slots(self):
        pass

    def get_ddr_version(self):
        pass

    def get_nvme_slots(self):
        pass


class Cpu(Computer_Component):

    def __init__(self, name: str, socket_type: str, power: int, price: float):
        self._socket_type = socket_type
        super().__init__(name, power, price)

    def get_socket_type(self):
        pass


class Gpu(Computer_Component):

    def __init__(self, name: str, power: int, price: float):
        super().__init__(name, power, price)


class Ram(Computer_Component):

    def __init__(self, name: str, number_of_slots: int, ddr_version: int, power: int, price: float):
        self._number_of_slots = number_of_slots
        self._ddr_version = ddr_version
        super().__init__(name, power, price)

    def get_number_of_slots(self):
        pass

    def get_ddr_version(self):
        pass


class Power_supply(Computer_Component):

    def __init__(self, name: str, power: int, price: float):
        super().__init__(name, power, price)


class Nvme_storage(Computer_Component):

    def __init__(self, name: str,  power: int, price: float):
        super().__init__(name, power, price)


class Sata_storage(Computer_Component):

    def __init__(self, name: str,  power: int, price: float):
        super().__init__(name, power, price)
