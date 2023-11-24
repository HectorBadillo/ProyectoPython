'''import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()
'''
import shutil
carpeta_origen = 'C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 9\\ejemplo_comprimir'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
