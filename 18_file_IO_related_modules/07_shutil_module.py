import shutil
# Copy a file
# shutil.copy('source_file.txt', 'destination_file.txt')  # copies 'source_file.txt' to 'destination_file.txt'

shutil.copytree('source_folder', 'destination_folder')  # copies the entire directory 'source_folder' to 'destination_folder'   
shutil.move('source_file.txt', 'destination_folder/')  # moves 'source_file.txt' to 'destination_folder/'
shutil.rmtree('destination_folder')  # removes the entire directory 'destination_folder' and all its contents

shutil.make_archive('archive_name', 'zip', 'source_folder')  # creates a zip archive named 'archive_name.zip' from 'source_folder'
shutil.unpack_archive('archive_name.zip', 'extracted_folder')  # extracts 'archive_name.zip' into 'extracted_folder'

shutil.copy2('source_file.txt', 'destination_file.txt')  # copies 'source_file.txt' to 'destination_file.txt' along with metadata
shutil.copytree('source_folder', 'destination_folder', ignore=shutil.ignore_patterns('*.txt'))  # copies 'source_folder' to 'destination_folder' while ignoring all .txt files