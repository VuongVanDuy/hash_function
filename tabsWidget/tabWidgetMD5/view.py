# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
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
        Form.resize(1227, 780)
        self.verticalLayout_10 = QVBoxLayout(Form)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.labelTitle = QLabel(Form)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.titleLayout.addWidget(self.labelTitle)


        self.verticalLayout_10.addLayout(self.titleLayout)

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

        self.plaintext = QTextEdit(Form)
        self.plaintext.setObjectName(u"plaintext")

        self.horizontalLayout_13.addWidget(self.plaintext)

        self.Ok = QPushButton(Form)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/iconsDark/mouse-pointer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Ok.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.Ok)

        self.Clear = QPushButton(Form)
        self.Clear.setObjectName(u"Clear")
        icon4 = QIcon()
        icon4.addFile(u":/icons/iconsDark/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Clear.setIcon(icon4)

        self.horizontalLayout_13.addWidget(self.Clear)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.plaintext_with_padding = QLineEdit(Form)
        self.plaintext_with_padding.setObjectName(u"plaintext_with_padding")

        self.horizontalLayout_11.addWidget(self.plaintext_with_padding)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.registerLayoutTop = QHBoxLayout()
        self.registerLayoutTop.setObjectName(u"registerLayoutTop")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.start = QPushButton(Form)
        self.start.setObjectName(u"start")
        self.start.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/iconsDark/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start.setIcon(icon5)

        self.horizontalLayout_12.addWidget(self.start)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.currentBlock = QSpinBox(Form)
        self.currentBlock.setObjectName(u"currentBlock")
        self.currentBlock.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.currentBlock)

        self.labelRound = QLabel(Form)
        self.labelRound.setObjectName(u"labelRound")

        self.horizontalLayout_12.addWidget(self.labelRound)

        self.round = QSpinBox(Form)
        self.round.setObjectName(u"round")

        self.horizontalLayout_12.addWidget(self.round)

        self.labelStep = QLabel(Form)
        self.labelStep.setObjectName(u"labelStep")

        self.horizontalLayout_12.addWidget(self.labelStep)

        self.stepRound = QSpinBox(Form)
        self.stepRound.setObjectName(u"stepRound")
        self.stepRound.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.stepRound)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_20)


        self.registerLayoutTop.addLayout(self.horizontalLayout_12)

        self.groupA = QGroupBox(Form)
        self.groupA.setObjectName(u"groupA")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupA.sizePolicy().hasHeightForWidth())
        self.groupA.setSizePolicy(sizePolicy)
        self.groupA.setMinimumSize(QSize(90, 68))
        self.groupA.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA5 = QVBoxLayout(self.groupA)
        self.verticalLayoutA5.setObjectName(u"verticalLayoutA5")
        self.labelValueA = QLabel(self.groupA)
        self.labelValueA.setObjectName(u"labelValueA")

        self.verticalLayoutA5.addWidget(self.labelValueA)


        self.registerLayoutTop.addWidget(self.groupA)

        self.groupB = QGroupBox(Form)
        self.groupB.setObjectName(u"groupB")
        sizePolicy.setHeightForWidth(self.groupB.sizePolicy().hasHeightForWidth())
        self.groupB.setSizePolicy(sizePolicy)
        self.groupB.setMinimumSize(QSize(90, 68))
        self.groupB.setMaximumSize(QSize(90, 68))
        self.verticalLayoutB = QVBoxLayout(self.groupB)
        self.verticalLayoutB.setObjectName(u"verticalLayoutB")
        self.labelValueB = QLabel(self.groupB)
        self.labelValueB.setObjectName(u"labelValueB")

        self.verticalLayoutB.addWidget(self.labelValueB)


        self.registerLayoutTop.addWidget(self.groupB)

        self.groupC = QGroupBox(Form)
        self.groupC.setObjectName(u"groupC")
        sizePolicy.setHeightForWidth(self.groupC.sizePolicy().hasHeightForWidth())
        self.groupC.setSizePolicy(sizePolicy)
        self.groupC.setMinimumSize(QSize(90, 68))
        self.groupC.setMaximumSize(QSize(90, 16777215))
        self.verticalLayoutC = QVBoxLayout(self.groupC)
        self.verticalLayoutC.setObjectName(u"verticalLayoutC")
        self.labelValueC = QLabel(self.groupC)
        self.labelValueC.setObjectName(u"labelValueC")

        self.verticalLayoutC.addWidget(self.labelValueC)


        self.registerLayoutTop.addWidget(self.groupC)

        self.groupD = QGroupBox(Form)
        self.groupD.setObjectName(u"groupD")
        sizePolicy.setHeightForWidth(self.groupD.sizePolicy().hasHeightForWidth())
        self.groupD.setSizePolicy(sizePolicy)
        self.groupD.setMinimumSize(QSize(90, 68))
        self.groupD.setMaximumSize(QSize(90, 68))
        self.verticalLayoutD = QVBoxLayout(self.groupD)
        self.verticalLayoutD.setObjectName(u"verticalLayoutD")
        self.labelValueD = QLabel(self.groupD)
        self.labelValueD.setObjectName(u"labelValueD")

        self.verticalLayoutD.addWidget(self.labelValueD)


        self.registerLayoutTop.addWidget(self.groupD)


        self.verticalLayout_10.addLayout(self.registerLayoutTop)

        self.mainMidLayout = QHBoxLayout()
        self.mainMidLayout.setObjectName(u"mainMidLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupF = QGroupBox(Form)
        self.groupF.setObjectName(u"groupF")
        sizePolicy.setHeightForWidth(self.groupF.sizePolicy().hasHeightForWidth())
        self.groupF.setSizePolicy(sizePolicy)
        self.groupF.setMinimumSize(QSize(110, 80))
        self.groupF.setMaximumSize(QSize(110, 80))
        self.verticalLayout_8 = QVBoxLayout(self.groupF)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelValueF = QLabel(self.groupF)
        self.labelValueF.setObjectName(u"labelValueF")

        self.verticalLayout_8.addWidget(self.labelValueF)


        self.gridLayout_5.addWidget(self.groupF, 0, 6, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.labelPlus2 = QLabel(Form)
        self.labelPlus2.setObjectName(u"labelPlus2")
        sizePolicy.setHeightForWidth(self.labelPlus2.sizePolicy().hasHeightForWidth())
        self.labelPlus2.setSizePolicy(sizePolicy)
        self.labelPlus2.setMinimumSize(QSize(60, 60))
        self.labelPlus2.setMaximumSize(QSize(60, 60))
        self.labelPlus2.setStyleSheet(u"QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 2px solid #1E90FF; \n"
"}\n"
"")
        self.labelPlus2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labelPlus2, 1, 1, 1, 4)

        self.frame_7 = QFrame(Form)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.vboxConstants = QVBoxLayout()
        self.vboxConstants.setObjectName(u"vboxConstants")
        self.groupAC = QGroupBox(self.frame_7)
        self.groupAC.setObjectName(u"groupAC")
        sizePolicy.setHeightForWidth(self.groupAC.sizePolicy().hasHeightForWidth())
        self.groupAC.setSizePolicy(sizePolicy)
        self.groupAC.setMinimumSize(QSize(200, 70))
        self.groupAC.setMaximumSize(QSize(200, 70))
        self.verticalLayoutAC = QVBoxLayout(self.groupAC)
        self.verticalLayoutAC.setObjectName(u"verticalLayoutAC")
        self.labelAC = QLabel(self.groupAC)
        self.labelAC.setObjectName(u"labelAC")

        self.verticalLayoutAC.addWidget(self.labelAC)


        self.vboxConstants.addWidget(self.groupAC, 0, Qt.AlignmentFlag.AlignRight)

        self.groupSC = QGroupBox(self.frame_7)
        self.groupSC.setObjectName(u"groupSC")
        sizePolicy.setHeightForWidth(self.groupSC.sizePolicy().hasHeightForWidth())
        self.groupSC.setSizePolicy(sizePolicy)
        self.groupSC.setMinimumSize(QSize(200, 70))
        self.groupSC.setMaximumSize(QSize(200, 70))
        self.verticalLayoutSC = QVBoxLayout(self.groupSC)
        self.verticalLayoutSC.setObjectName(u"verticalLayoutSC")
        self.labelSC = QLabel(self.groupSC)
        self.labelSC.setObjectName(u"labelSC")

        self.verticalLayoutSC.addWidget(self.labelSC)


        self.vboxConstants.addWidget(self.groupSC, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_6.addLayout(self.vboxConstants, 1, 0, 1, 1)

        self.groupInputBlock = QGroupBox(self.frame_7)
        self.groupInputBlock.setObjectName(u"groupInputBlock")
        self.gridLayoutInput = QGridLayout(self.groupInputBlock)
        self.gridLayoutInput.setObjectName(u"gridLayoutInput")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.groupInputBlock)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.group_1 = QGroupBox(self.frame_8)
        self.group_1.setObjectName(u"group_1")
        sizePolicy.setHeightForWidth(self.group_1.sizePolicy().hasHeightForWidth())
        self.group_1.setSizePolicy(sizePolicy)
        self.group_1.setMinimumSize(QSize(90, 68))
        self.group_1.setMaximumSize(QSize(90, 68))
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
        self.group_2.setMaximumSize(QSize(90, 68))
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
        self.group_3.setMaximumSize(QSize(90, 68))
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
        self.group_4.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA9 = QVBoxLayout(self.group_4)
        self.verticalLayoutA9.setObjectName(u"verticalLayoutA9")
        self.labelWord4 = QLabel(self.group_4)
        self.labelWord4.setObjectName(u"labelWord4")

        self.verticalLayoutA9.addWidget(self.labelWord4)


        self.horizontalLayout_14.addWidget(self.group_4)

        self.group_5 = QGroupBox(self.frame_8)
        self.group_5.setObjectName(u"group_5")
        sizePolicy.setHeightForWidth(self.group_5.sizePolicy().hasHeightForWidth())
        self.group_5.setSizePolicy(sizePolicy)
        self.group_5.setMinimumSize(QSize(90, 68))
        self.group_5.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_40 = QVBoxLayout(self.group_5)
        self.verticalLayoutA_40.setObjectName(u"verticalLayoutA_40")
        self.labelWord5 = QLabel(self.group_5)
        self.labelWord5.setObjectName(u"labelWord5")

        self.verticalLayoutA_40.addWidget(self.labelWord5)


        self.horizontalLayout_14.addWidget(self.group_5)

        self.group_6 = QGroupBox(self.frame_8)
        self.group_6.setObjectName(u"group_6")
        sizePolicy.setHeightForWidth(self.group_6.sizePolicy().hasHeightForWidth())
        self.group_6.setSizePolicy(sizePolicy)
        self.group_6.setMinimumSize(QSize(90, 68))
        self.group_6.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_41 = QVBoxLayout(self.group_6)
        self.verticalLayoutA_41.setObjectName(u"verticalLayoutA_41")
        self.labelWord6 = QLabel(self.group_6)
        self.labelWord6.setObjectName(u"labelWord6")

        self.verticalLayoutA_41.addWidget(self.labelWord6)


        self.horizontalLayout_14.addWidget(self.group_6)

        self.group_7 = QGroupBox(self.frame_8)
        self.group_7.setObjectName(u"group_7")
        sizePolicy.setHeightForWidth(self.group_7.sizePolicy().hasHeightForWidth())
        self.group_7.setSizePolicy(sizePolicy)
        self.group_7.setMinimumSize(QSize(90, 68))
        self.group_7.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_42 = QVBoxLayout(self.group_7)
        self.verticalLayoutA_42.setObjectName(u"verticalLayoutA_42")
        self.labelWord7 = QLabel(self.group_7)
        self.labelWord7.setObjectName(u"labelWord7")

        self.verticalLayoutA_42.addWidget(self.labelWord7)


        self.horizontalLayout_14.addWidget(self.group_7)

        self.group_8 = QGroupBox(self.frame_8)
        self.group_8.setObjectName(u"group_8")
        sizePolicy.setHeightForWidth(self.group_8.sizePolicy().hasHeightForWidth())
        self.group_8.setSizePolicy(sizePolicy)
        self.group_8.setMinimumSize(QSize(90, 68))
        self.group_8.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_43 = QVBoxLayout(self.group_8)
        self.verticalLayoutA_43.setObjectName(u"verticalLayoutA_43")
        self.labelWord8 = QLabel(self.group_8)
        self.labelWord8.setObjectName(u"labelWord8")

        self.verticalLayoutA_43.addWidget(self.labelWord8)


        self.horizontalLayout_14.addWidget(self.group_8)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.groupInputBlock)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.group_9 = QGroupBox(self.frame_9)
        self.group_9.setObjectName(u"group_9")
        sizePolicy.setHeightForWidth(self.group_9.sizePolicy().hasHeightForWidth())
        self.group_9.setSizePolicy(sizePolicy)
        self.group_9.setMinimumSize(QSize(90, 68))
        self.group_9.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_44 = QVBoxLayout(self.group_9)
        self.verticalLayoutA_44.setObjectName(u"verticalLayoutA_44")
        self.labelWord9 = QLabel(self.group_9)
        self.labelWord9.setObjectName(u"labelWord9")

        self.verticalLayoutA_44.addWidget(self.labelWord9)


        self.horizontalLayout_15.addWidget(self.group_9)

        self.group_10 = QGroupBox(self.frame_9)
        self.group_10.setObjectName(u"group_10")
        sizePolicy.setHeightForWidth(self.group_10.sizePolicy().hasHeightForWidth())
        self.group_10.setSizePolicy(sizePolicy)
        self.group_10.setMinimumSize(QSize(90, 68))
        self.group_10.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_45 = QVBoxLayout(self.group_10)
        self.verticalLayoutA_45.setObjectName(u"verticalLayoutA_45")
        self.labelWord10 = QLabel(self.group_10)
        self.labelWord10.setObjectName(u"labelWord10")

        self.verticalLayoutA_45.addWidget(self.labelWord10)


        self.horizontalLayout_15.addWidget(self.group_10)

        self.group_11 = QGroupBox(self.frame_9)
        self.group_11.setObjectName(u"group_11")
        sizePolicy.setHeightForWidth(self.group_11.sizePolicy().hasHeightForWidth())
        self.group_11.setSizePolicy(sizePolicy)
        self.group_11.setMinimumSize(QSize(90, 68))
        self.group_11.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_46 = QVBoxLayout(self.group_11)
        self.verticalLayoutA_46.setObjectName(u"verticalLayoutA_46")
        self.labelWord11 = QLabel(self.group_11)
        self.labelWord11.setObjectName(u"labelWord11")

        self.verticalLayoutA_46.addWidget(self.labelWord11)


        self.horizontalLayout_15.addWidget(self.group_11)

        self.group_12 = QGroupBox(self.frame_9)
        self.group_12.setObjectName(u"group_12")
        sizePolicy.setHeightForWidth(self.group_12.sizePolicy().hasHeightForWidth())
        self.group_12.setSizePolicy(sizePolicy)
        self.group_12.setMinimumSize(QSize(90, 68))
        self.group_12.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_47 = QVBoxLayout(self.group_12)
        self.verticalLayoutA_47.setObjectName(u"verticalLayoutA_47")
        self.labelWord12 = QLabel(self.group_12)
        self.labelWord12.setObjectName(u"labelWord12")

        self.verticalLayoutA_47.addWidget(self.labelWord12)


        self.horizontalLayout_15.addWidget(self.group_12)

        self.group_13 = QGroupBox(self.frame_9)
        self.group_13.setObjectName(u"group_13")
        sizePolicy.setHeightForWidth(self.group_13.sizePolicy().hasHeightForWidth())
        self.group_13.setSizePolicy(sizePolicy)
        self.group_13.setMinimumSize(QSize(90, 68))
        self.group_13.setMaximumSize(QSize(90, 68))
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
        self.group_14.setMaximumSize(QSize(90, 68))
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
        self.group_15.setMaximumSize(QSize(90, 68))
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
        self.group_16.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_51 = QVBoxLayout(self.group_16)
        self.verticalLayoutA_51.setObjectName(u"verticalLayoutA_51")
        self.labelWord16 = QLabel(self.group_16)
        self.labelWord16.setObjectName(u"labelWord16")

        self.verticalLayoutA_51.addWidget(self.labelWord16)


        self.horizontalLayout_15.addWidget(self.group_16)


        self.verticalLayout_9.addWidget(self.frame_9)


        self.gridLayoutInput.addLayout(self.verticalLayout_9, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupInputBlock, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 5, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_21, 3, 5, 1, 1)

        self.labelShift = QLabel(Form)
        self.labelShift.setObjectName(u"labelShift")
        sizePolicy.setHeightForWidth(self.labelShift.sizePolicy().hasHeightForWidth())
        self.labelShift.setSizePolicy(sizePolicy)
        self.labelShift.setMinimumSize(QSize(60, 60))
        self.labelShift.setMaximumSize(QSize(60, 60))
        self.labelShift.setStyleSheet(u"QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 2px solid #1E90FF; \n"
"}\n"
"")
        self.labelShift.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labelShift, 3, 1, 1, 4)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_22, 4, 5, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_23, 2, 5, 1, 1)

        self.labelPlus1 = QLabel(Form)
        self.labelPlus1.setObjectName(u"labelPlus1")
        sizePolicy.setHeightForWidth(self.labelPlus1.sizePolicy().hasHeightForWidth())
        self.labelPlus1.setSizePolicy(sizePolicy)
        self.labelPlus1.setMinimumSize(QSize(60, 60))
        self.labelPlus1.setMaximumSize(QSize(60, 60))
        self.labelPlus1.setStyleSheet(u"QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 2px solid #1E90FF; \n"
"}\n"
"")
        self.labelPlus1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labelPlus1, 0, 1, 1, 4)

        self.labelPlus3 = QLabel(Form)
        self.labelPlus3.setObjectName(u"labelPlus3")
        sizePolicy.setHeightForWidth(self.labelPlus3.sizePolicy().hasHeightForWidth())
        self.labelPlus3.setSizePolicy(sizePolicy)
        self.labelPlus3.setMinimumSize(QSize(60, 60))
        self.labelPlus3.setMaximumSize(QSize(60, 60))
        self.labelPlus3.setStyleSheet(u"QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 2px solid #1E90FF; \n"
"}\n"
"")
        self.labelPlus3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labelPlus3, 2, 1, 1, 4)

        self.labelPlus4 = QLabel(Form)
        self.labelPlus4.setObjectName(u"labelPlus4")
        sizePolicy.setHeightForWidth(self.labelPlus4.sizePolicy().hasHeightForWidth())
        self.labelPlus4.setSizePolicy(sizePolicy)
        self.labelPlus4.setMinimumSize(QSize(60, 60))
        self.labelPlus4.setMaximumSize(QSize(60, 60))
        self.labelPlus4.setStyleSheet(u"QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 2px solid #1E90FF; \n"
"}\n"
"")
        self.labelPlus4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labelPlus4, 4, 1, 1, 4)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_24, 0, 5, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_25, 1, 5, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.textEdit, 1, 6, 4, 1)


        self.mainMidLayout.addLayout(self.gridLayout_5)


        self.verticalLayout_10.addLayout(self.mainMidLayout)

        self.registerLayoutBottom = QHBoxLayout()
        self.registerLayoutBottom.setObjectName(u"registerLayoutBottom")
        self.groupH1 = QGroupBox(Form)
        self.groupH1.setObjectName(u"groupH1")
        sizePolicy.setHeightForWidth(self.groupH1.sizePolicy().hasHeightForWidth())
        self.groupH1.setSizePolicy(sizePolicy)
        self.groupH1.setMinimumSize(QSize(90, 68))
        self.groupH1.setMaximumSize(QSize(90, 68))
        self.verticalLayoutH1 = QVBoxLayout(self.groupH1)
        self.verticalLayoutH1.setObjectName(u"verticalLayoutH1")
        self.labelValueH1 = QLabel(self.groupH1)
        self.labelValueH1.setObjectName(u"labelValueH1")

        self.verticalLayoutH1.addWidget(self.labelValueH1)


        self.registerLayoutBottom.addWidget(self.groupH1)

        self.groupH2 = QGroupBox(Form)
        self.groupH2.setObjectName(u"groupH2")
        sizePolicy.setHeightForWidth(self.groupH2.sizePolicy().hasHeightForWidth())
        self.groupH2.setSizePolicy(sizePolicy)
        self.groupH2.setMinimumSize(QSize(90, 68))
        self.groupH2.setMaximumSize(QSize(90, 68))
        self.verticalLayoutH2 = QVBoxLayout(self.groupH2)
        self.verticalLayoutH2.setObjectName(u"verticalLayoutH2")
        self.labelValueH2 = QLabel(self.groupH2)
        self.labelValueH2.setObjectName(u"labelValueH2")

        self.verticalLayoutH2.addWidget(self.labelValueH2)


        self.registerLayoutBottom.addWidget(self.groupH2)

        self.groupH3 = QGroupBox(Form)
        self.groupH3.setObjectName(u"groupH3")
        sizePolicy.setHeightForWidth(self.groupH3.sizePolicy().hasHeightForWidth())
        self.groupH3.setSizePolicy(sizePolicy)
        self.groupH3.setMinimumSize(QSize(90, 68))
        self.groupH3.setMaximumSize(QSize(90, 68))
        self.verticalLayoutH3 = QVBoxLayout(self.groupH3)
        self.verticalLayoutH3.setObjectName(u"verticalLayoutH3")
        self.labelValueH3 = QLabel(self.groupH3)
        self.labelValueH3.setObjectName(u"labelValueH3")

        self.verticalLayoutH3.addWidget(self.labelValueH3)


        self.registerLayoutBottom.addWidget(self.groupH3)

        self.groupH4 = QGroupBox(Form)
        self.groupH4.setObjectName(u"groupH4")
        sizePolicy.setHeightForWidth(self.groupH4.sizePolicy().hasHeightForWidth())
        self.groupH4.setSizePolicy(sizePolicy)
        self.groupH4.setMinimumSize(QSize(90, 68))
        self.groupH4.setMaximumSize(QSize(90, 68))
        self.verticalLayoutH4 = QVBoxLayout(self.groupH4)
        self.verticalLayoutH4.setObjectName(u"verticalLayoutH4")
        self.labelValueH4 = QLabel(self.groupH4)
        self.labelValueH4.setObjectName(u"labelValueH4")

        self.verticalLayoutH4.addWidget(self.labelValueH4)


        self.registerLayoutBottom.addWidget(self.groupH4)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.registerLayoutBottom.addItem(self.horizontalSpacer_26)

        self.btnState = QPushButton(Form)
        self.btnState.setObjectName(u"btnState")
        self.btnState.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btnState.sizePolicy().hasHeightForWidth())
        self.btnState.setSizePolicy(sizePolicy)
        self.btnState.setMinimumSize(QSize(60, 40))
        self.btnState.setMaximumSize(QSize(60, 40))
        self.btnState.setStyleSheet(u"border: 3px solid green;\n"
"border-radius: 5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/iconsDark/plus-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnState.setIcon(icon6)
        self.btnState.setIconSize(QSize(35, 35))

        self.registerLayoutBottom.addWidget(self.btnState)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.registerLayoutBottom.addItem(self.horizontalSpacer_27)

        self.groupB_new = QGroupBox(Form)
        self.groupB_new.setObjectName(u"groupB_new")
        sizePolicy.setHeightForWidth(self.groupB_new.sizePolicy().hasHeightForWidth())
        self.groupB_new.setSizePolicy(sizePolicy)
        self.groupB_new.setMinimumSize(QSize(90, 68))
        self.groupB_new.setMaximumSize(QSize(90, 68))
        self.verticalLayoutB_new = QVBoxLayout(self.groupB_new)
        self.verticalLayoutB_new.setObjectName(u"verticalLayoutB_new")
        self.labelValueB_new = QLabel(self.groupB_new)
        self.labelValueB_new.setObjectName(u"labelValueB_new")

        self.verticalLayoutB_new.addWidget(self.labelValueB_new)


        self.registerLayoutBottom.addWidget(self.groupB_new)

        self.groupC_new = QGroupBox(Form)
        self.groupC_new.setObjectName(u"groupC_new")
        sizePolicy.setHeightForWidth(self.groupC_new.sizePolicy().hasHeightForWidth())
        self.groupC_new.setSizePolicy(sizePolicy)
        self.groupC_new.setMinimumSize(QSize(90, 68))
        self.groupC_new.setMaximumSize(QSize(90, 68))
        self.verticalLayoutC_new = QVBoxLayout(self.groupC_new)
        self.verticalLayoutC_new.setObjectName(u"verticalLayoutC_new")
        self.labelValueC_new = QLabel(self.groupC_new)
        self.labelValueC_new.setObjectName(u"labelValueC_new")

        self.verticalLayoutC_new.addWidget(self.labelValueC_new)


        self.registerLayoutBottom.addWidget(self.groupC_new)

        self.groupD_new = QGroupBox(Form)
        self.groupD_new.setObjectName(u"groupD_new")
        sizePolicy.setHeightForWidth(self.groupD_new.sizePolicy().hasHeightForWidth())
        self.groupD_new.setSizePolicy(sizePolicy)
        self.groupD_new.setMinimumSize(QSize(90, 68))
        self.groupD_new.setMaximumSize(QSize(90, 68))
        self.verticalLayoutD_new = QVBoxLayout(self.groupD_new)
        self.verticalLayoutD_new.setObjectName(u"verticalLayoutD_new")
        self.labelValueD_new = QLabel(self.groupD_new)
        self.labelValueD_new.setObjectName(u"labelValueD_new")

        self.verticalLayoutD_new.addWidget(self.labelValueD_new)


        self.registerLayoutBottom.addWidget(self.groupD_new)

        self.groupA_new = QGroupBox(Form)
        self.groupA_new.setObjectName(u"groupA_new")
        sizePolicy.setHeightForWidth(self.groupA_new.sizePolicy().hasHeightForWidth())
        self.groupA_new.setSizePolicy(sizePolicy)
        self.groupA_new.setMinimumSize(QSize(90, 68))
        self.groupA_new.setMaximumSize(QSize(90, 68))
        self.verticalLayoutA_new = QVBoxLayout(self.groupA_new)
        self.verticalLayoutA_new.setObjectName(u"verticalLayoutA_new")
        self.labelValueA_new = QLabel(self.groupA_new)
        self.labelValueA_new.setObjectName(u"labelValueA_new")

        self.verticalLayoutA_new.addWidget(self.labelValueA_new)


        self.registerLayoutBottom.addWidget(self.groupA_new)


        self.verticalLayout_10.addLayout(self.registerLayoutBottom)

        self.hashLayout = QHBoxLayout()
        self.hashLayout.setObjectName(u"hashLayout")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.hashLayout.addWidget(self.label_7)

        self.hash_hex = QLineEdit(Form)
        self.hash_hex.setObjectName(u"hash_hex")
        self.hash_hex.setReadOnly(True)

        self.hashLayout.addWidget(self.hash_hex)

        self.finish = QPushButton(Form)
        self.finish.setObjectName(u"finish")
        self.finish.setIcon(icon5)

        self.hashLayout.addWidget(self.finish)


        self.verticalLayout_10.addLayout(self.hashLayout)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.btnDetailStep = QPushButton(Form)
        self.btnDetailStep.setObjectName(u"btnDetailStep")
        self.btnDetailStep.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/iconsDark/activity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetailStep.setIcon(icon7)

        self.navLayout.addWidget(self.btnDetailStep)

        self.btnPreviousStep = QPushButton(Form)
        self.btnPreviousStep.setObjectName(u"btnPreviousStep")
        self.btnPreviousStep.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u":/icons/iconsDark/chevrons-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreviousStep.setIcon(icon8)

        self.navLayout.addWidget(self.btnPreviousStep)

        self.btnNextStep = QPushButton(Form)
        self.btnNextStep.setObjectName(u"btnNextStep")
        self.btnNextStep.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/iconsDark/chevrons-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNextStep.setIcon(icon9)

        self.navLayout.addWidget(self.btnNextStep)

        self.btnPreviousRound = QPushButton(Form)
        self.btnPreviousRound.setObjectName(u"btnPreviousRound")
        self.btnPreviousRound.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u":/icons/iconsDark/rewind.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreviousRound.setIcon(icon10)

        self.navLayout.addWidget(self.btnPreviousRound)

        self.btnNextRound = QPushButton(Form)
        self.btnNextRound.setObjectName(u"btnNextRound")
        self.btnNextRound.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u":/icons/iconsDark/fast-forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNextRound.setIcon(icon11)

        self.navLayout.addWidget(self.btnNextRound)

        self.btnPreviousBlock = QPushButton(Form)
        self.btnPreviousBlock.setObjectName(u"btnPreviousBlock")
        self.btnPreviousBlock.setEnabled(False)
        self.btnPreviousBlock.setIcon(icon10)

        self.navLayout.addWidget(self.btnPreviousBlock)

        self.btnNextBlock = QPushButton(Form)
        self.btnNextBlock.setObjectName(u"btnNextBlock")
        self.btnNextBlock.setEnabled(False)
        self.btnNextBlock.setIcon(icon11)

        self.navLayout.addWidget(self.btnNextBlock)


        self.verticalLayout_10.addLayout(self.navLayout)


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
        self.Clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Form", u"PlainText after\n"
" add padding:", None))
        self.start.setText(QCoreApplication.translate("Form", u"Start round", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Current block", None))
        self.labelRound.setText(QCoreApplication.translate("Form", u"Round:", None))
        self.labelStep.setText(QCoreApplication.translate("Form", u"Step:", None))
        self.groupA.setTitle(QCoreApplication.translate("Form", u"A", None))
        self.labelValueA.setText("")
        self.groupB.setTitle(QCoreApplication.translate("Form", u"B", None))
        self.labelValueB.setText("")
        self.groupC.setTitle(QCoreApplication.translate("Form", u"C", None))
        self.labelValueC.setText("")
        self.groupD.setTitle(QCoreApplication.translate("Form", u"D", None))
        self.labelValueD.setText("")
        self.groupF.setTitle(QCoreApplication.translate("Form", u"F", None))
        self.labelValueF.setText("")
        self.labelPlus2.setText(QCoreApplication.translate("Form", u"[ + ]", None))
        self.groupAC.setTitle(QCoreApplication.translate("Form", u"Addition constant (AC)", None))
        self.labelAC.setText("")
        self.groupSC.setTitle(QCoreApplication.translate("Form", u"Shift constant (SC)", None))
        self.labelSC.setText("")
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
        self.labelShift.setText(QCoreApplication.translate("Form", u"[ <<< ]", None))
        self.labelPlus1.setText(QCoreApplication.translate("Form", u"[ + ]", None))
        self.labelPlus3.setText(QCoreApplication.translate("Form", u"[ + ]", None))
        self.labelPlus4.setText(QCoreApplication.translate("Form", u"[ + ]", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">STEP</span><span style=\" font-size:14pt;\">: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">input</span><span style=\" font-size:14pt;\">:  (A B C D)</span></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">(B C D) --(</span><span style=\" font-size:14pt; font-style:italic;\">f_function)</span><span style=\" font-size:14pt;\">--&gt; F \u2295 A  --&gt; \u2295 BLOCK[k], (k=0...15) --&gt; \u2295 C[i] --&gt; shift left --&gt; \u2295 B -&gt; B1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">C1 := B; D1 := C; A1 := D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">(\u2295: add with module 2</span><span style=\" font-size:14pt; vertical-align:super;\">32</span><span style=\" font-size:14pt;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-si"
                        "ze:14pt; font-weight:700; text-decoration: underline;\">output</span><span style=\" font-size:14pt;\">: (A1 B1 C1 D1)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.groupH1.setTitle(QCoreApplication.translate("Form", u"H1", None))
        self.labelValueH1.setText("")
        self.groupH2.setTitle(QCoreApplication.translate("Form", u"H2", None))
        self.labelValueH2.setText("")
        self.groupH3.setTitle(QCoreApplication.translate("Form", u"H3", None))
        self.labelValueH3.setText("")
        self.groupH4.setTitle(QCoreApplication.translate("Form", u"H4", None))
        self.labelValueH4.setText("")
        self.btnState.setText("")
        self.groupB_new.setTitle(QCoreApplication.translate("Form", u"B", None))
        self.labelValueB_new.setText("")
        self.groupC_new.setTitle(QCoreApplication.translate("Form", u"C", None))
        self.labelValueC_new.setText("")
        self.groupD_new.setTitle(QCoreApplication.translate("Form", u"D", None))
        self.labelValueD_new.setText("")
        self.groupA_new.setTitle(QCoreApplication.translate("Form", u"A", None))
        self.labelValueA_new.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Hash value (hex):", None))
        self.finish.setText(QCoreApplication.translate("Form", u"finish process", None))
        self.btnDetailStep.setText(QCoreApplication.translate("Form", u"Detail step", None))
        self.btnPreviousStep.setText(QCoreApplication.translate("Form", u"Previous Step", None))
        self.btnNextStep.setText(QCoreApplication.translate("Form", u"Next Step", None))
        self.btnPreviousRound.setText(QCoreApplication.translate("Form", u"Previous Round", None))
        self.btnNextRound.setText(QCoreApplication.translate("Form", u"Next Round", None))
        self.btnPreviousBlock.setText(QCoreApplication.translate("Form", u"Previous Block", None))
        self.btnNextBlock.setText(QCoreApplication.translate("Form", u"Next Block", None))
    # retranslateUi

