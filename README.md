# APstatus (WIP)
Aplikace, která slouží k monitorování dostupnosti síťových prvků a zařízení
na Gymnáziu Jana Keplera (Wi-Fi AP, tiskárny, IP telefony, switche).
- Aplikace je přístupná přes webové rozhraní.
- Sada zkoumaných síťových prvků je modifikovatelná. Buď přes konfigurační
soubor, nebo po přihlášení správce přímo přes webové rozhraní (wip).
- Aplikace je jednoduše instalovatelná a nasaditelná pomocí technologie
Docker.

Instalace:
1. Git clone
2. Sežente si Docker
3. docker build -t apstatus .
4. docker-compose up
