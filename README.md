
# Financial Calculator

## Запуск тестов

1. Установите `uv` (если ещё не установлен):
curl -LsSf https://astral.sh/uv/install.sh | sh
   
2. После установки закройте и откройте терминал заново.

3. Перейдите в папку проекта:
cd financial_calc

4. Установите зависимости:
uv sync

5. Запустите тесты:
uv run pytest -v