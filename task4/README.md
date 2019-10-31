# Задание 4

**Входные данные (Input):** 
На вход подаётся журнал выполнения некоторой многопоточной программы. Известно, что формат каждой строки журнала выглядит так:

\<HH\>:\<MM\>:\<SS\> \<TID\> \<PAYLOAD\> ,

где: HH - часы, MM - минуты, SS - секунды, TID - идентификатор потока, PAYLOAD - полезная нагрузка.


**Выходные данные (Output):** 
Необходимо найти номера всех строк, предшествующих задержкам выполнения программы. Задержкой считается отсутствие сообщений от данного потока более 3 секунд.

**Example:**

Для следующего журнала выполнения, правильным ответом будет **"4 5"**

`Total processor utilization across all cores: 46`

`Total processor utilization across all cores: 62`

`Total processor utilization across all cores: 53`

`Total processor utilization across all cores: 64`

`Total processor utilization across all cores: 73`

__Данные представлены в `dataset_267210_1.txt`__
