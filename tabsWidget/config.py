from dataclasses import dataclass, field

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
        border-radius: 30px;
        min-width: 60px;
        min-height: 60px;
        max-width: 60px;
        max-height: 60px;
    }
    '''

    OperatorDefault: str = '''QPushButton {
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #73C2FB, stop: 1 #2E86C1);
        border: 1px solid #2E86C1;
        border-radius: 30px;
        min-width: 60px;
        min-height: 60px;
        max-width: 60px;
        max-height: 60px;
    }
    '''