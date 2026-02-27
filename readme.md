# 🚀 WebLogic Server 12.1.3 Automated Deployment

![Ansible](https://img.shields.io/badge/Ansible-2.9+-black?style=for-the-badge&logo=ansible)
![Java](https://img.shields.io/badge/Java-8-orange?style=for-the-badge&logo=openjdk)
![WebLogic](https://img.shields.io/badge/Oracle-WebLogic_12c-blue?style=for-the-badge&logo=oracle)

Автоматизированное развертывание **Oracle WebLogic Server 12.1.3** с помощью Ansible. Этот плейбук берет на себя всю "грязную" работу: от настройки ядра Linux до создания рабочего домена.

---

## 🛠 Основные возможности
* **System Ready:** Создание групп (`oinstall`, `dba`), пользователя `oracle` и настройка `limits.conf`.
* **JDK Setup:** Установка и настройка Oracle JDK 8.
* **WLS Install:** Тихая (Silent) установка Middleware бинарников.
* **Domain Config:** Создание домена, настройка Admin Server и Node Manager через WLST.

---

## 📂 Подготовка (Pre-requisites)

Перед запуском необходимо самостоятельно скачать дистрибутивы Oracle (из-за лицензионных ограничений) и разместить их в папках:

1. **JDK:** `roles/linux-jdk/files/jdk-8u311-linux-x64.tar.gz`
2. **WebLogic:** `roles/fmw-software/files/fmw_12.1.3.0.0_wls.jar`

---

## ⚙️ Настройка (Configuration)

### Инвентарь (`hosts`)

Отредактируйте файл `hosts`, указав IP вашего сервера:
```bash
[weblogic]
wls-node-01 ansible_host=192.168.1.4

[weblogic:vars]
ansible_user=root
ansible_port=22
```
### 🚀 Запуск установки

Выполните команду. Флаг -k запросит пароль от root.

```bash
ansible-playbook -i hosts weblogic-fmw-domain.yml -k -vv | tee install_detailed.log
```
Далее необходимо пароль от root

## 🏁 Управление после установки

После завершения все действия выполняются под пользователем oracle.

### Шаг 1: Вход и переход в директорию
```bash
ssh root@192.168.1.4
sudo su - oracle
cd /oracle/product/fmw/user_projects/domains/base_domain/bin
```
### Шаг 2: Запуск сервисов в фоне
Сервис,Команда запуска
```bash
Node Manager,nohup ./startNodeManager.sh > nm.out &
Admin Server,nohup ./startWebLogic.sh &
```
🔗 Доступ к консоли

👉 http://192.168.1.4:7001/console