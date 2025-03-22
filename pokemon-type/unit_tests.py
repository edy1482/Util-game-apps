# This file contains the unit tests for all the functions pokemon-type-helper file

import unittest
import pokemon_type_helper

class Test_Type_Advantage_Set(unittest.TestCase):
    def setUp(self):
        self.test_set_1 = ["Grass"]
        self.test_set_2 = ["Water", "Ground", "Rock"]
        self.test_set_3 = ["Ground", "Rock", "Fire", "Electric", "Poison", "Steel", "Flying", "Ice", "Bug"]
        self.test_set_4 = ["Fire"]
        self.test_set_5 = ["Grass", "Ice", "Bug", "Steel"]
        self.test_set_6 = ["Water", "Ground", "Rock", "Grass", "Flying", "Dragon", "Psychic", "Dark", "Fairy", "Ice"]
        self.test_set_7 = []
        self.test_set_8 = 5
        self.test_set_9 = ["Egg"]
    
    def test_single(self):
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_1), self.test_set_2)
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_4), self.test_set_5)

    def test_multiple(self):
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_2), self.test_set_3)
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_5), self.test_set_6)
    
    @unittest.expectedFailure
    def test_fail(self):
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_1), self.test_set_7)
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_1), self.test_set_9)
        self.assertCountEqual(pokemon_type_helper.type_advantage_set(self.test_set_8), self.test_set_9)
    

if __name__ == '__main__':
    unittest.main()