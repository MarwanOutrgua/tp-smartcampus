from domain.profile import Profile


class Student:
    """Étudiant (association 1–1 avec Profile).

    Objectif: encapsuler les données + valider via setters.
    """

    def __init__(self, student_id: int, name: str, profile: Profile):
        # TODO (à faire):
        # 1) Initialiser l'identifiant (entier > 0)
        self.id = student_id
        # 2) Initialiser le nom
        self.name = name
        # 3) Initialiser le profil (doit être une instance de Profile)
        self.profile = profile

    @property
    def id(self) -> int:
        # TODO:
        # - Retourner l'attribut privé _id
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        # TODO:
        # - Convertir value en int: v = int(value)
        v = int(value)
        # - Vérifier v > 0
        if v <= 0:
            raise Exception("id doit être > 0.")
        self._id = v
      

    @property
    def name(self) -> str:
        # TODO :
        # - Retourner _name
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - Vérifier non vide:
        if v == "":
            raise Exception("name obligatoire.")
        self._name = v

    @property
    def profile(self) -> Profile:
        # TODO:
        # - Retourner _profile
        return self._profile

    @profile.setter
    def profile(self, value: Profile) -> None:
        # TODO:
        # - Vérifier que value est une instance de Profile
        if not isinstance(value, Profile):
            raise Exception("profile doit être une instance de Profile.")
        self._profile = value

    def __str__(self) -> str:
        # TODO:
        # - Retourner une représentation lisible
        return f"Student(id={self._id}, name={self._name}, profile={self._profile})"
