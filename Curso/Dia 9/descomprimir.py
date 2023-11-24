'''import zipfile

zip_abierto  = zipfile.ZipFile("archivo_comprimido.zip", "r")

zip_abierto.extractall()'''

import shutil

#shutil.unpack_archive("Todo_Comprimido.zip","Extraccion_Terminada",'zip')


shutil.unpack_archive('Proyecto+Dia+9.zip','Proyecto_descomprimido','zip')