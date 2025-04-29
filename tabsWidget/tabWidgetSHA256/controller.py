from PySide6.QtWidgets import QApplication, QFileDialog, QPushButton, QWidget, QGroupBox
from PySide6.QtCore import QTimer, QSize, QEventLoop
from PySide6.QtGui import QIcon
from .form import Ui_Form
from tabsWidget.config import StateWidget, get_instruction_algorithm, SHA256_INSTRUCTION
from tabsWidget.customWidget.customDialog import QCustomDialog
from hash.sha256 import SHA256

class ContainerControl(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SHA256 Widget")
        self.sha256Control = None
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.timer = None
        self.instruction.setText(get_instruction_algorithm(file_name=SHA256_INSTRUCTION))

        self.File.toggled.connect(self.change_radio_btn_file)
        self.plaintext.textChanged.connect(self.change_plain_text)
        self.btnDetailStep.clicked.connect(self.visual_step_round)
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.Ok.clicked.connect(self.AcceptPlainText)
        self.start.clicked.connect(self.start_round)
        self.btnNextStep.clicked.connect(self.next_step)
        self.btnPreviousStep.clicked.connect(self.pre_step)
        self.btnEndOfBlock.clicked.connect(self.end_of_block)
        self.btnStartOfBlock.clicked.connect(self.start_of_block)
        self.btnNextBlock.clicked.connect(lambda: self.next_block(effect_on=True))
        self.btnPreviousBlock.clicked.connect(lambda: self.pre_block(effect_on=True))
        self.finish.clicked.connect(self.finish_process)
        self.Clear.clicked.connect(self.clear_inputs)
        self.zoom_1.clicked.connect(self.show_zoom_plaintext)
        self.zoom_2.clicked.connect(self.show_zoom_plaintext_with_padding)
        self.zoom_3.clicked.connect(self.show_zoom_instruction)

    def show_zoom_instruction(self):
        content = self.instruction.toPlainText()
        customDialog = QCustomDialog(content=content, title="Instruction algorithm md5")
        customDialog.exec_()


    def show_zoom_plaintext(self):
        content = self.plaintext.text()
        if not content:
            return
        self.customDialog_1 = QCustomDialog(content=content, title="Plaintext", type="Plaintext")
        self.customDialog_1.show()

    def show_zoom_plaintext_with_padding(self):
        content = self.plaintext_with_padding.text()
        if not content:
            return
        self.customDialog_2 = QCustomDialog(content=content, title="Plaintext with padding")
        self.customDialog_2.show()

    def show_zoom_instruction(self):
        content = self.instruction.toPlainText()
        if not content:
            return
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
        self.sha256Control = SHA256(data)
        self.sha256Control.generate_hash()
        self.steps_of_block = []
        for i in range(len(self.sha256Control.blocks)):
            step_of_block = self.sha256Control.cache[f"block_{i}"]
            self.steps_of_block.append(step_of_block)

        plaintext_hex = self.sha256Control.cache["message"]["hex"]
        self.plaintext.setText(plaintext_hex)
        plaintext_with_padding = self.sha256Control.cache["message_after_padding"]["hex"]
        self.plaintext_with_padding.setText(plaintext_with_padding)
        self.start.setEnabled(True)
        self.finish.setEnabled(True)

    def clear_inputs(self):
        # Reset numeric fields
        self.currentBlock.setValue(0)
        self.step.setValue(1)

        # Clear all text fields
        fields_to_clear = [
           self.plaintext, self.plaintext_with_padding, self.hash_hex,
           self.labelValueH1, self.labelValueH2, self.labelValueH3, self.labelValueH4,
           self.labelValueH5, self.labelValueH6, self.labelValueH7, self.labelValueH8,
           self.labelValueA, self.labelValueB, self.labelValueC, self.labelValueD,
           self.labelValueE, self.labelValueF, self.labelValueG, self.labelValueH,
           self.labelValueA_new, self.labelValueB_new, self.labelValueC_new, self.labelValueD_new,
           self.labelValueE_new, self.labelValueF_new, self.labelValueG_new, self.labelValueH_new,
           self.labelWord1, self.labelWord2, self.labelWord3, self.labelWord4,
           self.labelWord5, self.labelWord6, self.labelWord7, self.labelWord8,
           self.labelWord9, self.labelWord10, self.labelWord11, self.labelWord12,
           self.labelWord13, self.labelWord14, self.labelWord15, self.labelWord16,
           self.labelAC, self.labelValueT1, self.labelValueT2, self.labelValueCh,
           self.labelValueMa, self.labelValueSum0, self.labelValueSum1, self.labelValueInterm
        ]
        for field in fields_to_clear:
           field.setText("")

        # Disable buttons
        buttons_to_disable = [
           self.Ok, self.start, self.finish, self.btnDetailStep,
           self.btnNextStep, self.btnEndOfBlock, self.btnNextBlock,
           self.btnPreviousStep, self.btnStartOfBlock, self.btnPreviousBlock
        ]
        self.set_enable_btns(list_btns=buttons_to_disable, active=False)

    def start_round(self):
        initialize_SHA_buffer = self.sha256Control.cache["initialize_SHA_buffer"]
        buffer_H = initialize_SHA_buffer.copy()
        buffer_ABCDEFGH = initialize_SHA_buffer.copy()
        buffer_ABCDEFGH["int_big_endian"] += self.steps_of_block[0]["buffers_state"]["int_big_endian"][0][:8]
        buffer_ABCDEFGH["hex_big_endian"] += self.steps_of_block[0]["buffers_state"]["hex_big_endian"][0][:8]
        buffer_CTSChMa = {
            "int_big_endian": self.steps_of_block[0]["buffers_state"]["int_big_endian"][0][8:],
            "hex_big_endian": self.steps_of_block[0]["buffers_state"]["hex_big_endian"][0][8:]
        }

        self.set_words_of_block(block=0, group_words=0)
        self.set_state_buffer_of_step(0, 1, buffer_CTSChMa, buffer_ABCDEFGH, buffer_H)
        self.set_enable_btns(list_btns=[self.btnDetailStep, self.btnNextStep, self.btnEndOfBlock, self.btnNextBlock],
                             active=True)
        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnStartOfBlock, self.btnPreviousBlock],
                             active=False)

    def finish_process(self):
        last_block = len(self.sha256Control.blocks) - 1
        self.currentBlock.setValue(last_block)
        self.step.setValue(63)
        self.set_words_of_block(block=last_block, group_words=3)
        if len(self.steps_of_block) >= 2:
            buffer_H = self.steps_of_block[-2]["end_of_block"]
        else:
            buffer_H = self.sha256Control.cache["initialize_SHA_buffer"]
        self.set_SHA_buffer_H12345678(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
        self.next_step()

    def next_step(self):
        curr_block = self.currentBlock.value()
        step = self.step.value()
        step_id = step - 1

        if step == 64:
            if curr_block >= len(self.sha256Control.blocks) - 1:
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnEndOfBlock, self.btnNextBlock],
                                     active=False)
                return
            self.next_block(effect_on=False)
        elif step < 64:
            newStep = step + 1

            buffer_ABCDEFGH = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id][:8]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id + 1][:8],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id][:8]
                                + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id + 1][:8]
            }
            buffer_CTSChMa = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id + 1][8:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id + 1][8:]
            }

            self.btnPreviousStep.setEnabled(True)
            self.set_state_buffer_of_step(curr_block, newStep, buffer_CTSChMa, buffer_ABCDEFGH, None)
            if (self.currentBlock.value() == len(self.sha256Control.blocks) - 1 and
                    newStep == 64):
                self.set_enable_btns(list_btns=[self.btnNextStep, self.btnEndOfBlock, self.btnNextBlock],
                                     active=False)
                self.hash_hex.setText(self.sha256Control.hash_hex)

        self.visual_state_change_step()

    def pre_step(self):
        curr_block = self.currentBlock.value()
        step = self.step.value()
        step_id = step - 1
      
        if step_id == 0:
            if curr_block == 0:
                return
            else:
                curr_block -= 1
                self.currentBlock.setValue(curr_block)
                self.set_words_of_block(block=curr_block, group_words=0)
                if curr_block == 0:
                    buffer_H = self.sha256Control.cache["initialize_SHA_buffer"]
                    self.set_SHA_buffer_H12345678(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
                else:
                    buffer_H = {
                        "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
                        "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                    }
                    self.set_SHA_buffer_H12345678(buffer_H["int_big_endian"], buffer_H["hex_big_endian"])
                self.step.setValue(63)
                self.next_step()
        elif step_id == 1:
            if curr_block == 0:
                self.start_round()
            else:
                self.currentBlock.setValue(curr_block + 1)
                self.pre_block(effect_on=False)
        else:
            newStep = step - 1

            buffer_ABCDEFGH = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id - 2][:8]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id - 1][:8],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id - 2][:8]
                                + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id - 1][:8]
            }
            buffer_CTSChMa = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id - 1][8:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id - 1][8:]
            }

            self.set_state_buffer_of_step(curr_block, newStep, buffer_CTSChMa, buffer_ABCDEFGH, None)

        self.btnNextStep.setEnabled(True)
        self.btnStartOfBlock.setEnabled(True)
        self.visual_state_change_step()

    def end_of_block(self):
        self.step.setValue(63)
        self.next_step()
        self.btnStartOfBlock.setEnabled(True)

    def start_of_block(self):
        self.step.setValue(2)
        self.pre_step()
        self.btnEndOfBlock.setEnabled(True)

    def next_block(self, effect_on=True):
        self.visual_state_change_block(notStart=True, effect_on=effect_on)

        curr_block = self.currentBlock.value() + 1
        if curr_block > len(self.sha256Control.blocks) - 1:
            self.btnNextBlock.setEnabled(False)
            return
        curr_step = 1
        step_id = curr_step - 1

        buffer_ABCDEFGH = {
            "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"]
                             + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id][:8],
            "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                            + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id][:8]
        }
        buffer_CTSChMa = {
            "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id][8:],
            "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id][8:]
        }
        buffer_H = {
            "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
            "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
        }

        self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnEndOfBlock, self.btnPreviousBlock],
                             active=True)
        self.btnStartOfBlock.setEnabled(False)
        self.set_state_buffer_of_step(curr_block, curr_step, buffer_CTSChMa, buffer_ABCDEFGH, buffer_H)
        if self.currentBlock.value() == len(self.sha256Control.blocks) - 1:
            self.btnNextBlock.setEnabled(False)

    def pre_block(self, effect_on=True):
        curr_block = self.currentBlock.value() - 1
        if curr_block < 0:
            return
        curr_step = 1
        step_id = curr_step - 1

        if curr_block == 0:
            self.visual_state_change_block(notStart=False, effect_on=effect_on)
            self.start_round()
            self.set_enable_btns(list_btns=[self.btnPreviousStep, self.btnStartOfBlock, self.btnPreviousBlock],
                                 active=False)
        else:
            self.visual_state_change_block(notStart=True, effect_on=effect_on)
            buffer_ABCDEFGH = {
                "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"]
                                 + self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id][:8],
                "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
                              + self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id][:8]
            }
            buffer_CTSChMa = {
                "int_big_endian": self.steps_of_block[curr_block]["buffers_state"]["int_big_endian"][step_id][8:],
                "hex_big_endian": self.steps_of_block[curr_block]["buffers_state"]["hex_big_endian"][step_id][8:]
            }
            buffer_H = {
                "int_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["int_big_endian"],
                "hex_big_endian": self.steps_of_block[curr_block - 1]["end_of_block"]["hex_big_endian"]
            }

            self.set_state_buffer_of_step(curr_block, curr_step, buffer_CTSChMa, buffer_ABCDEFGH, buffer_H)
            self.set_enable_btns(list_btns=[self.btnNextStep, self.btnEndOfBlock, self.btnNextBlock],
                                 active=True)
            self.btnStartOfBlock.setEnabled(False)

    def set_state_buffer_of_step(self, curr_block, curr_step, buffer_CTSChMa, buffer_ABCDEFGH, buffer_Hi):
        cmp1 = (self.step.value() - 1) // 16
        cmp2 = (curr_step - 1) // 16
        if cmp2 > cmp1:
            self.set_words_of_block(block=curr_block, group_words=cmp2)

        self.step.setValue(curr_step)
        if curr_block != self.currentBlock.value():
            self.currentBlock.setValue(curr_block)
        self.set_buffer_CTSChMa(buffer_CTSChMa["int_big_endian"], buffer_CTSChMa["hex_big_endian"])
        self.set_SHA_buffer_ABCDEFGH(buffer_ABCDEFGH["int_big_endian"], buffer_ABCDEFGH["hex_big_endian"])
        if buffer_Hi:
            self.set_SHA_buffer_H12345678(buffer_Hi["int_big_endian"], buffer_Hi["hex_big_endian"])

    def set_buffer_CTSChMa(self, integers_big_endian, hexs_big_endian):
        labels = [
            self.labelValueSum1, self.labelValueSum0, self.labelValueMa,
            self.labelValueCh, self.labelValueT1, self.labelValueT2, self.labelAC
        ]
        for i, label in enumerate(labels):
            label.setText(f"{integers_big_endian[i]}\n{hexs_big_endian[i]}")

    def set_SHA_buffer_H12345678(self, integers_big_endian, hexs_big_endian):
        labels = [
            self.labelValueH1, self.labelValueH2, self.labelValueH3, self.labelValueH4,
            self.labelValueH5, self.labelValueH6, self.labelValueH7, self.labelValueH8
        ]
        for i, label in enumerate(labels):
            label.setText(f"{integers_big_endian[i]}\n{hexs_big_endian[i]}")

    def set_SHA_buffer_ABCDEFGH(self, integers_big_endian, hexs_big_endian):
        labels = [
            self.labelValueA, self.labelValueB, self.labelValueC, self.labelValueD,
            self.labelValueE, self.labelValueF, self.labelValueG, self.labelValueH,
            self.labelValueA_new, self.labelValueB_new, self.labelValueC_new, self.labelValueD_new,
            self.labelValueE_new, self.labelValueF_new, self.labelValueG_new, self.labelValueH_new
        ]
        for i, label in enumerate(labels):
            label.setText(f"{integers_big_endian[i]}\n{hexs_big_endian[i]}")

    def set_enable_btns(self, list_btns: list[QPushButton], active=True):
        for btn in list_btns:
            btn.setEnabled(active)

    def get_words_in_round_of_block(self, block, group_words):
        # get words of block
        words_of_block = self.steps_of_block[block]["words_of_block"]
        words_parser = [
            (words_of_block["int_big_endian"][0:16], words_of_block["hex_big_endian"][0:16]),
            (words_of_block["int_big_endian"][16:32], words_of_block["hex_big_endian"][16:32]),
            (words_of_block["int_big_endian"][32:48], words_of_block["hex_big_endian"][32:48]),
            (words_of_block["int_big_endian"][48:64], words_of_block["hex_big_endian"][48:64])
        ]
        integers_big_endian, hexs_big_endian = words_parser[group_words]

        return integers_big_endian, hexs_big_endian
    
    def set_name_groupBox_of_word(self, group_words):
        groups = [
            self.group_1, self.group_2, self.group_3, self.group_4,
            self.group_5, self.group_6, self.group_7, self.group_8,
            self.group_9, self.group_10, self.group_11, self.group_12,
            self.group_13, self.group_14, self.group_15, self.group_16
        ]
        for i, group in enumerate(groups):
            group.setTitle(str(group_words * 16 + i + 1))

    def set_words_of_block(self, block, group_words):
        integers_big_endian, hexs_big_endian = self.get_words_in_round_of_block(block, group_words)

        labels = [
            self.labelWord1, self.labelWord2, self.labelWord3, self.labelWord4,
            self.labelWord5, self.labelWord6, self.labelWord7, self.labelWord8,
            self.labelWord9, self.labelWord10, self.labelWord11, self.labelWord12,
            self.labelWord13, self.labelWord14, self.labelWord15, self.labelWord16
        ]

        for i, label in enumerate(labels):
            label.setText(f"{integers_big_endian[i]}\n{hexs_big_endian[i]}")

        self.set_name_groupBox_of_word(group_words)


    def visual_state_change_step(self):
        step = self.step.value() - 1
        states = StateWidget()
        timeSkip = states.timeSkip // 2
        groupBoxWord = self.get_groupBox_of_word(step % 16)
        groupBoxWord.setStyleSheet(states.GroupActive)
        QTimer.singleShot(timeSkip, lambda: groupBoxWord.setStyleSheet(states.GroupDeFault))

    def visual_state_change_block(self, notStart=True, effect_on=True):
        """
        Updates the visual state of UI elements for a block transition.
        """
        if not effect_on:
            return

        states = StateWidget()
        elements_to_update = [
            (self.operator6, states.OperatorActive, states.OperatorDefault) if notStart else None,
            (self.groupH1, states.GroupRes, states.GroupDeFault),
            (self.groupH2, states.GroupRes, states.GroupDeFault),
            (self.groupH3, states.GroupRes, states.GroupDeFault),
            (self.groupH4, states.GroupRes, states.GroupDeFault),
            (self.groupH5, states.GroupRes, states.GroupDeFault),
            (self.groupH6, states.GroupRes, states.GroupDeFault),
            (self.groupH7, states.GroupRes, states.GroupDeFault),
            (self.groupH8, states.GroupRes, states.GroupDeFault),
            (self.groupA, states.GroupRes, states.GroupDeFault),
            (self.groupB, states.GroupRes, states.GroupDeFault),
            (self.groupC, states.GroupRes, states.GroupDeFault),
            (self.groupD, states.GroupRes, states.GroupDeFault),
            (self.groupE, states.GroupRes, states.GroupDeFault),
            (self.groupF, states.GroupRes, states.GroupDeFault),
            (self.groupG, states.GroupRes, states.GroupDeFault),
            (self.groupH, states.GroupRes, states.GroupDeFault)
        ]

        for element, style, _ in elements_to_update:
            if style:
                element.setStyleSheet(style)

        timeSkip = states.timeSkip // 2
        for element, _, style in elements_to_update:
            QTimer.singleShot(timeSkip, lambda el=element, s=style: el.setStyleSheet(s))

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
        current_block = self.currentBlock.value()
        step = self.step.value()
        step_id = step - 1
        intermediate_results = self.steps_of_block[current_block]["intermediate_results"][f"step_{step_id}"]
        integers_big_endian = intermediate_results["int_big_endian"]
        hexs_big_endian = intermediate_results["hex_big_endian"]

        word_object = self.get_groupBox_of_word(step_id)

        states = StateWidget()
        self.groupE.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.groupE, states.GroupDeFault)
        self.groupSum1.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupSum1, states.GroupDeFault)
        self.groupA.setStyleSheet(states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.groupA, states.GroupDeFault)
        self.groupSum0.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupSum0, states.GroupDeFault)
        self._apply_styles([self.groupE, self.groupF, self.groupG], states.GroupActive)


        self.next_object_with_delay(states.timeSkip, self.groupE, states.GroupDeFault)
        self._apply_styles([self.groupF, self.groupG], states.GroupDeFault)
        self.groupCh.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupCh, states.GroupDeFault)
        self._apply_styles([self.groupA, self.groupB, self.groupC], states.GroupActive)

        self.next_object_with_delay(states.timeSkip, self.groupA, states.GroupDeFault)
        self._apply_styles([self.groupB, self.groupC], states.GroupDeFault)
        self.groupMa.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupMa, states.GroupDeFault)
        self._apply_styles([self.groupH, self.groupSum1], states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator4, states.OperatorDefault)
        self._apply_styles([self.groupH, self.groupSum1], states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(f"{integers_big_endian[0]}\n{hexs_big_endian[0]}")

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.groupCh.setStyleSheet(states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator4, states.OperatorDefault)
        self.groupCh.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(f"{integers_big_endian[1]}\n{hexs_big_endian[1]}")

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.groupAC.setStyleSheet(states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        self.groupAC.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(f"{integers_big_endian[2]}\n{hexs_big_endian[2]}")

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        word_object.setStyleSheet(states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.operator4, states.OperatorDefault)
        word_object.setStyleSheet(states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(f"{integers_big_endian[3]}\n{hexs_big_endian[3]}")

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.next_object_with_delay(states.timeSkip, self.groupT1, states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupDeFault)
        self.groupT1.setStyleSheet(states.GroupDeFault)
        self._apply_styles([self.groupSum0, self.groupMa], states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorActive)

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.operator4.setStyleSheet(states.OperatorDefault)
        self._apply_styles([self.groupSum0, self.groupMa], states.GroupDeFault)
        self.groupIntermRes.setStyleSheet(states.GroupRes)
        self.labelValueInterm.setText(f"{integers_big_endian[4]}\n{hexs_big_endian[4]}")

        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupActive)
        self.next_object_with_delay(states.timeSkip, self.groupT2, states.GroupRes)

        # Update state buffers
        self.next_object_with_delay(states.timeSkip, self.groupIntermRes, states.GroupDeFault)
        self._apply_styles([self.groupT2, self.groupT1], states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)
        self.groupA_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        self._apply_styles([self.groupT2, self.groupT1, self.groupA_new], states.GroupDeFault)
        self.groupA.setStyleSheet(states.GroupActive)
        self.groupB_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupA, states.GroupDeFault)
        self.groupB_new.setStyleSheet(states.GroupDeFault)
        self.groupB.setStyleSheet(states.GroupActive)
        self.groupC_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupB, states.GroupDeFault)
        self.groupC_new.setStyleSheet(states.GroupDeFault)
        self.groupC.setStyleSheet(states.GroupActive)
        self.groupD_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupC, states.GroupDeFault)
        self.groupD_new.setStyleSheet(states.GroupDeFault)
        self._apply_styles([self.groupD, self.groupT1], states.GroupActive)
        self.operator2.setStyleSheet(states.OperatorActive)
        self.groupE_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.operator2, states.OperatorDefault)
        self._apply_styles([self.groupD, self.groupT1, self.groupE_new], states.GroupDeFault)
        self.groupE.setStyleSheet(states.GroupActive)
        self.groupF_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupE, states.GroupDeFault)
        self.groupF_new.setStyleSheet(states.GroupDeFault)
        self.groupF.setStyleSheet(states.GroupActive)
        self.groupG_new.setStyleSheet(states.GroupRes)

        self.next_object_with_delay(states.timeSkip, self.groupF, states.GroupDeFault)
        self.groupG_new.setStyleSheet(states.GroupDeFault)
        self.groupG.setStyleSheet(states.GroupActive)
        self.groupH_new.setStyleSheet(states.GroupRes)


        self.next_object_with_delay(states.timeSkip, self.groupG, states.GroupDeFault)
        self.groupH_new.setStyleSheet(states.GroupDeFault)
        self.labelValueInterm.setText("")

        self.change_to_btnDetailStep()

    def _apply_styles(self, widgets, style):
        for widget in widgets:
            widget.setStyleSheet(style)

    def set_default_style_object(self, object):
        if isinstance(object, QGroupBox):
            object.setStyleSheet(StateWidget().GroupDeFault)
        elif isinstance(object, QPushButton):
            object.setStyleSheet(StateWidget().OperatorDefault)

    def get_groupBox_of_word(self, step):
        group_boxes = [
            self.group_1, self.group_2, self.group_3, self.group_4, self.group_5,
            self.group_6, self.group_7, self.group_8, self.group_9, self.group_10,
            self.group_11, self.group_12, self.group_13, self.group_14, self.group_15, self.group_16
        ]
        if 0 <= step < len(group_boxes):
            return group_boxes[step]
        return None
