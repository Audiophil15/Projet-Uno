"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "UNO",
    version = "Graphique",
    description = "Jeu de UNO avec une interface graphique",
    options = { "build_exe" : {"build_exe" : "Jeu de UNO"}},
    executables = [Executable("MainGraphiqueOptimisation.py")],
)