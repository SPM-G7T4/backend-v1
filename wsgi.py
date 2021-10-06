"""App entry point.""" 
# Web server gateway interface
from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # remember to set debug=False for production