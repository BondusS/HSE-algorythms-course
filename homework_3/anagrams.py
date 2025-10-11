# Дан список слов. Сгруппируйте слова так, чтобы в одной группе оказались все анаграммы.

def group_anagrams(strs):
    groups = {}
    for word in strs:
        count = [0] * 26  # Массив для подсчёта букв
        for char in word:
            # Определяем индекс буквы в английском алфавите,
            # через разницу кодов в Unicode,
            # +1 в соответствующий счётчик
            count[ord(char) - ord('a')] += 1
        # Используем кортеж счётчиков как ключ
        key = tuple(count)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# Сложность алгоритма O(n*k), n - кол-во слов, k - длина слова

# Старт программы
if __name__ == "__main__":
    # Примеры использования
    words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words1))  # Выведет: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    words2 = ['ban', 'call', 'nab', 'clal', 'lalc', 'llac', 'ccall']
    print(group_anagrams(words2))  # Выведет: [['ban', 'nab'], ['call', 'clal', 'lalc', 'llac'], ['ccall']]
    words3 = ['abc', 'zxc', 'czx', 'aab', 'zcx', 'bac']
    print(group_anagrams(words3))  # Выведет: [['abc', 'bac'], ['zxc', 'czx', 'zcx'], ['aab']]
