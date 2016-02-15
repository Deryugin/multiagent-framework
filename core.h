#ifndef CORE_H
#define CORE_H

#include <QMainWindow>

namespace Ui {
class core;
}

class core : public QMainWindow
{
    Q_OBJECT

public:
    explicit core(QWidget *parent = 0);
    ~core();

private:
    int data[10][10];
    Ui::core *ui;
    void redrawData(void);
};

#endif // CORE_H
