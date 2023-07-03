# -*- coding: utf-8 -*

# - - - - IN-BUILT IMPORTS
import sys, os

# - - - - CLASS LIBRARY
class Compiler:

    @staticmethod
    def ironpython_active():
        """Checks if the current script is running in IronPython environment.

        Returns:
            (bool) True if IronPython, False if CPython
        """
        try:
            import clr
            return True
        except ImportError:
            return False
        
    #@staticmethod
    #def print_title():
    #    print("\n\nnpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbq\n\n   █▀▄▀█ ▄▀█ █▄▀ █▀▀ ░ █▀▀ █░█ █▀█ █▄█\n   █░▀░█ █▀█ █░█ ██▄ ▄ █▄█ █▀█ █▀▀ ░█░\n\nnpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbq\n\n")

    @staticmethod
    def print_title():
        print("""\n\nnpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbq\n\n   +MMMMm\n  +M(%)Py""-+\n  MAghP'_====>\n :MMMMMMP\n gMMMMMMM+\n+MMMMM*MM+\nMMMYY+  `MM+\nMM YYYY+  `M+\nM'   YYYKYY+`M+\nY     YYYAYYY+YY+\n\      *YYYUYYYYY+\n \        YHHSYYYYY\n  \          YHHHYYY+\n   `+   ++ +    IHHYY+\n     `-+  " " MMMMKHHYY\n        "'M++M+ MMMGGHHY\n          M  M     MMMGGHH+\n          M  M        YHHHHH\n         // //           YHHHH+\n        // //               YHHH+\n      _//_//_                 `HHHH++\n     // //\ \\                  `HHHHHh+\n                                  `YY `YY\n\n   █▀▄▀█ ▄▀█ █▄▀ █▀▀ ░ █▀▀ █░█ █▀█ █▄█\n   █░▀░█ █▀█ █░█ ██▄ ▄ █▄█ █▀█ █▀▀ ░█░\n\nnpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbq\n\n""")

    @staticmethod
    def collect_files(source_dir):
        """Collects relevant python script files.

        Args:
            source_dir (str): Root directory to collect_files.

        Returns:
            list(str): List of absolute file paths.

        """
        if not os.path.isdir(source_dir):
            raise ValueError("\"{}\" is not a valid directory.".format(source_dir))
        
        files = []
        ignore_list = [os.path.basename(__file__), "__init__.py"]

        for file in os.listdir(source_dir):
            abs_file_path = os.path.join(source_dir, file)
            # Ignore from ignore_list:
            if not file in ignore_list and file.endswith(".py"):
                print(abs_file_path)
                files.append(abs_file_path)
            # Recursion for sub-folders
            elif os.path.isdir(abs_file_path):
                files += Compiler.collect_files(abs_file_path)
        
        return files
    
    @staticmethod
    def build_plugin(source_dir, package_name, version="", extension="ghpy"):
        """Collects and compiles project files into a dll.

        Args:
            filename (str): Name of final output (.dll) file.
            source_folder (str): (optional) Folder to collect files from.
            copy_target (str) : (optional) File path to where the output needs to be copied.
            export_folder (str): Subfolder for output file.

        Returns:
            (bool) True if successful, False otherwise.

        """
        if not Compiler.ironpython_active():
            raise SystemError("IronPython is not running.")
    
        #Compiler.print_logo()
        Compiler.print_title()
        if version != "":
            package_name += "-{}".format(version)
        package_full_name = "{}.{}".format(package_name, extension)

        root_dir = os.path.dirname(source_dir)
        export_dir = os.path.join(root_dir, "bin")
        export_file = os.path.join(export_dir, package_full_name)

        # Create export folder:
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        # Collect necessary files from source_dir
        print("Collecting program files...\n")
        program_files = Compiler.collect_files(source_dir)            

        # Compile Plugin
        import clr
        clr.CompileModules(export_file, *program_files)
        print("\n\n\"{}\" was created successfully!\n\n".format(package_full_name))

        return package_name, package_full_name, export_file

# - - - - RUN SCRIPT
if __name__ == "__main__":
    
    args = sys.argv[1:]
    if len(args) > 4:
        raise SyntaxError("Script takes a maximum of 4 arguments. {} provided.".format(len(args)))
    
    name, full_name, path = Compiler.build_plugin(*args)

    # Set Output to GitHub Action
    with open(os.getenv("GITHUB_OUTPUT"), "a") as env:
        env.write("name={}\n".format(name))
        env.write("full-name={}\n".format(full_name))
        env.write("build={}\n".format(path))
