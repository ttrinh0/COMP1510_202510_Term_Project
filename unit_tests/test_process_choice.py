from unittest import TestCase


import check

class Test(TestCase):

    def test_process_choice_north(self):
        expected = check.process_choice("North")
        actual = 'Movement'
        self.assertEqual(expected, actual)

    def test_process_choice_south(self):
        expected = check.process_choice("South")
        actual = 'Movement'
        self.assertEqual(expected, actual)

    def test_process_choice_east(self):
        expected = check.process_choice("East")
        actual = 'Movement'
        self.assertEqual(expected, actual)

    def test_process_choice_west(self):
        expected = check.process_choice("West")
        actual = 'Movement'
        self.assertEqual(expected, actual)

    def test_process_choice_fish(self):
        expected = check.process_choice("Fish")
        actual = 'Fish'
        self.assertEqual(expected, actual)

    def test_process_choice_interact(self):
        expected = check.process_choice("Interact")
        actual = 'Interact'
        self.assertEqual(expected, actual)

    def test_process_choice_profile(self):
        expected = check.process_choice("Profile")
        actual = 'Profile'
        self.assertEqual(expected, actual)

    def test_process_choice_collection(self):
        expected = check.process_choice("Collection")
        actual = 'Collection'
        self.assertEqual(expected, actual)