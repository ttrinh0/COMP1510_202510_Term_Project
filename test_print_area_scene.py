from unittest import TestCase
from unittest.mock import patch
import io
import print_or_scene


class Test(TestCase):

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_area_scene_one(self, mock_output, _):
        character_test = {"Level": 1}
        print_or_scene.print_area_scene(character_test)
        expected = """\nYou make your way to Initium Pond. A calm pond full of fish.\n
⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

██╗███╗   ██╗██╗████████╗██╗██╗   ██╗███╗   ███╗    ██████╗  ██████╗ ███╗   ██╗██████╗ 
██║████╗  ██║██║╚══██╔══╝██║██║   ██║████╗ ████║    ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗
██║██╔██╗ ██║██║   ██║   ██║██║   ██║██╔████╔██║    ██████╔╝██║   ██║██╔██╗ ██║██║  ██║
██║██║╚██╗██║██║   ██║   ██║██║   ██║██║╚██╔╝██║    ██╔═══╝ ██║   ██║██║╚██╗██║██║  ██║
██║██║ ╚████║██║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║    ██║     ╚██████╔╝██║ ╚████║██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 

⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖\n
"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_area_scene_two(self, mock_output, _):
        character_test = {"Level": 2}
        print_or_scene.print_area_scene(character_test)
        expected = ("\nYou're really getting a hang of fishing. After talking to some fishers, you come to the "
                    "consensus\nthat you should head over to Medius River, another popular fishing spot.\n"
                    "It not as beginner friendly, but you think you can handle it.\n") + """
 ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

███╗   ███╗███████╗██████╗ ██╗██╗   ██╗███████╗    ██████╗ ██╗██╗   ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗██║██║   ██║██╔════╝    ██╔══██╗██║██║   ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║  ██║██║██║   ██║███████╗    ██████╔╝██║██║   ██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║  ██║██║██║   ██║╚════██║    ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗██████╔╝██║╚██████╔╝███████║    ██║  ██║██║ ╚████╔╝ ███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝

 ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖\n
"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_area_scene_three(self, mock_output, _):
        character_test = {"Level": 3}
        print_or_scene.print_area_scene(character_test)
        expected = ("\nYou take the trek to Ferefini Ocean. You overheard some fishers at the river talking about how "
                    "there\nmay be some information on where to find the Final Fishasy there.\n") + """
  ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
  
███████╗███████╗██████╗ ███████╗███████╗██╗███╗   ██╗██╗     ██████╗  ██████╗███████╗ █████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║████╗  ██║██║    ██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╗  █████╗  ██████╔╝█████╗  █████╗  ██║██╔██╗ ██║██║    ██║   ██║██║     █████╗  ███████║██╔██╗ ██║
██╔══╝  ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║██║╚██╗██║██║    ██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║
██║     ███████╗██║  ██║███████╗██║     ██║██║ ╚████║██║    ╚██████╔╝╚██████╗███████╗██║  ██║██║ ╚████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝     ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                       
  ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖\n
"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_area_scene_four(self, mock_output, _):
        character_test = {"Level": 4}
        print_or_scene.print_area_scene(character_test)
        expected = ("\nIn catching your latest fish, another fisher approaches you. They tell you that they know where "
                    "it is.\nThe Final Fishasy. You don't have any other leads so you take your chances.\n"
                    "This is it. You go to Ultimo Lake. Home of the Final Fishasy\n") + """
⊹࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪˖

██╗   ██╗██╗  ████████╗██╗███╗   ███╗ ██████╗     ██╗      █████╗ ██╗  ██╗███████╗
██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔═══██╗    ██║     ██╔══██╗██║ ██╔╝██╔════╝
██║   ██║██║     ██║   ██║██╔████╔██║██║   ██║    ██║     ███████║█████╔╝ █████╗  
██║   ██║██║     ██║   ██║██║╚██╔╝██║██║   ██║    ██║     ██╔══██║██╔═██╗ ██╔══╝  
╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║╚██████╔╝    ███████╗██║  ██║██║  ██╗███████╗
 ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
 
⊹࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪˖\n
"""
        self.assertEqual(expected, mock_output.getvalue())