from typing import Any, Union
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
        res = tuple((self.count, self.ingested.pop(0)))
        self.count += 1
        return res


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
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
                self.ingested.append(str(i))
        else:
            self.ingested.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
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
                self.ingested.append(i)
        else:
            self.ingested.append(str(data))


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
                self.ingested.append(i)
        else:
            self.ingested.append(i)


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


if __name__ == "__main__":
    main()
