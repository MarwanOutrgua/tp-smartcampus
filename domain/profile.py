class Profile:
    """Profil d’un étudiant (association 1–1 avec Student)."""

    def __init__(self, bio: str, email: str, phone: str):
        # TODO (commenté):
        # - Affecter via les propriétés pour déclencher les validations des setters
        self.bio = bio
        self.email = email
        self.phone = phone

    @property
    def bio(self) -> str:
        # TODO (commenté): retourner _bio
        return self._bio

    @bio.setter
    def bio(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        if v == "":
            raise Exception("bio obligatoire.")
        self._bio = v

    @property
    def email(self) -> str:
        # TODO : retourner _email
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        # TODO :
        v = str(value).strip()
        # - vérifier non vide et contient '@'
        if v and "@" in v:
            self._email = v
        else:
            raise Exception("L'email est invalide ou vide.")

    @property
    def phone(self) -> str:
        # TODO: retourner _phone
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        # TODO:
        # - vérifier non vide
        v = str(value).strip()
        if v != "":
            self._phone = v
        else:
            raise Exception("Obligatoire de saisi numero telephone")

    def __str__(self) -> str:
        # TODO: représentation lisible
        return f"bio : {self._bio} \n email : {self._email} \n phone : {self._phone} "
