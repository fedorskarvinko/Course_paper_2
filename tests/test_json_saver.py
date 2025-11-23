def test_add_delete(saver):
    vac = {"id": "1", "name": "Test"}
    saver.add_vacancy(vac)
    assert vac in saver.get_vacancies()
    saver.delete_vacancy(vac)
    assert vac not in saver.get_vacancies()


def test_no_dup(saver):
    vac = {"id": "1"}
    saver.add_vacancy(vac)
    saver.add_vacancy(vac)
    assert len(saver.get_vacancies()) == 1


def test_criteria(saver):
    saver.add_vacancy({"id": "1", "name": "A"})
    saver.add_vacancy({"id": "2", "name": "B"})
    assert len(saver.get_vacancies({"name": "A"})) == 1