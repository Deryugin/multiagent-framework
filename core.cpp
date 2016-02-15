#include "core.h"
#include "ui_core.h"
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <random>
#include <QLabel>
#include <QTimer>
#include <unistd.h>

FILE *input;

core::core(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::core)
{

    ui->setupUi(this);
    ui->gridLayout->setSpacing(0);

    input = fopen("../multiagent-visual/input", "r");

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            data[i][j] = 0;
        }
    }

    initData();
}

core::~core()
{
    delete ui;
}

void core::initData(void) {
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

void core::redrawData(void) {
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            QLayoutItem *label = ui->gridLayout->itemAt(i * 10 + j);
            std::ostringstream ss;
            ss << data[i][j];
            std::string shade = "(" + ss.str() + ", " + ss.str() + ", " + ss.str() + ")";
            QString shade_arg = QString::fromStdString(shade);
            QString styleSheet = "QLabel { background-color : rgb" + shade_arg + "; color : rgb" + shade_arg + "; }";
            label->widget()->setStyleSheet(styleSheet);
        }
    }
}

void core::updateData(int x, int y, int val) {
    data[x][y] = val;
    QLayoutItem *label = ui->gridLayout->itemAt(x * 10 + y);
    std::ostringstream ss;
    ss << data[x][y];
    std::string shade = "(" + ss.str() + ", " + ss.str() + ", " + ss.str() + ")";
    QString shade_arg = QString::fromStdString(shade);
    QString styleSheet = "QLabel { background-color : rgb" + shade_arg + "; color : rgb" + shade_arg + "; }";
    label->widget()->setStyleSheet(styleSheet);
}

void core::paintEvent(QPaintEvent *)
{
    int val;
    int n;

    fscanf(input, "%d %d", &n, &val);

    int x = n / 10;
    int y = n % 10;

    updateData(x, y, val);

    usleep(1000);
}
