import random, os, string, time
from subprocess import (
    run,
    Popen,
    PIPE
)
def run_code(code, input, lang):
    slug = "media/code/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    open(slug + ".in", "x").write(input)



    if lang == "c_cpp":
        open(slug + ".cpp", "x").write(code)

        compile_command = "g++ " + slug + ".cpp -o " + slug
        run_command = "./" + slug + " <" + slug + ".in> " + slug + ".out"

        compile_call = Popen([compile_command], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        com_out, com_err = compile_call.communicate()

        if com_err:
            error = str(com_err)
            error = error.replace(slug, "<br>code")

            remove_user_files(slug, [".cpp", ".in"])
            return ("error", "Compilation Error", error, None, None)
        else:
            timeStart = time.time()
            try: run(run_command,  shell=True, timeout=10)
            except:
                remove_user_files(slug, [".cpp", ".in", ".out"])
                return ("error", "Request Timedout! Max: 10 sec.", "", None, None)

            timeEnd = time.time() - timeStart
            size = (((os.stat(slug).st_size)/1024)/1024)


            try:
                output = open(slug + ".out", "r").read()
            except:
                remove_user_files(slug, [".cpp", ".in", ".out"])
                return ("error", "Error in execution!", "", None, None)

            remove_user_files(slug, [".cpp", ".in", ".out", ""])
            return ("success", "Code compiled successfully!", output, timeEnd, size)

    else:
        return ("error", "Invalid language!", None, None, None)



def signal_handler(signum, frame):
    raise Exception("Timed out!")

class Timeout(Exception):
    pass


def round_off(ele):
    if ele is not None:
        return round(ele, 3)
    else: return 0.00


def remove_user_files(slug, exts):
    for ext in exts:
        os.remove(slug + ext)
