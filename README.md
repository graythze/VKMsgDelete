# Delete VK Messages for Recipient  
**Удалить сообщения пользователя для двух сторон**

## 📋 Steps to Use  

1. **Get a Token**  
   Obtain a token for your VK page.  
   - Use [vkhost.github.io](https://vkhost.github.io/).  
   - Follow the instructions provided on the website to generate your token.  

2. **Set Up the Script**  
   - Open the file `msg_delete.py`.  
   - Define the range of messages to delete by setting:  
     - `min_msg`: ID of the first message to delete.  
     - `max_msg`: ID of the last message to delete.  
   - Insert the token you obtained in step 1 into the variable `vk_token`.  

3. **Run the Script**  
   - Launch your terminal.  
   - Run the script using the command:  
     ```bash
     python msg_delete.py
     ```  

4. **Revoke Permissions (For Security)**  
   - After the script completes, visit [VK External Services](https://id.vk.com/account/#/services).  
   - Locate the app you used in step 1 under **External services**.  
   - Revoke all permissions for the app.  

---

### ⚠️ Disclaimer  
Use this script responsibly. Deleting messages for both sides is irreversible. Ensure you have the proper permissions to modify message history.  

---

### 🛠 Requirements  
- Python installed on your system.  
- requests library 

