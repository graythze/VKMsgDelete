<div align="center">

# VK Message Remover  
## [🇷🇺 RUS](#rus) | [🇬🇧 ENG](#eng)

</div>

---

<div align="center">

# <a name="rus"></a>🇷🇺 RUS

</div>

# Цель
Скрипт позволяет удалить определенный промежуток сообщений для двух сторон.

Скрипт работает для личных сообщений, сообщений в беседах, а также для сообщений внутри ботов.

---

## 📋 Инструкция  

### 1. Получение токена
Получите токен для страницы VK:  
  - Для упрощения процедуры можно воспользоваться сервисом [vkhost.github.io](https://vkhost.github.io/). 

  `Предпочительное приложение для получения токена: Kate Mobile`

---

### 2. Запуск скрипта
  - Скачайте и установите [Python 3](https://www.python.org/downloads/). 
  - Откройте PowerShell, CMD или Terminal
  - Скачайте необходимые библиотеки с помощью команды:
    ```bash
    pip install requirements.txt
    ```  
  - Запустите скрипт с помощью команды:  
    ```bash
    python msg_delete.py --min_msg 1 --max_msg 15000000 --vk_token "VK Token"
    ```  
    - Аргумент `--min_msg` отвечает за ID первого сообщение, с которого нужно начать удаление.
    - Аргумент `--max_msg` отвечает за ID последнего сообщения, которое нужно удалить.
    - Аргумент `--vk_token` отвечает за ранее полученный токен VK

---

## ⚠️ Действия после использования скрипта

### Отзыв ранее сгенерированного токена
В целях безопасности, крайне рекомендуется отозвать ранее полученный токен приложения. Чтобы отозвать токен, нужно:
  - Перейти на страницу [Внешних сервисов VK](https://id.vk.com/account/#/services).
  - Найти приложение, которое ранее было использовано для получения токена в разделе **Внешние сервисы**.
  - Отозвать токен для данного приложения  

[⬆️ В начало](#vk-message-remover)  

---

<div align="center">

# <a name="eng"></a>🇬🇧 ENG

</div>

# Purpose
The script allows you to delete a specific range of messages for both parties.

It works for private messages, group chats, and bot messages.

---

## 📋 Instructions  

### 1. Getting a Token
Get a token for your VK page:  
  - To simplify the procedure, you can use [vkhost.github.io](https://vkhost.github.io/).  

  `Preferred application for getting a token: Kate Mobile`  

---

### 2. Running the Script
  - Download and install [Python 3](https://www.python.org/downloads/).  
  - Open PowerShell, CMD, or Terminal.  
  - Install the required libraries with the command:  
    ```bash
    pip install requirements.txt
    ```  
  - Run the script with the command:  
    ```bash
    python msg_delete.py --min_msg 1 --max_msg 15000000 --vk_token "VK Token"
    ```  
    - The `--min_msg` argument specifies the ID of the first message to delete.  
    - The `--max_msg` argument specifies the ID of the last message to delete.  
    - The `--vk_token` argument is the previously obtained VK token.  

---

## ⚠️ Actions After Using the Script  

### Revoking the Previously Generated Token
For security reasons, it is highly recommended to revoke the previously obtained application token. To revoke it, you need to:  
  - Go to the [VK External Services](https://id.vk.com/account/#/services) page.  
  - Find the application previously used to obtain the token in the **External Services** section.  
  - Revoke the token for this application.  

[⬆️ Back to Top](#vk-message-remover)  
