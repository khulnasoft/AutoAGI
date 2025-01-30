from backend.util.settings import AppEnvironment, BehaveAs, Settings

settings = Settings()


def configure_logging():
    import logging

    import autoagi_libs.logging.config

    if (
        settings.config.behave_as == BehaveAs.LOCAL
        or settings.config.app_env == AppEnvironment.LOCAL
    ):
        autoagi_libs.logging.config.configure_logging(force_cloud_logging=False)
    else:
        autoagi_libs.logging.config.configure_logging(force_cloud_logging=True)

    # Silence httpx logger
    logging.getLogger("httpx").setLevel(logging.WARNING)
