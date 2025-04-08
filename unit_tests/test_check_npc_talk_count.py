from unittest import TestCase
import check

class Test(TestCase):

    def test_check_npc_talk_count_none(self):
        character_test = {"NPC Talk": {"Sally": False, "Charles": False, "Rob": False, "Cornet": False, "Gilly": False,
                                       "Sandy": False, "Emile": False, "Aqua": False, "Coin": False}}
        expected = check.check_npc_talk_count(character_test)
        actual = 0
        self.assertEqual(expected, actual)

    def test_check_npc_talk_count_half(self):
        character_test = {"NPC Talk": {"Sally": True, "Charles": True, "Rob": True, "Cornet": True, "Gilly": True,
                                       "Sandy": False, "Emile": False, "Aqua": False, "Coin": False}}
        expected = check.check_npc_talk_count(character_test)
        actual = 5
        self.assertEqual(expected, actual)

    def test_check_npc_talk_count_all(self):
        character_test = {"NPC Talk": {"Sally": True, "Charles": True, "Rob": True, "Cornet": True, "Gilly": True,
                                       "Sandy": True, "Emile": True, "Aqua": True, "Coin": True}}
        expected = check.check_npc_talk_count(character_test)
        actual = 9
        self.assertEqual(expected, actual)

    def test_check_npc_talk_count_every_other(self):
        character_test = {"NPC Talk": {"Sally": True, "Charles": False, "Rob": True, "Cornet": False, "Gilly": True,
                                       "Sandy": False, "Emile": True, "Aqua": False, "Coin": True}}
        expected = check.check_npc_talk_count(character_test)
        actual = 5
        self.assertEqual(expected, actual)