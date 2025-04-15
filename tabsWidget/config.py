from dataclasses import dataclass
import os

def get_instruction_algorithm(file_name: str) -> str:
    """
    Get the introduction of the algorithm from the file.
    :param path_file: path to the file
    :return: introduction of the algorithm
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(base_dir, file_name)
    with open(path_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        intro = "".join(lines)
        return intro

MD5_INSTRUCTION = "md5_instruction.txt"
SHA1_INSTRUCTION = "sha1_instruction.txt"
SHA256_INSTRUCTION = "sha256_instruction.txt"

@dataclass
class StateWidget():
    timeSkip: int = 600
    # set color green for QGroupBox
    GroupActive: str = '''QGroupBox {
        background-color: #00ff00; 
        border: 2px solid #8f8f91;
        border-radius: 5px;
    }
    '''
    # set color default for QGroupBox
    GroupDeFault: str = ""

    GroupRes: str = '''QGroupBox {
            background-color: #FFA500; 
            border: 2px solid #8f8f91;
            border-radius: 5px;
        }
        '''

    OperatorActive: str = '''QPushButton {
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #66ff66, stop: 1 #00ff00);
        border: 1px solid #388E3C;
        border-radius: 25px;
        min-width: 50px;
        min-height: 50px;
        max-width: 50px;
        max-height: 50px;
    }
    '''

    OperatorDefault: str = '''QPushButton {
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #73C2FB, stop: 1 #2E86C1);
        border: 1px solid #2E86C1;
        border-radius: 25px;
        min-width: 50px;
        min-height: 50px;
        max-width: 50px;
        max-height: 50px;
    }
    '''
