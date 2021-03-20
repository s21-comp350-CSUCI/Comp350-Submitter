from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals

source_code = """
def example():
     return 'Hello World!'
 """

 loc = {}
 byte_code = compile_restricted(source_code, '<inline>', 'exec')
 exec(byte_code, safe_globals, loc)

 loc['example']()