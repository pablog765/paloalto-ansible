# Palo Alto Ansible Backup Automation 🚀

Este repositorio contiene la automatización para respaldar la configuración (Running Config) de los Firewalls Palo Alto de la institución.

## Estructura del Proyecto 📂
- `playbooks/`: Contiene el script `backup_email.yml` para ejecutar el respaldo y envío por correo.
- `inventory/`: Archivo `hosts.yml` con la IP, usuario y API Key del equipo.
- `backups/`: Directorio donde se almacenan los XML locales con fecha y hora.
- `vars/`: Variables de conexión cifradas o protegidas.

## Requisitos Previos 🛠️
1. **Python 3.11+** y ambiente virtual `venv-panos`.
2. **Ansible** con la colección `community.general` para el envío de correos.
3. Librerías: `pan-os-python`, `pan-python` y `xmltodict`.

## Ejecución 🚀
Para realizar un backup manual:
```bash
source venv-panos/bin/activate
ansible-playbook playbooks/backup_email.yml -i inventory/hosts.yml
