import os
from udemypy.database import settings
from datetime import datetime


def get_path(script_name: str) -> str:
    database_dir = os.path.dirname(__file__)
    scripts_dir = os.path.join(database_dir, "scripts")
    return os.path.join(scripts_dir, script_name)


def _set_variables_value(sql_script: str, variables: dict) -> str:
    """
    Replace variables name with their respective value
    in the given sql script.
    """
    if not variables:
        return sql_script

    for variable, value in variables.items():
        # String variable:
        if isinstance(value, str):
            sql_script = sql_script.replace(variable, f"'{value}'")
        elif isinstance(value, datetime):
            value_str = value.strftime("%Y-%m-%d %H:%M:%S")
            sql_script = sql_script.replace(variable, f"'{value_str}'")
        elif value is None:
            sql_script = sql_script.replace(variable, "NULL")
        else:
            sql_script = sql_script.replace(variable, str(value))

    return sql_script


def read_script(filename: str, variables: dict = None) -> list[str]:
    with open(filename, "r") as fd:
        sql_script = fd.read()
    # Replace variables with their values
    sql_script = _set_variables_value(sql_script, variables)

    return sql_script.split(";")


def modifies_database_state(sql_command: str) -> bool:
    """
    Returns True if the given sql command modifies the current
    database state. Else returns False
    """
    return any(cmd in sql_command for cmd in settings.UPDATE_DATABASE_COMMANDS)
