[app]

# Titre de votre application
title = TRIKA.TRAD

# Nom du package
package.name = trikatrad

# Domaine du package
package.domain = org.trika

# Dossier source contenant votre code
source.dir = .

# Extensions des fichiers à inclure
source.include_exts = py,png,jpg,jpeg,mp4,db,sqlite,json,txt

# Dossiers spécifiques à inclure
source.include_patterns = assets/*, images/*, videos/*

# Icône de l'application (basée sur votre fichier logo.png à la racine)
icon.filename = logo.png

# Version de l'application
version = 1.0.0

# Bibliothèques Python requises
requirements = python3,kivy,sqlite3,requests,deep-translator,pillow

# Orientation de l'écran forcée en portrait
orientation = portrait

# Mode plein écran
fullscreen = 1

# Permissions Android (Microphone, Stockage, Internet)
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# API Android cible
android.api = 33

# API minimale supportée
android.minapi = 21

# Architectures supportées
android.archs = arm64-v8a, armeabi-v7a

# Accepter automatiquement les licences SDK
android.accept_sdk_ext_license = True

[buildozer]
log_level = 2
warn_on_root = 1
