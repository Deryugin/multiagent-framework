#include "core.h"
#include "ui_core.h"
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <QLabel>

core::core(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::core)
{
    ui->setupUi(this);
    ui->gridLayout->setSpacing(0);


    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            data[i][j] = (2 * i * i + 2 * j * j) % 256;
        }
    }

    redrawData();
}

void core::redrawData(void) {
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            QLabel *label = new QLabel;
            std::ostringstream ss;
            ss << data[i][j];
            std::string shade = "(" + ss.str() + ", " + ss.str() + ", " + ss.str() + ")";
            QString shade_arg = QString::fromStdString(shade);
            QString styleSheet = "QLabel { background-color : rgb" + shade_arg + "; color : rgb" + shade_arg + "; }";
            label->setStyleSheet(styleSheet);
            label->setFixedHeight(30);
            label->setFixedWidth(30);
            label->setMargin(-1);
            ui->gridLayout->addWidget(label, i, j);
        }
    }
}

core::~core()
{
    delete ui;
}
