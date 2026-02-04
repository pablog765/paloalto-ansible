# Palo Alto Ansible Backup Automation 🚀

Este repositorio contiene la automatización para realizar respaldos de configuración (Running Config) de los Firewalls Palo Alto de la institución y enviarlos por correo electrónico.

## Estructura del Proyecto 📂
- `playbooks/`: Scripts YAML (`backup_config_email.yml` y `healthcheck.yml`).
- `inventory/`: Definición de equipos (`hosts.yml`).
- `backups/`: Almacenamiento local de archivos XML y logs.
- `vars/`: Credenciales y configuración del proveedor (`firewall.yml`).

## Requisitos Previos 🛠️
1. **Python 3.9+** (Librerías necesarias: `xmltodict`, `pan-python`, `pan-os-python`).
2. **Ansible 2.10+** con la colección `paloaltonetworks.panos`.
3. Acceso SMTP balanceado (Puerto 25).

## Ejecución Manual 🚀
Para verificar la conexión con el Firewall:
```bash
ansible-playbook playbooks/healthcheck.yml
```

Para ejecutar el respaldo y envío inmediato por correo:
```bash
ansible-playbook playbooks/backup_config_email.yml
```

## Automatización (Cron) ⏰
El respaldo está programado para ejecutarse todos los **miércoles y viernes a las 01:00 AM**.

Para ver o editar la programación:
```bash
sudo crontab -l
```

Configuración actual en crontab:
```cron
0 1 * * 3,5 cd /opt/paloalto-ansible && ansible-playbook playbooks/backup_config_email.yml >> /opt/paloalto-ansible/backups/automation.log 2>&1
```

---
*Ultima actualización: 4 de Febrero, 2026*
