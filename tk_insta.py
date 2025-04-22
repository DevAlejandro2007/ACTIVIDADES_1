import requests,instaloader,tkinter as tk
from PIL import Image, ImageTk 


def ventana_insta():
    ventana = tk.Tk()
    ventana.title("MENU INSTALOADER")
    ventana.geometry("800x1000")
    ventana.config(background= "lightblue")
    
    #Titulod etexto 
    texto = " INGRESA EL USUARIO PARA DESCARGAR SU FOTO DE PERFIL "
    titulo = tk.Label(master= ventana, text= texto, bg= "lightblue", fg= "black", font= ("Arial", 15))
    titulo.pack(padx= 10, pady= 10)
    
    user = tk.Entry(master= ventana, width=40, font= ("Arial", 15), background= "turquoise")
    user.pack(padx= 10, pady= 13)

    descargar = tk.Button(master = ventana, text = "DESCARGAR!!", font= ("Arial", 15), bg= "turquoise", fg= "white", command= lambda: nom_user())
    descargar.place(x = 100, y = 100)
    
    titulo2 = tk.Label(master= ventana, text= "", bg= "lightblue", fg= "black", font= ("Arial", 15))
    titulo2.pack(padx= 30, pady= 25)
    
    imagen_descarga = tk.Label(master= ventana, bg = "lightblue")
    imagen_descarga.pack(padx= 30, pady= 20)

    salir = tk.Button(master = ventana, text= "SALIR", font = ("Arial", 15) , bg = "turquoise", fg = "white", command = lambda: ventana.destroy())
    salir.place(x = 630, y = 100)
    
    def nom_user():
        user.delete(0,-1)
        user_name = user.get()
        def download_instagram_profile_picture(user_name):
        #CREAR INSTANCIA DE INSTALOADER
            try : 
                la = instaloader.Instaloader()
                profil = instaloader.Profile.from_username(la.context,user_name)

                profile_pic_url = profil.profile_pic_url

                respose = requests.get(profile_pic_url)

                if respose.status_code == 200:
                    with open(f"{user_name}.jpg","wb") as file:
                        file.write(respose.content)
                        img = Image.open(f"{user_name}.jpg")
                        img_tk = ImageTk.PhotoImage(img)
                        imagen_descarga.config(image=img_tk)
                        imagen_descarga.image = img_tk
                        print(f"LA FOTO DE PERFIL DE {user_name} HA SIDO DESCARAGADA EXITOSAMENTE")
                else:
                    print(f"NO SE PUDO DESCARGAR LA FOTO DE PERFIL DE {user_name}")
            except instaloader.exceptions.ProfileNotExistsException:
                print(f"ERROR, NO EXISTE {user_name}" )
            except Exception as e:
                print(f"OCURRIO UN ERROR {e}")

        if __name__ == "__main__":
            download_instagram_profile_picture(user_name)
    ventana.mainloop()

ventana_insta()