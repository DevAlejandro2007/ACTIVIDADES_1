import instaloader
import requests


def download_instagram_profile_picture(user_name):
    #CREAR INSTANCIA DE INSTALOADER
    L = instaloader.Instaloader()
    try : 
        profil = instaloader.Profile.from_username(L.context,user_name)

        profile_pic_url = profil.profile_pic_url


        respose = requests.get(profile_pic_url)

        if respose.status_code == 200:
            with open(f"{user_name}.jpg","wb") as file:
                file.write(respose.content)
            print(f"LA FOTO DE PERFIL DE {user_name} HA SIDO DESCARAGADA EXITOSAMENTE")
        else:
            print(f"NO SE PUDO DESCARGAR LA FOTO DE PERFIL DE {user_name}")
    except instaloader.exceptions.ProfileNotExistsException:
            print(f"ERROR, NO EXISTE {user_name}" )
    except Exception as e:
        print(f"OCURRIO UN ERROR {e}")

if __name__ == "__main__":
    user_name = input("INGRESE EL NOMBRE DE USUARIO DE INSTAGRAM")
    download_instagram_profile_picture(user_name)