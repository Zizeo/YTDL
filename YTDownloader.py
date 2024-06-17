
import customtkinter as ctk
import pldl
import ytdl
from PyQt6.QtWidgets import QApplication, QFileDialog


global str
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Fonction pour le bouton principal
def button_callback():

    if playlist_check.get() == 1:
        str=pldl.download_video(entry.get(), folder_entry.get(), audio_check.get()==1)
    else:
        str =ytdl.download_video(entry.get(), folder_entry.get(), audio_check.get()==1)
        
    message_label.configure(text=str)




# Fonction pour sélectionner un dossier
def selectfile():
    # shell = win32com.client.Dispatch("Shell.Application")
    # folder = shell.BrowseForFolder(0, "Select a folder:", 0, 0)
    # if folder:
    #     foldername = folder.Self.Path
    #     folder_entry.delete(0, ctk.END)
    #     folder_entry.insert(0, foldername)

    # foldername = filedialog.askdirectory(parent=app,initialdir='shell:MyComputerFolder', title='Please select a directory')
    foldername = QFileDialog.getExistingDirectory()
    folder_entry.delete(0, ctk.END)
    folder_entry.insert(0, foldername)

app = ctk.CTk()
filebrowser= QApplication([])
app.title("Youtube Downloader")
app.geometry("600x500")

# Frame pour l'entrée du lien YouTube
link_frame = ctk.CTkFrame(app)
link_frame.pack(pady=20, padx=20, fill="x")

entry_label = ctk.CTkLabel(link_frame, text="Enter YT link:")
entry_label.pack(side="left", padx=10)
entry = ctk.CTkEntry(link_frame, placeholder_text="Enter YT link...")
entry.pack(side="left", padx=10, fill="x", expand=True)

# Frame pour la sélection du dossier
folder_frame = ctk.CTkFrame(app)
folder_frame.pack(pady=20, padx=20, fill="x")

folder_label = ctk.CTkLabel(folder_frame, text="Select folder:")
folder_label.pack(side="left", padx=10)
folder_entry = ctk.CTkEntry(folder_frame, placeholder_text="Enter folder path...")
folder_entry.pack(side="left", padx=10, fill="x", expand=True)
browse_button = ctk.CTkButton(folder_frame, text="Browse", command=selectfile)
browse_button.pack(side="left", padx=10)

# Frame pour le bouton principal
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20, padx=20, fill="x")

button = ctk.CTkButton(button_frame, text="Download", command=button_callback)
button.pack(pady=20, fill="x", expand=True)

# Frame pour les checkboxes
checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=20, padx=20, fill="x")

audio_check = ctk.CTkCheckBox(checkbox_frame, text="only audio")
audio_check.pack(side="left", padx=20, pady=(0, 20))
playlist_check = ctk.CTkCheckBox(checkbox_frame, text="download whole playlist")
playlist_check.pack(side="left", padx=20, pady=(0, 20))

# Frame pour afficher les messages
message_frame = ctk.CTkFrame(app)
message_frame.pack(pady=20, padx=20, fill="x")

message_label = ctk.CTkLabel(message_frame, text="")
message_label.pack(pady=20, padx=20, fill="x")

app.mainloop()
