# Delete VK Messages for Recipient / Удалить сообщения пользователя для двух сторон  

## 📋 Steps to Use / Инструкция  

### 1. Get a Token / Получение токена  
- **English:**  
  Obtain a token for your VK page:  
  - Use [vkhost.github.io](https://vkhost.github.io/).  
  - Follow the instructions provided on the website to generate your token.  

- **Русский:**  
  Получите токен для вашей страницы VK:  
  - Используйте [vkhost.github.io](https://vkhost.github.io/).  
  - Следуйте инструкциям на сайте, чтобы сгенерировать токен.  

---

### 2. Set Up the Script / Настройка скрипта  
- **English:**  
  - Open the file `msg_delete.py`.  
  - Define the range of messages to delete by setting:  
    - `min_msg`: ID of the first message to delete.  
    - `max_msg`: ID of the last message to delete.  
  - Insert the token you obtained in step 1 into the variable `vk_token`.  

- **Русский:**  
  - Откройте файл `msg_delete.py`.  
  - Укажите диапазон сообщений для удаления:  
    - `min_msg`: ID первого сообщения, которое нужно удалить.  
    - `max_msg`: ID последнего сообщения, которое нужно удалить.  
  - Вставьте полученный токен в переменную `vk_token`.  

---

### 3. Run the Script / Запуск скрипта  
- **English:**  
  - Launch your terminal.  
  - Run the script using the command:  
    ```bash
    python msg_delete.py
    ```  

- **Русский:**  
  - Откройте терминал.  
  - Запустите скрипт с помощью команды:  
    ```bash
    python msg_delete.py
    ```  

---

### 4. Revoke Permissions (For Security) / Отзыв разрешений (для безопасности)  
- **English:**  
  - After the script completes, visit [VK External Services](https://id.vk.com/account/#/services).  
  - Locate the app you used in step 1 under **External services**.  
  - Revoke all permissions for the app.  

- **Русский:**  
  - После завершения работы скрипта перейдите в [Внешние сервисы VK](https://id.vk.com/account/#/services).  
  - Найдите приложение, которым вы пользовались на шаге 1, в разделе **Внешние сервисы**.  
  - Отзовите все разрешения для приложения.  

---

## ⚠️ Disclaimer / Внимание  
- **English:**  
  Use this script responsibly. Deleting messages for both sides is irreversible. Ensure you have the proper permissions to modify message history.  

- **Русский:**  
  Используйте скрипт ответственно. Удаление сообщений для обеих сторон является необратимым. Убедитесь, что у вас есть необходимые права для изменения истории сообщений.  

---

## 🛠 Requirements / Требования  
- **English:**  
  - Python installed on your system.  
  - requests library 

- **Русский:**  
  - Установленный Python.  
  - библиотека requests  
