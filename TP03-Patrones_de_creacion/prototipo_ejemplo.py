import copy

class UserPreferences:
    def __init__(self, language, theme, notifications_enabled):
        self.language = language
        self.theme = theme
        self.notifications_enabled = notifications_enabled

    def __str__(self):
        return f"Language: {self.language}, Theme: {self.theme}, Notifications: {self.notifications_enabled}"

    def __copy__(self):
        return type(self)(
            self.language,
            self.theme,
            self.notifications_enabled
        )

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        return type(self)(
            copy.deepcopy(self.language, memo),
            copy.deepcopy(self.theme, memo),
            copy.deepcopy(self.notifications_enabled, memo)
        )


if __name__ == "__main__":
    # Configuración base para nuevos usuarios
    base_preferences = UserPreferences("es", "dark", True)
    print("Preferencias base:", base_preferences)

    # Clonar para un nuevo usuario y personalizar
    user1_preferences = copy.deepcopy(base_preferences)
    user1_preferences.language = "en"
    user1_preferences.theme = "light"
    print("Usuario 1:", user1_preferences)

    # Clonar para otro usuario y personalizar
    user2_preferences = copy.deepcopy(base_preferences)
    user2_preferences.notifications_enabled = False
    print("Usuario 2:", user2_preferences)

    # Verifica que los cambios no afectan a la base
    print("Preferencias base después de clonar:", base_preferences)

    # Verifica que ambos objetos son diferentes
    print("¿Son diferentes los objetos configuracion de usuario?", user1_preferences is not user2_preferences)