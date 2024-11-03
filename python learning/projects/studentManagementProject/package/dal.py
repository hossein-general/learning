

def save_data():
    try:
        file_object = open(file="", mode= "w")
    except BaseException as err:
        return "There was an error while saving data in dal", err

    else:
        file_object.close()
        
    finally:
        if "file_object" in locals() and (not file_object.closed)
        file_object.close()

