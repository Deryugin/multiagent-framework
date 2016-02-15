#include "core.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    core w;
    w.show();

    return a.exec();
}
