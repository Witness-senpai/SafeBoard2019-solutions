# Задание 2

На стандартный вход программы подаются полностью собранные логи службы мониторинга загрузки процессора, где каждая строка содержит в себе значение загрузки процессора на момент измерения. Нормальная загрузка процессора находится в диапазоне +/- 10% (включительно) от среднего значения (по всем значениям). Если какие-то значения не входят в диапазон, то это считается отклонением. Количество входных строк может быть любым. Необходимо вывести количество найденных отклонений.

**Входные данные (Input):** 
Total processor utilization across all cores: N1
Total processor utilization across all cores: N2
Total processor utilization across all cores: N3
где:
N - значение загрузки процессора на момент измерения.


**Выходные данные (Output):** 
M
где:
​​​​​​​M - количество найденных отклонений

**Sample Input:**
Total processor utilization across all cores: 46
Total processor utilization across all cores: 62
Total processor utilization across all cores: 53
Total processor utilization across all cores: 64
Total processor utilization across all cores: 73

**Sample Output:**
3