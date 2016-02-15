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
    Ui::core *ui;
};

#endif // CORE_H
