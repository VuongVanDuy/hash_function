from turtledemo.clock import current_day

from PySide6.QtWidgets import QApplication, QTabWidget, QFileDialog, QPushButton
from PySide6.QtCore import QTimer
from form import Ui_Form
from config import SateWidget
from hash.md5 import MD5

class mainHandle(Ui_Form, QTabWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.md5Control = None
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.File.toggled.connect(self.change_radio_btn_file)
        self.plaintext.textChanged.connect(self.change_plain_text)
        self.btnDetailStep.clicked.connect(self.step_round)
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.Ok.clicked.connect(self.AcceptPlainText)
        self.start.clicked.connect(self.start_round)
        self.btnNextStep.clicked.connect(self.next_step)
        self.btnPreviousStep.clicked.connect(self.pre_step)
        self.btnNextRound.clicked.connect(self.next_round)
        self.btnNextBlock.clicked.connect(self.next_block)

    def change_radio_btn_file(self):
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.writeInput.setEnabled(not self.File.isChecked())

    def change_plain_text(self):
        if self.plaintext.text():
            self.Ok.setEnabled(True)
        else:
            self.Ok.setEnabled(False)

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "All Files (*)")
        # read file
        if not path:
            return
        with open(path, "r") as f:
            data = f.read()
        self.plaintext.setText(data)
        self.md5Control = MD5(data)

    def AcceptPlainText(self):
        if not self.md5Control:
            return
        self.md5Control.generate_hash()
        self.steps_of_block = []
        for i in range(len(self.md5Control.blocks)):
            step_of_block = self.md5Control.cache[f"block_{i}"]
            self.steps_of_block.append(step_of_block)

        plaintext_hex = self.md5Control.cache["message"]["hex"]
        self.plaintext.setText(plaintext_hex)
        plaintext_with_padding = self.md5Control.cache["message_after_padding"]["hex"]
        self.plaintext_with_padding.setText(plaintext_with_padding)
        self.start.setEnabled(True)

    def start_round(self):
        curr_block = self.currentBlock.value()
        initialize_MD_buffer = self.md5Control.cache["initialize_MD_buffer"]
        buffer_H = initialize_MD_buffer.copy()
        buffer_ABCDF = initialize_MD_buffer.copy()
        buffer_ABCDF["little_endian"] += self.steps_of_block[curr_block]["buffers_state"]["little_endian"][0][2:]
        buffer_ABCDF["big_endian"] += self.steps_of_block[curr_block]["buffers_state"]["big_endian"][0][2:]
        buffer_AC_SC = {
            "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][0][:2],
            "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][0][:2]
        }
        self.set_words_of_block(curr_block)
        self.set_state_buffer_of_step(0, 1, 1, buffer_AC_SC, buffer_ABCDF, buffer_H)
        self.set_enable_btn([self.btnDetailStep, self.btnNextStep, self.btnPreviousStep,
                             self.btnNextRound, self.btnNextBlock])

    def next_step(self):
        curr_block = self.currentBlock.value()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)

        if step >= 63:
            self.next_block()
        else:
            if (step + 1) % 16 == 0:
                newRound = current_round + 1
                newStepRound = 1
            else:
                newRound = current_round
                newStepRound = current_step_of_round + 1

            buffer_ABCDF = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][2:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step + 1][2:],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][2:6]
                                + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step + 1][2:]
            }
            buffer_AC_SC = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step + 1][:2],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step + 1][:2]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC_SC, buffer_ABCDF, None)

    def pre_step(self):
        curr_block = self.currentBlock.value()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)
        if step == 0 and curr_block == 0 and current_round == 1:
            return
        elif step == 0 and curr_block > 0 and current_round == 1:
            curr_block -= 1
            step = 63
            newStepRound = 16
            newRound = 4
            buffer_H = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 1][2:],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 1][2:]
            }
        else:
            if step % 16 == 1:
                newRound = current_round - 1
                newStepRound = 16
            else:
                newRound = current_round
                newStepRound = current_step_of_round - 1

            buffer_ABCDF = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 2][2:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 1][2:],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 2][2:6]
                                + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 1][2:]
            }
            buffer_AC_SC = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 1][:2],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 1][:2]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC_SC, buffer_ABCDF, None)

    def pre_round(self):
        curr_block = self.currentBlock.value()
        current_round = self.round.value()
        if current_round == 1:
            pass
        elif current_round > 1:
            newRound = current_round - 1
            newStepRound = 1
            step = (newRound - 1) * 16
            buffer_ABCDF = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 2][2:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 1][2:],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 2][2:6]
                                + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 1][2:]
            }
            buffer_AC_SC = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][:2],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][:2]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC_SC, buffer_ABCDF, None)

    def next_round(self):
        curr_block = self.currentBlock.value()
        current_round = self.round.value()
        if current_round == 4:
            self.next_block()
        elif current_round < 4:
            newRound = current_round + 1
            newStepRound = 1
            step = (newRound - 1) * 16
            buffer_ABCDF = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step - 1][2:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][2:],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step - 1][2:6]
                              + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][2:]
            }
            buffer_AC_SC = {
                "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][:2],
                "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][:2]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC_SC, buffer_ABCDF, None)

    def next_block(self):
        curr_block = self.currentBlock.value() + 1
        if curr_block > len(self.md5Control.blocks) - 1:
            return
        current_round = 1
        current_step_of_round = 1
        step = 0

        buffer_ABCDF = {
            "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"]
                             + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][2:],
            "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
                            + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][2:]
        }
        buffer_AC_SC = {
            "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][:2],
            "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][:2]
        }
        buffer_H = {
            "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"],
            "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
        }

        self.set_state_buffer_of_step(curr_block, current_round, current_step_of_round, buffer_AC_SC, buffer_ABCDF, buffer_H)

    def pre_block(self):
        curr_block = self.currentBlock.value() - 1
        if curr_block < 0:
            return
        current_round = 1
        current_step_of_round = 1
        step = 0

        buffer_ABCDF = {
            "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"]
                             + self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][2:],
            "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
                          + self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][2:]
        }
        buffer_AC_SC = {
            "little_endian": self.steps_of_block[curr_block]["buffers_state"]["little_endian"][step][:2],
            "big_endian": self.steps_of_block[curr_block]["buffers_state"]["big_endian"][step][:2]
        }
        buffer_H = {
            "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"],
            "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
        }

        self.set_state_buffer_of_step(curr_block, current_round, current_step_of_round,
                                      buffer_AC_SC, buffer_ABCDF, buffer_H)

    def set_state_buffer_of_step(self, curr_block, round, stepRound, buffer_AC_SC, buffers_ABCDF, buffer_Hi):
        self.round.setValue(round)
        self.stepRound.setValue(stepRound)
        if curr_block != self.currentBlock.value():
            self.currentBlock.setValue(curr_block)
            self.set_words_of_block(curr_block)
        self.set_buffer_shift_and_constant(buffer_AC_SC["big_endian"], buffer_AC_SC["little_endian"])
        self.set_MD_buffer_ABCDF(buffers_ABCDF["little_endian"], buffers_ABCDF["big_endian"])
        if buffer_Hi:
            self.set_MD_buffer_H1234(buffer_Hi["little_endian"], buffer_Hi["big_endian"])

    def set_buffer_shift_and_constant(self, integers_big_endian, hexs_little_endian):
        self.labelAC.setText(str(integers_big_endian[0]) + '\n' + hexs_little_endian[0])
        self.labelSC.setText(str(integers_big_endian[1]) + '\n' + hexs_little_endian[1])

    def set_MD_buffer_H1234(self, integers_little_endian, hexs_big_endian):
        self.labelValueH1.setText(str(integers_little_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelValueH2.setText(str(integers_little_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelValueH3.setText(str(integers_little_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelValueH4.setText(str(integers_little_endian[3]) + '\n' + hexs_big_endian[3])

    def set_MD_buffer_ABCDF(self, integers_little_endian, hexs_big_endian):
        self.labelValueA.setText(str(integers_little_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelValueB.setText(str(integers_little_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelValueC.setText(str(integers_little_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelValueD.setText(str(integers_little_endian[3]) + '\n' + hexs_big_endian[3])
        self.labelValueA_new.setText(str(integers_little_endian[4]) + '\n' + hexs_big_endian[4])
        self.labelValueB_new.setText(str(integers_little_endian[5]) + '\n' + hexs_big_endian[5])
        self.labelValueC_new.setText(str(integers_little_endian[6]) + '\n' + hexs_big_endian[6])
        self.labelValueD_new.setText(str(integers_little_endian[7]) + '\n' + hexs_big_endian[7])
        self.labelValueF.setText(str(integers_little_endian[8]) + '\n' + hexs_big_endian[8])

    def set_enable_btn(self, list_btn: list[QPushButton]):
        for btn in list_btn:
            btn.setEnabled(True)

    def set_words_of_block(self, block):
        # set words of block
        words_of_block = self.steps_of_block[block]["words_of_block"]
        integers_little_endian = words_of_block["little_endian"]
        hexs_big_endian = words_of_block["big_endian"]
        self.labelWord1.setText(str(integers_little_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelWord2.setText(str(integers_little_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelWord3.setText(str(integers_little_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelWord4.setText(str(integers_little_endian[3]) + '\n' + hexs_big_endian[3])
        self.labelWord5.setText(str(integers_little_endian[4]) + '\n' + hexs_big_endian[4])
        self.labelWord6.setText(str(integers_little_endian[5]) + '\n' + hexs_big_endian[5])
        self.labelWord7.setText(str(integers_little_endian[6]) + '\n' + hexs_big_endian[6])
        self.labelWord8.setText(str(integers_little_endian[7]) + '\n' + hexs_big_endian[7])
        self.labelWord9.setText(str(integers_little_endian[8]) + '\n' + hexs_big_endian[8])
        self.labelWord10.setText(str(integers_little_endian[9]) + '\n' + hexs_big_endian[9])
        self.labelWord11.setText(str(integers_little_endian[10]) + '\n' + hexs_big_endian[10])
        self.labelWord12.setText(str(integers_little_endian[11]) + '\n' + hexs_big_endian[11])
        self.labelWord13.setText(str(integers_little_endian[12]) + '\n' + hexs_big_endian[12])
        self.labelWord14.setText(str(integers_little_endian[13]) + '\n' + hexs_big_endian[13])
        self.labelWord15.setText(str(integers_little_endian[14]) + '\n' + hexs_big_endian[14])
        self.labelWord16.setText(str(integers_little_endian[15]) + '\n' + hexs_big_endian[15])

    def step_round(self):
        states = SateWidget()
        self.groupB.setStyleSheet(states.GroupActive)
        QTimer.singleShot(states.timeSkip, lambda: self.next_object(self.groupB, states.GroupDeFault))
        QTimer.singleShot(states.timeSkip, lambda: self.next_object(self.groupC, states.GroupActive))

        QTimer.singleShot(2 * states.timeSkip, lambda: self.next_object(self.groupC, states.GroupDeFault))
        QTimer.singleShot(2 * states.timeSkip, lambda: self.next_object(self.groupD, states.GroupActive))

        QTimer.singleShot(3 * states.timeSkip, lambda: self.next_object(self.groupD, states.GroupDeFault))
        QTimer.singleShot(3 * states.timeSkip, lambda: self.next_object(self.groupF, states.GroupRes))

        QTimer.singleShot(4 * states.timeSkip, lambda: self.next_object(self.groupA, states.GroupActive))
        QTimer.singleShot(4 * states.timeSkip, lambda: self.next_object(self.groupF, states.GroupActive))
        QTimer.singleShot(4 * states.timeSkip, lambda: self.next_object(self.labelPlus1, states.OperatorActive))

        QTimer.singleShot(5 * states.timeSkip, lambda: self.next_object(self.labelPlus1, states.OperatorDefault))
        QTimer.singleShot(5 * states.timeSkip, lambda: self.next_object(self.groupA, states.GroupDeFault))
        QTimer.singleShot(5 * states.timeSkip, lambda: self.next_object(self.groupF, states.GroupDeFault))
        QTimer.singleShot(5 * states.timeSkip, lambda: self.next_object(self.group_1, states.GroupActive))
        QTimer.singleShot(5 * states.timeSkip, lambda: self.next_object(self.labelPlus2, states.OperatorActive))

        QTimer.singleShot(6 * states.timeSkip, lambda: self.next_object(self.labelPlus2, states.OperatorDefault))
        QTimer.singleShot(6 * states.timeSkip, lambda: self.next_object(self.group_1, states.GroupDeFault))
        QTimer.singleShot(6 * states.timeSkip, lambda: self.next_object(self.groupAC, states.GroupActive))
        QTimer.singleShot(6 * states.timeSkip, lambda: self.next_object(self.labelPlus3, states.OperatorActive))

        QTimer.singleShot(7 * states.timeSkip, lambda: self.next_object(self.labelPlus3, states.OperatorDefault))
        QTimer.singleShot(7 * states.timeSkip, lambda: self.next_object(self.groupAC, states.GroupDeFault))
        QTimer.singleShot(7 * states.timeSkip, lambda: self.next_object(self.groupSC, states.GroupActive))
        QTimer.singleShot(7 * states.timeSkip, lambda: self.next_object(self.labelShift, states.OperatorActive))

        QTimer.singleShot(8 * states.timeSkip, lambda: self.next_object(self.labelShift, states.OperatorDefault))
        QTimer.singleShot(8 * states.timeSkip, lambda: self.next_object(self.groupSC, states.GroupDeFault))
        QTimer.singleShot(8 * states.timeSkip, lambda: self.next_object(self.groupB, states.GroupActive))
        QTimer.singleShot(8 * states.timeSkip, lambda: self.next_object(self.labelPlus4, states.OperatorActive))
        QTimer.singleShot(8 * states.timeSkip, lambda: self.next_object(self.groupB_new, states.GroupRes))

        QTimer.singleShot(9 * states.timeSkip, lambda: self.next_object(self.labelPlus4, states.OperatorDefault))
        QTimer.singleShot(9 * states.timeSkip, lambda: self.next_object(self.groupC_new, states.GroupRes))

        QTimer.singleShot(10 * states.timeSkip, lambda: self.next_object(self.groupB, states.GroupDeFault))
        QTimer.singleShot(10 * states.timeSkip, lambda: self.next_object(self.groupC, states.GroupActive))
        QTimer.singleShot(10 * states.timeSkip, lambda: self.next_object(self.groupD_new, states.GroupRes))

        QTimer.singleShot(11 * states.timeSkip, lambda: self.next_object(self.groupC, states.GroupDeFault))
        QTimer.singleShot(11 * states.timeSkip, lambda: self.next_object(self.groupD, states.GroupActive))
        QTimer.singleShot(11 * states.timeSkip, lambda: self.next_object(self.groupA_new, states.GroupRes))

        QTimer.singleShot(12 * states.timeSkip, lambda: self.next_object(self.groupD, states.GroupDeFault))
        QTimer.singleShot(12 * states.timeSkip, lambda: self.next_object(self.groupA_new, states.GroupDeFault))
        QTimer.singleShot(12 * states.timeSkip, lambda: self.next_object(self.groupB_new, states.GroupDeFault))
        QTimer.singleShot(12 * states.timeSkip, lambda: self.next_object(self.groupC_new, states.GroupDeFault))
        QTimer.singleShot(12 * states.timeSkip, lambda: self.next_object(self.groupD_new, states.GroupDeFault))

    def next_object(self, object, styleSheet):
        object.setStyleSheet(styleSheet)

    # def get_group_step(self, step):
    #     if step == 1:
    #         return self.group_1
    #     elif step == 2:
    #         return self.group_2
    #     elif step == 3:
    #         return self.group_3
    #     elif step == 4:
    #         return self.group_4
    #     elif step == 5:
    #         return self.group_5
    #     elif step == 6:
    #         return self.group_6
    #     elif step == 7:
    #         return self.group_71227
    #     elif step == 8:
    #         return self.group_8
    #     elif step == 9:
    #         return self.group_9
    #     elif step == 10:
    #         return self.group_10
    #     elif step == 11:
    #         return self.group_11
    #     elif step == 12:
    #         return self.group_12
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main = mainHandle()
    main.show()
    sys.exit(app.exec())