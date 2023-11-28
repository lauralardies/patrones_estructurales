import datetime


def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                output.append(str(datetime.datetime.now()))
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log