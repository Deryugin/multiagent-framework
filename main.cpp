#include "core.h"
#include <QApplication>
#include <QThread>
#include <QThread>
#include <QTime>
#include <QTimer>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    core w;

    w.show();

    return a.exec();
}
