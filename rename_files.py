import os

# Definisci la directory che contiene i file
directory = 'C:\\Users\\marco\\Downloads\\archive(4)\\images\\images\\Albrecht_Durer'

# Mappa dei caratteri non leggibili ai caratteri leggibili
char_map = {
    '╠ê': 'ü',   # Modifica questa mappa secondo le tue necessità
    'Ôòá├¬': 'ü', 
     'uü': 'u' # Aggiungi altre mappature se necessario
    # Aggiungi altre mappature se necessario
}

# Funzione per rinominare i file
def rename_files(directory):
    for filename in os.listdir(directory):
        new_filename = filename
        for bad_char, good_char in char_map.items():
            new_filename = new_filename.replace(bad_char, good_char)
        
        # Rinominare il file se il nome è cambiato
        if new_filename != filename:
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")

# Esegui la funzione
rename_files(directory)
