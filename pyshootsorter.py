import os
import exifread
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from datetime import datetime
from shutil import move
from tqdm import tqdm

SOURCE_FOLDER = 'Z:\\bucket'
VIDEO_DEST = 'Z:\\Video'
PHOTO_DEST = 'Z:\\Photo\\RAW'


def extract_date_from_nef(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
        
    try:
        with open(file_path, 'rb') as file:
            tags = exifread.process_file(file)
            if "EXIF DateTimeOriginal" in tags:
                date_tag = str(tags["EXIF DateTimeOriginal"])
                date_obj = datetime.strptime(date_tag, '%Y:%m:%d %H:%M:%S')
                return date_obj
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        raise
    except Exception as e:
        print(f"Unable to extract date from image {file_path}: {e}")
    return None

def extract_date_from_video(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
        
    try:
        parser = createParser(file_path)
        if not parser:
            print(f"Cannot parse video file {file_path}")
            return None
        with parser:
            try:
                metadata = extractMetadata(parser)
                return metadata.get('creation_date')
            except Exception as e:
                print(f"Cannot extract metadata from video {file_path}: {e}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        raise
    except Exception as e:
        print(f"Error processing video file {file_path}: {e}")
    return None

def organize_files():
    all_files = []
    try:
        for root, _, files in os.walk(SOURCE_FOLDER):
            for file in files:
                all_files.append(os.path.join(root, file))
    except KeyboardInterrupt:
        print("\nRecherche de fichiers interrompue par l'utilisateur.")
        return
    except Exception as e:
        print(f"Error walking through source folder: {e}")
        return
        
    # Initialize counters for statistics
    moved_count = 0
    error_count = 0
    
    try:
        # Create progress bar with more information
        with tqdm(all_files, desc="Organizing", ncols=120, unit="file", leave=True) as progress_bar:
            for file_path in progress_bar:
                if not os.path.exists(file_path):
                    tqdm.write(f"File no longer exists: {file_path}")
                    continue
                    
                # Process the file
                file_name = os.path.basename(file_path)
                file_extension = file_name.split('.')[-1].lower()
                
                # Show current file in progress bar
                progress_bar.set_description(f"Processing: {file_name[:15]}{'...' if len(file_name) > 15 else ''}")

                if file_extension in ["jpg", "jpeg", "png", "tif", "tiff", "nef", "dng"]:
                    date_obj = extract_date_from_nef(file_path)
                    dest_folder = PHOTO_DEST
                elif file_extension in ["mp4", "mov", "avi", "mkv"]:
                    date_obj = extract_date_from_video(file_path)
                    dest_folder = VIDEO_DEST
                else:
                    continue

                if date_obj:
                    target_folder = os.path.join(dest_folder, date_obj.strftime('%Y%m%d'))
                    os.makedirs(target_folder, exist_ok=True)
                    try:
                        move(file_path, os.path.join(target_folder, file_name))
                        moved_count += 1
                        # Update progress bar with stats
                        progress_bar.set_postfix(moved=moved_count, errors=error_count)
                    except Exception as e:
                        error_count += 1
                        progress_bar.set_postfix(moved=moved_count, errors=error_count)
                        # Still print errors but don't disrupt the progress bar
                        tqdm.write(f"Error moving {file_name}: {e}")
    except Exception as e:
        print(f"Error during file organization: {e}")

def verify_photos_placement(base_folder):
    all_files = []
    try:
        for root, _, files in os.walk(base_folder):
            for file in files:
                all_files.append(os.path.join(root, file))
    except KeyboardInterrupt:
        print("\nRecherche de fichiers interrompue par l'utilisateur.")
        return
    except Exception as e:
        print(f"Error walking through base folder: {e}")
        return
    
    # Initialize counters
    verified_count = 0
    misplaced_count = 0
    
    try:
        # Create progress bar with more information
        with tqdm(all_files, desc="Verifying", ncols=120, unit="file", leave=True) as progress_bar:
            for file_path in progress_bar:
                if not os.path.exists(file_path):
                    tqdm.write(f"File no longer exists: {file_path}")
                    continue
                    
                file_name = os.path.basename(file_path)
                file_extension = file_name.split('.')[-1].lower()
                
                # Show current file in progress bar
                progress_bar.set_description(f"Verifying: {file_name[:15]}{'...' if len(file_name) > 15 else ''}")

                if file_extension in ["jpg", "jpeg", "png", "tif", "tiff", "nef"]:
                    date_obj = extract_date_from_nef(file_path)
                    if date_obj:
                        correct_folder = os.path.join(base_folder, date_obj.strftime('%Y%m%d'))
                        verified_count += 1
                        if os.path.dirname(file_path) != correct_folder:
                            misplaced_count += 1
                            # Use tqdm.write to avoid disrupting the progress bar
                            tqdm.write(f"{file_name} is not in the correct folder. It should be in {correct_folder} but is currently in {os.path.dirname(file_path)}.")
                        # Update progress bar with stats
                        progress_bar.set_postfix(verified=verified_count, misplaced=misplaced_count)
    except Exception as e:
        print(f"Error during verification: {e}")

def count_photos_in_folder(base_folder):
    count = 0
    for _, _, files in os.walk(base_folder):
        for file in files:
            file_extension = file.split('.')[-1].lower()
            if file_extension in ["jpg", "jpeg", "png", "tif", "tiff", "nef", "dng"]:
                count += 1
    return count

def main():
    try:
        while True:
            print("\nVeuillez choisir un mode :")
            print("1: Trie des fichiers")
            print("2: Vérification de l'emplacement des photos")
            print("3: Quitter")
            
            try:
                choice = input("Entrez le numéro du mode choisi : ")

                if choice == "1":
                    organize_files()
                    print("Trie terminé.")
                elif choice == "2":
                    total_photos = count_photos_in_folder(PHOTO_DEST)
                    confirmation = input(f"Il y a {total_photos} photos à vérifier. Voulez-vous continuer? (Oui/Non) ").lower()
                    if confirmation in ["oui", "o"]:
                        verify_photos_placement(PHOTO_DEST)
                        print("Vérification terminée.")
                    else:
                        print("Vérification annulée.")
                elif choice == "3":
                    print("Au revoir!")
                    break
                else:
                    print("Choix invalide, veuillez réessayer.")
            except KeyboardInterrupt:
                print("\nOpération annulée par l'utilisateur.")
                response = input("\nVoulez-vous quitter le programme? (Oui/Non): ").lower()
                if response in ["oui", "o", "yes", "y"]:
                    print("Au revoir!")
                    break
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur. Au revoir!")
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite: {e}")
    finally:
        print("\nFin du programme.")

if __name__ == "__main__":
    main()
