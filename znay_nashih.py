from template import generate

name = 'znay_nashih'
data = """\
[[['Карасев', 'Старкевич', 'Иван'],
  ['Дощатников', 'Карасев', 'Старкевич'],
  ['Ступин', 'Карасев', 'Старкевич'],
  ['Карасев', 'Старкевич', 'Иван', 'Корзинкина'],
  ['Карасев', 'Старкевич', 'Самуил Самойлович'],
  ['Карасев', 'Старкевич', 'Анахоретов'],
  ['Надежда Александровна', 'Корзинкина', 'Лакей', 'Мазаров', 'Карасев', 'Старкевич']],
 [['Мазаров', 'Ступин', 'Дощатников', 'Самоварников', 'Карасев', 'Лакей', 'Надежда Александровна'],
  ['Надежда Александровна', 'Федосья Алексеевна'],
  ['Мазаров', 'Ступин', 'Дощатников', 'Самоварников', 'Карасев', 'Лакей', 'Надежда Александровна', 'Рыжий мужик', 'Невзрачный', 'Артельщик']],
 [['Анахоретов', 'Мазаров', 'Ступин'],
  ['Анахоретов', 'Мазаров', 'Ступин', 'Карасев', 'Старкевич', 'Дощатников', '1й и 2й члены', 'Исправник', 'Терентьев']],
 [['Ступин', 'Дощатников', 'Самоварников'],
  ['Анахоретов', 'Ступин', 'Дощатников', 'Самоварников'],
  ['Ступин', 'Дощатников', 'Самоварников', 'Мазаров', 'Надежда Александровна'],
  ['Старкевич', 'Карасев', 'Иван'],
  ['Старкевич', 'Самоварников', 'Дощатников'],
  ['Карасев', 'Старкевич', 'Самоварников', 'Дощатников', 'Ступин', 'Мазаров', '1й и 2й члены', 'Исправник', 'Корзинкина']]]
"""

generate(name, data)