# Insta Downloader
Bienvenue sur la documentation d'**instaDownloader**. Il s'agit d'un petit logiciel python permettant de télécharger des éléments Instagram (Post, stories, photo de profil, etc).

InstaDownloader est basé sur une librairie Python, [Instaloader.py](https://github.com/instaloader/instaloader)
___

## Sommaire
1. [Installation](#install)
   - Prérequis
   - Téléchargement
2. [Utilisation](#use)
3. [Contribution](#contrib)
4. [Crédit](#credit)
5. [licence](#licence)

## <a name="install"></a>Installation

### Prérequis
Avant d'installer **InstaDownloader**, vous devez installer certains modules tiers : 
- Python 3 : [www.python.org](https://www.python.org/)
- Pip (recommandé) : [pip.pypa.io](https://pip.pypa.io/en/stable/)
- *Instaloader* : [instaloader.github.io](https://instaloader.github.io/installation.html#install)


### Téléchargement
Pour le télécharger, vous pouvez faire un [*fork*](https://docs.github.com/en/get-started/quickstart/fork-a-repo) du projet (lien : https://github.com/antton-dev/InstaDownloader.git)

Vous pouvez aussi télécharger l'ensemble du projet en [archive ZIP](https://github.com/antton-dev/InstaDownloader/archive/refs/heads/master.zip).

Une fois le projet téléchargé, vérifiez la présence de tous les fichiers :
- instadownloader.py
- téléchargements

Note : Le fichier `.gitignore` peut être supprimé une fois le projet installé.

## <a name="use"></a>Utilisation
Pour utiliser InstaDownloader, lancez un terminal et placez vous dans le dossier racine du projet (`cd instadownloader`).
Exécutez la commande suivante pour lancer le script : `python intadownloader.py`.
Laissez vous guider par les instructions données par le programme.

### Liste des commandes
|  Numéro |  Nom |  Description 
|:-------:|:----:|:-----------:|
| 1 | Avatar  | Télécharger l'image de profile  |
| 2 | Story   | Télécharger la story actuelle (-24h)  |
| 3 | Posts   | Télécharger toutes les publications   |
| 4 |Highlight| Télécharger tous les \"highlights\" (stories épinglées) |

## <a name="contrib"></a>Contribution
Vous pouvez librement contribuer au projet en soumettant une *Pull Request*. Vous pouvez aussi déposer une *Issue* si vous rencontez un problème ou un bug.


## <a name="credit"></a>Crédit
Ce logiciel utilise des logiciels tiers :

### Instaloader.py 
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

## <a name="licence"></a>Licence 
Le Logiciel InstaDownloader est soumis à la licence :

**MIT License**

Copyright (c) [2022] [AnttonDev]
    
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
   
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
