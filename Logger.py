class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize the logger here (e.g., configure logging settings)
            cls._instance.log_file = "web_app_log.txt"
        return cls._instance

    def log_message(self, message):
        with open(self.log_file, "a") as log_file:
            log_file.write(message + "\n")

if __name__ == "__main__":
    logger_instance1 = Logger()
    logger_instance2 = Logger()

    print("Are both instances the same object?", logger_instance1 is logger_instance2)

    # Log messages using the singleton logger
    logger_instance1.log_message("Log message 1 from instance 1")
    logger_instance2.log_message("Log message 2 from instance 2")