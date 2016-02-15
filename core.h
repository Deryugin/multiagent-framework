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
    void updateData(int x, int y, int val);

private:
    int data[10][10];
    Ui::core *ui;
    void redrawData(void);
    void initData(void);

protected:
    void paintEvent(QPaintEvent *event);
};

#endif // CORE_H
