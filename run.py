import os
import app_flask as app
import routes
import managers.jwt as jwt_manager
from assets.banner import banner as banner

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print(banner)
    print(">> A todo vapor na porta ", port, "\n")

    app_to_run = app.create_app()

    jwt_manager.configure_manager(app_to_run)

    app_to_run = app.configure_app(app_to_run).run(host='0.0.0.0', port=port) 
    
    print("\n>> Fim da linha meu chapa!\n")