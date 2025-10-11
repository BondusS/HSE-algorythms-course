class HashTable:
    # Конструктор класса
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = 0.75
        self.table = [[] for _ in range(self.capacity)]  # Используем список списков

    # Вычисление хэша в приведённом диапазоне
    def _hash(self, key):
        return hash(key) % self.capacity

    # Увеличение ёмкости таблицы
    def _resize(self):
        self.capacity *= 2
        new_table = [[] for _ in range(self.capacity)]
        # Обновление хэшей для всех элементов
        for bucket in self.table:
            for key, value in bucket:
                index = self._hash(key)
                new_table[index].append((key, value))
        self.table = new_table

    # Вставка элемента
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        # Проверка, не существует ли уже такой ключ
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновление значения
                return
        bucket.append((key, value))
        self.size += 1
        # Проверка необходимости рехеширования
        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()

    # Поиск значения по ключу
    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  # Ключ не найден

    # Удаление элемента по ключу
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False  # Ключ не найден


# Старт программы
if __name__ == "__main__":
    # Примеры использования
    ht = HashTable()
    ht.insert("key1", 10)
    ht.insert("key2", 20)
    print(ht.search("key1"))  # Вывод: 10
    ht.delete("key2")
    print(ht.search("key2"))  # Вывод: None
    print('Done' if ht.delete("key2") else 'Not done')  # Вывод: Not done
