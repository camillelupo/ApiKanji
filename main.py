from tool.kanjidic import get_kanjidic2_data
from api import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=7776)
