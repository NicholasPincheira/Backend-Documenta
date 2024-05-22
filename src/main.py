import os
from app import create_app

def main():

    app.run(port=int(os.environ.get('PORT', 5000)))


if __name__ == "__main__":
    main()
