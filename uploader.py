import os
import os.path

from datetime import datetime
from uuid import uuid4

from subprocess import Popen, PIPE

import notify2

def copy_clipboard(msg):
    ''' Copy `msg` to the clipboard '''
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))     

def mostrarNotificacion(title, message):
    notify2.init("Test")
    notice = notify2.Notification(title, message)
    notice.show()
    return

os.chdir('/home/miguel-debian/DocumentosComun/dev/imagenes-publicas-obsidian')

prefijoGithub = "https://raw.githubusercontent.com/miguelbayon/imagenes-publicas-obsidian/main/"           

nombreCaptura = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
extensionCaptura = ".png"

print("La captura se guardará como " + nombreCaptura + extensionCaptura)
print("Iniciando flameshot...")

orden = "flameshot gui --path " + nombreCaptura
os.system(orden)

existeArchivo = os.path.isfile("./" + nombreCaptura + extensionCaptura)

if (not existeArchivo) :
    print("Captura abortada")

else :
    print("La captura se creo correctamente")
    orden = "git add " + nombreCaptura + extensionCaptura
    os.system(orden)
    orden = "git commit -m 'Nueva imagen " + nombreCaptura + extensionCaptura + "'"
    os.system(orden)
    orden = "git push"
    os.system(orden)
    textoMarkdown = "![Imagen](" + prefijoGithub + nombreCaptura + extensionCaptura + ")" 
    copy_clipboard(textoMarkdown)
    print("Texto copiado al portapapeles: " + textoMarkdown)
    mostrarNotificacion("Uploader dice", "Captura subida");

