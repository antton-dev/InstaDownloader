import instaloader

ig = instaloader.Instaloader(dirname_pattern="telechargements/{profile}")    # Loading Instance
print('Pour commencer, connectez vous à votre compte instagram :')
login = input("username : ")
ig.interactive_login(login)    # (ask password on terminal)

TargetUsername = input("Nom d'utilisateur cible (celui à télécharger) : ")
profileId = ig.check_profile_id(TargetUsername).userid   # id of target user

print("  Numéro   |     Nom     |   Description  ")
print("     1     |    Avatar   |   Télécharger l'image de profile de " + TargetUsername)
print("     2     |    Story    |   Télécharger la story actuelle (-24h) de " + TargetUsername)
print("     3     |    Posts    |   Télécharger toutes les publications de " + TargetUsername)
print("     4     |  Highlights |   Télécharger tous les \"highlights\" (stories épinglées) de " + TargetUsername)

request = int(input("Que télécharger ? (Numéro - voir ci-dessus)"))

if request == 1:
    ig.download_profile(TargetUsername, profile_pic_only=True)

elif request == 2:
    ig.download_stories(userids=[profileId])

elif request == 3:
    posts = instaloader.Profile.from_username(ig.context, TargetUsername).get_posts()
    for post in posts:
        ig.download_post(post, TargetUsername)

elif request == 4:
    ig.download_highlights(user=profileId)


