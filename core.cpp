#include "core.h"
#include "ui_core.h"

core::core(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::core)
{
    ui->setupUi(this);
}

core::~core()
{
    delete ui;
}
