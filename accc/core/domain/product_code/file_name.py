from dataclasses import dataclass


@dataclass
class FileName:
    value: str

    def __post_init__(self):
        if len(self.value.split()) == 0:
            raise ValueError("Empty string is not supported.")

        if self.value.endswith(".py"):
            self.value = self.value[:-3]

    def __str__(self):
        return self.value
