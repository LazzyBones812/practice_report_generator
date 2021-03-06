import requests


def test_1():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 200


def test_2():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {

            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422

def test_3():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_4():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Michael",
            "surname": "Shlunev",
            "patronymic": "Evgenevich",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_5():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "",
            "surname": "",
            "patronymic": "",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_6():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Mark",
                "surname": "Polyak",
                "patronymic": "Dmitrievich",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_7():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "34Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_8():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "34Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_9():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "34Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_10():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Мих23аил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_11():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлу34нев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_12():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евген34ьевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_13():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил34",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_14():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев34",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_15():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич34",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_16():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юл34ия",
                "surname": "34Антохина",
                "patronymic": "Анатольевна34",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_17():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "34",
                "surname": "",
                "patronymic": "M34",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_18():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "МихаилМихаилМихаилМихаилМихаилМихаилМихаилМихаилМихаил",
            "surname": "ШлуневШлуневШлуневШлуневШлуневШлуневШлуневШлунев",
            "patronymic": "ЕвгеньевичЕвгеньевичЕвгеньевичЕвгеньевичЕвгеньевичЕвгеньевичЕвгеньевичЕвгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_19():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "М",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург 2022",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422


def test_20():
    body = {
        "organisation": {
            "founder": "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
            "name": "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»",
            "faculty": "ИНСТИТУТ НЕПРЕРЫВНОГО И ДИСТАНЦИОННОГО ОБРАЗОВАНИЯ",
            "department": "КАФЕДРА информационных технологий и программной инженерии"
        },
        "student": {
            "name": "Михаил",
            "surname": "Шлунев",
            "patronymic": "Евгеньевич",
            "group": "4936"
        },
        "report": {
            "subject_name": "Операционные системы",
            "task_name": "ЛР1. Знакомство с командным интерпретатором bash",
            "task_type": "Лабораторная работа",
            "footer": "Санкт-Петербург",
            "teacher": {
                "name": "Юлия",
                "surname": "Антохина",
                "patronymic": "Анатольевна",
                "status": "Ректор, д.т.н., проф."
            }
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/", json=body)
    assert response.status_code == 422
