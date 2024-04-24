# import os
# import logging
# import structlog
# # import dynaconf

# # settings = dynaconf.settings(envvar_prefix="APP")

# # debug = settings.get("DEBUG")
# # host = settings.get("HOST")
# # port = settings.get("PORT")

# # level = os.environ.get("LOG_LEVEL", "INFO").upper()
# # LOG_LEVEL = getattr(logging, level)

# # structlog.configure(
# #     wrapper_class=structlog.make_filtering_bound_logger(LOG_LEVEL))
# # logger = structlog.get_logger()

# logger.debug("Database connection established")
# logger.info("Processing data from the API")
# logger.warning("Resource usage is nearing capacity")
# logger.error("Failed to save the file. Please check permissions")
# logger.critical("System has encountered a critical failure. Shutting down")

def read_env_file(filepath):
    result = []
    with open(filepath, 'r', encoding="UTF-8") as file:
        for line in file:
            # Removing leading and trailing whitespaces
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Finding the position of the first '='
            equal_index = line.find('=')
            if equal_index != -1:
                key = line[:equal_index].strip()
                value = line[equal_index+1:].split('#', 1)[0].strip()
                result.append({'name':key, 'value': value})
    return result

def read_file_content(filepath):
    with open(filepath, 'r', encoding="UTF-8") as file:
        return file.read()
