import sqlite3

# Chemin vers votre fichier de base de données SQLite
db_path = 'db.sqlite3'

# Connexion à la base de données SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Liste des tables à supprimer
tables_to_drop = [
    "Edusco_customuser_groups",
    "Edusco_customuser_user_permissions",
    "auth_group",
    "auth_group_permissions",
    "auth_permission",
    "auth_user",
    "django_content_type",
    "django_migrations",
    "socialaccount_socialapp_sites",
  
    # Ajoutez d'autres tables si nécessaire
]

# Supprimer les tables
for table in tables_to_drop:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Fermer la connexion
conn.commit()   
conn.close()

print("Tables supprimées avec succès.")