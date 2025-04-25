from PySide6.QtWidgets import QApplication, QFileDialog, QPushButton, QWidget, QGroupBox
from PySide6.QtCore import QTimer, QSize, QEventLoop
from PySide6.QtGui import QIcon
from .form import Ui_Form
from tabsWidget.config import StateWidget, get_instruction_algorithm, MD5_INSTRUCTION
from tabsWidget.customWidget.customDialog import QCustomDialog
from hash.md5 import MD5

class ContainerControl(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.md5Control = None
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.timer = None
        self.instruction.setText(get_instruction_algorithm(file_name=MD5_INSTRUCTION))

        self.File.toggled.connect(self.change_radio_btn_file)
        self.plaintext.textChanged.connect(self.change_plain_text)
        self.btnDetailStep.clicked.connect(self.visual_step_round)
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.Ok.clicked.connect(self.AcceptPlainText)
        self.start.clicked.connect(self.start_round)
        self.btnNextStep.clicked.connect(self.next_step)
        self.btnPreviousStep.clicked.connect(self.pre_step)
        self.btnNextRound.clicked.connect(self.next_round)
        self.btnPreviousRound.clicked.connect(self.pre_round)
        self.btnNextBlock.clicked.connect(lambda: self.next_block(effect_on=True))
        self.btnPreviousBlock.clicked.connect(lambda: self.pre_block(effect_on=True))
        self.finish.clicked.connect(self.finish_process)
        self.Clear.clicked.connect(self.clear_inputs)
        self.zoom_1.clicked.connect(self.show_zoom_plaintext)
        self.zoom_2.clicked.connect(self.show_zoom_plaintext_with_padding)
        self.zoom_3.clicked.connect(self.show_zoom_instruction)

    def show_zoom_plaintext(self):
        content = self.plaintext.text()
        self.customDialog_1 = QCustomDialog(content=content, title="Plaintext", type="Plaintext")
        self.customDialog_1.show()

    def show_zoom_plaintext_with_padding(self):
        content = self.plaintext_with_padding.text()
        self.customDialog_2 = QCustomDialog(content=content, title="Plaintext with padding")
        self.customDialog_2.show()

    def show_zoom_instruction(self):
        content = self.instruction.toPlainText()
        customDialog = QCustomDialog(content=content, title="Instruction algorithm md5")
        customDialog.exec_()

    def change_radio_btn_file(self):
        self.btnChooseFile.setEnabled(self.File.isChecked())
        if self.File.isChecked():
            self.plaintext.setReadOnly(True)
        else:
            self.plaintext.setReadOnly(False)

    def change_plain_text(self):
        if self.plaintext.text():
            self.Ok.setEnabled(True)
        else:
            self.Ok.setEnabled(False)

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(None, "Choose File", "", "All Files (*)")
        # read file
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        self.plaintext.setText(data)


    def AcceptPlainText(self):
        data = self.plaintext.text()
        if not data:
            return
        self.md5Control = MD5(data)
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
        self.finish.setEnabled(True)

    def clear_inputs(self):
        self.plaintext.clear()
        self.plaintext_with_padding.clear()
        self.hash_hex.clear()
        self.currentBlock.setValue(0)
        self.round.setValue(1)
        self.stepRound.setValue(1)
        self.labelValueH1.setText("")
        self.labelValueH2.setText("")
        self.labelValueH3.setText("")
        self.labelValueH4.setText("")
        self.labelValueA.setText("")
        self.labelValueB.setText("")
        self.labelValueC.setText("")
        self.labelValueD.setText("")
        self.labelValueA_new.setText("")
        self.labelValueB_new.setText("")
        self.labelValueC_new.setText("")
        self.labelValueD_new.setText("")
        self.labelValueF.setText("")
        self.labelWord1.setText("")
        self.labelWord2.setText("")
        self.labelWord3.setText("")
        self.labelWord4.setText("")
        self.labelWord5.setText("")
        self.labelWord6.setText("")
        self.labelWord7.setText("")
        self.labelWord8.setText("")
        self.labelWord9.setText("")
        self.labelWord10.setText("")
        self.labelWord11.setText("")
        self.labelWord12.setText("")
        self.labelWord13.setText("")
        self.labelWord14.setText("")
        self.labelWord15.setText("")
        self.labelWord16.setText("")
        self.labelAC.setText("")
        self.labelSC.setText("")
        self.set_enable_btns(
            list_btns=[self.Ok,
                       self.start,
                       self.finish,
                       self.btnDetailStep,
                       self.btnNextStep,
                       self.btnNextRound,
                       self.btnNextBlock,
                       self.btnPreviousStep,
                       self.btnPreviousRound,
                       self.btnPreviousBlock], active=False)

    def start_round(self):
        initialize_MD_buffer = self.md5Control.cache["initialize_MD_buffer"]
        buffer_H = initialize_MD_buffer.copy()
        buffer_ABCDF = initialize_MD_buffer.copy()
        buffer_ABCDF["little_endian"] += self.steps_of_block[0]["buffers_state"]["little_endian"][0][2:]
        buffer_ABCDF["big_endian"] += self.steps_of_block[0]["buffers_state"]["big_endian"][0][2:]
        buffer_AC_SC = {
            "little_endian": self.steps_of_block[0]["buffers_state"]["little_endian"][0][:2],
            "big_endian": self.steps_of_block[0]["buffers_state"]["big_endian"][0][:2]
        }
        self.set_words_of_block(0)
        self.set_state_buffer_of_step(0, 1, 1, buffer_AC_SC, buffer_ABCDF, buffer_H)
        self.set_enable_btns(list_btns=[self.btnDetailStep, self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                             active=True)
        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound, self.btnPreviousBlock],
                             active=False)

    def finish_process(self):
        self.currentBlock.setValue(len(self.md5Control.blocks) - 1)
        self.round.setValue(4)
        self.set_words_of_block(len(self.md5Control.blocks) - 1)
        if len(self.steps_of_block) >= 2:
            buffer_H = self.steps_of_block[-2]["end_of_block"]
        else:
            buffer_H = self.md5Control.cache["initialize_MD_buffer"]
        self.set_MD_buffer_H1234(buffer_H["little_endian"], buffer_H["big_endian"])
        self.stepRound.setValue(15)
        self.next_step()

    def set_name_group_f(self, round):
        if round == 1:
            self.groupF.setTitle("F")
        elif round == 2:
            self.groupF.setTitle("G")
        elif round == 3:
            self.groupF.setTitle("H")
        elif round == 4:
            self.groupF.setTitle("I")

    def next_step(self):
        curr_block = self.currentBlock.value()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)

        if step == 63:
            if curr_block >= len(self.md5Control.blocks) - 1:
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                     active=False)
                return
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

            self.btnPreviousStep.setEnabled(True)
            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC_SC, buffer_ABCDF, None)
            if (self.currentBlock.value() == len(self.md5Control.blocks) - 1 and
                    newRound == 4 and newStepRound == 16):
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                     active=False)
                self.hash_hex.setText(self.md5Control.hash_hex)

        self.visual_state_change_step()

    def pre_step(self):
        curr_block = self.currentBlock.value()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)
        if step == 0:
            if curr_block == 0:
                return
            else:
                curr_block -= 1
                self.currentBlock.setValue(curr_block)
                self.set_words_of_block(curr_block)
                if curr_block == 0:
                    buffer_H = self.md5Control.cache["initialize_MD_buffer"]
                    self.set_MD_buffer_H1234(buffer_H["little_endian"], buffer_H["big_endian"])
                else:
                    buffer_H = {
                        "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"],
                        "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
                    }
                    self.set_MD_buffer_H1234(buffer_H["little_endian"], buffer_H["big_endian"])
                self.round.setValue(4)
                self.stepRound.setValue(15)
                self.next_step()
        elif step == 1:
            if curr_block == 0:
                self.start_round()
            else:
                self.currentBlock.setValue(curr_block + 1)
                self.pre_block()
        else:
            if step % 16 == 0:
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

        self.btnNextStep.setEnabled(True)
        self.visual_state_change_step()

    def next_round(self):
        curr_block = self.currentBlock.value()
        current_round = self.round.value()
        if current_round == 4:
            if curr_block >= len(self.md5Control.blocks) - 1:
                self.set_enable_btns(list_btns=[self.btnNextRound, self.btnNextBlock],
                                     active=False)
                return
            else:
                self.next_block(effect_on=False)
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
            self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound],
                                 active=True)

            if (self.currentBlock.value() == len(self.md5Control.blocks) - 1 and newRound == 4):
                self.btnNextRound.setEnabled(False)
        self.visual_state_change_step()

    def pre_round(self):
        self.btnNextRound.setEnabled(True)
        curr_block = self.currentBlock.value()
        current_round = self.round.value()
        if current_round == 1:
            if curr_block == 0:
                return
            else:
                curr_block -= 1
                self.currentBlock.setValue(curr_block)
                self.set_words_of_block(curr_block)
                if curr_block == 0:
                    buffer_H = self.md5Control.cache["initialize_MD_buffer"]
                    self.set_MD_buffer_H1234(buffer_H["little_endian"], buffer_H["big_endian"])
                else:
                    buffer_H = {
                        "little_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["little_endian"],
                        "big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["big_endian"]
                    }
                    self.set_MD_buffer_H1234(buffer_H["little_endian"], buffer_H["big_endian"])
                self.round.setValue(3)
                self.next_round()
        elif current_round == 2:
            if curr_block == 0:
                self.start_round()
            else:
                self.currentBlock.setValue(curr_block + 1)
                self.pre_block(effect_on=False)
        else:
            newRound = current_round - 1
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
        self.visual_state_change_step()

    def next_block(self, effect_on=True):
        self.visual_state_change_block(notStart=True, effect_on=effect_on)

        curr_block = self.currentBlock.value() + 1
        if curr_block > len(self.md5Control.blocks) - 1:
            self.btnNextBlock.setEnabled(False)
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

        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound, self.btnPreviousBlock],
                             active=True)
        self.set_state_buffer_of_step(curr_block, current_round, current_step_of_round, buffer_AC_SC, buffer_ABCDF, buffer_H)
        if self.currentBlock.value() == len(self.md5Control.blocks) - 1:
            self.btnNextBlock.setEnabled(False)

    def pre_block(self, effect_on=True):
        curr_block = self.currentBlock.value() - 1
        if curr_block < 0:
            return
        current_round = 1
        current_step_of_round = 1
        step = 0

        if curr_block == 0:
            self.visual_state_change_block(notStart=False, effect_on=effect_on)
            self.start_round()
            self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound, self.btnPreviousBlock],
                                 active=False)
        else:
            self.visual_state_change_block(notStart=True, effect_on=effect_on)
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
            self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                 active=True)

    def set_state_buffer_of_step(self, curr_block, round, stepRound, buffer_AC_SC, buffers_ABCDF, buffer_Hi):
        self.round.setValue(round)
        self.stepRound.setValue(stepRound)
        self.set_name_group_f(round)
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

    def set_enable_btns(self, list_btns: list[QPushButton], active=True):
        for btn in list_btns:
            btn.setEnabled(active)

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

    def visual_state_change_step(self):
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)
        states = StateWidget()
        timeSkip = states.timeSkip // 2
        groupBoxWord = self.get_groupBox_of_word(step)
        groupBoxWord.setStyleSheet(states.GroupActive)
        QTimer.singleShot(timeSkip, lambda: groupBoxWord.setStyleSheet(states.GroupDeFault))

    def visual_state_change_block(self, notStart=True, effect_on=True):
        if not effect_on:
            return
        states = StateWidget()
        if notStart:
            self.operator6.setStyleSheet(states.OperatorActive)
        self.groupH1.setStyleSheet(states.GroupRes)
        self.groupH2.setStyleSheet(states.GroupRes)
        self.groupH3.setStyleSheet(states.GroupRes)
        self.groupH4.setStyleSheet(states.GroupRes)
        self.groupA.setStyleSheet(states.GroupRes)
        self.groupB.setStyleSheet(states.GroupRes)
        self.groupC.setStyleSheet(states.GroupRes)
        self.groupD.setStyleSheet(states.GroupRes)

        timeSkip = states.timeSkip // 2
        if notStart:
            QTimer.singleShot(timeSkip, lambda: self.operator6.setStyleSheet(states.OperatorDefault))
        QTimer.singleShot(timeSkip, lambda: self.groupH1.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH2.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH3.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH4.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupA.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupB.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupC.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupD.setStyleSheet(states.GroupDeFault))

    def cancel_detail_step(self):
        self.stop_flag = True
        self.change_to_btnDetailStep()

    def change_to_btnDetailStep(self):
        self.btnDetailStep.setText("Detail Step")
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/activity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetailStep.setIcon(icon)
        self.btnDetailStep.clicked.disconnect()
        self.btnDetailStep.clicked.connect(self.visual_step_round)

    def change_to_btnCancel(self):
        self.btnDetailStep.setText("Cancel")
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetailStep.setIcon(icon)
        self.btnDetailStep.clicked.disconnect()
        self.btnDetailStep.clicked.connect(self.cancel_detail_step)

    def single_shot_sync(self, delay, callback):
        """
        Chờ đợi delay (ms) rồi gọi callback.
        Hàm này sẽ block luồng hiện tại cho đến khi callback được thực thi.
        """
        loop = QEventLoop()
        QTimer.singleShot(delay, lambda: (callback(), loop.quit()))
        loop.exec()

    def next_object_with_delay(self, timeSkip, target, style):
        if self.timer is None:
            self.set_default_style_object(target)
            return
        self.single_shot_sync(timeSkip, lambda: self._check_and_execute(target, style))

    def _check_and_execute(self, target, style):
        if self.stop_flag:
            self.set_default_style_object(target)
            del self.timer
            self.timer = None
        else:
            target.setStyleSheet(style)

    def visual_step_round(self):
        self.change_to_btnCancel()
        self.stop_flag = False  # Reset stop flag
        self.timer = QTimer()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 16 + (current_step_of_round - 1)
        word_object = self.get_groupBox_of_word(step)

        states = StateWidget()
        self.groupB.setStyleSheet(states.GroupActive)
        self.groupC.setStyleSheet(states.GroupActive)
        self.groupD.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.groupD, states.GroupDeFault)
        self.groupB.setStyleSheet(states.GroupDeFault)
        self.groupC.setStyleSheet(states.GroupDeFault)
        self.groupF.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupA, states.GroupActive)
        self.groupF.setStyleSheet(states.GroupActive)
        self.operator1.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator1, states.OperatorDefault)
        self.groupA.setStyleSheet(states.GroupDeFault)
        self.groupF.setStyleSheet(states.GroupDeFault)
        word_object.setStyleSheet(states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        word_object.setStyleSheet(states.GroupDeFault)
        self.groupAC.setStyleSheet(states.GroupActive)
        self.operator3.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator3, states.OperatorDefault)
        self.groupAC.setStyleSheet(states.GroupDeFault)
        self.groupSC.setStyleSheet(states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator4, states.OperatorDefault)
        self.groupSC.setStyleSheet(states.GroupDeFault)
        self.groupB.setStyleSheet(states.GroupActive)
        self.operator5.setStyleSheet(states.OperatorActive)
        self.groupB_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.operator5, states.OperatorDefault)
        self.groupB_new.setStyleSheet(states.GroupDeFault)
        self.groupC_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupB, states.GroupDeFault)
        self.groupC.setStyleSheet(states.GroupActive)
        self.groupC_new.setStyleSheet(states.GroupDeFault)
        self.groupD_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupC, states.GroupDeFault)
        self.groupD.setStyleSheet(states.GroupActive)
        self.groupD_new.setStyleSheet(states.GroupDeFault)
        self.groupA_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupD, states.GroupDeFault)
        self.groupA_new.setStyleSheet(states.GroupDeFault)

        self.change_to_btnDetailStep()

    def set_default_style_object(self, object):
        if isinstance(object, QGroupBox):
            object.setStyleSheet(StateWidget().GroupDeFault)
        elif isinstance(object, QPushButton):
            object.setStyleSheet(StateWidget().OperatorDefault)

    def get_word_of_step(self, step):
        if step < 16:
            word = step
        elif step < 32:
            word = (5 * step + 1) % 16
        elif step < 48:
            word = (3 * step + 5) % 16
        else:
            word = (7 * step) % 16

        return word

    def get_groupBox_of_word(self, step):
        word = self.get_word_of_step(step) + 1

        if word == 1:
            return self.group_1
        elif word == 2:
            return self.group_2
        elif word == 3:
            return self.group_3
        elif word == 4:
            return self.group_4
        elif word == 5:
            return self.group_5
        elif word == 6:
            return self.group_6
        elif word == 7:
            return self.group_7
        elif word == 8:
            return self.group_8
        elif word == 9:
            return self.group_9
        elif word == 10:
            return self.group_10
        elif word == 11:
            return self.group_11
        elif word == 12:
            return self.group_12
        elif word == 13:
            return self.group_13
        elif word == 14:
            return self.group_14
        elif word == 15:
            return self.group_15
        elif word == 16:
            return self.group_16
