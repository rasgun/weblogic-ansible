# Читаем базовый шаблон
readTemplate('{{ oracle_home }}/wlserver/common/templates/wls/wls.jar')

# Настройка AdminServer
cd('Servers/AdminServer')
set('ListenAddress', '{{ admin_listen_address }}')
set('ListenPort', {{ admin_port }})

# Настройка логина и пароля администратора
cd('/')
cd('Security/base_domain/User/weblogic')
set('Password', '{{ wls_admin_password }}')

# Сохранение домена
setOption('OverwriteDomain', 'true')
writeDomain('{{ domain_home }}')
closeTemplate()
exit()