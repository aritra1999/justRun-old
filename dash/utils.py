import random, os, string, time
import subprocess
def run_code(code, input, lang):
    slug = "media/code/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    open(slug + ".in", "x").write(input)

    command = ""

    if lang == "c_cpp":
        ext = ".cpp"
        open(slug + ".cpp", "x").write(code)

        compile_command = "g++ " + slug + ".cpp -o " + slug
        run_command = "./" + slug + " <" + slug + ".in> " + slug + ".out"

        timeStart = time.time()

        useless_cat_call = subprocess.Popen([compile_command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        out, err = useless_cat_call.communicate()

        timeEnd = time.time() - timeStart

        if err:
            error = str(err)
            error = error.replace(slug, "<br>code")
            return ("error", "Compilation Error", error, None, None)
        else:

            return ("error", "Compilation Error", "Hello World", None, None)



    else:
        return ("error", "Invalid language!", None, None, None)


    # Getting Output
    # try: output = open(slug + ".out", "r").read()
    # except: return ("error", "Error in execution!", None, None, None)
    # os.remove(slug + ".out")
