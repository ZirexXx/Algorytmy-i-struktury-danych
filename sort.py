class Sort:
    @staticmethod
    def bubble_sort(data: list) -> list:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] < data[j]:
                    data[i], data[j] = data[j], data[i]
        return data

    @staticmethod
    def selection_sort(data: list) -> list:
        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

    @staticmethod
    def insertion_sort(data: list) -> list:
        n: int = len(data)
        for i in range(1, n):
            key = data[i]
            j = i-1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j = j - 1
                data[j + 1] = key
        return data

    #   ODWRÓCONY PORZĄDEK SORTOWANIA

    @staticmethod
    def reversed_bubble_sort(data: list) -> list:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
        return data

    @staticmethod
    def reversed_selection_sort(data: list) -> list:
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] > data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

    @staticmethod
    def reversed_insertion_sort(data: list) -> list:
        n: int = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] < key:
                data[j + 1] = data[j]
                j = j - 1
                data[j + 1] = key
        return data
