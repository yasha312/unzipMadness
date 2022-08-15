import argparse
import zipfile
import os

def make_dir(dir_name, incr=1):
    if not (os.path.exists(dir_name)):
        os.mkdir(dir_name)
        return dir_name
    else:
        while os.path.exists(dir_name+f'_{incr}'):
            incr+=1
        new_dir_name = dir_name+f'_{incr}'
        os.mkdir(new_dir_name)
        return new_dir_name


def unzip1(file_to_unzip, output_dir):
    #output_dir=make_dir(output_dir)
    with zipfile.ZipFile(file_to_unzip, "r") as Zfile:
        Zfile.extractall(output_dir)


def unzip_all(input_dir, central_out=None):
    list_of_files = os.listdir(input_dir)
    #print(list_of_files)
    if central_out is not None:
        central_out=make_dir(central_out)

    for file in list_of_files:
        file = input_dir + file
        #print(f'one file is {file}')
        if file.endswith(".zip"):
            if central_out is not None:
                unzip1(file, central_out)
            else:
                dir_name = file[:-4]
                dir_name=make_dir(dir_name)
                unzip1(file, dir_name)



def main(args):
        unzip_all(args.input_dir, args.output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="dir to unzip")
    parser.add_argument("-o", "--output_dir", help="dir to extract to", action="store",dest="output_dir")
    args=parser.parse_args()
    main(args)
