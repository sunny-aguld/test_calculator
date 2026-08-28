from GUI.main_window import calculate_multiply

class FakeEntry:
    def __init__(self, value=""):
        self.value = value

    def get(self):
        return self.value

    def delete(self, start, end):
        self.value = ""

    def insert(self, index, value):
        self.value = value

def test_calculate_multiply():
    entry_input1 = FakeEntry("3")
    entry_input2 = FakeEntry("4")
    entry_result = FakeEntry()

    calculate_multiply(entry_input1, entry_input2, entry_result)

    assert entry_result.get() == "12.0"
