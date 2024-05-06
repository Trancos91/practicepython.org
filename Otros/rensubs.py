#!/usr/bin/env python3
import os
import sys
import argparse
from textwrap import dedent

class RenombradorSubtitulos:
    """Objeto que recopila los arvhivos de video y de subtítulos con las
    extensiones indicadas en su constructor, y que contiene los métodos
    para acceder a las mismas."""
    def __init__(self, ext_video, ext_srt="srt"):
        self.ext_video = ext_video
        self.ext_srt = ext_srt
    
    def conseguir_listas(self,):
        videos = self.conseguir_videos()
        srts = self.conseguir_srts()
        return (videos, srts)
    
    def conseguir_videos(self) :
        """Devuelve una lista con todos los videos que finalizan en la 
        extensión señalada."""
        videos = []
        for archivo in os.listdir() :
            if os.path.splitext(archivo)[1] == f".{self.ext_video}" : videos.append(archivo)
        videos.sort()
        if not videos:
            raise RuntimeError("No se encontró ningún video con esa extensión")
        return videos
    
    def conseguir_srts(self) :
        """Devuelve una lista con todos los archivos de subtítulos que
        finalizan en la extensión señalada."""
        srts = []
        for archivo in os.listdir() :
            if os.path.splitext(archivo)[1] == f".{self.ext_srt}" : srts.append(archivo)
        srts.sort()
        if not srts:
            raise RuntimeError("No se encontró ningún subtítulo con esa extensión")
        return srts
    
    def combinar_videos_srts(self, videos, srts) :
        """Devuelve una lista de tuplas de cada archivo de video y de 
        subtítulos, ordenados alfabéticamente"""
        
        def check_continuar(archivo_menos, archivo_mas):
            rtas_pos = ("si", "sí", "s", "y", "ye", "yes", "chi", "shi", "ti", "da", "dal", "dale")
            rtas_neg = ("n", "no", "nop", "nope", "nopo", "ni ahi", "ni ahí", "niahí")
            
            print("-" * 8, "ATENCIÓN", "-" * 8)
            print()
            print(dedent(f"""\
            Hay menos archivos de {archivo_menos} que de {archivo_mas}.
            Quedarán archivos de {archivo_mas} sin modificar.
            Se modificarán los demás archivos que sí tienen
            un correspondiente."""))
            print()
            seguir = input(dedent("""\
            Esto podría significar que los subtítulos no correspondan
            con los videos. Estás segurx de que querés seguir adelante? """))
            while True:
                if seguir.lower() in rtas_pos:
                    return 
                elif seguir.lower() in rtas_neg:
                    raise RuntimeError("Usuarix canceló la operación")
                else:
                    seguir = input("Por favor ingresá 'sí' o 'no' como respuesta: ")
                    
        if len(videos) < len(srts):
            check_continuar("video", "subtítulos")
        elif len(videos) > len(srts):
            check_continuar("subtítulos", "video")
            
        lista_comb = [(videos[n], srts[n]) for n in range(len(min([videos, srts], key=len)))]
                    
        return lista_comb
    
    def cambiar_nombre_srts(self, lista_combinada):
        """Opera directamente sobre los archivos en la lista combinada,
        cambiando el nombre de los archivos de subtítulos al de los de
        video."""
        for video, srt in lista_combinada :
            nombre_txt = os.path.splitext(video)[0]
            extension = f".{self.ext_srt}"
            os.rename(srt, nombre_txt + extension)
        print("Se cambiaron los nombres de los subtítulos")

def main():
    parser = argparse.ArgumentParser(description="Script de conversión de" 
        "títulos pensado para emparejar subtítulos con títulos del archivo", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,
                        help="mostrar este mensaje de ayuda y salir")
    parser.add_argument("ext_video", help="extensión del video, sin punto (ej:"
                        "'mkv').")
    parser.add_argument("ext_srt", help="extensión del subtítulo, sin punto "
                        "(ej: 'srt'). Por defecto es .srt",nargs="?", default="srt")
    args = parser.parse_args()
    renombrador = RenombradorSubtitulos(args.ext_video, args.ext_srt)
    (lista_videos, lista_srt) = renombrador.conseguir_listas()
    lista_combinada = renombrador.combinar_videos_srts(lista_videos, lista_srt)
    renombrador.cambiar_nombre_srts(lista_combinada)

if __name__ == "__main__":
    sys.tracebacklimit = 0 # tracebacklimit definido en 0 para evitar que
                           # muestre los tracebcks al levantar la excepción
                           # si lx usuarix cancela el programa.
    main()
