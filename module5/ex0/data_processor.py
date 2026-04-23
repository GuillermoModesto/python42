from typing import Any, Union, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.ingested = []
        self.count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.ingested) != 0:
            return self.ingested.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if not isinstance(data, list):
            return False
        for i in data:
            if isinstance(i, (int, float)):
                continue
            else:
                return False
        return True

    def ingest(
            self,
            data: Union[int, float, list[int], list[float]]
            ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data.")
        if isinstance(data, list):
            for i in data:
                self.ingested.append(tuple((self.count, str(i))))
                self.count += 1
        else:
            self.ingested.append(tuple((self.count, str(data))))
            self.count += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if not isinstance(data, list):
            return False
        for i in data:
            if isinstance(i, str):
                continue
            else:
                return False
        return True

    def ingest(
            self,
            data: Union[str, list[str]]
            ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data.")
        if isinstance(data, list):
            for i in data:
                self.ingested.append(tuple((self.count, i)))
                self.count += 1
        else:
            self.ingested.append(tuple((self.count, str(data))))
            self.count += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        for i in data:
            if not isinstance(i, dict):
                return False
            if not all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in i.items()
            ):
                return False
        return True

    def ingest(
            self,
            data: Union[dict[str, str], list[dict[str, str]]]
            ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data.")
        if isinstance(data, list):
            for i in data:
                self.ingested.append(tuple((self.count, i)))
                self.count += 1
        else:
            self.ingested.append(tuple((self.count, str(data))))
            self.count += 1


def main():
    print("=== Code Nexus - Data Processor ===\n")
    numbers = NumericProcessor()
    print("Testing Numeric Processor...")
    print(
        f"Trying to validate input '42': {numbers.validate(42)}"
    )
    print(
        f"Trying to validate input 'Hello': {numbers.validate('Hello')}"
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numbers.ingest('foo')
    except Exception as e:
        print(e)
    print("Processing data: [1, 2, 3, 4, 5]")
    numbers.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        pair = numbers.output()
        print(f"Numeric value {pair[0]}: {pair[1]}")

    print()
    text = TextProcessor()
    print("Testing Text Processor...")
    print(
        f"Trying to validate input '42': {text.validate(42)}"
    )
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    pair = text.output()
    print(f"Text value {pair[0]}: {pair[1]}")

    print()
    log = LogProcessor()
    print("Testing Log Processor...")
    print(
        f"Trying to validate input 'Hello': {log.validate('Hello')}"
    )
    print(
        "Processing data: "
        "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
        "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
        )
    log.ingest(
        [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
            )
    print("Extracting 2 value...")
    for i in range(2):
        pair = log.output()
        print(f"Log entry {pair[0]}: "
              f"{pair[1]['log_level']}: {pair[1]['log_message']}")


if __name__ == "__main__":
    main()
