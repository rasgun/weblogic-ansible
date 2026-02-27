\# 🚀 WebLogic Server 12.1.3 Automated Deployment



!\[Ansible](https://img.shields.io/badge/Ansible-2.9+-black?style=for-the-badge\&logo=ansible)

!\[Java](https://img.shields.io/badge/Java-8-orange?style=for-the-badge\&logo=openjdk)

!\[WebLogic](https://img.shields.io/badge/Oracle-WebLogic\_12c-blue?style=for-the-badge\&logo=oracle)



Автоматизированное развертывание \*\*Oracle WebLogic Server 12.1.3\*\* с помощью Ansible. Плейбук подготавливает операционную систему, устанавливает JDK и WLS, а также создает рабочий домен.



---



\## 📂 Подготовка дистрибутивов

Перед запуском скачайте и разместите файлы в папках ролей:

1\. \*\*JDK:\*\* `roles/linux-jdk/files/jdk-8u311-linux-x64.tar.gz`

2\. \*\*WLS:\*\* `roles/fmw-software/files/fmw\_12.1.3.0.0\_wls.jar`



---



\## ⚙️ Настройка окружения



\### 1. Инвентаризация (`hosts`)

Укажите IP вашего сервера в файле `hosts`:

```ini

\[weblogic]

wls-node-01 ansible\_host=192.168.1.4



\[weblogic:vars]

ansible\_user=root

ansible\_port=22



2\. Переменные окружения (infra-vars.yml)



Проверьте ключевые параметры в файле переменных:



&nbsp;   oracle\_home: путь к Middleware (бинарные файлы).



&nbsp;   domain\_home: путь к конфигурации домена.



&nbsp;   wls\_admin\_password: пароль для входа в консоль управления.



🚀 Запуск установки



Используйте команду ниже для запуска процесса. Флаг -k инициирует запрос пароля SSH для пользователя root.

Bash



ansible-playbook -i hosts weblogic-fmw-domain.yml -k -vv | tee install\_detailed.log



&nbsp;   Note: Флаг -vv обеспечит подробный вывод для отладки, а tee запишет полный лог в файл install\_detailed.log.



🏁 Управление после установки



После завершения плейбука все действия выполняются под пользователем oracle.

Шаг 1: Вход на сервер

Bash



ssh root@192.168.1.4

sudo su - oracle



Шаг 2: Запуск Node Manager



Необходим для управления инстансами через консоль. Запускается в фоновом режиме:

Bash



cd /oracle/product/fmw/user\_projects/domains/base\_domain/bin

nohup ./startNodeManager.sh > nm.out 2>\&1 \&



Шаг 3: Проверка Node Manager (опционально)



Чтобы убедиться, что Node Manager запустился успешно, проверьте порт 5556:

Bash



netstat -an | grep 5556



Шаг 4: Запуск Admin Server

Bash



cd /oracle/product/fmw/user\_projects/domains/base\_domain/bin

./startWebLogic.sh



🔗 Доступ к консоли



После успешного запуска Admin Server консоль управления будет доступна по адресу:

📌 https://www.google.com/url?sa=E\&source=gmail\&q=http://192.168.1.4:7001/console

