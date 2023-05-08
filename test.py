# Добавьте новые условия в elif и else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 0 or remainder >= 5:  
        print(f'У вас {messages_count} новых сообщений')
    elif remainder >= 11 and remainder <= 19:  
        print(f'У вас {messages_count} новых сообщений')        
    elif remainder == 1 and remainder != 11:  
        print(f'У вас {messages_count} новое сообщение')

    else:  
        print(f'У вас {messages_count} новых сообщения')
