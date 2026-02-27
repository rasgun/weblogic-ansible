🚀 WebLogic 12.1.3 Automated Deployment (Ansible)



Данный проект предназначен для автоматизированной установки Oracle WebLogic Server 12.1.3 и создания базового домена на чистом сервере (Linux). Все действия выполняются от имени пользователя oracle, что соответствует стандартам безопасности и администрирования Oracle.

📋 Содержание



    Требования



    Структура проекта



    Быстрый старт (Настройка)



    Запуск установки



    Что делать после установки



🛠 Требования



Перед запуском убедитесь, что у вас есть:



    Удаленный сервер: Свежая ОС семейства Linux (CentOS/RHEL/Oracle Linux рекомендуются).



    Локальная машина: Установленный Ansible (версия 2.9+).



    Дистрибутивы: В папку roles/fmw-software/files/ и roles/linux-jdk/files/ нужно положить:



        jdk-8u311-linux-x64.tar.gz



        fmw\_12.1.3.0.0\_wls.jar



📂 Структура проекта



    linux-jdk: Установка Java (JDK 8).



    linux-wls: Подготовка ОС (создание пользователя oracle, групп, лимитов).



    fmw-software: "Тихая" установка бинарников WebLogic.



    fmw-domain: Создание домена, Admin-сервера и настройка портов.



⚙️ Быстрый старт (Настройка)

Шаг 1: Настройка доступа к серверу



Отредактируйте файл hosts. Укажите IP вашего сервера и пользователя (обычно root для первой настройки):

Ini, TOML



\[weblogic]

server-prod-01 ansible\_host=192.168.1.4



\[weblogic:vars]

ansible\_user=root

ansible\_port=22



Шаг 2: Настройка переменных (infra-vars)



Откройте infra-vars.yml и проверьте основные пути:



    oracle\_home: путь к установке WebLogic.



    domain\_home: путь к будущему домену.



    wls\_admin\_user/wls\_admin\_password: ваши учетные данные для входа в консоль WebLogic.



🚀 Запуск установки



Для запуска процесса используйте следующую команду. Мы добавили логирование, чтобы вы могли отследить каждый шаг.

Bash



ansible-playbook -i hosts weblogic-fmw-domain.yml -k -vv | tee install\_detailed.log



После запуска плейбука необходимо ввести пароль от root пользователя



Что значат флаги:



    -k: Ansible спросит у вас пароль от пользователя root.



    -vv: Очень подробный вывод (важно для первого раза).



    | tee ...: Запись всего процесса в файл лога.





Если возникли ошибки в процессе установки, посмотреть их можно следующей командой



grep -E "FAILED|FATAL" install\_detailed.log





🏁 Что делать после установки?



Когда плейбук завершит работу, ваш WebLogic будет готов, но его нужно запустить.



    Зайдите на сервер:

    Bash



    ssh root@192.168.1.4



    Переключитесь на пользователя oracle:

    Bash



    sudo su - oracle



    Запустите AdminServer:

    Bash



    cd /oracle/product/fmw/user\_projects/domains/base\_domain/bin

    nohup ./startWebLogic.sh \&

 

    Запустите Nodmanager:

    Bash

 

    sudo su - oracle

    cd /oracle/product/fmw/user\_projects/domains/base\_domain/bin

    nohup ./startNodeManager.sh \&



    Войдите в консоль управления:

    Откройте браузер и перейдите по адресу:

    http://192.168.1.4:7001/console

