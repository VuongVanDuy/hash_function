from dataclasses import dataclass, field

@dataclass
class SateWidget():
    timeSkip: int = 700
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

    OperatorActive: str = '''QLabel {
        border: 2px solid green;
        background-color: #9370DB;
        border-radius: 5px;
    }
    '''

    OperatorDefault: str = '''QLabel {
        border: 2px solid green;
        border-radius: 5px;
    }
    
    QLabel:hover {
        border: 2px solid #1E90FF;  /* Màu xanh dương khi hover */
    }
    '''

    ButtonNextBlockDefault: str = '''QPushButton {
        border: 3px solid green;
        border-radius: 5px;
    }
    '''
    ButtonNextBlockActive: str = '''QPushButton {
            background-color: #00ff00; 
            border: 2px solid #8f8f91;
            border-radius: 5px;
    }
    '''
