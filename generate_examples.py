##########################################################################
#This file is part of WTFramework. 
#
#    WTFramework is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WTFramework is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WTFramework.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################
import os

# This file takes the files in the /tests directory, then converts them 
# into strings in wtframework/wtf/_devtools_/filetemplates/examples.py




if __name__ == '__main__':
    example_path = os.path.join('wtframework', 'wtf', '_devtools_', 'filetemplates', '_examples_.py')
    print example_path
    examples_file = open(example_path,
                         "w")
    examples_file.write("""##########################################################################
#This file is part of WTFramework. 
#
#    WTFramework is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WTFramework is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WTFramework.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################
examples = {}

""" )

    
    for root, dirs, files in os.walk('tests'):
        for example_file in files:
            if not example_file.endswith(".py"):
                continue

            fpath = os.path.join(root, example_file)
            print "processing ", fpath
            
            the_file = open(fpath)
            
            examples_file.write("examples['" + fpath + "'] = '''")
            
            examples_file.write( the_file.read().replace("'''", '"""') )
            
            examples_file.write("\n'''\n\n")
    
    
    
    examples_file.close()

