#-------------------------------------------------
#
# Project created by QtCreator 2016-02-15T15:29:06
#
#-------------------------------------------------

QMAKE_CXXFLAGS += -std=gnu++11
QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = multiagent-visual
TEMPLATE = app


SOURCES += main.cpp\
        core.cpp

HEADERS  += core.h

FORMS    += core.ui
