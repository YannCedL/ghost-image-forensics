# script simple pour lancer l'app ghost d'un coup
import uvicorn
import webbrowser
import threading
import time

def ouvrir_navigateur():
    # attend 1.5 seconde que le serveur demarre et ouvre la page web
    time.sleep(1.5)
    webbrowser.open("http://localhost:8020")

if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print(" 👻  Lancement de GHOST Image Forensics UI on port 8020")
    print(" Ouverture du navigateur sur http://localhost:8020")
    print("------------------------------------------------------------------")
    
    # ouvrir la page automatiquement
    threading.Thread(target=ouvrir_navigateur, daemon=True).start()
    
    # demarrage du serveur web fastapi
    uvicorn.run("ghost_image_forensics.api:app", host="127.0.0.1", port=8020, reload=True)
