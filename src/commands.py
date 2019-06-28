class Command():
    def __init__(self, user):
        self.logged_user = user

    def execute(self):
        pass

class OpenCommand(Command):
    def __init__(self, logged_user, db_access):
        super().__init__(logged_user)
        self.db_access = db_access

    def execute(self):
        self.db_access.add_log("Door opened by user: " + self.logged_user.username, "INFO")
        print("DOOR OPENED")
        return "DOOR OPENED"


class AddUserCommand(Command):
    def __init__(self, logged_user, db_access, command_arguments):
        super().__init__(logged_user)
        self.db_access = db_access
        self.command_arguments = command_arguments

    def execute(self):
        self.db_access.add_user(self.command_arguments[1])
        self.db_access.add_log("Added user: " + str(self.command_arguments[1]) + " by: " + self.logged_user.username)
        print("USER ADDED")
        return "USER ADDED"


class RemoveUserCommand(Command):
    def __init__(self, logged_user, db_access, command_arguments):
        super().__init__(logged_user)
        self.db_access = db_access
        self.command_arguments = command_arguments

    def execute(self):
        self.db_access.remove_user_by_username(self.command_arguments[1])
        self.db_access.add_log("Removed user: " + str(self.command_arguments[1]) + " by: " + self.logged_user.username)
        print("USER REMOVED")
        return "USER REMOVED"


class GetAllLogsCommand(Command):
    def __init__(self, logged_user, db_access, command_arguments):
        super().__init__(logged_user)
        self.db_access = db_access
        self.command_arguments = command_arguments

    def execute(self):
        string_to_send = ""
        logs = self.db_access.get_all_logs()
        print(str(logs))

        if len(logs) == 0:
            string_to_send = "NO LOGS"
        else:
            for log in logs:
                string_to_send += str(log.message) + " " + str(log.level) + " " + str(log.source) + " " + str(
                    log.timestamp) + "\n"

        self.db_access.add_log("All logs get by: " + self.logged_user.username)
        return string_to_send


class PasswordChangeCommand(Command):
    def __init__(self, logged_user, db_access, command_arguments, readConfig, changePassword):
        super().__init__(logged_user)
        self.db_access = db_access
        self.command_arguments = command_arguments
        self.readConfig = readConfig
        self.changePassword = changePassword

    def execute(self):
        if (len(self.command_arguments) < 2):
            print("NOT ENOUGH ARGS")
            return "NOT ENOUGH ARGS"

        if (self.command_arguments[1] != self.readConfig("PASSWORD")):
            print("PASSWORD MISMATCH")
            return "PASSWORD MISMATCH"

        self.changePassword(self.command_arguments[2])
        print("PASSWORD CHANGED")
        return "PASSWORD CHANGED"


class ConfigCommand(Command):
    def __init__(self, logged_user, db_access, command_arguments, changeConfig):
        super().__init__(logged_user)
        self.db_access = db_access
        self.command_arguments = command_arguments
        self.changeConfig = changeConfig

    def execute(self):
        if (len(self.command_arguments) < 2):
            print("NOT ENOUGH ARGS")
            return "NOT ENOUGH ARGS"

        return self.changeConfig(self.command_arguments[1], self.command_arguments[2])


class ShowConfigCommand(Command):
    def __init__(self, showConfig, user):
        super().__init__(user)
        self.showConfig = showConfig

    def execute(self):
        print(self.showConfig())
        return self.showConfig()


def get_command(command_name, *args, **kwargs):
    return {
        "open": OpenCommand(*args, **kwargs),
        "add_user": AddUserCommand(*args, **kwargs),
        "remove_user": RemoveUserCommand(*args, **kwargs),
        "get_all_logs": GetAllLogsCommand(*args, **kwargs),
        "password_change": PasswordChangeCommand(*args, **kwargs),
        "show_config": ShowConfigCommand(*args, **kwargs)
    }[command_name.lower()]