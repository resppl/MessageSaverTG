# 🇺🇸 | MessageSaverTG

A special script has been developed to ensure the preservation of personal messages from users, regardless of whether you are online or offline. Here's how the script works:

# 📂 Automatic Folder Creation

Upon receiving a message from a user, a folder is automatically created, named after their ID, with their Telegram username in parentheses. Inside this folder, additional subfolders are created:

    📸 media: For storing media files.
    💬 stickers For storing sticker files.
    🖼️ photo For storing photos.

# 🌐 log.html Page Generation

As soon as a user sends you a message or you initiate a conversation, a webpage named log.html is generated in the corresponding folder (with the user’s ID and username). This webpage displays user information:

    📱 Telegram ID
    🧑‍💼 Full name
    🏷️ Username
    📞 Phone number
    🌐 TON Web 3.0 address
    🖼️ Profile picture (if available)
    💬 Message History

At the bottom of the page, incoming and outgoing messages are listed. For each message, attached media files can be viewed via hyperlinks.

# 🔒 Message Preservation

This script ensures that your conversation is saved even if the user deletes messages, both on their side and yours. As soon as a message or media file is sent by the user, it is immediately saved to your server.

# 📱 Easy Access Across Devices

The logs can be viewed from both mobile devices and any other device, with the layout remaining intact and unchanged. No need for manual exports!

# 🛠️ Script Installation Guide

To install the script, you need to first install the Telethon library. This can be done easily by executing the following command in your terminal or command prompt:

    pip install telethon

After installing the library, you will need to edit the script file called "MessageSaverTG.py" to include your personal configuration settings in it. In particular, you need to change the API ID and API HASH to match your credentials. These values can be obtained on the Telegram developer portal. Without proper API settings, the script will not work properly.

# ⚙️ File Download Size Limit Configuration

Additionally, the script has a predefined download limit of 200 MB for files. This means that any file larger than 200 MB will not be downloaded by the script. If you wish to change this limit, you can simply edit the **MAX_FILE_SIZE_MB** variable in the script to the desired file size (in megabytes). For example, you can increase the size limit to 500 MB by modifying the variable like this:

    MAX_FILE_SIZE_MB = 500

# 🚀 Running the Script

After completing the necessary edits to the script, you can run it without any issues. The script will function properly, automatically handling the processing and saving of user messages and media files, as described earlier.

By following these steps, you will be able to set up and run the script on your server or personal machine without encountering problems.

# 🇷🇺 | MessageSaverTG

Разработан специальный скрипт, обеспечивающий сохранность личных сообщений пользователей, независимо от того, находитесь ли вы онлайн или офлайн. Вот как работает скрипт:

# 📂 Автоматическое создание папки

При получении сообщения от пользователя автоматически создается папка, названная по его ID, с указанием имени пользователя Telegram в скобках. Внутри этой папки создаются дополнительные вложенные папки:

    📸 media: Для хранения медиафайлов.
    💬 stickers: Для хранения стикеров.
    🖼️ photo: Для хранения фотографий.

# 🌐 log.html Создание страницы

Как только пользователь отправляет вам сообщение или вы начинаете разговор, в соответствующей папке (с идентификатором и именем пользователя) создается веб-страница с именем log.html. На этой веб-странице отображается информация о пользователе:

    📱 Telegram ID
    🧑‍💼 Полное имя
    🏷️ Имя пользователя
    📞 Номер телефона
    🌐 Адрес Web 3.0
    🖼️ Фотография профиля (если есть)
    💬 История сообщений

В нижней части страницы перечислены входящие и исходящие сообщения. Для каждого сообщения можно просмотреть прикрепленные медиафайлы с помощью гиперссылок.

# 🔒 Сохранение сообщений
Этот скрипт обеспечивает сохранение беседы, даже если пользователь удаляет сообщения, как со своей, так и с вашей стороны. Как только пользователь отправляет сообщение или медиафайл, они сразу же сохраняются на вашем сервере.

# 📱 Легкий доступ с разных устройств
Журналы можно просматривать как с мобильных устройств, так и с любых других.

# 🛠️ Гайд по установке скрипта

Чтобы установить скрипт, необходимо сначала установить библиотеку Telethon. Это можно легко сделать, выполнив следующую команду в терминале или командной строке:

    pip install telethon

После установки библиотеки вам нужно будет изменить файл скрипта под названием "MessageSaverTG.py", чтобы включить в него ваши личные настройки конфигурации. В частности, необходимо изменить API ID и API HASH, чтобы они соответствовали вашим учетным данным. Эти значения можно получить на портале разработчиков Telegram. Без правильных настроек API скрипт не будет работать должным образом.

# ⚙️ Конфигурация ограничения размера загрузки файлов

Кроме того, скрипт имеет предопределенный лимит загрузки файлов в 200 МБ. Это означает, что любой файл размером более 200 МБ не будет загружен скриптом. Если вы хотите изменить это ограничение, вы можете просто изменить переменную **MAX_FILE_SIZE_MB** в скрипте на желаемый размер файла (в мегабайтах). Например, вы можете увеличить ограничение на размер до 500 МБ, изменив переменную следующим образом:

    MAX_FILE_SIZE_MB = 500

# 🚀 Запуск скрипта

После внесения необходимых изменений в скрипт вы можете запускать его без каких-либо проблем. Скрипт будет работать правильно, автоматически обрабатывая и сохраняя пользовательские сообщения и медиафайлы, как было описано ранее.

Следуя этим шагам, вы сможете настроить и запустить скрипт на своем сервере или персональной машине без проблем.
