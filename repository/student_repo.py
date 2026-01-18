from domain.student import Student


class StudentRepository:
    """Repository en mémoire (dict id -> Student)."""

    def __init__(self):
        self._data: dict[int, Student] = {}

    def add(self, student: Student) -> None:
        # TODO (à faire):
        # - Vérifier type Student
        if not isinstance(student, Student):
            raise TypeError(
                f"Attendu : instance de Student, reçu : {type(student).__name__}")
        # - Refuser doublon d'id (si student.id déjà dans _data)
        for s in self._data:
            if s == student.id:
                return
        # - Stocker: self._data[student.id] = student
        self._data[student.id] = student

    def get_by_id(self, student_id: int) -> Student | None:
        # TODO:
        # - Retourner self._data.get(int(student_id))
        return self._data.get(int(student_id))

    def list_all(self) -> list[Student]:
        # TODO:
        # - Retourner list(self._data.values())
        return list(self._data.values())
