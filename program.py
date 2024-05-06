import os


def deleteAllBelow(path: str) -> None:
    fileList = os.listdir(path)
    for i in fileList:
        full_path = os.path.join(path, i)
        if not (os.path.isfile(full_path)):
            deleteAllBelow(full_path)
        else:
            try:
                os.remove(full_path)
                print("removed " + full_path)

            except Exception as error:
                print(error)
    fileList = os.listdir(path)
    for i in fileList:
        try:
            full_path = os.path.join(path, i)
            os.rmdir(full_path)
            print("removed " + full_path)
        except Exception as error:
            print(error)


deleteAllBelow('C:\\Users\\ron\\Desktop\\testCode')
