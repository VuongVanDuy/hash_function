from PySide6.QtWidgets import QApplication, QFileDialog, QPushButton, QWidget, QGroupBox
from PySide6.QtCore import QTimer, QSize, QEventLoop
from PySide6.QtGui import QIcon
from .form import Ui_Form
from tabsWidget.config import StateWidget, get_instruction_algorithm, SHA1_INSTRUCTION
from tabsWidget.customWidget.customDialog import QCustomDialog
from hash.sha1 import SHA1

class ContainerControl(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.sha1Control = None
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.timer = None
        self.instruction.setText(get_instruction_algorithm(file_name=SHA1_INSTRUCTION))

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
        self.sha1Control = SHA1(data)
        self.sha1Control.generate_hash()
        self.steps_of_block = []
        for i in range(len(self.sha1Control.blocks)):
            step_of_block = self.sha1Control.cache[f"block_{i}"]
            self.steps_of_block.append(step_of_block)

        plaintext_hex = self.sha1Control.cache["message"]["hex"]
        self.plaintext.setText(plaintext_hex)
        plaintext_with_padding = self.sha1Control.cache["message_after_padding"]["hex"]
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
        self.labelValueH5.setText("")
        self.labelValueA.setText("")
        self.labelValueB.setText("")
        self.labelValueC.setText("")
        self.labelValueD.setText("")
        self.labelValueE.setText("")
        self.labelValueA_new.setText("")
        self.labelValueB_new.setText("")
        self.labelValueC_new.setText("")
        self.labelValueD_new.setText("")
        self.labelValueE_new.setText("")
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
        self.labelSC_A.setText("")
        self.labelSC_B.setText("")
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
        initialize_SHA_buffer = self.sha1Control.cache["initialize_SHA_buffer"]
        buffer_H = initialize_SHA_buffer.copy()
        buffer_ABCDEF = initialize_SHA_buffer.copy()
        buffer_ABCDEF["int_big_endian"] += self.steps_of_block[0]["buffers_state"]["int_big_endian"][0][1:]
        buffer_ABCDEF["hex_big_endian"] += self.steps_of_block[0]["buffers_state"]["hex_big_endian"][0][1:]
        buffer_AC = {
            "int_big_endian": self.steps_of_block[0]["buffers_state"]["int_big_endian"][0][0],
            "hex_big_endian": self.steps_of_block[0]["buffers_state"]["hex_big_endian"][0][0]
        }
        self.labelSC_A.setText('5' + '\n' + '00 00 00 05')
        self.labelSC_B.setText('30' + '\n' + '00 00 00 1E')
        self.set_words_of_block(block=0, round=1)
        self.set_state_buffer_of_step(0, 1, 1, buffer_AC, buffer_ABCDEF, buffer_H)
        self.set_enable_btns(list_btns=[self.btnDetailStep, self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                             active=True)
        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound, self.btnPreviousBlock],
                             active=False)

    def finish_process(self):
        last_block = len(self.sha1Control.blocks) - 1
        self.currentBlock.setValue(last_block)
        self.round.setValue(4)
        self.set_words_of_block(block=last_block, round=4)
        if len(self.steps_of_block) >= 2:
            buffer_H = self.steps_of_block[-2]["end_of_block"]
        else:
            buffer_H = self.sha1Control.cache["initialize_SHA_buffer"]
        self.set_MD_buffer_H12345(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
        self.stepRound.setValue(19)
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
        step = (current_round - 1) * 20 + (current_step_of_round - 1)

        if step == 79:
            if curr_block >= len(self.sha1Control.blocks) - 1:
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                     active=False)
                return
            self.next_block()
        else:
            if (step + 1) % 20 == 0:
                newRound = current_round + 1
                newStepRound = 1
            else:
                newRound = current_round
                newStepRound = current_step_of_round + 1

            buffer_ABCDEF = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][1:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step + 1][1:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][1:6]
                                + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step + 1][1:]
            }
            buffer_AC = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step + 1][0],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step + 1][0]
            }

            self.btnPreviousStep.setEnabled(True)
            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC, buffer_ABCDEF, None)
            if (self.currentBlock.value() == len(self.sha1Control.blocks) - 1 and
                    newRound == 4 and newStepRound == 20):
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                     active=False)
                self.hash_hex.setText(self.sha1Control.hash_hex)

        self.visual_state_change_step()

    def pre_step(self):
        curr_block = self.currentBlock.value()
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 20 + (current_step_of_round - 1)
        if step == 0:
            if curr_block == 0:
                return
            else:
                curr_block -= 1
                self.currentBlock.setValue(curr_block)
                self.set_words_of_block(curr_block)
                if curr_block == 0:
                    buffer_H = self.sha1Control.cache["initialize_SHA_buffer"]
                    self.set_MD_buffer_H12345(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
                else:
                    buffer_H = {
                        "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
                        "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                    }
                    self.set_MD_buffer_H12345(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
                self.round.setValue(4)
                self.stepRound.setValue(19)
                self.next_step()
        elif step == 1:
            if curr_block == 0:
                self.start_round()
            else:
                self.currentBlock.setValue(curr_block + 1)
                self.pre_block()
        else:
            if step % 20 == 0:
                newRound = current_round - 1
                newStepRound = 20
            else:
                newRound = current_round
                newStepRound = current_step_of_round - 1

            buffer_ABCDEF = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step - 2][1:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step - 1][1:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step - 2][1:6]
                                + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step - 1][1:]
            }
            buffer_AC = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step - 1][0],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step - 1][0]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC, buffer_ABCDEF, None)

        self.btnNextStep.setEnabled(True)
        self.visual_state_change_step()

    def next_round(self):
        curr_block = self.currentBlock.value()
        current_round = self.round.value()
        if current_round == 4:
            if curr_block >= len(self.sha1Control.blocks) - 1:
                self.set_enable_btns(list_btns=[self.btnNextRound, self.btnNextBlock],
                                     active=False)
                return
            else:
                self.next_block(effect_on=False)
        elif current_round < 4:
            newRound = current_round + 1
            newStepRound = 1
            step = (newRound - 1) * 20
            buffer_ABCDEF = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step - 1][1:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][1:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step - 1][1:6]
                              + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][1:]
            }
            buffer_AC = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][0],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][0]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC, buffer_ABCDEF, None)
            self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound],
                                 active=True)

            if (self.currentBlock.value() == len(self.sha1Control.blocks) - 1 and newRound == 4):
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
                    buffer_H = self.sha1Control.cache["initialize_SHA_buffer"]
                    self.set_MD_buffer_H12345(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
                else:
                    buffer_H = {
                        "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
                        "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                    }
                    self.set_MD_buffer_H12345(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
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
            step = (newRound - 1) * 20
            buffer_ABCDEF = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step - 1][1:6]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][1:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step - 1][1:6]
                              + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][1:]
            }
            buffer_AC = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][0],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][0]
            }

            self.set_state_buffer_of_step(curr_block, newRound, newStepRound, buffer_AC, buffer_ABCDEF, None)
        self.visual_state_change_step()

    def next_block(self, effect_on=True):
        self.visual_state_change_block(notStart=True, effect_on=effect_on)

        curr_block = self.currentBlock.value() + 1
        if curr_block > len(self.sha1Control.blocks) - 1:
            self.btnNextBlock.setEnabled(False)
            return
        current_round = 1
        current_step_of_round = 1
        step = 0

        buffer_ABCDEF = {
            "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"]
                             + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][1:],
            "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                            + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][1:]
        }
        buffer_AC = {
            "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][0],
            "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][0]
        }
        buffer_H = {
            "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
            "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
        }

        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnPreviousRound, self.btnPreviousBlock],
                             active=True)
        self.set_state_buffer_of_step(curr_block, current_round, current_step_of_round, buffer_AC, buffer_ABCDEF, buffer_H)
        if self.currentBlock.value() == len(self.sha1Control.blocks) - 1:
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
            buffer_ABCDEF = {
                "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][1:],
                "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                              + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][1:]
            }
            buffer_AC = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step][0],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step][0]
            }
            buffer_H = {
                "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
                "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
            }

            self.set_state_buffer_of_step(curr_block, current_round, current_step_of_round,
                                          buffer_AC, buffer_ABCDEF, buffer_H)
            self.set_enable_btns(list_btns=[self.btnNextStep, self.btnNextRound, self.btnNextBlock],
                                 active=True)

    def set_state_buffer_of_step(self, curr_block, round, stepRound, buffer_AC, buffers_ABCDF, buffer_Hi):
        self.round.setValue(round)
        self.stepRound.setValue(stepRound)
        self.set_name_group_f(round)
        if curr_block != self.currentBlock.value():
            self.currentBlock.setValue(curr_block)
        self.set_words_of_block(block=curr_block, round=round)
        self.set_buffer_constant(buffer_AC["int_big_endian"], buffer_AC["hex_big_endian"])
        self.set_MD_buffer_ABCDEF(buffers_ABCDF["int_big_endian"], buffers_ABCDF["hex_big_endian"])
        if buffer_Hi:
            self.set_MD_buffer_H12345(buffer_Hi["int_big_endian"], buffer_Hi["hex_big_endian"])

    def set_buffer_constant(self, integer_big_endian, hex_big_endian):
        self.labelAC.setText(str(integer_big_endian) + '\n' + hex_big_endian)

    def set_MD_buffer_H12345(self, integers_big_endian, hexs_big_endian):
        self.labelValueH1.setText(str(integers_big_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelValueH2.setText(str(integers_big_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelValueH3.setText(str(integers_big_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelValueH4.setText(str(integers_big_endian[3]) + '\n' + hexs_big_endian[3])
        self.labelValueH5.setText(str(integers_big_endian[4]) + '\n' + hexs_big_endian[4])

    def set_MD_buffer_ABCDEF(self, integers_big_endian, hexs_big_endian):
        self.labelValueA.setText(str(integers_big_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelValueB.setText(str(integers_big_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelValueC.setText(str(integers_big_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelValueD.setText(str(integers_big_endian[3]) + '\n' + hexs_big_endian[3])
        self.labelValueE.setText(str(integers_big_endian[4]) + '\n' + hexs_big_endian[4])
        self.labelValueA_new.setText(str(integers_big_endian[5]) + '\n' + hexs_big_endian[5])
        self.labelValueB_new.setText(str(integers_big_endian[6]) + '\n' + hexs_big_endian[6])
        self.labelValueC_new.setText(str(integers_big_endian[7]) + '\n' + hexs_big_endian[7])
        self.labelValueD_new.setText(str(integers_big_endian[8]) + '\n' + hexs_big_endian[8])
        self.labelValueE_new.setText(str(integers_big_endian[9]) + '\n' + hexs_big_endian[9])
        self.labelValueF.setText(str(integers_big_endian[10]) + '\n' + hexs_big_endian[10])

    def set_enable_btns(self, list_btns: list[QPushButton], active=True):
        for btn in list_btns:
            btn.setEnabled(active)

    def get_words_in_round_of_block(self, block, round):
        # get words of block
        words_of_block = self.steps_of_block[block]["words_of_block"]
        integers_big_endian = words_of_block["int_big_endian"][(round - 1) * 20: round * 20]
        hexs_big_endian = words_of_block["hex_big_endian"][(round - 1) * 20: round * 20]
        return integers_big_endian, hexs_big_endian

    def set_words_of_block(self, block, round):
        # set words in round of block
        integers_big_endian, hexs_big_endian = self.get_words_in_round_of_block(block, round)
        self.labelWord1.setText(str(integers_big_endian[0]) + '\n' + hexs_big_endian[0])
        self.labelWord2.setText(str(integers_big_endian[1]) + '\n' + hexs_big_endian[1])
        self.labelWord3.setText(str(integers_big_endian[2]) + '\n' + hexs_big_endian[2])
        self.labelWord4.setText(str(integers_big_endian[3]) + '\n' + hexs_big_endian[3])
        self.labelWord5.setText(str(integers_big_endian[4]) + '\n' + hexs_big_endian[4])
        self.labelWord6.setText(str(integers_big_endian[5]) + '\n' + hexs_big_endian[5])
        self.labelWord7.setText(str(integers_big_endian[6]) + '\n' + hexs_big_endian[6])
        self.labelWord8.setText(str(integers_big_endian[7]) + '\n' + hexs_big_endian[7])
        self.labelWord9.setText(str(integers_big_endian[8]) + '\n' + hexs_big_endian[8])
        self.labelWord10.setText(str(integers_big_endian[9]) + '\n' + hexs_big_endian[9])
        self.labelWord11.setText(str(integers_big_endian[10]) + '\n' + hexs_big_endian[10])
        self.labelWord12.setText(str(integers_big_endian[11]) + '\n' + hexs_big_endian[11])
        self.labelWord13.setText(str(integers_big_endian[12]) + '\n' + hexs_big_endian[12])
        self.labelWord14.setText(str(integers_big_endian[13]) + '\n' + hexs_big_endian[13])
        self.labelWord15.setText(str(integers_big_endian[14]) + '\n' + hexs_big_endian[14])
        self.labelWord16.setText(str(integers_big_endian[15]) + '\n' + hexs_big_endian[15])
        self.labelWord17.setText(str(integers_big_endian[16]) + '\n' + hexs_big_endian[16])
        self.labelWord18.setText(str(integers_big_endian[17]) + '\n' + hexs_big_endian[17])
        self.labelWord19.setText(str(integers_big_endian[18]) + '\n' + hexs_big_endian[18])
        self.labelWord20.setText(str(integers_big_endian[19]) + '\n' + hexs_big_endian[19])


    def visual_state_change_step(self):
        current_step_of_round = self.stepRound.value()
        current_round = self.round.value()
        step = (current_round - 1) * 20 + (current_step_of_round - 1)
        states = StateWidget()
        timeSkip = states.timeSkip // 2
        groupBoxWord = self.get_groupBox_of_word(step % 20)
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
        self.groupH5.setStyleSheet(states.GroupRes)
        self.groupA.setStyleSheet(states.GroupRes)
        self.groupB.setStyleSheet(states.GroupRes)
        self.groupC.setStyleSheet(states.GroupRes)
        self.groupD.setStyleSheet(states.GroupRes)
        self.groupE.setStyleSheet(states.GroupRes)

        timeSkip = states.timeSkip // 2
        if notStart:
            QTimer.singleShot(timeSkip, lambda: self.operator6.setStyleSheet(states.OperatorDefault))
        QTimer.singleShot(timeSkip, lambda: self.groupH1.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH2.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH3.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH4.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupH5.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupA.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupB.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupC.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupD.setStyleSheet(states.GroupDeFault))
        QTimer.singleShot(timeSkip, lambda: self.groupE.setStyleSheet(states.GroupDeFault))

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
        current_block = self.currentBlock.value()
        step = (current_round - 1) * 20 + (current_step_of_round - 1)
        integers_big_endian = self.steps_of_block[current_block]["intermediate_results"][f"step_{step}"]["int_big_endian"]
        hexs_big_endian = self.steps_of_block[current_block]["intermediate_results"][f"step_{step}"]["hex_big_endian"]

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
        # self.groupF.setStyleSheet(states.GroupDeFault)
        self.groupSC_A.setStyleSheet(states.GroupActive)
        self.operator5.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator5, states.OperatorDefault)
        self.groupA.setStyleSheet(states.GroupDeFault)
        self.groupSC_A.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(str(integers_big_endian[0]) + '\n' + hexs_big_endian[0])

        self.next_object_with_delay(states.timeSkip, self.groupF, states.GroupActive)
        self.operator1.setStyleSheet(states.OperatorActive)
        self.groupIntermRes.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.operator1, states.OperatorDefault)
        self.groupF.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(str(integers_big_endian[1]) + '\n' + hexs_big_endian[1])

        self.next_object_with_delay(states.timeSkip, self.groupE, states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)
        self.groupIntermRes.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        self.groupE.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(str(integers_big_endian[2]) + '\n' + hexs_big_endian[2])

        self.next_object_with_delay(states.timeSkip, word_object, states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)
        self.groupIntermRes.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        word_object.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(str(integers_big_endian[3]) + '\n' + hexs_big_endian[3])

        self.next_object_with_delay(states.timeSkip, self.groupAC, states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)
        self.groupIntermRes.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        self.groupAC.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(str(integers_big_endian[4]) + '\n' + hexs_big_endian[4])

        # update state buffers
        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.groupA_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupDeFault)
        self.groupA_new.setStyleSheet(states.GroupDeFault)
        self.groupA.setStyleSheet(states.GroupActive)
        self.groupB_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupA, states.GroupDeFault)
        self.groupB_new.setStyleSheet(states.GroupDeFault)
        self.groupB.setStyleSheet(states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)
        self.groupSC_B.setStyleSheet(states.GroupActive)
        self.groupC_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupB, states.GroupDeFault)
        self.operator4.setStyleSheet(states.OperatorDefault)
        self.groupSC_B.setStyleSheet(states.GroupDeFault)
        self.groupC_new.setStyleSheet(states.GroupDeFault)
        self.groupC.setStyleSheet(states.GroupActive)
        self.groupD_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupC, states.GroupDeFault)
        self.groupD_new.setStyleSheet(states.GroupDeFault)
        self.groupD.setStyleSheet(states.GroupActive)
        self.groupE_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupD, states.GroupDeFault)
        self.groupE_new.setStyleSheet(states.GroupDeFault)
        self.labelValueInterm.setText('')

        self.change_to_btnDetailStep()

    def set_default_style_object(self, object):
        if isinstance(object, QGroupBox):
            object.setStyleSheet(StateWidget().GroupDeFault)
        elif isinstance(object, QPushButton):
            object.setStyleSheet(StateWidget().OperatorDefault)

    def get_groupBox_of_word(self, step):
        word = step + 1

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
        elif word == 17:
            return self.group_17
        elif word == 18:
            return self.group_18
        elif word == 19:
            return self.group_19
        elif word == 20:
            return self.group_20
