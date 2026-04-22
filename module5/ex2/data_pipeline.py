from typing import Any, Union, List, Protocol
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
            return tuple((self.count, self.ingested.pop(0)))
        return None


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
                self.ingested.append(str(i))
                self.count += 1
        else:
            self.ingested.append(str(data))
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
                self.ingested.append(i)
                self.count += 1
        else:
            self.ingested.append(str(data))
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
                self.ingested.append(i)
                self.count += 1
        else:
            self.ingested.append(data)
            self.count += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream():
    def __init__(self):
        print("Initialize Data Stream...\n")
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for ele in stream:
            valid = False
            for proc in self.processors:
                if (proc.validate(ele)):
                    proc.ingest(ele)
                    valid = True
                    break
            if (not valid):
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{ele}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print('No processor found, no data')
            return
        for proc in self.processors:
            print(f"{proc.__class__.__name__}:"
                  f" total {proc.count} items processed,"
                  f" remaining: {len(proc.ingested)} on procesor"
                  )
            
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            i = 0
            while i < nb:
                plugin.process_output([proc.output()])
                i += 1


class CSVPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(data)


class JSONPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        print(data)


def main():
    print("=== Code Nexus - Data Pipeline ==\n")
    dataStream = DataStream()
    dataStream.print_processors_stats()
    print("Registering Processors")
    dataStream.register_processor(NumericProcessor())
    dataStream.register_processor(TextProcessor())
    dataStream.register_processor(LogProcessor())
    print(
        "Send first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], "
        "[{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil isconnected'}], "
        "42, ['Hi', 'five']]"
        )
    dataStream.process_stream([
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
         'log_message': 'User wil isconnected'}
         ],
        42, ['Hi', 'five']
    ])
    print()
    dataStream.print_processors_stats()

    dataStream.output_pipeline(3, CSVPlugin())

if __name__ == "__main__":
    main()
