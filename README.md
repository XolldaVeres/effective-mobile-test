# Effective Mobile DevOps Test

## 📌 Описание

Простое веб-приложение, развернутое с использованием Docker и Docker Compose.

Состоит из:
- backend (Flask приложение)
- nginx (reverse proxy)

Nginx принимает HTTP-запросы на порт 80 и проксирует их в backend.

---

## 🚀 Быстрый запуск

```bash
git clone https://github.com/XolldaVeres/effective-mobile-test.git
cd effective-mobile-test
sudo docker-compose up -d
