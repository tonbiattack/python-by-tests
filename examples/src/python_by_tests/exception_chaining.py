def required_setting(settings: dict[str, str]) -> str:
    try:
        return settings["region"]
    except KeyError as error:
        raise ValueError("region must be configured") from error
