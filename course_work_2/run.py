from flask import Flask, jsonify
from app.main.views import main_blueprint
import logging


app = Flask(__name__)

app.register_blueprint(main_blueprint)

# Создание объекта логгера
logger = logging.getLogger('error_logger')
logger.setLevel(logging.ERROR)

# Создание обработчика для перенаправления журнала в файл или другую цель
handler = logging.FileHandler("api.log")
handler.setLevel(logging.ERROR)

# Создание форматирования записей журнала
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(handler)


@app.errorhandler(Exception)
def not_found_error(error):
    logger.exception(f"Произошла ошибка. Введенная ссылка не найдена: ")
    return jsonify({"error": "Произошла ошибка - 404"}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.exception("Произошла ошибка на стороне сервера: ")
    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
