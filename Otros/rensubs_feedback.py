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
        self.__ext_video__ = ext_video
        self.__ext_srt__ = ext_srt
        self.__lista_videos__ = self.conseguir_videos(ext_video)
        self.__lista_srts__ = self.conseguir_srts(ext_srt)
        self.__lista_combinada__ = self.combinar_videos_srts(self.__lista_videos__, self.__lista_srts__)
    
    def get_ext_video(self): 
        return self.__ext_video__
    def get_ext_srt(self): 
        return self.__ext_srt__
    def get_lista_videos(self):
        return self.__lista_videos__
    def get_lista_srts(self):
        return self.__lista_srts__
    def get_lista_combinada(self):
        return self.__lista_combinada__
    
    def conseguir_videos(self, ext) :
        """Devuelve una lista con todos los videos que finalizan en la 
        extensión señalada."""
        videos = []
        for archivo in os.listdir() :
            if os.path.splitext(archivo)[1] == f".{ext}" : videos.append(archivo)
        videos.sort()
        if not videos:
            raise RuntimeError("No se encontró ningún video con esa extensión")
        return videos
    
    def conseguir_srts(self, ext) :
        """Devuelve una lista con todos los archivos de subtítulos que
        finalizan en la extensión señalada."""
        srts = []
        for archivo in os.listdir() :
            if os.path.splitext(archivo)[1] == f".{ext}" : srts.append(archivo)
        srts.sort()
        if not srts:
            raise RuntimeError("No se encontró ningún subtítulo con esa extensión")
        return srts
    
    def combinar_videos_srts(self, videos, srts) :
        """Devuelve una lista de tuplas de cada archivo de video y de 
        subtítulos, ordenados alfabéticamente"""
        lista_comb = [(videos[n], srts[n]) for n in range(len(min([videos, srts], key=len)))]
        
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
        return lista_comb
    
    def cambiar_nombre_srts(self):
        """Opera directamente sobre los archivos en la lista combinada,
        cambiando el nombre de los archivos de subtítulos al de los de
        video."""
        for par in self.__lista_combinada__ :
            nombre_txt = os.path.splitext(par[0])[0]
            extension = f".{args.ext_srt}"
            os.rename(par[1], nombre_txt + extension)
        print("Se cambiaron los nombres de los subtítulos")

def main():
    renombrador = RenombradorSubtitulos(args.ext_video, args.ext_srt)
    renombrador.cambiar_nombre_srts()

if __name__ == "__main__":
    sys.tracebacklimit = 0 # tracebacklimit definido en 0 para evitar que
                           # muestre los tracebcks al levantar la excepción
                           # si lx usuarix cancela el programa.
    parser = argparse.ArgumentParser(description="Script de conversión de" 
        "títulos pensado para emparejar subtítulos con títulos del archivo", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,
                        help="mostrar este mensaje de ayuda y salir")
    parser.add_argument("ext_video", help="extensión del video, sin punto (ej:"
                        "'mkv').")
    parser.add_argument("ext_srt", help="extensión del subtítulo, sin punto "
                        "(ej: 'srt'). Por defecto es .srt",nargs="?", default="srt")
    args = parser.parse_args()
    main()
