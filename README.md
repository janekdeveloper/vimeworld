# vimeworld
Python модуль для удобной работы с api

# Быстрый старт
```py
#Импортируем необходимые модули из библиотеки vimeworld
import vimeworld
from vimeworld import Client, users


bot = Client()
bot.start() # Запускаем бота (начинаем взаимодействие с сервером)

# Создаем экземпляр класса users, который предоставляет функции для работы с пользователями на сервере Vimeworld
us = users(bot)

player_id = us.get_by_nick('sad_Devil').user_id # Получаем ID игрока сервера по нику.
player_name = us.get_by_nick('sad_Devil').username # Получаем ник игрока сервера по нику
level = us.get_by_nick('sad_Devil').level # Получаем уровень игрока на сервере по нику
levelpercentage = us.get_by_nick('sad_Devil').levelPercentage # Получаем процент уровня игрока по нику
rank = us.get_by_nick('sad_Devil').rank # Получаем привилегию игрока по нику, список привилегий смотрите ниже.
playedtime = us.get_by_nick('sad_Devil').playedSeconds # Получаем сумму того времени когда игрок был на сервере 
lastseen = us.get_by_nick('sad_Devil').lastSeen # Получаем последний заход
guild_id = us.get_by_nick('sad_Devil').guild_id # Получаем ID гильдии в которой есть игрок, поиск информации о гильдии будет реализован в 0.0.2

print(f"{player_id}\n{player_name}\n{level}\n{levelpercentage}\n{rank}\n{playedtime}\n{lastseen}\n{guild_id}") # Вывод информации
```
Вывод:
```cmd
4222985
sad_Devil
65
0.08196
HOLY
5103280
1706135176
24594
```
# Список привилегий

  <section class="doc-content" id="index-page">
			<section class="left-docs">
				<h3>
					<a id="inforanks">
						Ранги игроков
						</a>
				</h3>
		<table>
      <thead>
        <tr>
          <th style="text-align: center">Ранг</th>
          <th style="text-align: center">Название</th>
          <th style="text-align: center">Префикс</th>
          <th style="text-align: center">Цвет</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center">PLAYER</td>
      <td style="text-align: center">Игрок</td>
      <td style="text-align: center"> </td>
      <td style="text-align: center"> </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">VIP</td>
      <td style="text-align: center">VIP</td>
      <td style="text-align: center"><b style="color: #00be00">[V]</b></td>
      <td style="text-align: center">#00be00</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">PREMIUM</td>
      <td style="text-align: center">Premium</td>
      <td style="text-align: center"><b style="color: #00dada">[P]</b></td>
      <td style="text-align: center">#00dada</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">HOLY</td>
      <td style="text-align: center">Holy</td>
      <td style="text-align: center"><b style="color: #ffba2d">[H]</b></td>
      <td style="text-align: center">#ffba2d</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">IMMORTAL</td>
      <td style="text-align: center">Immortal</td>
      <td style="text-align: center"><b style="color: #e800d5">[I]</b></td>
      <td style="text-align: center">#e800d5</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">BUILDER</td>
      <td style="text-align: center">Билдер</td>
      <td style="text-align: center"><b style="color: #009c00">[Билдер]</b></td>
      <td style="text-align: center">#009c00</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">SRBUILDER</td>
      <td style="text-align: center">Проверенный билдер</td>
      <td style="text-align: center"><b style="color: #009c00">[Пр. билдер]</b></td>
      <td style="text-align: center">#009c00</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">MAPLEAD</td>
      <td style="text-align: center">Главный билдер</td>
      <td style="text-align: center"><b style="color: #009c00">[Гл. билдер]</b></td>
      <td style="text-align: center">#009c00</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">YOUTUBE</td>
      <td style="text-align: center">YouTube</td>
      <td style="text-align: center"><b style="color: #fe3f3f">[YouTube]</b></td>
      <td style="text-align: center">#fe3f3f</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">DEV</td>
      <td style="text-align: center">Разработчик</td>
      <td style="text-align: center"><b style="color: #00bebe">[Dev]</b></td>
      <td style="text-align: center">#00bebe</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">ORGANIZER</td>
      <td style="text-align: center">Организатор</td>
      <td style="text-align: center"><b style="color: #00bebe">[Организатор]</b></td>
      <td style="text-align: center">#00bebe</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">HELPER</td>
      <td style="text-align: center">Хелпер</td>
      <td style="text-align: center"><b style="color: #1b00ff">[Хелпер]</b></td>
      <td style="text-align: center">#1b00ff</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">MODER</td>
      <td style="text-align: center">Модератор</td>
      <td style="text-align: center"><b style="color: #1b00ff">[Модер]</b></td>
      <td style="text-align: center">#1b00ff</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">WARDEN</td>
      <td style="text-align: center">Проверенный модератор</td>
      <td style="text-align: center"><b style="color: #1b00ff">[Модер]</b></td>
      <td style="text-align: center">#1b00ff</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">CHIEF</td>
      <td style="text-align: center">Главный модератор</td>
      <td style="text-align: center"><b style="color: #1b00ff">[Гл. модер]</b></td>
      <td style="text-align: center">#1b00ff</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="text-align: center">ADMIN</td>
      <td style="text-align: center">Главный админ</td>
      <td style="text-align: center"> <b style="color: #00bebe">[Гл. админ]</b></td>
      <td style="text-align: center">#00bebe</td>
    </tr>
  </tbody>
</table>
      </section>
  </section>

# Доп. информация
Кроме `us.get_by_nick('sad_Devil')` можно использовать `us.get_by_id(id)`

#### Цели:
- [x] Получение базовой информации про игрока через имя, ID
- [ ] Получение друзей игрока
- [ ] Получение статуса игрока(онлайн/оффлайн)
- [ ] Получение статистики игрока
- [ ] Получение ачивок игрока
- [ ] Получение последних матчей игрока
* Это лишь небольшая часть того что я планирую добавить в библиотеку.

#### Контакты:
* `sad_Devil` - VimeWorld
* `bytdev` - Discord
