# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1167, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1167, 750))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setMinimumSize(QtCore.QSize(160, 80))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.input_text = QtWidgets.QPlainTextEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy)
        self.input_text.setObjectName("input_text")
        self.gridLayout.addWidget(self.input_text, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridFrame)
        self.groupButtom = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupButtom.sizePolicy().hasHeightForWidth())
        self.groupButtom.setSizePolicy(sizePolicy)
        self.groupButtom.setObjectName("groupButtom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupButtom)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputTxt = QtWidgets.QLineEdit(self.groupButtom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTxt.sizePolicy().hasHeightForWidth())
        self.inputTxt.setSizePolicy(sizePolicy)
        self.inputTxt.setObjectName("inputTxt")
        self.horizontalLayout.addWidget(self.inputTxt)
        self.numberInput = QtWidgets.QLineEdit(self.groupButtom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberInput.sizePolicy().hasHeightForWidth())
        self.numberInput.setSizePolicy(sizePolicy)
        self.numberInput.setObjectName("numberInput")
        self.horizontalLayout.addWidget(self.numberInput)
        self.crawlersBtn = QtWidgets.QPushButton(self.groupButtom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crawlersBtn.sizePolicy().hasHeightForWidth())
        self.crawlersBtn.setSizePolicy(sizePolicy)
        self.crawlersBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.crawlersBtn.setObjectName("crawlersBtn")
        self.horizontalLayout.addWidget(self.crawlersBtn)
        self.verticalLayout.addWidget(self.groupButtom)
        self.verticalWidget = QtWidgets.QWidget(self.frame)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.proGressDisplay = QtWidgets.QTextEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proGressDisplay.sizePolicy().hasHeightForWidth())
        self.proGressDisplay.setSizePolicy(sizePolicy)
        self.proGressDisplay.setObjectName("proGressDisplay")
        self.verticalLayout_2.addWidget(self.proGressDisplay)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOPen = QtWidgets.QAction(MainWindow)
        self.actionOPen.setObjectName("actionOPen")

        self.retranslateUi(MainWindow)
        self.crawlersBtn.clicked.connect(self.onClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputTxt, self.crawlersBtn)
        MainWindow.setTabOrder(self.crawlersBtn, self.input_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "豆瓣助手"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>*{</p><p>background:red</p><p>}</p></body></html>"))
        self.input_text.setPlainText(_translate("MainWindow", "可爬取的内容************************\n"
"文学 · · · · · ·\n"
"小说(5954853)    外国文学(2260203)    文学(2012837)    随笔(1273858)\n"
"中国文学(1271577)    经典(1264828)    日本文学(989651)    散文(766379)\n"
"村上春树(475552)    诗歌(374004)    童话(336694)    儿童文学(290461)\n"
"名著(289569)    古典文学(278123)    王小波(252523)    余华(250469)\n"
"杂文(236254)    张爱玲(206440)    当代文学(194563)    外国名著(128519)\n"
"钱钟书(124692)    鲁迅(108613)    诗词(93890)    茨威格(71577)\n"
"米兰·昆德拉(58673)    杜拉斯(46107)    港台(8708)\n"
"流行 · · · · · ·\n"
"漫画(1384534)    推理(1082943)    绘本(989003)    青春(726258)\n"
"东野圭吾(686623)    科幻(625654)    悬疑(624559)    言情(555093)\n"
"奇幻(370119)    武侠(345324)    推理小说(342683)    日本漫画(321082)\n"
"耽美(284006)    韩寒(267829)    网络小说(241143)    亦舒(240312)\n"
"三毛(232095)    科幻小说(208047)    阿加莎·克里斯蒂(182915)    安妮宝贝(176110)\n"
"金庸(172382)    穿越(161846)    郭敬明(156436)    轻小说(150290)\n"
"魔幻(139432)    青春文学(134597)    几米(119032)    J.K.罗琳(102921)\n"
"幾米(102625)    张小娴(98278)    古龙(79839)    高木直子(75738)\n"
"校园(70724)    沧月(67336)    余秋雨(59045)    落落(58541)\n"
"文化 · · · · · ·\n"
"历史(2433161)    心理学(1582476)    哲学(1352939)    传记(876224)\n"
"社会学(873696)    文化(830803)    艺术(597804)    社会(515872)\n"
"设计(443996)    政治(435284)    建筑(294870)    宗教(293480)\n"
"电影(277278)    政治学(272408)    数学(257041)    中国历史(223432)\n"
"回忆录(204118)    思想(184608)    国学(166671)    人物传记(151514)\n"
"艺术史(143905)    人文(142435)    音乐(135659)    绘画(128963)\n"
"戏剧(122644)    西方哲学(97073)    二战(89072)    近代史(88097)\n"
"军事(84524)    佛教(83116)    考古(59803)    自由主义(50974)\n"
"美术(45466)\n"
"生活 · · · · · ·\n"
"爱情(1079523)    成长(707586)    生活(633091)    旅行(603415)\n"
"心理(500253)    励志(447949)    女性(414751)    摄影(323295)\n"
"教育(262923)    职场(234621)    美食(214769)    游记(168569)\n"
"灵修(134194)    健康(98126)    情感(96696)    人际关系(55183)\n"
"两性(52967)    手工(42498)    养生(40282)    家居(27433)\n"
"自助游(2740)\n"
"经管 · · · · · ·\n"
"经济学(493283)    管理(475904)    经济(403011)    商业(366519)\n"
"金融(320082)    投资(267993)    营销(176825)    理财(135587)\n"
"创业(128081)    股票(74422)    广告(73484)    企业史(25425)\n"
"策划(9547)\n"
"科技 · · · · · ·\n"
"科普(704504)    互联网(267070)    编程(176327)    科学(163917)\n"
"交互设计(73883)    用户体验(60129)    算法(59048)    科技(33396)\n"
"web(22431)    交互(5579)    通信(5420)    UE(5375)\n"
"UCD(3598)    神经网络(3429)    程序(1335)"))
        self.inputTxt.setPlaceholderText(_translate("MainWindow", "输入要爬取内容"))
        self.numberInput.setPlaceholderText(_translate("MainWindow", "输入要爬取的数目"))
        self.crawlersBtn.setText(_translate("MainWindow", "爬取"))
        self.proGressDisplay.setPlaceholderText(_translate("MainWindow", "进度框："))
        self.actionOPen.setText(_translate("MainWindow", "OPen"))
