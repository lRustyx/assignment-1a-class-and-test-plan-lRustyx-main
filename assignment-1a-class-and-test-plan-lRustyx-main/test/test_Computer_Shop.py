'''
Unit test for Computer_shop class

Author: Justin Wong
Email: jxwong@uwaterloo.ca
Date: 6 October 2023
Student ID: 20701305


'''


import unittest
from Computer_Shop.Computer_Shop import ComputerShop, Gpu, Cpu, Mother_board, Ram, Power_supply, Nvme_storage, Sata_storage


class Test_computer_shop(unittest.TestCase):

    def setUp(self):
        # Cpu
        self.AMD_5600X = Cpu('AMD_5600X', 'AM4', 65, 220)
        self.AMD_7800X3D = Cpu('AMD_7800X3D', 'AM5', 120, 530)
        self.AMD_7950X = Cpu('AMD_7950X', 'AM5', 170, 750)
        self.AMD_3600 = Cpu('AMD_3600', 'AM4', 65, 140)
        self.Intel_13700K = Cpu('Intel_13700K', 'LGA1700', 125, 550)
        self.Intel_12600K = Cpu('Intel_12600K', 'LGA1700', 125, 320)
        self.Intel_10700K = Cpu('Intel_10700K', 'LGA1200', 125, 420)

        # Gpu
        self.AMD_7900XTX = Gpu('AMD_7900XTX', 300, 760)
        self.AMD_6800XT = Gpu('AMD_6800XT', 355, 1350)
        self.Nvidia_3060 = Gpu('Nvidia_3060', 170, 400)
        self.Nvidia_4070ti = Gpu('Nvidia_4070ti', 285, 1050)
        self.Nvidia_4090 = Gpu('Nvidia_4090', 450, 2200)

        # Ram
        self.Corsair_32GB_DDR5_6000 = Ram(
            'Corsair_32GB_DDR5_6000', 2, 5, 30, 125)
        self.Corsair_16GB_DDR4_3200 = Ram(
            'Corsair_16GB_DDR4_3200', 2, 4, 30, 50)

        # Motherboard
        self.MSI_Z690_A = Mother_board(
            'MSI_Z690_A', 'LGA1700', 4, 5, 4, 6, 50, 235)
        self.MSI_B560M = Mother_board(
            'MSI_B560M', 'LGA1200', 4, 4, 2, 4, 40, 120)
        self.MSI_B650M_A = Mother_board(
            'MSI_B650M_A', 'AM5', 4, 5, 2, 4, 40, 200)
        self.MSI_B550 = Mother_board('MSI_B550', 'AM4', 4, 4, 2, 4, 40, 190)

        # Power Supply
        self.Corsair_RM850x = Power_supply('Corsair_RM850x', 850, 165)
        self.Corsair_RM1000x = Power_supply('Corsair_RM1000x', 1000, 250)
        self.Corsair_TX550M = Power_supply('Corsair_TX550M', 550, 180)

        # NVME Storage
        self.Samsung_980_1TB = Nvme_storage('Samsung_980_1TB', 10, 100)
        self.Samsung_980_2TB = Nvme_storage('Samsung_980_2TB', 10, 245)

        # SATA Storage
        self.Seagate_Barracuda_2TB = Sata_storage(
            'Seagate_Barracuda_2TB', 10, 70)
        self.Seagate_Barracuda_4TB = Sata_storage(
            'Seagate_Barracuda_4TB', 10, 105)
        self.Seagate_Barracuda_8TB = Sata_storage(
            'Seagate_Barracuda_8TB', 10, 165)

    def test_initialization(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertEqual(computer.get_name(), 'CanadaComputers')
        self.assertEqual(computer.get_location(), '123 Batman Ave')

        computer = ComputerShop('PC Canada', '200 University Ave W')
        self.assertEqual(computer.get_name(), 'PC Canada')
        self.assertEqual(computer.get_location(), '200 University Ave W')

        # unusual
        computer = ComputerShop('23&6758GGU9489y*^&%&*^T',
                                '98709N879H7*&96876H98&H(*7h^98)')
        self.assertEqual(computer.get_name(), '23&6758GGU9489y*^&%&*^T')
        self.assertEqual(computer.get_location(),
                         '98709N879H7*&96876H98&H(*7h^98)')

        computer = ComputerShop('中国第一电脑店', '寒舍')
        self.assertEqual(computer.get_name(), '中国第一电脑店')
        self.assertEqual(computer.get_location(), '寒舍')

        # error
        computer = ComputerShop('', '')
        self.assertRaises(computer.get_name(), ValueError)
        self.assertRaises(computer.get_location(), ValueError)

        computer = ComputerShop(3.14159265, 1234546)
        self.assertRaises(computer.get_name(), TypeError)
        self.assertRaises(computer.get_location(), TypeError)

    def test_set_name(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_name('AmericanComputers')
        self.assertEqual(computer.get_name(), 'AmericanComputers')

        computer = ComputerShop('MicroCenter', '123 Batman Ave')
        computer.set_name('MacroCenter')
        self.assertEqual(computer.get_name(), 'MacroCenter')

        # unusual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_name('2334g653ggert\"g')
        self.assertEqual(computer.get_name(), '2334g653ggert\"g')

        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_name('加拿大计算机商店')
        self.assertEqual(computer.get_name(), '加拿大计算机商店')

        # error

        # New name is empty string
        computer = ComputerShop('McDonalds', '456 Superman Drive')
        computer.set_name('')
        self.assertRaises(computer.get_name(), ValueError)  # TODO

        # New name is not string
        computer = ComputerShop('MicroCenter', '123 Batman Ave')
        computer.set_name(123)
        self.assertRaises(computer.get_name(), TypeError)  # TODO

    def test_set_location(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_location('69420 blazeit highway')
        self.assertEqual(computer.get_location(), '69420 blazeit highway')

        computer = ComputerShop('MicroCenter', '123 Batman Ave')
        computer.set_location('5050 Thanos Lane')
        self.assertEqual(computer.get_location(), '5050 Thanos Lane')

        # unusual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_location('ty34g653gger\t\"g')
        self.assertEqual(computer.get_location(), 'ty34g653gger\t\"g')

        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        computer.set_location('加拿大计算机商店')
        self.assertEqual(computer.get_location(), '加拿大计算机商店')

        # error

        # New location is empty sting
        computer = ComputerShop('McDonalds', '456 Superman Drive')
        computer.set_location('')
        self.assertRaises(computer.get_location(), ValueError)
        # New location is not a string
        computer = ComputerShop('MicroCenter', '123 Batman Ave')
        computer.set_location(8392)
        self.assertRaises(computer.get_location(), TypeError)

    def test_get_inventory(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertEqual(computer.get_inventory(), {})

        computer = ComputerShop('CanadaComputers', '123 Batman Ave', {
                                'Nvidia_4070ti': self.Nvidia_4070ti})
        self.assertEqual(computer.get_inventory(), {'Nvidia_4070ti': 15})

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Nvidia_4070ti': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})

        # unusual

        # error

        pass

    def test_add_stock(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})
        computer.add_stock('Intel_13700K', 45)
        computer.add_stock('Corsair_32GB_DDR5_6000', 12)
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 60, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 27})

        # unusual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_12600K': {'component': self.Intel_12600K, 'stock': 15}, 'Samsung_980_2TB': {'component': self.Samsung_980_2TB, 'stock': 15}, 'Corsair_16GB_DDR4_3200': {'component': self.Corsair_16GB_DDR4_3200, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 15, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 15})
        computer.add_stock('Intel_12600K', 452389457902345782)
        computer.add_stock('Corsair_16GB_DDR4_3200', 128592810345)
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 452389457902345797, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 128592810360})

        # error

        # Adding stock to unregistered component
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})
        self.assertRaises(computer.add_stock(
            'Intel_12600K', 10), NameError)

        # Stock is not int
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_12600K': {'component': self.Intel_12600K, 'stock': 15}, 'Samsung_980_2TB': {'component': self.Samsung_980_2TB, 'stock': 15}, 'Corsair_16GB_DDR4_3200': {'component': self.Corsair_16GB_DDR4_3200, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 15, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 15})
        self.assertRaises(computer.add_stock(
            'Intel_12600K', 10.0), TypeError)

        # Stock is negative
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_12600K': {'component': self.Intel_12600K, 'stock': 15}, 'Samsung_980_2TB': {'component': self.Samsung_980_2TB, 'stock': 15}, 'Corsair_16GB_DDR4_3200': {'component': self.Corsair_16GB_DDR4_3200, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 15, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 15})
        self.assertRaises(computer.add_stock(
            'Intel_12600K', -1), ValueError)

        pass

    def test_remove_stock(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})
        computer.remove_stock('Intel_13700K', 1)
        computer.remove_stock('Corsair_32GB_DDR5_6000', 1)
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 14, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 14})

        # unusual

        # error

        # Removing stock of unregistered item
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})
        self.assertRaises(computer.remove_stock(
            'Intel_12600K', 10), NameError)

        # Stock not int
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_12600K': {'component': self.Intel_12600K, 'stock': 15}, 'Samsung_980_2TB': {'component': self.Samsung_980_2TB, 'stock': 15}, 'Corsair_16GB_DDR4_3200': {'component': self.Corsair_16GB_DDR4_3200, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 15, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 15})
        self.assertRaises(computer.remove_stock(
            'Intel_12600K', 10.0), TypeError)

        # Stock is negative
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_12600K': {'component': self.Intel_12600K, 'stock': 15}, 'Samsung_980_2TB': {'component': self.Samsung_980_2TB, 'stock': 15}, 'Corsair_16GB_DDR4_3200': {'component': self.Corsair_16GB_DDR4_3200, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_12600K': 15, 'Samsung_980_2TB': 15, 'Corsair_16GB_DDR4_3200': 15})
        self.assertRaises(computer.remove_stock(
            'Intel_12600K', -1), ValueError)

        # Value is more than stock
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {
                         'Intel_13700K': 15, 'Corsair_RM1000x': 15, 'Corsair_32GB_DDR5_6000': 15})
        self.assertRaises(computer.remove_stock(
            'Intel_13700K', 16), ValueError)

    def test_set_inventory(self):
        # usual

        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertEqual(computer.get_inventory(), {})
        computer.set_inventory({'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {
                               'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {
                         'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {
                         'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})

        computer.set_inventory({})
        self.assertEqual(ComputerShop.get_inventory(), {})

        # unusual

        # error

        # Component does not have parent class Computer_Component
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {'Intel_13700K': {'component': 'Intel_13700K', 'stock': 15}}, TypeError))

        # inventory reference key not string
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {13700: {'component': self.Intel_13700K, 'stock': 15}}, TypeError))

        # Stock not given
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {13700: {'component': self.Intel_13700K}}, ValueError))

        # component not given
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {'Intel_13700K': {'stock': 15}}, ValueError))

        # Stock negative
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {'Intel_13700K': {'component': self.Intel_13700K, 'stock': -1}}, ValueError))

        # Stock not int
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertRaises(computer.set_inventory(
            {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15.0}}, TypeError))

    def test_add_to_inventory(self):

        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertEqual(computer.get_inventory(), {})
        computer.add_to_inventory(self.Intel_13700K, 100)
        self.assertEqual(computer.get_inventory(), {'Intel_13700K': {
                         'component': self.Intel_13700K, 'stock': 100}})

        # stock is negative
        computer = ComputerShop('CanadaComputers', '123 Batman Ave')
        self.assertEqual(computer.get_inventory(), {})
        computer.add_to_inventory(self.Intel_13700K, -1)
        self.assertRaises(computer.get_inventory(), ValueError)

        # component already exists
        computer = ComputerShop('CanadaComputers', '123 Batman Ave', {
                                'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}})
        self.assertEqual(computer.get_inventory(), {})
        computer.add_to_inventory(self.Intel_13700K, 1)
        self.assertRaises(computer.get_inventory(), ValueError)

    def test_remove_from_inventory(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Ave', {
                                'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}})
        computer.remove_from_inventory('Intel_13700K')
        self.assertEqual(computer.get_inventory(), {})

        # item not in inventory
        computer = ComputerShop('CanadaComputers', '123 Batman Ave', {
                                'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}})
        computer.remove_from_inventory('Intel_12600K')
        self.assertRaises(computer.get_inventory(), ValueError)

    def test__available_in_inventory(self):
        # usual

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer._available_in_inventory([]), True)

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 15}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer._available_in_inventory(
            ['Intel_13700K', 'Corsair_RM1000x']), True)

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 1}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer._available_in_inventory(
            ['Intel_13700K', 'Intel_13700K', 'Corsair_RM1000x']), False)

        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 1}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertEqual(computer._available_in_inventory(
            ['Intel_13600K', 'Corsair_RM1000x']), False)

        # list entry not string
        computer = ComputerShop('CanadaComputers', '123 Batman Ave',
                                {'Intel_13700K': {'component': self.Intel_13700K, 'stock': 1}, 'Corsair_RM1000x': {'component': self.Corsair_RM1000x, 'stock': 15}, 'Corsair_32GB_DDR5_6000': {'component': self.Corsair_32GB_DDR5_6000, 'stock': 15}})
        self.assertRaises(computer._available_in_inventory(
            ['Intel_13600K', 12345]), TypeError)

        pass

    def test__get_price(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(computer._get_price(components), 2535)

        components = []
        self.assertEqual(computer._get_price(components), 0)

        components = [self.AMD_7950X, self.MSI_B650M_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4090, self.Corsair_RM1000x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(computer._get_price(components), 3935)

        pass

    def test__validate_number_components(self):
        # usual
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), True)

        # unusual
        components = [self.Intel_12600K, self.MSI_B550, self.Corsair_16GB_DDR4_3200,
                      self.Corsair_RM850x, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), True)

        # error

        # Two CPU
        components = [self.Intel_13700K, self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # No CPU
        components = [self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # Two motherboard
        components = [self.Intel_13700K, self.MSI_Z690_A, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # No motherboard
        components = [self.Intel_13700K, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # Two power supplies
        components = [self.Intel_13700K, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # No power supply
        components = [self.Intel_13700K, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # No storage
        components = [self.Intel_13700K, self.MSI_Z690_A,
                      self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti, self.Corsair_RM850x]
        self.assertEqual(
            computer._validate_number_components(components), False)
        # No RAM
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_number_components(components), False)

    def test__validate_cpu_motherboard_combination(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        # usual
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)

        components = [self.Intel_10700K, self.MSI_B560M, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)

        components = [self.AMD_5600X, self.MSI_B550, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)

        components = [self.AMD_7950X, self.MSI_B650M_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)

        # unusual
        components = [self.Intel_13700K, self.MSI_Z690_A]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)
        components = [self.AMD_5600X, self.MSI_B550]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), True)

        components = [self.Intel_13700K, self.MSI_B560M, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), False)

        components = [self.AMD_7800X3D, self.MSI_B550, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_cpu_motherboard_combination(components), False)

        pass

    def test__validate_ram_motherboard_combination(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        # usual
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_ram_motherboard_combination(components), True)

        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_ram_motherboard_combination(components), True)

        # Too many RAM
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Corsair_32GB_DDR5_6000,
                      self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_ram_motherboard_combination(components), False)
        # DDR mismatch
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_16GB_DDR4_3200,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_ram_motherboard_combination(components), False)
        components = [self.AMD_5600X, self.MSI_B550, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_ram_motherboard_combination(components), False)

    def test__validate_power_requirement(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        # usual
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_power_requirement(components), True)

        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM1000x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_power_requirement(components), True)

        components = [self.AMD_7950X, self.MSI_B650M_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4090, self.Corsair_TX550M, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_power_requirement(components), False)

    def test__validate_storage_motherboard_combination(self):
        computer = ComputerShop('CanadaComputers', '123 Batman Drive')

        # usual
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000,
                      self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_storage_motherboard_combination(components), True)
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Samsung_980_2TB, self.Samsung_980_2TB, self.Samsung_980_2TB]
        self.assertEqual(
            computer._validate_storage_motherboard_combination(components), True)
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti,
                      self.Corsair_RM850x, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_storage_motherboard_combination(components), True)

        # Too many NVME drives
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti, self.Corsair_RM850x,
                      self.Samsung_980_2TB, self.Samsung_980_2TB, self.Samsung_980_2TB, self.Samsung_980_2TB, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_storage_motherboard_combination(components), False)

        # Too many SATA drives
        components = [self.Intel_13700K, self.MSI_Z690_A, self.Corsair_32GB_DDR5_6000, self.Nvidia_4070ti, self.Corsair_RM850x, self.Samsung_980_2TB, self.Seagate_Barracuda_8TB,
                      self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB, self.Seagate_Barracuda_8TB]
        self.assertEqual(
            computer._validate_storage_motherboard_combination(components), False)
