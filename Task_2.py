class Logger:

    def __init__(self) -> None:
        self._logs = {}
        self._size = 0
        self._last_timestamp = 0

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self._last_timestamp:
            return False
        if message not in self._logs:
            self._logs[message] = timestamp
            self._size += 1
            if self._size > 100:
                self.clean(timestamp)
            self._last_timestamp = timestamp
            return True
        elif timestamp - self._logs[message] >= 10:
            self._logs[message] = timestamp
            self._last_timestamp = timestamp
            return True

        return False

    def clean(self, timestamp):
        deleted = 0
        for message in self._logs.keys():
            if timestamp - self._logs[message] >= 10:
                del self._logs[message]
                self._size -= 1
                deleted += 1
        return deleted > 0

    def loggerSize(self):
        return self._size


logger = Logger()

# logger.shouldPrintMessage(1, "foo");
# logger.shouldPrintMessage(2, "bar");
while True:
    print("Enter command:")
    print("1. Print message")
    print("2. Clean logger")
    print("3. Get logger size")
    print("4. Exit")
    command = input()
    if command == "1":
        timestamp = int(input("Enter timestamp: "))
        message = input("Enter message: ")
        result = logger.shouldPrintMessage(timestamp, message)
        print(f"Print message: {result}")
    elif command == "2":
        timestamp = int(input("Enter timestamp: "))
        result = logger.clean(timestamp)
        print(f"Clean logger: {result}")
    elif command == "3":
        result = logger.loggerSize()
        print(f"Logger size: {result}")
    elif command == "4":
        break
    else:
        print("Invalid command")