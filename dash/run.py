import random, os, string, time
from .utils import remove_user_files
from subprocess import (
    run,
    Popen,
    PIPE
)
"""
    1. Save "Input" in a file with ".in" extension
    2. Checking for languages
        If language is invalid -> Return 
    3. Defining Compile and Run commands.
    4. Execute Compile Command.
        If Error -> Return 
    5. Execute Run Command.
        If timeTaken -> 10 sec. Return 
    6. Grab final output. 
    7. Remove all generated files. 
    8. Return(verdict, message, output, timeTaken, memory) 
"""
def run_code(code, input, lang):
    lang_ext = ""
    slug = "media/code/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))


    # 1. Save "Input" in a file with ".in" extension
    open(slug + ".in", "x").write(input)


    # 2. Checking for languages
    if lang == "c_cpp":
        lang_ext = ".cpp"
        open(slug + lang_ext, "x").write(code)


        # 3. Defining Compile and Run commands.
        compile_command = "g++ " + slug + ".cpp -o " + slug
        run_command = "./" + slug + " <" + slug + ".in> " + slug + ".out"


        # 4. Execute Compile Command.
        compile_call = Popen([compile_command], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        com_out, com_err = compile_call.communicate()


        if com_err:
            error = str(com_err)
            error = error.replace(slug, "code")

            remove_user_files(slug, [lang_ext, ".in"])
            return ("error", "Compilation Error", error, None, None)
        else:
            # 5. Execute Run Command.
            timeStart = time.time()
            try:
                run(run_command, shell=True, timeout=10)
            except:
                remove_user_files(slug, [lang_ext, ".in", ".out", ""])
                return ("error", "Request Timedout! Max: 10 sec.", "", None, None)

            timeEnd = time.time() - timeStart
            size = (((os.stat(slug).st_size) / 1024) / 1024)
    elif lang == "python":
        lang_ext = ".py"
        open(slug + lang_ext, "x").write(code)


        # 3. Defining Compile and Run commands.
        run_command = "python3 " + slug + ".py <" + slug + ".in> " + slug + ".out"


        # 5. Execute Run Command. | Compile + Run
        timeStart = time.time()
        compile_call = Popen([run_command], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        run_out, run_err = compile_call.communicate()

        if run_err:
            error = str(run_err)
            error = error.replace(slug, "code")

            remove_user_files(slug, [lang_ext, ".in"])
            return ("error", "Compilation Error", error, None, None)
        else:
            timeEnd = time.time() - timeStart
            size = (((os.stat(slug + ".py").st_size) / 1024) / 1024)
    elif lang == "java":
        lang_ext = ".java"
        open(slug + lang_ext, "x").write(code)


        # 3. Defining Compile and Run commands.
        run_command = "java " + slug + ".java <" + slug + ".in> " + slug + ".out"


        # 5. Execute Run Command. | Compile + Run
        timeStart = time.time()
        compile_call = Popen([run_command], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        run_out, run_err = compile_call.communicate()

        if run_err:
            error = str(run_err)
            error = error.replace(slug, "code")

            remove_user_files(slug, [lang_ext, ".in"])
            return ("error", "Compilation Error", error, None, None)
        else:
            timeEnd = time.time() - timeStart
            size = (((os.stat(slug + ".java").st_size) / 1024) / 1024)
    else:
        return ("error", "Invalid language!", "", None, None)



    # 6. Grab final output
    try:
        output = open(slug + ".out", "r").read()
    except:
        remove_user_files(slug, [lang_ext, ".in", ".out"])
        return ("error", "Error in execution!", "", None, None)


    # 7. Remove all generated files.
    remove_user_files(slug, [lang_ext, ".in", ".out", ""])


    # 8. Return verdict
    return ("success", "Code compiled successfully!", output, timeEnd, size)

