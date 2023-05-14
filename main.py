from tool.kanjidic import get_kanjidic2_data
from api import create_app

app = create_app()


if __name__ == '__main__':
    app.run(port=7778)
