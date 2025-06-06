# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formTxJTrF.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.NonModal)
        Form.resize(1505, 783)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_22 = QVBoxLayout(Form)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelTitle = QLabel(Form)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"QLabel {\n"
"        font-family: 'Arial', sans-serif;\n"
"        font-size: 24px;\n"
"        font-weight: bold;\n"
"        color: #4CAF50;  /* M\u00e0u xanh l\u00e1 */\n"
"        background-color: #f4f4f4; /* M\u00e0u n\u1ec1n s\u00e1ng */\n"
"        padding: 5px;\n"
"        border-radius: 5px;\n"
"    }")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelTitle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Text = QRadioButton(Form)
        self.Text.setObjectName(u"Text")
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Text.setIcon(icon)
        self.Text.setChecked(True)

        self.verticalLayout_7.addWidget(self.Text)

        self.File = QRadioButton(Form)
        self.File.setObjectName(u"File")
        icon1 = QIcon()
        icon1.addFile(u":/icons/iconsDark/file-text.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.File.setIcon(icon1)

        self.verticalLayout_7.addWidget(self.File)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.btnChooseFile = QPushButton(Form)
        self.btnChooseFile.setObjectName(u"btnChooseFile")
        icon2 = QIcon()
        icon2.addFile(u":/icons/iconsDark/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnChooseFile.setIcon(icon2)
        self.btnChooseFile.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.btnChooseFile)

        self.plaintext = QLineEdit(Form)
        self.plaintext.setObjectName(u"plaintext")

        self.horizontalLayout_13.addWidget(self.plaintext)

        self.Ok = QPushButton(Form)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/iconsDark/mouse-pointer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Ok.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.Ok)

        self.zoom_1 = QPushButton(Form)
        self.zoom_1.setObjectName(u"zoom_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/iconsDark/zoom-in.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoom_1.setIcon(icon4)

        self.horizontalLayout_13.addWidget(self.zoom_1)

        self.Clear = QPushButton(Form)
        self.Clear.setObjectName(u"Clear")
        icon5 = QIcon()
        icon5.addFile(u":/icons/iconsDark/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Clear.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.Clear)


        self.verticalLayout_22.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.plaintext_with_padding = QLineEdit(Form)
        self.plaintext_with_padding.setObjectName(u"plaintext_with_padding")

        self.horizontalLayout_11.addWidget(self.plaintext_with_padding)

        self.zoom_2 = QPushButton(Form)
        self.zoom_2.setObjectName(u"zoom_2")
        self.zoom_2.setIcon(icon4)

        self.horizontalLayout_11.addWidget(self.zoom_2)


        self.verticalLayout_22.addLayout(self.horizontalLayout_11)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame1 = QFrame(Form)
        self.frame1.setObjectName(u"frame1")
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout_8 = QHBoxLayout(self.frame1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.frame1)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.start = QPushButton(self.frame_6)
        self.start.setObjectName(u"start")
        self.start.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/iconsDark/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start.setIcon(icon6)

        self.verticalLayout_28.addWidget(self.start)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.currentBlock = QSpinBox(self.frame_6)
        self.currentBlock.setObjectName(u"currentBlock")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentBlock.sizePolicy().hasHeightForWidth())
        self.currentBlock.setSizePolicy(sizePolicy2)
        self.currentBlock.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.currentBlock)


        self.verticalLayout_28.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelStep = QLabel(self.frame_6)
        self.labelStep.setObjectName(u"labelStep")

        self.horizontalLayout_5.addWidget(self.labelStep)

        self.step = QSpinBox(self.frame_6)
        self.step.setObjectName(u"step")
        sizePolicy2.setHeightForWidth(self.step.sizePolicy().hasHeightForWidth())
        self.step.setSizePolicy(sizePolicy2)
        self.step.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.step)


        self.verticalLayout_28.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_28.addWidget(self.label_3)

        self.instruction = QTextEdit(self.frame_6)
        self.instruction.setObjectName(u"instruction")
        self.instruction.setEnabled(True)
        self.instruction.setMinimumSize(QSize(0, 200))
        self.instruction.setReadOnly(True)

        self.verticalLayout_28.addWidget(self.instruction)

        self.zoom_3 = QPushButton(self.frame_6)
        self.zoom_3.setObjectName(u"zoom_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zoom_3.sizePolicy().hasHeightForWidth())
        self.zoom_3.setSizePolicy(sizePolicy3)
        self.zoom_3.setMinimumSize(QSize(75, 0))
        self.zoom_3.setIcon(icon4)

        self.verticalLayout_28.addWidget(self.zoom_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame1)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.groupInputBlock = QGroupBox(self.frame_7)
        self.groupInputBlock.setObjectName(u"groupInputBlock")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupInputBlock.sizePolicy().hasHeightForWidth())
        self.groupInputBlock.setSizePolicy(sizePolicy4)
        self.verticalLayout = QVBoxLayout(self.groupInputBlock)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.groupInputBlock)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.group_1 = QGroupBox(self.frame_8)
        self.group_1.setObjectName(u"group_1")
        sizePolicy.setHeightForWidth(self.group_1.sizePolicy().hasHeightForWidth())
        self.group_1.setSizePolicy(sizePolicy)
        self.group_1.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA6 = QVBoxLayout(self.group_1)
        self.verticalLayoutA6.setObjectName(u"verticalLayoutA6")
        self.labelWord1 = QLabel(self.group_1)
        self.labelWord1.setObjectName(u"labelWord1")

        self.verticalLayoutA6.addWidget(self.labelWord1)


        self.horizontalLayout_14.addWidget(self.group_1)

        self.group_2 = QGroupBox(self.frame_8)
        self.group_2.setObjectName(u"group_2")
        sizePolicy.setHeightForWidth(self.group_2.sizePolicy().hasHeightForWidth())
        self.group_2.setSizePolicy(sizePolicy)
        self.group_2.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA7 = QVBoxLayout(self.group_2)
        self.verticalLayoutA7.setObjectName(u"verticalLayoutA7")
        self.labelWord2 = QLabel(self.group_2)
        self.labelWord2.setObjectName(u"labelWord2")

        self.verticalLayoutA7.addWidget(self.labelWord2)


        self.horizontalLayout_14.addWidget(self.group_2)

        self.group_3 = QGroupBox(self.frame_8)
        self.group_3.setObjectName(u"group_3")
        sizePolicy.setHeightForWidth(self.group_3.sizePolicy().hasHeightForWidth())
        self.group_3.setSizePolicy(sizePolicy)
        self.group_3.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA8 = QVBoxLayout(self.group_3)
        self.verticalLayoutA8.setObjectName(u"verticalLayoutA8")
        self.labelWord3 = QLabel(self.group_3)
        self.labelWord3.setObjectName(u"labelWord3")

        self.verticalLayoutA8.addWidget(self.labelWord3)


        self.horizontalLayout_14.addWidget(self.group_3)

        self.group_4 = QGroupBox(self.frame_8)
        self.group_4.setObjectName(u"group_4")
        sizePolicy.setHeightForWidth(self.group_4.sizePolicy().hasHeightForWidth())
        self.group_4.setSizePolicy(sizePolicy)
        self.group_4.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA9 = QVBoxLayout(self.group_4)
        self.verticalLayoutA9.setObjectName(u"verticalLayoutA9")
        self.labelWord4 = QLabel(self.group_4)
        self.labelWord4.setObjectName(u"labelWord4")

        self.verticalLayoutA9.addWidget(self.labelWord4)


        self.horizontalLayout_14.addWidget(self.group_4)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_2 = QFrame(self.groupInputBlock)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_5 = QGroupBox(self.frame_2)
        self.group_5.setObjectName(u"group_5")
        sizePolicy.setHeightForWidth(self.group_5.sizePolicy().hasHeightForWidth())
        self.group_5.setSizePolicy(sizePolicy)
        self.group_5.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_40 = QVBoxLayout(self.group_5)
        self.verticalLayoutA_40.setObjectName(u"verticalLayoutA_40")
        self.labelWord5 = QLabel(self.group_5)
        self.labelWord5.setObjectName(u"labelWord5")

        self.verticalLayoutA_40.addWidget(self.labelWord5)


        self.horizontalLayout.addWidget(self.group_5)

        self.group_6 = QGroupBox(self.frame_2)
        self.group_6.setObjectName(u"group_6")
        sizePolicy.setHeightForWidth(self.group_6.sizePolicy().hasHeightForWidth())
        self.group_6.setSizePolicy(sizePolicy)
        self.group_6.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_41 = QVBoxLayout(self.group_6)
        self.verticalLayoutA_41.setObjectName(u"verticalLayoutA_41")
        self.labelWord6 = QLabel(self.group_6)
        self.labelWord6.setObjectName(u"labelWord6")

        self.verticalLayoutA_41.addWidget(self.labelWord6)


        self.horizontalLayout.addWidget(self.group_6)

        self.group_7 = QGroupBox(self.frame_2)
        self.group_7.setObjectName(u"group_7")
        sizePolicy.setHeightForWidth(self.group_7.sizePolicy().hasHeightForWidth())
        self.group_7.setSizePolicy(sizePolicy)
        self.group_7.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_42 = QVBoxLayout(self.group_7)
        self.verticalLayoutA_42.setObjectName(u"verticalLayoutA_42")
        self.labelWord7 = QLabel(self.group_7)
        self.labelWord7.setObjectName(u"labelWord7")

        self.verticalLayoutA_42.addWidget(self.labelWord7)


        self.horizontalLayout.addWidget(self.group_7)

        self.group_8 = QGroupBox(self.frame_2)
        self.group_8.setObjectName(u"group_8")
        sizePolicy.setHeightForWidth(self.group_8.sizePolicy().hasHeightForWidth())
        self.group_8.setSizePolicy(sizePolicy)
        self.group_8.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_43 = QVBoxLayout(self.group_8)
        self.verticalLayoutA_43.setObjectName(u"verticalLayoutA_43")
        self.labelWord8 = QLabel(self.group_8)
        self.labelWord8.setObjectName(u"labelWord8")

        self.verticalLayoutA_43.addWidget(self.labelWord8)


        self.horizontalLayout.addWidget(self.group_8)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.groupInputBlock)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.group_9 = QGroupBox(self.frame)
        self.group_9.setObjectName(u"group_9")
        sizePolicy.setHeightForWidth(self.group_9.sizePolicy().hasHeightForWidth())
        self.group_9.setSizePolicy(sizePolicy)
        self.group_9.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_44 = QVBoxLayout(self.group_9)
        self.verticalLayoutA_44.setObjectName(u"verticalLayoutA_44")
        self.labelWord9 = QLabel(self.group_9)
        self.labelWord9.setObjectName(u"labelWord9")

        self.verticalLayoutA_44.addWidget(self.labelWord9)


        self.horizontalLayout_2.addWidget(self.group_9)

        self.group_10 = QGroupBox(self.frame)
        self.group_10.setObjectName(u"group_10")
        sizePolicy.setHeightForWidth(self.group_10.sizePolicy().hasHeightForWidth())
        self.group_10.setSizePolicy(sizePolicy)
        self.group_10.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_45 = QVBoxLayout(self.group_10)
        self.verticalLayoutA_45.setObjectName(u"verticalLayoutA_45")
        self.labelWord10 = QLabel(self.group_10)
        self.labelWord10.setObjectName(u"labelWord10")

        self.verticalLayoutA_45.addWidget(self.labelWord10)


        self.horizontalLayout_2.addWidget(self.group_10)

        self.group_11 = QGroupBox(self.frame)
        self.group_11.setObjectName(u"group_11")
        sizePolicy.setHeightForWidth(self.group_11.sizePolicy().hasHeightForWidth())
        self.group_11.setSizePolicy(sizePolicy)
        self.group_11.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_46 = QVBoxLayout(self.group_11)
        self.verticalLayoutA_46.setObjectName(u"verticalLayoutA_46")
        self.labelWord11 = QLabel(self.group_11)
        self.labelWord11.setObjectName(u"labelWord11")

        self.verticalLayoutA_46.addWidget(self.labelWord11)


        self.horizontalLayout_2.addWidget(self.group_11)

        self.group_12 = QGroupBox(self.frame)
        self.group_12.setObjectName(u"group_12")
        sizePolicy.setHeightForWidth(self.group_12.sizePolicy().hasHeightForWidth())
        self.group_12.setSizePolicy(sizePolicy)
        self.group_12.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_47 = QVBoxLayout(self.group_12)
        self.verticalLayoutA_47.setObjectName(u"verticalLayoutA_47")
        self.labelWord12 = QLabel(self.group_12)
        self.labelWord12.setObjectName(u"labelWord12")

        self.verticalLayoutA_47.addWidget(self.labelWord12)


        self.horizontalLayout_2.addWidget(self.group_12)


        self.verticalLayout.addWidget(self.frame)

        self.frame_9 = QFrame(self.groupInputBlock)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.group_13 = QGroupBox(self.frame_9)
        self.group_13.setObjectName(u"group_13")
        sizePolicy.setHeightForWidth(self.group_13.sizePolicy().hasHeightForWidth())
        self.group_13.setSizePolicy(sizePolicy)
        self.group_13.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_48 = QVBoxLayout(self.group_13)
        self.verticalLayoutA_48.setObjectName(u"verticalLayoutA_48")
        self.labelWord13 = QLabel(self.group_13)
        self.labelWord13.setObjectName(u"labelWord13")

        self.verticalLayoutA_48.addWidget(self.labelWord13)


        self.horizontalLayout_15.addWidget(self.group_13)

        self.group_14 = QGroupBox(self.frame_9)
        self.group_14.setObjectName(u"group_14")
        sizePolicy.setHeightForWidth(self.group_14.sizePolicy().hasHeightForWidth())
        self.group_14.setSizePolicy(sizePolicy)
        self.group_14.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_49 = QVBoxLayout(self.group_14)
        self.verticalLayoutA_49.setObjectName(u"verticalLayoutA_49")
        self.labelWord14 = QLabel(self.group_14)
        self.labelWord14.setObjectName(u"labelWord14")

        self.verticalLayoutA_49.addWidget(self.labelWord14)


        self.horizontalLayout_15.addWidget(self.group_14)

        self.group_15 = QGroupBox(self.frame_9)
        self.group_15.setObjectName(u"group_15")
        sizePolicy.setHeightForWidth(self.group_15.sizePolicy().hasHeightForWidth())
        self.group_15.setSizePolicy(sizePolicy)
        self.group_15.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_50 = QVBoxLayout(self.group_15)
        self.verticalLayoutA_50.setObjectName(u"verticalLayoutA_50")
        self.labelWord15 = QLabel(self.group_15)
        self.labelWord15.setObjectName(u"labelWord15")

        self.verticalLayoutA_50.addWidget(self.labelWord15)


        self.horizontalLayout_15.addWidget(self.group_15)

        self.group_16 = QGroupBox(self.frame_9)
        self.group_16.setObjectName(u"group_16")
        sizePolicy.setHeightForWidth(self.group_16.sizePolicy().hasHeightForWidth())
        self.group_16.setSizePolicy(sizePolicy)
        self.group_16.setMinimumSize(QSize(90, 68))
        self.verticalLayoutA_51 = QVBoxLayout(self.group_16)
        self.verticalLayoutA_51.setObjectName(u"verticalLayoutA_51")
        self.labelWord16 = QLabel(self.group_16)
        self.labelWord16.setObjectName(u"labelWord16")

        self.verticalLayoutA_51.addWidget(self.labelWord16)


        self.horizontalLayout_15.addWidget(self.group_16)


        self.verticalLayout.addWidget(self.frame_9)


        self.gridLayout_2.addWidget(self.groupInputBlock, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frameLay11 = QFrame(self.frame1)
        self.frameLay11.setObjectName(u"frameLay11")
        self.frameLay11.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_3 = QGridLayout(self.frameLay11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupSum1 = QGroupBox(self.frameLay11)
        self.groupSum1.setObjectName(u"groupSum1")
        sizePolicy3.setHeightForWidth(self.groupSum1.sizePolicy().hasHeightForWidth())
        self.groupSum1.setSizePolicy(sizePolicy3)
        self.groupSum1.setMinimumSize(QSize(110, 68))
        self.verticalLayout_8 = QVBoxLayout(self.groupSum1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelValueSum1 = QLabel(self.groupSum1)
        self.labelValueSum1.setObjectName(u"labelValueSum1")

        self.verticalLayout_8.addWidget(self.labelValueSum1)


        self.gridLayout_3.addWidget(self.groupSum1, 0, 2, 1, 1)

        self.groupMa = QGroupBox(self.frameLay11)
        self.groupMa.setObjectName(u"groupMa")
        sizePolicy3.setHeightForWidth(self.groupMa.sizePolicy().hasHeightForWidth())
        self.groupMa.setSizePolicy(sizePolicy3)
        self.groupMa.setMinimumSize(QSize(110, 68))
        self.verticalLayoutAC = QVBoxLayout(self.groupMa)
        self.verticalLayoutAC.setObjectName(u"verticalLayoutAC")
        self.labelValueMa = QLabel(self.groupMa)
        self.labelValueMa.setObjectName(u"labelValueMa")

        self.verticalLayoutAC.addWidget(self.labelValueMa)


        self.gridLayout_3.addWidget(self.groupMa, 3, 2, 1, 1)

        self.groupIntermRes = QGroupBox(self.frameLay11)
        self.groupIntermRes.setObjectName(u"groupIntermRes")
        sizePolicy3.setHeightForWidth(self.groupIntermRes.sizePolicy().hasHeightForWidth())
        self.groupIntermRes.setSizePolicy(sizePolicy3)
        self.groupIntermRes.setMinimumSize(QSize(145, 68))
        self.verticalLayout_12 = QVBoxLayout(self.groupIntermRes)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelValueInterm = QLabel(self.groupIntermRes)
        self.labelValueInterm.setObjectName(u"labelValueInterm")

        self.verticalLayout_12.addWidget(self.labelValueInterm)


        self.gridLayout_3.addWidget(self.groupIntermRes, 3, 0, 1, 1)

        self.operator1 = QPushButton(self.frameLay11)
        self.operator1.setObjectName(u"operator1")
        self.operator1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.operator1.sizePolicy().hasHeightForWidth())
        self.operator1.setSizePolicy(sizePolicy)
        self.operator1.setMinimumSize(QSize(52, 52))
        self.operator1.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #73C2FB, stop: 1 #2E86C1);\n"
"    border: 1px solid #2E86C1;\n"
"    border-radius: 25px;\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"    max-width: 50px;\n"
"    max-height: 50px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/iconsDark/rotate_left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operator1.setIcon(icon7)
        self.operator1.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.operator1, 0, 1, 1, 1)

        self.groupT2 = QGroupBox(self.frameLay11)
        self.groupT2.setObjectName(u"groupT2")
        sizePolicy3.setHeightForWidth(self.groupT2.sizePolicy().hasHeightForWidth())
        self.groupT2.setSizePolicy(sizePolicy3)
        self.groupT2.setMinimumSize(QSize(145, 68))
        self.verticalLayout_27 = QVBoxLayout(self.groupT2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelValueT2 = QLabel(self.groupT2)
        self.labelValueT2.setObjectName(u"labelValueT2")

        self.verticalLayout_27.addWidget(self.labelValueT2)


        self.gridLayout_3.addWidget(self.groupT2, 1, 0, 1, 1)

        self.operator2 = QPushButton(self.frameLay11)
        self.operator2.setObjectName(u"operator2")
        sizePolicy.setHeightForWidth(self.operator2.sizePolicy().hasHeightForWidth())
        self.operator2.setSizePolicy(sizePolicy)
        self.operator2.setMinimumSize(QSize(52, 52))
        self.operator2.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #73C2FB, stop: 1 #2E86C1);\n"
"    border: 1px solid #2E86C1;\n"
"    border-radius: 25px;\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"    max-width: 50px;\n"
"    max-height: 50px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/iconsDark/plus-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operator2.setIcon(icon8)
        self.operator2.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.operator2, 2, 1, 1, 1)

        self.operator4 = QPushButton(self.frameLay11)
        self.operator4.setObjectName(u"operator4")
        sizePolicy.setHeightForWidth(self.operator4.sizePolicy().hasHeightForWidth())
        self.operator4.setSizePolicy(sizePolicy)
        self.operator4.setMinimumSize(QSize(52, 52))
        self.operator4.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #73C2FB, stop: 1 #2E86C1);\n"
"    border: 1px solid #2E86C1;\n"
"    border-radius: 25px;\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"    max-width: 50px;\n"
"    max-height: 50px;\n"
"}")
        self.operator4.setIcon(icon8)
        self.operator4.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.operator4, 3, 1, 1, 1)

        self.groupSum0 = QGroupBox(self.frameLay11)
        self.groupSum0.setObjectName(u"groupSum0")
        self.groupSum0.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.groupSum0.sizePolicy().hasHeightForWidth())
        self.groupSum0.setSizePolicy(sizePolicy3)
        self.groupSum0.setMinimumSize(QSize(110, 68))
        self.verticalLayout_13 = QVBoxLayout(self.groupSum0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelValueSum0 = QLabel(self.groupSum0)
        self.labelValueSum0.setObjectName(u"labelValueSum0")

        self.verticalLayout_13.addWidget(self.labelValueSum0)


        self.gridLayout_3.addWidget(self.groupSum0, 1, 2, 1, 1)

        self.groupAC = QGroupBox(self.frameLay11)
        self.groupAC.setObjectName(u"groupAC")
        sizePolicy3.setHeightForWidth(self.groupAC.sizePolicy().hasHeightForWidth())
        self.groupAC.setSizePolicy(sizePolicy3)
        self.groupAC.setMinimumSize(QSize(145, 68))
        self.verticalLayout_24 = QVBoxLayout(self.groupAC)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelAC = QLabel(self.groupAC)
        self.labelAC.setObjectName(u"labelAC")

        self.verticalLayout_24.addWidget(self.labelAC)


        self.gridLayout_3.addWidget(self.groupAC, 2, 0, 1, 1)

        self.groupT1 = QGroupBox(self.frameLay11)
        self.groupT1.setObjectName(u"groupT1")
        sizePolicy3.setHeightForWidth(self.groupT1.sizePolicy().hasHeightForWidth())
        self.groupT1.setSizePolicy(sizePolicy3)
        self.groupT1.setMinimumSize(QSize(145, 68))
        self.verticalLayout_26 = QVBoxLayout(self.groupT1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(6, -1, -1, -1)
        self.labelValueT1 = QLabel(self.groupT1)
        self.labelValueT1.setObjectName(u"labelValueT1")

        self.verticalLayout_26.addWidget(self.labelValueT1)


        self.gridLayout_3.addWidget(self.groupT1, 0, 0, 1, 1)

        self.groupCh = QGroupBox(self.frameLay11)
        self.groupCh.setObjectName(u"groupCh")
        sizePolicy3.setHeightForWidth(self.groupCh.sizePolicy().hasHeightForWidth())
        self.groupCh.setSizePolicy(sizePolicy3)
        self.groupCh.setMinimumSize(QSize(110, 68))
        self.verticalLayoutSC = QVBoxLayout(self.groupCh)
        self.verticalLayoutSC.setObjectName(u"verticalLayoutSC")
        self.labelValueCh = QLabel(self.groupCh)
        self.labelValueCh.setObjectName(u"labelValueCh")

        self.verticalLayoutSC.addWidget(self.labelValueCh)


        self.gridLayout_3.addWidget(self.groupCh, 2, 2, 1, 1)

        self.operator3 = QPushButton(self.frameLay11)
        self.operator3.setObjectName(u"operator3")
        sizePolicy.setHeightForWidth(self.operator3.sizePolicy().hasHeightForWidth())
        self.operator3.setSizePolicy(sizePolicy)
        self.operator3.setMinimumSize(QSize(52, 52))
        self.operator3.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #73C2FB, stop: 1 #2E86C1);\n"
"    border: 1px solid #2E86C1;\n"
"    border-radius: 25px;\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"    max-width: 50px;\n"
"    max-height: 50px;\n"
"}")
        self.operator3.setIcon(icon7)
        self.operator3.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.operator3, 1, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.frameLay11)


        self.gridLayout_8.addWidget(self.frame1, 0, 0, 1, 1)

        self.frameLay1 = QFrame(Form)
        self.frameLay1.setObjectName(u"frameLay1")
        sizePolicy.setHeightForWidth(self.frameLay1.sizePolicy().hasHeightForWidth())
        self.frameLay1.setSizePolicy(sizePolicy)
        self.frameLay1.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_4 = QGridLayout(self.frameLay1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.frameLay1)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupH7 = QGroupBox(self.frame_5)
        self.groupH7.setObjectName(u"groupH7")
        sizePolicy.setHeightForWidth(self.groupH7.sizePolicy().hasHeightForWidth())
        self.groupH7.setSizePolicy(sizePolicy)
        self.groupH7.setMinimumSize(QSize(90, 68))
        self.verticalLayout_20 = QVBoxLayout(self.groupH7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.labelValueH7 = QLabel(self.groupH7)
        self.labelValueH7.setObjectName(u"labelValueH7")

        self.verticalLayout_20.addWidget(self.labelValueH7)


        self.gridLayout_7.addWidget(self.groupH7, 2, 2, 1, 1)

        self.groupH1 = QGroupBox(self.frame_5)
        self.groupH1.setObjectName(u"groupH1")
        sizePolicy.setHeightForWidth(self.groupH1.sizePolicy().hasHeightForWidth())
        self.groupH1.setSizePolicy(sizePolicy)
        self.groupH1.setMinimumSize(QSize(90, 68))
        self.verticalLayout_14 = QVBoxLayout(self.groupH1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.labelValueH1 = QLabel(self.groupH1)
        self.labelValueH1.setObjectName(u"labelValueH1")

        self.verticalLayout_14.addWidget(self.labelValueH1)


        self.gridLayout_7.addWidget(self.groupH1, 1, 0, 1, 1)

        self.groupH8 = QGroupBox(self.frame_5)
        self.groupH8.setObjectName(u"groupH8")
        sizePolicy.setHeightForWidth(self.groupH8.sizePolicy().hasHeightForWidth())
        self.groupH8.setSizePolicy(sizePolicy)
        self.groupH8.setMinimumSize(QSize(90, 68))
        self.verticalLayout_21 = QVBoxLayout(self.groupH8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.labelValueH8 = QLabel(self.groupH8)
        self.labelValueH8.setObjectName(u"labelValueH8")

        self.verticalLayout_21.addWidget(self.labelValueH8)


        self.gridLayout_7.addWidget(self.groupH8, 2, 3, 1, 1)

        self.groupH6 = QGroupBox(self.frame_5)
        self.groupH6.setObjectName(u"groupH6")
        sizePolicy.setHeightForWidth(self.groupH6.sizePolicy().hasHeightForWidth())
        self.groupH6.setSizePolicy(sizePolicy)
        self.groupH6.setMinimumSize(QSize(90, 68))
        self.verticalLayout_19 = QVBoxLayout(self.groupH6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.labelValueH6 = QLabel(self.groupH6)
        self.labelValueH6.setObjectName(u"labelValueH6")

        self.verticalLayout_19.addWidget(self.labelValueH6)


        self.gridLayout_7.addWidget(self.groupH6, 2, 1, 1, 1)

        self.groupH4 = QGroupBox(self.frame_5)
        self.groupH4.setObjectName(u"groupH4")
        sizePolicy.setHeightForWidth(self.groupH4.sizePolicy().hasHeightForWidth())
        self.groupH4.setSizePolicy(sizePolicy)
        self.groupH4.setMinimumSize(QSize(90, 68))
        self.verticalLayout_17 = QVBoxLayout(self.groupH4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.labelValueH4 = QLabel(self.groupH4)
        self.labelValueH4.setObjectName(u"labelValueH4")

        self.verticalLayout_17.addWidget(self.labelValueH4)


        self.gridLayout_7.addWidget(self.groupH4, 1, 3, 1, 1)

        self.groupH5 = QGroupBox(self.frame_5)
        self.groupH5.setObjectName(u"groupH5")
        sizePolicy.setHeightForWidth(self.groupH5.sizePolicy().hasHeightForWidth())
        self.groupH5.setSizePolicy(sizePolicy)
        self.groupH5.setMinimumSize(QSize(90, 68))
        self.verticalLayout_18 = QVBoxLayout(self.groupH5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelValueH5 = QLabel(self.groupH5)
        self.labelValueH5.setObjectName(u"labelValueH5")

        self.verticalLayout_18.addWidget(self.labelValueH5)


        self.gridLayout_7.addWidget(self.groupH5, 2, 0, 1, 1)

        self.groupH3 = QGroupBox(self.frame_5)
        self.groupH3.setObjectName(u"groupH3")
        sizePolicy.setHeightForWidth(self.groupH3.sizePolicy().hasHeightForWidth())
        self.groupH3.setSizePolicy(sizePolicy)
        self.groupH3.setMinimumSize(QSize(90, 68))
        self.verticalLayout_16 = QVBoxLayout(self.groupH3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelValueH3 = QLabel(self.groupH3)
        self.labelValueH3.setObjectName(u"labelValueH3")

        self.verticalLayout_16.addWidget(self.labelValueH3)


        self.gridLayout_7.addWidget(self.groupH3, 1, 2, 1, 1)

        self.groupH2 = QGroupBox(self.frame_5)
        self.groupH2.setObjectName(u"groupH2")
        sizePolicy.setHeightForWidth(self.groupH2.sizePolicy().hasHeightForWidth())
        self.groupH2.setSizePolicy(sizePolicy)
        self.groupH2.setMinimumSize(QSize(90, 68))
        self.verticalLayout_15 = QVBoxLayout(self.groupH2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.labelValueH2 = QLabel(self.groupH2)
        self.labelValueH2.setObjectName(u"labelValueH2")

        self.verticalLayout_15.addWidget(self.labelValueH2)


        self.gridLayout_7.addWidget(self.groupH2, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 5, 1, 1, 1)

        self.frame_3 = QFrame(self.frameLay1)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupA = QGroupBox(self.frame_3)
        self.groupA.setObjectName(u"groupA")
        sizePolicy.setHeightForWidth(self.groupA.sizePolicy().hasHeightForWidth())
        self.groupA.setSizePolicy(sizePolicy)
        self.groupA.setMinimumSize(QSize(90, 68))
        self.verticalLayout_29 = QVBoxLayout(self.groupA)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.labelValueA = QLabel(self.groupA)
        self.labelValueA.setObjectName(u"labelValueA")

        self.verticalLayout_29.addWidget(self.labelValueA)


        self.gridLayout_5.addWidget(self.groupA, 0, 0, 1, 1)

        self.groupB = QGroupBox(self.frame_3)
        self.groupB.setObjectName(u"groupB")
        sizePolicy.setHeightForWidth(self.groupB.sizePolicy().hasHeightForWidth())
        self.groupB.setSizePolicy(sizePolicy)
        self.groupB.setMinimumSize(QSize(90, 68))
        self.verticalLayout_30 = QVBoxLayout(self.groupB)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.labelValueB = QLabel(self.groupB)
        self.labelValueB.setObjectName(u"labelValueB")

        self.verticalLayout_30.addWidget(self.labelValueB)


        self.gridLayout_5.addWidget(self.groupB, 0, 1, 1, 1)

        self.groupC = QGroupBox(self.frame_3)
        self.groupC.setObjectName(u"groupC")
        sizePolicy.setHeightForWidth(self.groupC.sizePolicy().hasHeightForWidth())
        self.groupC.setSizePolicy(sizePolicy)
        self.groupC.setMinimumSize(QSize(90, 68))
        self.verticalLayout_31 = QVBoxLayout(self.groupC)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.labelValueC = QLabel(self.groupC)
        self.labelValueC.setObjectName(u"labelValueC")

        self.verticalLayout_31.addWidget(self.labelValueC)


        self.gridLayout_5.addWidget(self.groupC, 0, 2, 1, 1)

        self.groupD = QGroupBox(self.frame_3)
        self.groupD.setObjectName(u"groupD")
        sizePolicy.setHeightForWidth(self.groupD.sizePolicy().hasHeightForWidth())
        self.groupD.setSizePolicy(sizePolicy)
        self.groupD.setMinimumSize(QSize(90, 68))
        self.verticalLayout_32 = QVBoxLayout(self.groupD)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.labelValueD = QLabel(self.groupD)
        self.labelValueD.setObjectName(u"labelValueD")

        self.verticalLayout_32.addWidget(self.labelValueD)


        self.gridLayout_5.addWidget(self.groupD, 0, 3, 1, 1)

        self.groupE = QGroupBox(self.frame_3)
        self.groupE.setObjectName(u"groupE")
        sizePolicy.setHeightForWidth(self.groupE.sizePolicy().hasHeightForWidth())
        self.groupE.setSizePolicy(sizePolicy)
        self.groupE.setMinimumSize(QSize(90, 68))
        self.verticalLayout_33 = QVBoxLayout(self.groupE)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.labelValueE = QLabel(self.groupE)
        self.labelValueE.setObjectName(u"labelValueE")

        self.verticalLayout_33.addWidget(self.labelValueE)


        self.gridLayout_5.addWidget(self.groupE, 1, 0, 1, 1)

        self.groupF = QGroupBox(self.frame_3)
        self.groupF.setObjectName(u"groupF")
        sizePolicy.setHeightForWidth(self.groupF.sizePolicy().hasHeightForWidth())
        self.groupF.setSizePolicy(sizePolicy)
        self.groupF.setMinimumSize(QSize(90, 68))
        self.verticalLayout_34 = QVBoxLayout(self.groupF)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.labelValueF = QLabel(self.groupF)
        self.labelValueF.setObjectName(u"labelValueF")

        self.verticalLayout_34.addWidget(self.labelValueF)


        self.gridLayout_5.addWidget(self.groupF, 1, 1, 1, 1)

        self.groupG = QGroupBox(self.frame_3)
        self.groupG.setObjectName(u"groupG")
        sizePolicy.setHeightForWidth(self.groupG.sizePolicy().hasHeightForWidth())
        self.groupG.setSizePolicy(sizePolicy)
        self.groupG.setMinimumSize(QSize(90, 68))
        self.verticalLayout_35 = QVBoxLayout(self.groupG)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.labelValueG = QLabel(self.groupG)
        self.labelValueG.setObjectName(u"labelValueG")

        self.verticalLayout_35.addWidget(self.labelValueG)


        self.gridLayout_5.addWidget(self.groupG, 1, 2, 1, 1)

        self.groupH = QGroupBox(self.frame_3)
        self.groupH.setObjectName(u"groupH")
        sizePolicy.setHeightForWidth(self.groupH.sizePolicy().hasHeightForWidth())
        self.groupH.setSizePolicy(sizePolicy)
        self.groupH.setMinimumSize(QSize(90, 68))
        self.verticalLayout_36 = QVBoxLayout(self.groupH)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.labelValueH = QLabel(self.groupH)
        self.labelValueH.setObjectName(u"labelValueH")

        self.verticalLayout_36.addWidget(self.labelValueH)


        self.gridLayout_5.addWidget(self.groupH, 1, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.frameLay1)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupA_new = QGroupBox(self.frame_4)
        self.groupA_new.setObjectName(u"groupA_new")
        sizePolicy.setHeightForWidth(self.groupA_new.sizePolicy().hasHeightForWidth())
        self.groupA_new.setSizePolicy(sizePolicy)
        self.groupA_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_2 = QVBoxLayout(self.groupA_new)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelValueA_new = QLabel(self.groupA_new)
        self.labelValueA_new.setObjectName(u"labelValueA_new")

        self.verticalLayout_2.addWidget(self.labelValueA_new)


        self.gridLayout_6.addWidget(self.groupA_new, 0, 0, 1, 1)

        self.groupB_new = QGroupBox(self.frame_4)
        self.groupB_new.setObjectName(u"groupB_new")
        sizePolicy.setHeightForWidth(self.groupB_new.sizePolicy().hasHeightForWidth())
        self.groupB_new.setSizePolicy(sizePolicy)
        self.groupB_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_3 = QVBoxLayout(self.groupB_new)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelValueB_new = QLabel(self.groupB_new)
        self.labelValueB_new.setObjectName(u"labelValueB_new")

        self.verticalLayout_3.addWidget(self.labelValueB_new)


        self.gridLayout_6.addWidget(self.groupB_new, 0, 1, 1, 1)

        self.groupC_new = QGroupBox(self.frame_4)
        self.groupC_new.setObjectName(u"groupC_new")
        sizePolicy.setHeightForWidth(self.groupC_new.sizePolicy().hasHeightForWidth())
        self.groupC_new.setSizePolicy(sizePolicy)
        self.groupC_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_4 = QVBoxLayout(self.groupC_new)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelValueC_new = QLabel(self.groupC_new)
        self.labelValueC_new.setObjectName(u"labelValueC_new")

        self.verticalLayout_4.addWidget(self.labelValueC_new)


        self.gridLayout_6.addWidget(self.groupC_new, 0, 2, 1, 1)

        self.groupD_new = QGroupBox(self.frame_4)
        self.groupD_new.setObjectName(u"groupD_new")
        sizePolicy.setHeightForWidth(self.groupD_new.sizePolicy().hasHeightForWidth())
        self.groupD_new.setSizePolicy(sizePolicy)
        self.groupD_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_5 = QVBoxLayout(self.groupD_new)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelValueD_new = QLabel(self.groupD_new)
        self.labelValueD_new.setObjectName(u"labelValueD_new")

        self.verticalLayout_5.addWidget(self.labelValueD_new)


        self.gridLayout_6.addWidget(self.groupD_new, 0, 3, 1, 1)

        self.groupE_new = QGroupBox(self.frame_4)
        self.groupE_new.setObjectName(u"groupE_new")
        sizePolicy.setHeightForWidth(self.groupE_new.sizePolicy().hasHeightForWidth())
        self.groupE_new.setSizePolicy(sizePolicy)
        self.groupE_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_6 = QVBoxLayout(self.groupE_new)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelValueE_new = QLabel(self.groupE_new)
        self.labelValueE_new.setObjectName(u"labelValueE_new")

        self.verticalLayout_6.addWidget(self.labelValueE_new)


        self.gridLayout_6.addWidget(self.groupE_new, 1, 0, 1, 1)

        self.groupF_new = QGroupBox(self.frame_4)
        self.groupF_new.setObjectName(u"groupF_new")
        sizePolicy.setHeightForWidth(self.groupF_new.sizePolicy().hasHeightForWidth())
        self.groupF_new.setSizePolicy(sizePolicy)
        self.groupF_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_9 = QVBoxLayout(self.groupF_new)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelValueF_new = QLabel(self.groupF_new)
        self.labelValueF_new.setObjectName(u"labelValueF_new")

        self.verticalLayout_9.addWidget(self.labelValueF_new)


        self.gridLayout_6.addWidget(self.groupF_new, 1, 1, 1, 1)

        self.groupG_new = QGroupBox(self.frame_4)
        self.groupG_new.setObjectName(u"groupG_new")
        sizePolicy.setHeightForWidth(self.groupG_new.sizePolicy().hasHeightForWidth())
        self.groupG_new.setSizePolicy(sizePolicy)
        self.groupG_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_10 = QVBoxLayout(self.groupG_new)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelValueG_new = QLabel(self.groupG_new)
        self.labelValueG_new.setObjectName(u"labelValueG_new")

        self.verticalLayout_10.addWidget(self.labelValueG_new)


        self.gridLayout_6.addWidget(self.groupG_new, 1, 2, 1, 1)

        self.groupH_new = QGroupBox(self.frame_4)
        self.groupH_new.setObjectName(u"groupH_new")
        sizePolicy.setHeightForWidth(self.groupH_new.sizePolicy().hasHeightForWidth())
        self.groupH_new.setSizePolicy(sizePolicy)
        self.groupH_new.setMinimumSize(QSize(90, 68))
        self.verticalLayout_11 = QVBoxLayout(self.groupH_new)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelValueH_new = QLabel(self.groupH_new)
        self.labelValueH_new.setObjectName(u"labelValueH_new")

        self.verticalLayout_11.addWidget(self.labelValueH_new)


        self.gridLayout_6.addWidget(self.groupH_new, 1, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frameLay1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 0);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout_4.addWidget(self.label_4, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.operator6 = QPushButton(self.frameLay1)
        self.operator6.setObjectName(u"operator6")
        self.operator6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.operator6.sizePolicy().hasHeightForWidth())
        self.operator6.setSizePolicy(sizePolicy)
        self.operator6.setMinimumSize(QSize(52, 52))
        self.operator6.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #73C2FB, stop: 1 #2E86C1);\n"
"    border: 1px solid #2E86C1;\n"
"    border-radius: 25px;\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"    max-width: 50px;\n"
"    max-height: 50px;\n"
"}")
        self.operator6.setIcon(icon8)
        self.operator6.setIconSize(QSize(35, 35))

        self.gridLayout_4.addWidget(self.operator6, 5, 0, 1, 1)

        self.label_5 = QLabel(self.frameLay1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(85, 170, 0);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 0, 0, 5, 1)

        self.label_6 = QLabel(self.frameLay1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(85, 170, 0);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout_4.addWidget(self.label_6, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_8.addWidget(self.frameLay1, 0, 1, 2, 1)

        self.frame_10 = QFrame(Form)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.Shape.Box)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.finish = QPushButton(self.frame_10)
        self.finish.setObjectName(u"finish")
        self.finish.setEnabled(False)
        self.finish.setIcon(icon6)

        self.gridLayout.addWidget(self.finish, 1, 2, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.hash_hex = QLineEdit(self.frame_10)
        self.hash_hex.setObjectName(u"hash_hex")
        self.hash_hex.setReadOnly(True)

        self.gridLayout.addWidget(self.hash_hex, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.frame_10)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 3)


        self.gridLayout_8.addWidget(self.frame_10, 1, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_8)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.btnDetailStep = QPushButton(Form)
        self.btnDetailStep.setObjectName(u"btnDetailStep")
        self.btnDetailStep.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/iconsDark/activity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetailStep.setIcon(icon9)

        self.navLayout.addWidget(self.btnDetailStep)

        self.btnStepByStep = QPushButton(Form)
        self.btnStepByStep.setObjectName(u"btnStepByStep")
        self.btnStepByStep.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u":/icons/iconsDark/feather.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepByStep.setIcon(icon10)

        self.navLayout.addWidget(self.btnStepByStep)

        self.btnPreviousStep = QPushButton(Form)
        self.btnPreviousStep.setObjectName(u"btnPreviousStep")
        self.btnPreviousStep.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u":/icons/iconsDark/chevrons-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreviousStep.setIcon(icon11)

        self.navLayout.addWidget(self.btnPreviousStep)

        self.btnNextStep = QPushButton(Form)
        self.btnNextStep.setObjectName(u"btnNextStep")
        self.btnNextStep.setEnabled(False)
        icon12 = QIcon()
        icon12.addFile(u":/icons/iconsDark/chevrons-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNextStep.setIcon(icon12)

        self.navLayout.addWidget(self.btnNextStep)

        self.btnStartOfBlock = QPushButton(Form)
        self.btnStartOfBlock.setObjectName(u"btnStartOfBlock")
        self.btnStartOfBlock.setEnabled(False)
        icon13 = QIcon()
        icon13.addFile(u":/icons/iconsDark/rewind.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStartOfBlock.setIcon(icon13)

        self.navLayout.addWidget(self.btnStartOfBlock)

        self.btnEndOfBlock = QPushButton(Form)
        self.btnEndOfBlock.setObjectName(u"btnEndOfBlock")
        self.btnEndOfBlock.setEnabled(False)
        icon14 = QIcon()
        icon14.addFile(u":/icons/iconsDark/fast-forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEndOfBlock.setIcon(icon14)

        self.navLayout.addWidget(self.btnEndOfBlock)

        self.btnPreviousBlock = QPushButton(Form)
        self.btnPreviousBlock.setObjectName(u"btnPreviousBlock")
        self.btnPreviousBlock.setEnabled(False)
        self.btnPreviousBlock.setIcon(icon13)

        self.navLayout.addWidget(self.btnPreviousBlock)

        self.btnNextBlock = QPushButton(Form)
        self.btnNextBlock.setObjectName(u"btnNextBlock")
        self.btnNextBlock.setEnabled(False)
        self.btnNextBlock.setIcon(icon14)

        self.navLayout.addWidget(self.btnNextBlock)


        self.verticalLayout_22.addLayout(self.navLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("Form", u"Performing compression step", None))
        self.Text.setText(QCoreApplication.translate("Form", u"Text", None))
        self.File.setText(QCoreApplication.translate("Form", u"File", None))
        self.btnChooseFile.setText(QCoreApplication.translate("Form", u"Choose file", None))
        self.Ok.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.zoom_1.setText(QCoreApplication.translate("Form", u"Zoom in", None))
        self.Clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Form", u"PlainText after\n"
" add padding:", None))
        self.zoom_2.setText(QCoreApplication.translate("Form", u"Zoom in", None))
        self.start.setText(QCoreApplication.translate("Form", u"Start round", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Current block", None))
        self.labelStep.setText(QCoreApplication.translate("Form", u"Step:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Instruction algorithm:", None))
        self.instruction.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.zoom_3.setText(QCoreApplication.translate("Form", u"Zoom in", None))
        self.groupInputBlock.setTitle(QCoreApplication.translate("Form", u"Selected part from input data block", None))
        self.group_1.setTitle(QCoreApplication.translate("Form", u"1", None))
        self.labelWord1.setText("")
        self.group_2.setTitle(QCoreApplication.translate("Form", u"2", None))
        self.labelWord2.setText("")
        self.group_3.setTitle(QCoreApplication.translate("Form", u"3", None))
        self.labelWord3.setText("")
        self.group_4.setTitle(QCoreApplication.translate("Form", u"4", None))
        self.labelWord4.setText("")
        self.group_5.setTitle(QCoreApplication.translate("Form", u"5", None))
        self.labelWord5.setText("")
        self.group_6.setTitle(QCoreApplication.translate("Form", u"6", None))
        self.labelWord6.setText("")
        self.group_7.setTitle(QCoreApplication.translate("Form", u"7", None))
        self.labelWord7.setText("")
        self.group_8.setTitle(QCoreApplication.translate("Form", u"8", None))
        self.labelWord8.setText("")
        self.group_9.setTitle(QCoreApplication.translate("Form", u"9", None))
        self.labelWord9.setText("")
        self.group_10.setTitle(QCoreApplication.translate("Form", u"10", None))
        self.labelWord10.setText("")
        self.group_11.setTitle(QCoreApplication.translate("Form", u"11", None))
        self.labelWord11.setText("")
        self.group_12.setTitle(QCoreApplication.translate("Form", u"12", None))
        self.labelWord12.setText("")
        self.group_13.setTitle(QCoreApplication.translate("Form", u"13", None))
        self.labelWord13.setText("")
        self.group_14.setTitle(QCoreApplication.translate("Form", u"14", None))
        self.labelWord14.setText("")
        self.group_15.setTitle(QCoreApplication.translate("Form", u"15", None))
        self.labelWord15.setText("")
        self.group_16.setTitle(QCoreApplication.translate("Form", u"16", None))
        self.labelWord16.setText("")
        self.groupSum1.setTitle(QCoreApplication.translate("Form", u"Sum1", None))
        self.labelValueSum1.setText("")
        self.groupMa.setTitle(QCoreApplication.translate("Form", u"Ma", None))
        self.labelValueMa.setText("")
        self.groupIntermRes.setTitle(QCoreApplication.translate("Form", u"Intermediate results", None))
        self.labelValueInterm.setText("")
        self.operator1.setText("")
        self.groupT2.setTitle(QCoreApplication.translate("Form", u"T2", None))
        self.labelValueT2.setText("")
        self.operator2.setText("")
        self.operator4.setText("")
        self.groupSum0.setTitle(QCoreApplication.translate("Form", u"Sum0", None))
        self.labelValueSum0.setText("")
        self.groupAC.setTitle(QCoreApplication.translate("Form", u"Addition constant (AC)", None))
        self.labelAC.setText("")
        self.groupT1.setTitle(QCoreApplication.translate("Form", u"T1", None))
        self.labelValueT1.setText("")
        self.groupCh.setTitle(QCoreApplication.translate("Form", u"Ch", None))
        self.labelValueCh.setText("")
        self.operator3.setText("")
        self.groupH7.setTitle(QCoreApplication.translate("Form", u"H7", None))
        self.labelValueH7.setText("")
        self.groupH1.setTitle(QCoreApplication.translate("Form", u"H1", None))
        self.labelValueH1.setText("")
        self.groupH8.setTitle(QCoreApplication.translate("Form", u"H8", None))
        self.labelValueH8.setText("")
        self.groupH6.setTitle(QCoreApplication.translate("Form", u"H6", None))
        self.labelValueH6.setText("")
        self.groupH4.setTitle(QCoreApplication.translate("Form", u"H4", None))
        self.labelValueH4.setText("")
        self.groupH5.setTitle(QCoreApplication.translate("Form", u"H5", None))
        self.labelValueH5.setText("")
        self.groupH3.setTitle(QCoreApplication.translate("Form", u"H3", None))
        self.labelValueH3.setText("")
        self.groupH2.setTitle(QCoreApplication.translate("Form", u"H2", None))
        self.labelValueH2.setText("")
        self.groupA.setTitle(QCoreApplication.translate("Form", u"A", None))
        self.labelValueA.setText("")
        self.groupB.setTitle(QCoreApplication.translate("Form", u"B", None))
        self.labelValueB.setText("")
        self.groupC.setTitle(QCoreApplication.translate("Form", u"C", None))
        self.labelValueC.setText("")
        self.groupD.setTitle(QCoreApplication.translate("Form", u"D", None))
        self.labelValueD.setText("")
        self.groupE.setTitle(QCoreApplication.translate("Form", u"E", None))
        self.labelValueE.setText("")
        self.groupF.setTitle(QCoreApplication.translate("Form", u"F", None))
        self.labelValueF.setText("")
        self.groupG.setTitle(QCoreApplication.translate("Form", u"G", None))
        self.labelValueG.setText("")
        self.groupH.setTitle(QCoreApplication.translate("Form", u"H", None))
        self.labelValueH.setText("")
        self.groupA_new.setTitle(QCoreApplication.translate("Form", u"A", None))
        self.labelValueA_new.setText("")
        self.groupB_new.setTitle(QCoreApplication.translate("Form", u"B", None))
        self.labelValueB_new.setText("")
        self.groupC_new.setTitle(QCoreApplication.translate("Form", u"C", None))
        self.labelValueC_new.setText("")
        self.groupD_new.setTitle(QCoreApplication.translate("Form", u"D", None))
        self.labelValueD_new.setText("")
        self.groupE_new.setTitle(QCoreApplication.translate("Form", u"E", None))
        self.labelValueE_new.setText("")
        self.groupF_new.setTitle(QCoreApplication.translate("Form", u"F", None))
        self.labelValueF_new.setText("")
        self.groupG_new.setTitle(QCoreApplication.translate("Form", u"G", None))
        self.labelValueG_new.setText("")
        self.groupH_new.setTitle(QCoreApplication.translate("Form", u"H", None))
        self.labelValueH_new.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"New values of buffer for next step", None))
        self.operator6.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"The value of buffer in the current step", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"The buffer is initialized at the beginning of each block", None))
        self.finish.setText(QCoreApplication.translate("Form", u"Finish process", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Hash value (hex):", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SHA-256, designed by the U.S. NSA and published by NIST in 2001 as part of FIPS 180-2, doubles the digest size of SHA-1 to 256 bits and uses a more complex message schedule. It was created to address collision-resistance weaknesses in SHA-1 and today underpins everything from TLS to blockchain proof-of-work.</p></body></html>", None))
        self.btnDetailStep.setText(QCoreApplication.translate("Form", u"Detail step", None))
        self.btnStepByStep.setText(QCoreApplication.translate("Form", u"Step by step", None))
        self.btnPreviousStep.setText(QCoreApplication.translate("Form", u"Previous Step", None))
        self.btnNextStep.setText(QCoreApplication.translate("Form", u"Next Step", None))
        self.btnStartOfBlock.setText(QCoreApplication.translate("Form", u"Start Of Block", None))
        self.btnEndOfBlock.setText(QCoreApplication.translate("Form", u"End Of Block", None))
        self.btnPreviousBlock.setText(QCoreApplication.translate("Form", u"Previous Block", None))
        self.btnNextBlock.setText(QCoreApplication.translate("Form", u"Next Block", None))
    # retranslateUi

