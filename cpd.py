import os

def search_and_remove(directory):
    search_string = r'\x50\x65\x72\x66\x6f\x72\x6d\x48\x74\x74\x70\x52\x65\x71\x75\x65\x73\x74","\x61\x73\x73\x65\x72\x74","\x6c\x6f\x61\x64'
    total_files = 0
    files_processed = 0
    lines_processed = 0
    lines_deleted = 0

    # Create log file with current date and time as title
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"log_{current_time}.txt"
    log_file = open(log_filename, "w")
    log_file.write(f"Log created at: {current_time}\n\n")
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".lua"):
                total_files += 1
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r+") as file:
                        lines = file.readlines()
                        file.seek(0)
                        line_number = 0
                        for line in lines:
                            lines_processed += 1
                            line_number += 1
                            if search_string in line:
                                print("Found in:", file_path)
                                print("Line Number:", line_number)
                                print("Line:", line)
                                choice = input("Do you want to remove this line? (Y/N): ")
                                if choice.upper() == 'Y':
                                    lines_deleted += 1
                                    continue
                            file.write(line)
                        file.truncate()
                    files_processed += 1
                except Exception as e:
                    print(f"Error processing file: {file_path}, {e}")
    log_file.write(f"Total files: {total_files}\n")
    log_file.write(f"Files processed: {files_processed}\n")
    log_file.write(f"Lines processed: {lines_processed}\n")
    log_file.write(f"Lines deleted: {lines_deleted}\n")
    log_file.close()
    print(f"Total files: {total_files}")
    print(f"Files processed: {files_processed}")
    print(f"Lines processed: {lines_processed}")
    print(f"Lines deleted: {lines_deleted}")
    print("Log saved as:", log_filename)

# Get directory input from user
directory = input("Enter directory to search for .lua files: ")
search_and_remove(directory)
