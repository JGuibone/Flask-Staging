# item = ns.ParseName('song.mp4')
# from pathlib import Path
# file = Path(r'C:\path\to\file.ext')
# ns = sh.NameSpace(str(file.parent))
#  item = ns.ParseName(str(file.name))
import win32com.client

def get_file_metadata(path, filename, metadata):
    # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
    # filename must include extension, i.e. "PID manual.pdf"
    # Returns dictionary containing all file metadata.
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
    ns = sh.NameSpace(path)
    this = win32com

    # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
    file_metadata = dict()
    item = ns.ParseName(str(filename))
    for ind, attribute in enumerate(metadata):
        attr_value = ns.GetDetailsOf(item, ind)
        if attr_value:
            file_metadata[attribute] = attr_value

    return file_metadata

if __name__ == '__main__':
    folder = 'C:\staging'
    filename = 'digital_dice.png'
    metadata = ['Date modified', 'Date created']
    print(get_file_metadata(folder, filename, metadata))