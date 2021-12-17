import telebot
from telebot import types
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)

joinedFile = open('joined.txt', 'r')
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

text = {}
qs = {}


@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    if not str(id) in joinedUsers:
        if id != 1647407069:
            joinedFile = open('joined.txt', 'a')
            joinedFile.write(str(id) + '\n')
            joinedUsers.add(id)
            bot.send_message(message.chat.id, 'Вы успешно присоединились к презентации!!!')
        else:
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            b1 = types.InlineKeyboardButton(text='Начать презентацию', callback_data='Presentation')
            b2 = types.InlineKeyboardButton(text='Начать тест', callback_data='Test')
            b3 = types.InlineKeyboardButton(text='Донат', callback_data='Donat')
            keyboard.add(b1, b2, b3)
            bot.send_message(id, 'Выберите комманду:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Presentation':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_1')
        keyboard.add(b1)
        text[call.message.chat.id, 'slide_1'] = 'Презентация на тему: "Cинильная кислота"' \
                                                '\n\nСини́льная (циа́нистая) кислота́ ' \
                                                '(цианистый водород, циановодород, нитрил муравьиной кислоты) — неорганическое соединение, ' \
                                                'представляющее собой бесцветную легкоподвижную жидкость с запахом горького миндаля. ' \
                                                'Кислота с химической формулой HCN.' \
                                                '\n\nСинильная кислота впервые получена в 1782 г. К. Шееле (Швеция). ' \
                                                'В качестве отравляющего вещества впервые она была применена в 1916 г. французскими войсками. ' \
                                                'Всего до конца первой мировой войны французская армия применила около 4 тыс. т синильной кислоты, ' \
                                                'но ожидаемого боевого эффекта не достигла из-за несовершенства средств применения'

        file = open('slide_1.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_1'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_1':
        for user in joinedUsers:
            file = open('slide_1.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_1'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_2')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_2'] = 'Основные области потребления' \
                                               '\n\nОсновными областями потребления синильной кислоты являются производства метакрилатов, ' \
                                               'перерабатываемых в так называемое органическое стекло, акрилонитрила ' \
                                               'цианидов, потребляемых промышленностью пестицидов (гербицидов и средств борьбы с вредителями ' \
                                               'сельского хозяйства). Все более возрастающее количество синильной кислоты перерабатывается в ' \
                                               'аминокислоты, детергенты, комплексообразователи для металлургической промышленности. ' \
                                               'Сама синильная кислота используется как фумигант для окуривания цитрусовых и оливковых деревьев, ' \
                                               'а также для уничтожения насекомых и грызунов в зернохранилищах, на железнодорожных складах, ' \
                                               'на морских судах.' \
                                               '\n\nВ вооруженных силах США синильной кислотой были снаряжены 1000-фн авиационные химические бомбы ' \
                                               'взрывного принципа действия, относящиеся по табельности к группе С. Они кодируются одним зеленым ' \
                                               'кольцом и маркируются надписью «АС GAS».'

        file = open('slide_2.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_2'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_2':
        for user in joinedUsers:
            file = open('slide_2.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_2'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_3')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_3'] = 'Токсические свойства' \
                                               '\n\nСинильная кислота поражает организм при вдыхании ее пара, при приеме с водой и продуктами ' \
                                               'питания, путем резорбции через кожу, при попадании в кровь через раневые поверхности. ' \
                                               'Наибольшую опасность представляет вдыхание пара АС.' \
                                               '\n\nСинильная кислота является веществом, вызывающим кислородное голодание тканевого типа. ' \
                                               'Синильная кислота и её соли, растворенные в крови, достигают тканей, где вступают во ' \
                                               'взаимодействие с трехвалентной формой железа цитохромоксидазы. Соединившись с цианидом, ' \
                                               'цитохромоксидаза утрачивает способность переносить электроны на молекулярный кислород. ' \
                                               'Вследствие выхода из строя конечного звена окисления блокируется вся дыхательная цепь и ' \
                                               'развивается тканевая гипоксия. Кислород доставляется к тканям в достаточном количестве с ' \
                                               'артериальной кровью, но ими не усваивается и переходит в неизмененном виде в венозное русло. ' \
                                               'Одновременно нарушаются процессы образования макроэргов, необходимых для нормальной деятельности ' \
                                               'различных органов и систем.'

        file = open('slide_3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_3'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_3':
        for user in joinedUsers:
            file = open('slide_3.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_3'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_4')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_4'] = 'Действие на нервную систему' \
                                               '\n\nВ результате тканевой гипоксии, развивающейся под влиянием синильной кислоты, ' \
                                               'в первую очередь нарушаются функции центральной нервной системы.'

        file = open('slide_4.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_4'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_4':
        for user in joinedUsers:
            file = open('slide_4.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_4'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_5')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_5'] = 'Действие на дыхательную систему' \
                                               '\n\nВ результате острого отравления наблюдается резко выраженное увеличение частоты и ' \
                                               'глубины дыхания. Развивающуюся одышку следует рассматривать как компенсаторную реакцию организма на гипоксию. ' \
                                               'Стимулирующее действие синильной кислоты на дыхание обусловлено возбуждением хеморецепторов каротидного синуса ' \
                                               'и непосредственным действием яда на клетки дыхательного центра. Первоначальное возбуждение дыхания по ' \
                                               'мере развития интоксикации сменяется его угнетением вплоть до полной остановки. ' \
                                               'Причинами этих нарушений являются тканевая гипоксия и истощение энергетических ресурсов в клетках каротидного синуса ' \
                                               'и в центрах продолговатого мозга.'

        file = open('slide_5.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_5'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_5':
        for user in joinedUsers:
            file = open('slide_5.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_5'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_6')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_6'] = 'Действие на сердечно-сосудистую систему' \
                                               '\n\nПроникая в кровь, она снижает способность клеток воспринимать кислород из притекающей крови. ' \
                                               'Наступает кислородное голодание. А так как нервные клетки больше всех остальных нуждаются в кислороде, ' \
                                               'они первыми страдают от действия синильной кислоты. В начальном периоде интоксикации ' \
                                               'наблюдается замедление сердечного ритма. Повышение артериального давления и увеличение минутного ' \
                                               'объема сердца происходят за счет возбуждения синильной кислотой хеморецепторов каротидного синуса ' \
                                               'и клеток сосудодвигательного центра, с одной стороны, выброса катехоламинов из надпочечников и ' \
                                               'вследствие этого спазма сосудов — с другой. По мере развития отравления артериальное давление падает, ' \
                                               'пульс учащается, развивается острая сердечно-сосудистая недостаточность и наступает остановка сердца.'

        file = open('slide_6.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_6'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_6':
        for user in joinedUsers:
            file = open('slide_6.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_6'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_7')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_7'] = 'Физические свойства' \
                                               '\n\nСинильная кислота представляет собой бесцветную, прозрачную и очень подвижную жидкость со ' \
                                               'своеобразным запахом, в малых концентрациях напоминающим запах горького миндаля. ' \
                                               'Плотность жидкого ОВ при температуре 20°С 0,6894 г/см3, плотность пара по воздуху 0,947.' \
                                               '\n\nСинильная кислота во всех соотношениях смешивается с водой и растворяется в большинстве органических растворителей, ' \
                                               'за исключением перфторуглеводородов и минеральных масел.' \
                                               '\n\nТемпература кипения 25,7° С, давление насыщенного пара 612 мм рт. ст. при температуре 20°С, максимальная концентрация ' \
                                               'при этой температуре 873 мг/л. При минус 13,3° С безводная синильная кислота затвердевает.' \
                                               '\n\nНА ВИДЕО НЕИЗВЕСТНО ЧТО! ПРОСТО НАЩЕЛ ВИДЕО В ИНЕТЕ! СМОТРИТЕ НА ЗДОРОВЬЕ!!!'

        file = open('slide_7.mp4', 'rb')
        bot.send_video(call.message.chat.id, file, None, text[call.message.chat.id, 'slide_7'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_7':
        for user in joinedUsers:
            file = open('slide_7.mp4', 'rb')
            bot.send_video(user, file, None, text[call.message.chat.id, 'slide_7'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text='Показать', callback_data='Slide_8')
        keyboard.add(b1)
        text[
            call.message.chat.id, 'slide_8'] = 'Как защититься? Доступно ли автосохранение?' \
                                               '\n\nСовременный фильтрующий противогаз надежно защищает органы дыхания от воздействия АС. ' \
                                               'При длительном пребывании в атмосфере, зараженной АС, особенно в закрытых помещениях, ' \
                                               'где могут быть созданы высокие концентрации вещества, необходимо пользоваться защитной одеждой.' \
                                               '\n\nПри поражении АС следует применить антидот, например амилнитрит. ' \
                                               'Раздавленную ампулу с антидотом быстро вводят под лицевую часть противогаза, ' \
                                               'при необходимости делают искусственное дыхание. Следует помнить, что при вдыхании ' \
                                               'содержимого одной ампулы антидота до 20% гемоглобина крови превращается в метгемоглобин, ' \
                                               'не участвующий в переносе кислорода от легких к тканям. Поэтому при оказании первой помощи ' \
                                               'пораженному рекомендуется использовать не более двух ампул с амилнитритом.' \
                                               '\n\nА вообще, тебе ничего не поможет!!!) Удачи!'

        file = open('slide_8.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, text[call.message.chat.id, 'slide_8'], reply_markup=keyboard)
        file.close()

    if call.data == 'Slide_8':
        for user in joinedUsers:
            file = open('slide_8.jpg', 'rb')
            bot.send_photo(user, file, text[call.message.chat.id, 'slide_8'])
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b2 = types.InlineKeyboardButton(text='Начать тест', callback_data='Test')
        b3 = types.InlineKeyboardButton(text='Донат', callback_data='Donat')
        keyboard.add(b2, b3)
        bot.send_message(call.message.chat.id, 'Выберите комманду:', reply_markup=keyboard)

        time.sleep(5)
        for user in joinedUsers:
            keyboard1 = types.InlineKeyboardMarkup(row_width=1)
            b21 = types.InlineKeyboardButton(text='Начать тест', callback_data='Test')
            keyboard1.add(b21)
            bot.send_message(user, 'Предлагаю тебе пройти тест! Проверь свои знания по этой теме!!', reply_markup=keyboard1)

    if call.data == 'Test':
        buttons = [
            types.InlineKeyboardButton(text='1. Токсических свойствах некоторых химических веществ',
                                       callback_data='T1'),
            types.InlineKeyboardButton(text='2. Изменение состава воздушной среды в зоне заражения',
                                       callback_data='F1'),
            types.InlineKeyboardButton(text='3. Применение биологических веществ', callback_data='F1')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.send_message(call.message.chat.id,
                         f"Химическое оружие – это оружие массового поражения, действие которого основано на:",
                         reply_markup=keyboard)

    if call.data == 'F1':
        qs[call.message.chat.id, "q1"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(text='Зарин, Зоман, Ви-Икс, иприт, синильная кислота, фосген',
                                       callback_data='T2'),
            types.InlineKeyboardButton(text='Би-Зет', callback_data='F2'),
            types.InlineKeyboardButton(text='Си-Эс, Си-Ар, адамсин, хлорацетофенон', callback_data='F2')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Какие БТХВ смертельного поражающего действия?', reply_markup=keyboard)

    if call.data == 'T1':
        qs[call.message.chat.id, "q1"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(text='Зарин, Зоман, Ви-Икс, иприт, синильная кислота, фосген',
                                       callback_data='T2'),
            types.InlineKeyboardButton(text='Би-Зет', callback_data='F2'),
            types.InlineKeyboardButton(text='Си-Эс, Си-Ар, адамсин, хлорацетофенон', callback_data='F2')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Какие БТХВ смертельного поражающего действия?', reply_markup=keyboard)

    if call.data == 'F2':
        qs[call.message.chat.id, "q2"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(
                text='При вдыхании зараженного воздуха, попадании ОВ в глаза, на кожу, при употреблении зараженной воды и пищи',
                callback_data='T3'),
            types.InlineKeyboardButton(text='С одежды, обуви и головных уборов', callback_data='F3'),
            types.InlineKeyboardButton(text='Попадая на средства защиты кожи и органов дыхания', callback_data='F3')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Как отравляющие вещества проникают в организм человека?', reply_markup=keyboard)

    if call.data == 'T2':
        qs[call.message.chat.id, "q2"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(
                text='При вдыхании зараженного воздуха, попадании ОВ в глаза, на кожу, при употреблении зараженной воды и пищи',
                callback_data='T3'),
            types.InlineKeyboardButton(text='С одежды, обуви и головных уборов', callback_data='F3'),
            types.InlineKeyboardButton(text='Попадая на средства защиты кожи и органов дыхания', callback_data='F3')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Как отравляющие вещества проникают в организм человека?', reply_markup=keyboard)

    if call.data == 'T3':
        qs[call.message.chat.id, "q3"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(
                text='проникновение опасных веществ через органы дыхания и кожные покровы в организм человека',
                callback_data='T4'),
            types.InlineKeyboardButton(text='интенсивное излучение гамма лучей, поражающее людей', callback_data='F4'),
            types.InlineKeyboardButton(text='лучистый поток энергии', callback_data='F4')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Поражающие факторы химических аварий с выбросом аварийно химически опасных веществ (АХОВ) – это',
                              reply_markup=keyboard)

    if call.data == 'F3':
        qs[call.message.chat.id, "q3"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(
                text='проникновение опасных веществ через органы дыхания и кожные покровы в организм человека',
                callback_data='T4'),
            types.InlineKeyboardButton(text='интенсивное излучение гамма лучей, поражающее людей', callback_data='F4'),
            types.InlineKeyboardButton(text='лучистый поток энергии', callback_data='F4')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Поражающие факторы химических аварий с выбросом аварийно химически опасных веществ (АХОВ) – это',
                              reply_markup=keyboard)

    if call.data == 'F4':
        qs[call.message.chat.id, "q4"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(
                text='территория заражения',
                callback_data='F5'),
            types.InlineKeyboardButton(text='зона химического заражения', callback_data='T5'),
            types.InlineKeyboardButton(text='область химического заражения', callback_data='F5')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Территория или акватория, в пределах которой распространены или куда '
                                   'принесены опасные химические вещества в концентрациях и количествах, '
                                   'создающих опасность для жизни и здоровья людей, животных и растений в '
                                   'течение определенного времени – это',
                              reply_markup=keyboard)

    if call.data == 'T4':
        qs[call.message.chat.id, "q4"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(
                text='территория заражения',
                callback_data='F5'),
            types.InlineKeyboardButton(text='зона химического заражения', callback_data='T5'),
            types.InlineKeyboardButton(text='область химического заражения', callback_data='F5')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Территория или акватория, в пределах которой распространены или куда '
                                   'принесены опасные химические вещества в концентрациях и количествах, '
                                   'создающих опасность для жизни и здоровья людей, животных и растений в '
                                   'течение определенного времени – это',
                              reply_markup=keyboard)

    if call.data == 'T5':
        qs[call.message.chat.id, "q5"] = '1 балл'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Ура, тест успешно завершен. Идет подсчет баллов! Твои ответы:'
                                               f'\n\n1. Вопрос - {qs[call.message.chat.id, "q1"]}'
                                               f'\n2. Вопрос - {qs[call.message.chat.id, "q2"]}'
                                               f'\n3. Вопрос - {qs[call.message.chat.id, "q3"]}'
                                               f'\n4. Вопрос - {qs[call.message.chat.id, "q4"]}'
                                               f'\n5. Вопрос - {qs[call.message.chat.id, "q5"]}')

        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Ты Молодец!!!')
        time.sleep(2.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Ты можешь мне помочь!!!'
                                   f'\n\nОтправь мне сколько не жалко на СберБанк по номеру +7(938)454-73-36 со словом "Добро!"'
                                   f'\nили c предложением "Валера, больше не кури!!!". Поможем мне накопить 2000р')

    if call.data == 'F5':
        qs[call.message.chat.id, "q5"] = '0 баллов'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Ура, тест успешно завершен. Идет подсчет баллов! Твои ответы:'
                                   f'\n\n1. Вопрос - {qs[call.message.chat.id, "q1"]}'
                                   f'\n2. Вопрос - {qs[call.message.chat.id, "q2"]}'
                                   f'\n3. Вопрос - {qs[call.message.chat.id, "q3"]}'
                                   f'\n4. Вопрос - {qs[call.message.chat.id, "q4"]}'
                                   f'\n5. Вопрос - {qs[call.message.chat.id, "q5"]}')

        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Ты Молодец!!!')
        time.sleep(2.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Ты можешь мне помочь!!!'
                                   f'\n\nОтправь мне сколько не жалко на СберБанк по номеру +7(938)454-73-36 со словом "Добро!"'
                                   f'\nили c предложением "Валера, больше не кури!!!". Поможем мне накопить 2000р')

bot.polling(none_stop=True, interval=0)
