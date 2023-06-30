# Practice
19.06.2023
 - Я скачал Passoffice. В процессе использования я познакомился с различными возможностями, предоставляемыми 
   приложением. Это позволило мне получить общее представление о его функционале и способностях. Нашел баг связанный с остановкой задач.

20.06.2023
 - Получил исходники тестов от ментора Алексея Нехорошева. Проанализировал код и запустил тесты для проверки его функциональности.

21.06.2023
 - Написал тесты для удаления заявки и посетителя. Добавил проверку успешность теста “Добавление посетителя”. Разобрался как сделать тесты на
  +	Проверку, что авторизация прошла успешно
  +	Проверку, что создалась заявка и находится в обработке

22.06.2023  
 - Допилил тест для создания заявки. Декомпозировал процесс так, чтобы была возможно создать заявку кем-то одним, а обработать уже другим оператором. Добавил 
   проверку, что регистрация прошла успешно. Добавил проверку статуса заявки(Разрешена/Обработана).

23.06.2023
- Реализовал кейс:
 Создан сотрудник через посетителя. Дальше создается оператор через этого сотрудника. Необходимо зайти под двумя сотрудниками - один под админом, второй под           созданным сотрудником. Из под админа снять чек-бокс активный у оператора. Перейти на окно, где открыт сотрудник и убедится, что его выкинуло из системы. Попробовать  зайти снова через оператора. И убедится, что зайти не получается. 

27.06.2023
- Получил кейс. В процессе выполнения столкнулся с тем, что СКД не видит активных карт. Алексей дал новое задание:
 Реализовать функцию для выбора типа пропуска. Раньше создание заявки происходило только с гостевым пропуском. Теперь есть возможность выдавать постоянный пропуск и частично временный.
 Добавил функцю для удаления оператора. Избавился от повторяющихся локаторов.

28.06.2023
- Исправил некоторые замечания по коду(Проверка на успешность добавления/удаления посетителя). Теперь проверка успешности добавления пользователя происходит по ID.
- Практически реализовал интегрирование LyriX. Декомпозировал функцию, чтобы была возможнсть переиспользовать участки кода для других интеграций. 

29.06.2023
 - Продолжил работу с интегрированием LyriX. Начал реализовывать функцию для APACS. Добавил функцию выбора между Lyrix/APACS.

30.06.2023
 - Продолжил работу над интегрированием LyriX и APACS. Исправил два костыля, связанных с обработкой исключений. Занимался рефакторингом кода.
